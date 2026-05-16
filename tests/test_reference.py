"""Tests for reference artifact validation helpers."""

from pathlib import Path
from typing import Final

from judicial_record.reference import (
    _ArtifactResult,
    _kind_to_section,
    _make_stub,
    _merge,
    _process_artifact,
)
from judicial_record.utils.ref_utils import LeanDecl

EXAMPLE_ARTIFACT_ID: Final[str] = "example"
EXAMPLE_CORE_MODULE: Final[str] = "Example.Core"
EXAMPLE_REFACTORED_MODULE: Final[str] = "Example.Refactored"
EXAMPLE_SURFACE_MODULE: Final[str] = "Example.Surface"
EXAMPLE_TYPE_NAME: Final[str] = "ExampleType"
EXAMPLE_THEOREM_NAME: Final[str] = "example_theorem"
EXAMPLE_CITE_ID: Final[str] = "AR.EXAMPLE"
EXAMPLE_OLD_CITE_ID: Final[str] = "AR.OLD"
EXAMPLE_NEW_CITE_ID: Final[str] = "AR.NEW"
SKIPPED_GENERATED_OR_NON_TOML: Final[str] = "skipped (generated or non-toml)"


def test_artifact_result_records_failure() -> None:
    """Artifact results record failures and mark the result as not ok."""
    result = _ArtifactResult(artifact_id=EXAMPLE_ARTIFACT_ID)

    result.fail("broken artifact")

    assert not result.ok
    assert result.messages
    assert "FAIL" in result.messages[0]
    assert "broken artifact" in result.messages[0]


def test_artifact_result_records_warning() -> None:
    """Artifact results record warnings without failing the result."""
    result = _ArtifactResult(artifact_id=EXAMPLE_ARTIFACT_ID)

    result.warn("check this")

    assert result.ok
    assert result.messages
    assert "warn" in result.messages[0]
    assert "check this" in result.messages[0]


def test_kind_to_section_removes_registry_suffix() -> None:
    """Artifact kinds map to their terminal registry section."""
    assert _kind_to_section("substrate-type-registry") == "type"
    assert _kind_to_section("se-theorem-registry") == "theorem"
    assert _kind_to_section("requirement-registry") == "requirement"


def test_kind_to_section_handles_non_registry_kind() -> None:
    """Artifact kinds without registry suffix still map to their terminal token."""
    assert _kind_to_section("source-definitions") == "definitions"
    assert _kind_to_section("type") == "type"


def test_make_stub_for_type_decl() -> None:
    """Stub generation preserves Lean declaration identity."""
    decl = LeanDecl(
        name=EXAMPLE_TYPE_NAME,
        kind="structure",
        section="type",
    )

    stub = _make_stub(decl, EXAMPLE_CORE_MODULE)

    assert stub == {
        "id": EXAMPLE_TYPE_NAME,
        "cite_id": "",
        "name": "",
        "lean_symbol": EXAMPLE_TYPE_NAME,
        "source_module": EXAMPLE_CORE_MODULE,
        "description": "",
    }


def test_make_stub_for_theorem_includes_status() -> None:
    """Theorem stubs include a pending status."""
    decl = LeanDecl(
        name=EXAMPLE_THEOREM_NAME,
        kind="theorem",
        section="theorem",
    )

    stub = _make_stub(decl, EXAMPLE_CORE_MODULE)

    assert stub["id"] == EXAMPLE_THEOREM_NAME
    assert stub["lean_symbol"] == EXAMPLE_THEOREM_NAME
    assert stub["source_module"] == EXAMPLE_CORE_MODULE
    assert stub["status"] == "pending"


def test_merge_preserves_existing_human_fields_when_not_placeholder() -> None:
    """Merge preserves populated human-authored fields unless overwrite is true."""
    existing = {
        "id": EXAMPLE_TYPE_NAME,
        "cite_id": EXAMPLE_CITE_ID,
        "name": "Example type",
        "lean_symbol": EXAMPLE_TYPE_NAME,
        "source_module": EXAMPLE_CORE_MODULE,
        "description": "Human description.",
    }
    stub = {
        "id": EXAMPLE_TYPE_NAME,
        "cite_id": "",
        "name": "",
        "lean_symbol": EXAMPLE_TYPE_NAME,
        "source_module": EXAMPLE_REFACTORED_MODULE,
        "description": "",
    }

    merged = _merge(existing, stub, overwrite=False)

    assert merged["cite_id"] == EXAMPLE_CITE_ID
    assert merged["name"] == "Example type"
    assert merged["description"] == "Human description."
    assert merged["source_module"] == EXAMPLE_CORE_MODULE


def test_merge_fills_placeholder_human_fields() -> None:
    """Merge fills placeholder human-authored fields from the stub."""
    existing = {
        "id": EXAMPLE_TYPE_NAME,
        "cite_id": "",
        "name": "",
        "lean_symbol": EXAMPLE_TYPE_NAME,
        "source_module": EXAMPLE_CORE_MODULE,
        "description": "",
    }
    stub = {
        "id": EXAMPLE_TYPE_NAME,
        "cite_id": EXAMPLE_CITE_ID,
        "name": "Example type",
        "lean_symbol": EXAMPLE_TYPE_NAME,
        "source_module": EXAMPLE_CORE_MODULE,
        "description": "Human description.",
    }

    merged = _merge(existing, stub, overwrite=False)

    assert merged["cite_id"] == EXAMPLE_CITE_ID
    assert merged["name"] == "Example type"
    assert merged["description"] == "Human description."


def test_merge_overwrites_when_requested() -> None:
    """Merge overwrites existing fields when overwrite is true."""
    existing = {
        "id": "Old",
        "cite_id": EXAMPLE_OLD_CITE_ID,
        "name": "Old name",
        "lean_symbol": "Old",
        "source_module": "Old.Core",
        "description": "Old description.",
    }
    stub = {
        "id": "New",
        "cite_id": EXAMPLE_NEW_CITE_ID,
        "name": "New name",
        "lean_symbol": "New",
        "source_module": "New.Core",
        "description": "New description.",
    }

    merged = _merge(existing, stub, overwrite=True)

    assert merged == stub


def test_process_artifact_skips_generated_artifact(tmp_path: Path) -> None:
    """Generated artifacts are skipped without requiring Lean files."""
    artifact = {
        "id": "requirements-json",
        "path": "reference/requirements.json",
        "format": "json",
        "generated": True,
        "kind": "requirement-registry",
    }

    result = _process_artifact(
        artifact,
        repo_root=tmp_path,
        lean_root=tmp_path,
        index_surface_module=EXAMPLE_SURFACE_MODULE,
        dry_run=True,
        overwrite=False,
    )

    assert result.ok
    assert not result.wrote
    assert result.messages
    assert SKIPPED_GENERATED_OR_NON_TOML in result.messages[0]


def test_process_artifact_skips_non_toml_artifact(tmp_path: Path) -> None:
    """Non-TOML artifacts are skipped without requiring Lean files."""
    artifact = {
        "id": "report",
        "path": "reference/report.md",
        "format": "markdown",
        "generated": False,
        "kind": "report",
    }

    result = _process_artifact(
        artifact,
        repo_root=tmp_path,
        lean_root=tmp_path,
        index_surface_module=EXAMPLE_SURFACE_MODULE,
        dry_run=True,
        overwrite=False,
    )

    assert result.ok
    assert not result.wrote
    assert result.messages
    assert SKIPPED_GENERATED_OR_NON_TOML in result.messages[0]
