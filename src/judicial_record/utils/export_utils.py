"""export_utils.py - reusable export utilities for specification repositories."""

from dataclasses import asdict, dataclass
import json
from pathlib import Path

from judicial_record.spec_config import SpecConfig
from judicial_record.utils.extractor_utils import (
    Requirement,
    assert_alphabetical_order,
    assert_exact_identifier_coverage,
    extract_heading_identifiers,
    extract_identifier_notes,
)
from judicial_record.utils.load_utils import load_text
from judicial_record.utils.path_utils import data_spec_path, repo_root


@dataclass(frozen=True)
class ConformanceCheck:
    """Generated conformance check section."""

    id: str
    checks: list[str]
    failure_conditions: list[str]


@dataclass(frozen=True)
class ConformanceExport:
    """Generated conformance checks export."""

    schema: str
    spec: dict[str, str]
    checks: list[ConformanceCheck]


@dataclass(frozen=True)
class RequirementExport:
    """Generated requirements export."""

    schema: str
    spec: dict[str, str]
    requirements: list[Requirement]


@dataclass(frozen=True)
class ScopeExclusionExport:
    """Generated scope exclusions export."""

    schema: str
    spec: dict[str, str]
    excluded: list[str]


def build_conformance_export(
    config: SpecConfig,
    *,
    version: str,
    root: Path | None = None,
) -> ConformanceExport:
    """Build conformance-checks.json content."""
    repo = root or repo_root()
    ids = canonical_ids(config, repo)
    checks = extract_conformance_checks(
        load_text(repo / config.conformance_file_name),
        ids,
        config,
    )

    return ConformanceExport(
        schema=config.conformance_schema,
        spec=spec_metadata(config, version),
        checks=checks,
    )


def build_requirements_export(
    config: SpecConfig,
    *,
    version: str,
    root: Path | None = None,
) -> RequirementExport:
    """Build requirements.json content."""
    repo = root or repo_root()
    requirements = canonical_requirements(config, repo)
    ids = [requirement.id for requirement in requirements]

    spec_ids = extract_heading_identifiers(
        load_text(repo / config.spec_file_name),
        expected_prefix=config.spec_id,
    )
    conformance_ids = extract_heading_identifiers(
        load_text(repo / config.conformance_file_name),
        expected_prefix=config.spec_id,
    )

    assert_exact_identifier_coverage(
        canonical_ids=ids,
        found_ids=spec_ids,
        source_name=config.spec_file_name,
    )
    assert_exact_identifier_coverage(
        canonical_ids=ids,
        found_ids=conformance_ids,
        source_name=config.conformance_file_name,
    )

    assert_alphabetical_order(spec_ids, source_name=config.spec_file_name)
    assert_alphabetical_order(conformance_ids, source_name=config.conformance_file_name)

    return RequirementExport(
        schema=config.requirements_schema,
        spec=spec_metadata(config, version),
        requirements=requirements,
    )


def build_scope_exclusions_export(
    config: SpecConfig,
    *,
    version: str,
    root: Path | None = None,
) -> ScopeExclusionExport:
    """Build scope-exclusions.json content."""
    repo = root or repo_root()
    exclusions = extract_scope_exclusions(
        load_text(repo / config.spec_file_name), config
    )

    return ScopeExclusionExport(
        schema=config.scope_exclusions_schema,
        spec=spec_metadata(config, version),
        excluded=exclusions,
    )


def canonical_ids(config: SpecConfig, root: Path | None = None) -> list[str]:
    """Return canonical requirement identifiers."""
    return [requirement.id for requirement in canonical_requirements(config, root)]


def canonical_requirements(
    config: SpecConfig,
    root: Path | None = None,
) -> list[Requirement]:
    """Return canonical requirements from the identifiers file."""
    repo = root or repo_root()
    return extract_identifier_notes(
        load_text(repo / config.identifiers_file_name),
        expected_prefix=config.spec_id,
    )


def export_all(
    config: SpecConfig,
    *,
    version: str,
    root: Path | None = None,
    check: bool = False,
) -> list[Path]:
    """Generate or check all data/spec JSON artifacts."""
    repo = root or repo_root()

    outputs = [
        (
            data_spec_path("requirements.json", repo),
            build_requirements_export(config, version=version, root=repo),
        ),
        (
            data_spec_path("scope-exclusions.json", repo),
            build_scope_exclusions_export(config, version=version, root=repo),
        ),
        (
            data_spec_path("conformance-checks.json", repo),
            build_conformance_export(config, version=version, root=repo),
        ),
    ]

    written_paths: list[Path] = []

    for path, data in outputs:
        rendered = json.dumps(asdict(data), indent=2, ensure_ascii=False) + "\n"

        if check:
            if not path.exists():
                raise FileNotFoundError(f"Missing generated artifact: {path}")
            current = path.read_text(encoding="utf-8")
            if current != rendered:
                raise ValueError(f"Generated artifact is stale: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered, encoding="utf-8")

        written_paths.append(path)

    return written_paths


def extract_conformance_checks(
    markdown: str,
    ids: list[str],
    config: SpecConfig,
) -> list[ConformanceCheck]:
    """Extract check bullets and failure conditions from the conformance file."""
    lines = markdown.splitlines()
    checks: list[ConformanceCheck] = []
    heading_prefix = f"## {config.spec_id}."

    for index, line in enumerate(lines):
        stripped = line.strip()

        if not stripped.startswith(heading_prefix):
            continue

        identifier = stripped.removeprefix("## ").strip()
        if identifier not in ids:
            raise ValueError(f"Unknown conformance identifier: {identifier}")

        section_lines: list[str] = []
        cursor = index + 1

        while cursor < len(lines):
            candidate = lines[cursor].strip()
            if candidate.startswith("## "):
                break
            section_lines.append(candidate)
            cursor += 1

        section_checks = [
            item.removeprefix("- ").strip()
            for item in section_lines
            if item.startswith("- ") and not item.startswith("- Fail if:")
        ]

        failure_conditions = [
            item.removeprefix("- Fail if:").strip()
            for item in section_lines
            if item.startswith("- Fail if:")
        ]

        failure_conditions.extend(
            item for item in section_lines if "constitutes non-conformance" in item
        )

        checks.append(
            ConformanceCheck(
                id=identifier,
                checks=section_checks,
                failure_conditions=failure_conditions,
            )
        )

    assert_exact_identifier_coverage(
        canonical_ids=ids,
        found_ids=[check.id for check in checks],
        source_name=config.conformance_file_name,
    )

    return checks


def extract_scope_exclusions(markdown: str, config: SpecConfig) -> list[str]:
    """Extract bullets from the SPEC_ID.SCOPE.EXCLUSIONS section."""
    lines = markdown.splitlines()
    exclusions: list[str] = []
    in_section = False
    heading = f"## {config.spec_id}.SCOPE.EXCLUSIONS"

    for line in lines:
        stripped = line.strip()

        if stripped == heading:
            in_section = True
            continue

        if in_section and stripped.startswith("## "):
            break

        if in_section and stripped.startswith("- "):
            exclusions.append(stripped.removeprefix("- ").strip())

    return exclusions


def spec_metadata(config: SpecConfig, version: str) -> dict[str, str]:
    """Return shared specification metadata."""
    return {
        "id": config.spec_id,
        "name": config.spec_name,
        "version": version,
        "status": config.spec_status,
    }
