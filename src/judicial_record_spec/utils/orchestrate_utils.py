"""orchestrate_utils.py - validation orchestration helpers."""

from pathlib import Path

from judicial_record_spec.export import export_all
from judicial_record_spec.validate import validate_all


def run_ref_export(
    *,
    version: str,
    root: Path | None = None,
    check: bool = False,
) -> list[Path]:
    """Run reference export checks.

    Reference export means generated data/spec artifacts.
    """
    return export_all(version=version, root=root, check=check)


def run_ref_validate(
    *,
    version: str,
    root: Path | None = None,
) -> None:
    """Validate generated reference artifacts."""
    export_all(version=version, root=root, check=True)


def run_validate(
    *,
    version: str,
    root: Path | None = None,
    strict: bool = False,
) -> None:
    """Run validation checks."""
    validate_all(version=version, root=root)

    if strict:
        export_all(version=version, root=root, check=True)
