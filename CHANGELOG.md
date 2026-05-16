# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

---

## [0.1.0] - 2026-05-16

### Added

- Initial working draft specification.
- Stable requirement identifiers.
- Conformance checklist.
- Repository structure, citation metadata, and licensing.
- Python validation and export utilities for specification consistency checks.
- Generated `data/spec/` artifacts for requirements, conformance checks, and scope exclusions.
- Tests for identifier extraction, specification coverage, conformance coverage,
  generated export consistency, and reusable export utilities.
- Shared command entry points for validation, reference export, reference validation,
  and manifest version synchronization.
- Shared specification configuration for repository identity, source file names,
  normative source metadata, export schemas, and generated artifact metadata.
- Reusable Markdown extraction, export, load, path, orchestration, and reference utilities.
- Working draft support for Accountable Record systems and SE verification profiles.

---

## Notes on Versioning and Releases

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

- **MAJOR** versions indicate breaking changes to normative requirements,
  identifiers, or conformance criteria.
- **MINOR** versions indicate backward-compatible additions or clarifications.
- **PATCH** versions indicate editorial fixes, documentation updates, or
  non-normative changes.

Versions are defined by git tags of the form `vX.Y.Z`.
Tagged releases are the authoritative source of version state.

Documentation and badges, where present, should reference the latest tagged
release.

## Release Procedure (Required)

Follow these steps exactly when creating a new release.

### Task 1. Update release metadata (manual edits)

1.1. `CITATION.cff` - update `version` and `date-released`
1.2. CHANGELOG.md: add section, move unreleased entries, update links

### Task 2. Sync and Validate

```shell
uv run se-manifest-version-sync
uv pip uninstall se-manifest-schema
uv cache clean se-manifest-schema
uv sync --extra dev --extra docs --upgrade

uv run se-validate
uv run se-ref-export
uv run se-ref-export --check
uv run se-ref-validate
uv run se-validate --strict

git add -A
uvx pre-commit run --all-files
uv run python -m pyright
uv run python -m pytest
git add -A
uvx pre-commit run --all-files
```

### Task 3. Commit, tag, push

```shell
git add -A
git commit -m "Prep X.Y.Z"
git push -u origin main
```

Verify actions run on GitHub. After success:

```shell
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

### Task 4. Verify tag consistency

```shell
uv run python -m se_manifest_schema validate --strict --require-tag
```

Confirms CITATION.cff version matches the pushed git tag.
Run this after `git push origin vX.Y.Z`; it will fail before that point.

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/structural-explainability/judicial-record/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/structural-explainability/judicial-record/releases/tag/v0.1.0
