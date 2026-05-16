"""Tests for generated data/spec exports."""

from dataclasses import asdict
import json

from judicial_record_spec.export import (
    build_conformance_export,
    build_requirements_export,
    build_scope_exclusions_export,
    canonical_ids,
    export_all,
)
from judicial_record_spec.spec_config import SPEC_CONFIG
from judicial_record_spec.utils.load_utils import load_fallback_version
from judicial_record_spec.utils.path_utils import data_spec_path, repo_root


def test_conformance_export_contains_canonical_identifiers() -> None:
    """conformance-checks.json export includes all canonical identifiers."""
    root = repo_root()
    version = load_fallback_version(root)
    export = build_conformance_export(version=version, root=root)

    exported_ids = [check.id for check in export.checks]

    assert export.schema == "se-boundary-conformance-checks-1"
    assert export.spec["id"] == SPEC_CONFIG.spec_id
    assert export.spec["version"] == version
    assert exported_ids == canonical_ids(root)


def test_conformance_export_has_failure_conditions() -> None:
    """Each conformance export check includes failure conditions."""
    root = repo_root()
    version = load_fallback_version(root)
    export = build_conformance_export(version=version, root=root)

    for check in export.checks:
        assert check.failure_conditions


def test_scope_export_metadata_uses_spec_config() -> None:
    """Generated scope exclusions export uses configured spec metadata."""
    root = repo_root()
    export = build_scope_exclusions_export(version="0.1.0", root=root)

    assert export.spec["id"] == SPEC_CONFIG.spec_id
    assert export.spec["name"] == SPEC_CONFIG.spec_name
    assert export.spec["version"] == "0.1.0"
    assert export.spec["status"] == SPEC_CONFIG.spec_status


def test_conformance_export_metadata_uses_spec_config() -> None:
    """Generated conformance export uses configured spec metadata."""
    root = repo_root()
    export = build_conformance_export(version="0.1.0", root=root)

    assert export.spec["id"] == SPEC_CONFIG.spec_id
    assert export.spec["name"] == SPEC_CONFIG.spec_name
    assert export.spec["version"] == "0.1.0"
    assert export.spec["status"] == SPEC_CONFIG.spec_status


def test_conformance_sections_have_check_items() -> None:
    """Each conformance section has at least one checklist item."""
    root = repo_root()
    export = build_conformance_export(version="0.1.0", root=root)

    missing = [check.id for check in export.checks if not check.checks]

    assert not missing


def test_export_metadata_uses_spec_config() -> None:
    """Generated exports use configured spec metadata."""
    root = repo_root()
    export = build_requirements_export(version="0.1.0", root=root)

    assert export.spec["id"] == SPEC_CONFIG.spec_id
    assert export.spec["name"] == SPEC_CONFIG.spec_name
    assert export.spec["version"] == "0.1.0"
    assert export.spec["status"] == SPEC_CONFIG.spec_status


def test_generated_conformance_checks_json_matches_builder() -> None:
    """conformance-checks.json matches the export builder output."""
    root = repo_root()
    version = load_fallback_version(root)
    path = data_spec_path("conformance-checks.json", root)
    expected = asdict(build_conformance_export(version=version, root=root))
    actual = json.loads(path.read_text(encoding="utf-8"))

    assert actual == expected


def test_generated_exports_are_current() -> None:
    """Generated data/spec JSON files match current Markdown sources."""
    root = repo_root()
    version = load_fallback_version(root)
    export_all(version=version, root=root, check=True)


def test_generated_requirements_json_matches_builder() -> None:
    """requirements.json matches the export builder output."""
    root = repo_root()
    version = load_fallback_version(root)
    path = data_spec_path("requirements.json", root)
    expected = asdict(build_requirements_export(version=version, root=root))
    actual = json.loads(path.read_text(encoding="utf-8"))

    assert actual == expected


def test_generated_scope_exclusions_json_matches_builder() -> None:
    """scope-exclusions.json matches the export builder output."""
    root = repo_root()
    version = load_fallback_version(root)
    path = data_spec_path("scope-exclusions.json", root)
    expected = asdict(build_scope_exclusions_export(version=version, root=root))
    actual = json.loads(path.read_text(encoding="utf-8"))

    assert actual == expected


def test_requirements_export_contains_canonical_identifiers() -> None:
    """requirements.json export includes all canonical identifiers."""
    root = repo_root()
    version = load_fallback_version(root)
    export = build_requirements_export(version=version, root=root)

    exported_ids = [requirement.id for requirement in export.requirements]

    assert export.schema == "se-boundary-requirements-1"
    assert export.spec["id"] == SPEC_CONFIG.spec_id
    assert export.spec["version"] == version
    assert exported_ids == canonical_ids(root)


def test_scope_exclusions_export_is_non_empty() -> None:
    """scope-exclusions.json export contains excluded concerns."""
    root = repo_root()
    version = load_fallback_version(root)
    export = build_scope_exclusions_export(version=version, root=root)

    assert export.schema == "se-boundary-scope-exclusions-1"
    assert export.spec["id"] == SPEC_CONFIG.spec_id
    assert export.spec["version"] == version
    assert export.excluded
    assert "legal advice" in export.excluded


def test_scope_exclusions_include_expected_core_exclusions() -> None:
    """Scope exclusions include required Judicial Record exclusions."""
    root = repo_root()
    export = build_scope_exclusions_export(version="0.1.0", root=root)

    assert "legal advice" in export.excluded
    assert "legal correctness" in export.excluded
    assert "binding authority" in export.excluded
    assert "judicial legitimacy" in export.excluded
    assert "legal research replacement" in export.excluded
