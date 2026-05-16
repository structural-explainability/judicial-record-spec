"""Export generated machine-readable specification artifacts."""

from pathlib import Path

from judicial_record_spec.spec_config import SPEC_CONFIG
from judicial_record_spec.utils.export_utils import (
    ConformanceCheck,
    ConformanceExport,
    RequirementExport,
    ScopeExclusionExport,
)
from judicial_record_spec.utils.export_utils import (
    build_conformance_export as _build_conformance_export,
)
from judicial_record_spec.utils.export_utils import (
    build_requirements_export as _build_requirements_export,
)
from judicial_record_spec.utils.export_utils import (
    build_scope_exclusions_export as _build_scope_exclusions_export,
)
from judicial_record_spec.utils.export_utils import (
    canonical_ids as _canonical_ids,
)
from judicial_record_spec.utils.export_utils import (
    canonical_requirements as _canonical_requirements,
)
from judicial_record_spec.utils.export_utils import (
    export_all as _export_all,
)
from judicial_record_spec.utils.export_utils import (
    extract_conformance_checks as _extract_conformance_checks,
)
from judicial_record_spec.utils.export_utils import (
    extract_scope_exclusions as _extract_scope_exclusions,
)


def canonical_requirements(root: Path | None = None):
    """Return canonical requirements from IDENTIFIERS.md."""
    return _canonical_requirements(SPEC_CONFIG, root)


def canonical_ids(root: Path | None = None) -> list[str]:
    """Return canonical requirement identifiers."""
    return _canonical_ids(SPEC_CONFIG, root)


def build_requirements_export(
    *,
    version: str,
    root: Path | None = None,
) -> RequirementExport:
    """Build requirements.json content."""
    return _build_requirements_export(SPEC_CONFIG, version=version, root=root)


def extract_scope_exclusions(markdown: str) -> list[str]:
    """Extract bullets from the SPEC_ID.SCOPE.EXCLUSIONS section."""
    return _extract_scope_exclusions(markdown, SPEC_CONFIG)


def build_scope_exclusions_export(
    *,
    version: str,
    root: Path | None = None,
) -> ScopeExclusionExport:
    """Build scope-exclusions.json content."""
    return _build_scope_exclusions_export(SPEC_CONFIG, version=version, root=root)


def extract_conformance_checks(
    markdown: str,
    ids: list[str],
) -> list[ConformanceCheck]:
    """Extract check bullets and failure conditions from CONFORMANCE.md."""
    return _extract_conformance_checks(markdown, ids, SPEC_CONFIG)


def build_conformance_export(
    *,
    version: str,
    root: Path | None = None,
) -> ConformanceExport:
    """Build conformance-checks.json content."""
    return _build_conformance_export(SPEC_CONFIG, version=version, root=root)


def export_all(
    *,
    version: str,
    root: Path | None = None,
    check: bool = False,
) -> list[Path]:
    """Generate or check all data/spec JSON artifacts."""
    return _export_all(SPEC_CONFIG, version=version, root=root, check=check)
