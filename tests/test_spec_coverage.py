"""Tests for SPEC.md requirement coverage."""

from judicial_record_spec.spec_config import SPEC_CONFIG
from judicial_record_spec.utils.extractor_utils import (
    assert_alphabetical_order,
    assert_exact_identifier_coverage,
    extract_heading_identifiers,
    extract_identifier_notes,
)
from judicial_record_spec.utils.load_utils import load_text
from judicial_record_spec.utils.path_utils import repo_root


def test_spec_covers_all_canonical_identifiers() -> None:
    """SPEC.md contains exactly the canonical requirement identifiers."""
    root = repo_root()

    requirements = extract_identifier_notes(
        load_text(root / SPEC_CONFIG.identifiers_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )
    canonical_ids = [requirement.id for requirement in requirements]

    spec_ids = extract_heading_identifiers(
        load_text(root / SPEC_CONFIG.spec_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    assert_exact_identifier_coverage(
        canonical_ids=canonical_ids,
        found_ids=spec_ids,
        source_name=SPEC_CONFIG.spec_file_name,
    )


def test_spec_has_no_duplicate_identifier_headings() -> None:
    """SPEC.md has no duplicate requirement headings."""
    root = repo_root()

    spec_ids = extract_heading_identifiers(
        load_text(root / SPEC_CONFIG.spec_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    assert len(spec_ids) == len(set(spec_ids))


def test_spec_has_non_empty_identifier_sections() -> None:
    """Each SPEC.md requirement heading has section content."""
    root = repo_root()
    spec_text = load_text(root / SPEC_CONFIG.spec_file_name)
    spec_ids = extract_heading_identifiers(
        spec_text, expected_prefix=SPEC_CONFIG.spec_id
    )

    for index, identifier in enumerate(spec_ids):
        section_start = spec_text.index(f"## {identifier}")
        if index + 1 < len(spec_ids):
            section_end = spec_text.index(f"## {spec_ids[index + 1]}")
        else:
            section_end = len(spec_text)

        section_text = spec_text[section_start:section_end].strip()

        assert section_text
        assert section_text != f"## {identifier}"


def test_spec_identifier_headings_are_alphabetical() -> None:
    """SPEC.md requirement headings are alphabetical."""
    root = repo_root()

    spec_ids = extract_heading_identifiers(
        load_text(root / SPEC_CONFIG.spec_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    assert_alphabetical_order(spec_ids, source_name=SPEC_CONFIG.spec_file_name)
