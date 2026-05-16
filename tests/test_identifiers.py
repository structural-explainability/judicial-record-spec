"""Tests for canonical requirement identifiers."""

from judicial_record_spec.spec_config import SPEC_CONFIG
from judicial_record_spec.utils.extractor_utils import extract_identifier_notes
from judicial_record_spec.utils.load_utils import load_text
from judicial_record_spec.utils.path_utils import repo_root


def test_each_identifier_has_one_note() -> None:
    """Each canonical identifier has one non-empty note."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / SPEC_CONFIG.identifiers_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    for requirement in requirements:
        assert requirement.note
        assert (
            requirement.normative_source
            == f"{SPEC_CONFIG.normative_source_file_name}#{requirement.id}"
        )


def test_identifiers_are_alphabetical() -> None:
    """Canonical identifiers are listed alphabetically."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / SPEC_CONFIG.identifiers_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    identifiers = [requirement.id for requirement in requirements]

    assert identifiers == sorted(identifiers)


def test_identifiers_are_extractable() -> None:
    """IDENTIFIERS.md contains extractable canonical identifiers."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / SPEC_CONFIG.identifiers_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    assert requirements


def test_identifiers_are_unique() -> None:
    """Canonical identifiers are unique."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / SPEC_CONFIG.identifiers_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    identifiers = [requirement.id for requirement in requirements]

    assert len(identifiers) == len(set(identifiers))


def test_identifiers_use_expected_prefix() -> None:
    """All canonical identifiers use the prefix."""
    root = repo_root()
    requirements = extract_identifier_notes(
        load_text(root / SPEC_CONFIG.identifiers_file_name),
        expected_prefix=SPEC_CONFIG.spec_id,
    )

    for requirement in requirements:
        assert requirement.id.startswith(SPEC_CONFIG.spec_id)
