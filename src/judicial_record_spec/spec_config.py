"""spec_config.py - specification identity and export configuration."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SpecConfig:
    """Configuration for generated specification artifacts."""

    spec_id: str
    spec_name: str
    spec_status: str

    identifiers_file_name: str = "IDENTIFIERS.md"
    spec_file_name: str = "SPEC.md"
    conformance_file_name: str = "CONFORMANCE.md"

    requirements_schema: str = "se-boundary-requirements-1"
    scope_exclusions_schema: str = "se-boundary-scope-exclusions-1"
    conformance_schema: str = "se-boundary-conformance-checks-1"

    @property
    def normative_source_file_name(self) -> str:
        """Return the Markdown file containing normative requirement sections."""
        return self.spec_file_name


SPEC_CONFIG = SpecConfig(
    spec_id="JR",
    spec_name="Judicial Record",
    spec_status="working-draft",
)
