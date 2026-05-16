# judicial-record-spec

[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/judicial-record-spec)
[![Tooling](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/judicial-record-spec/actions/workflows/ci-python.yml/badge.svg?branch=main)](https://github.com/structural-explainability/judicial-record-spec/actions/workflows/ci-python.yml)
[![Links](https://github.com/structural-explainability/judicial-record-spec/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/structural-explainability/judicial-record-spec/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/structural-explainability/judicial-record-spec/security)

> Judicial accountable record system for opinions, claims,
> holdings, citations, dependencies, and later treatment.

## Overview

Judicial Record defines a domain record system for representing judicial
decisions and related legal reasoning artifacts as durable, inspectable records.

Judicial Record records:

- claims made in opinions
- holdings declared in decisions
- citations to authorities
- dependencies among citations
- later treatment of decisions
- source spans for traceable references
- review status and procedural history

Judicial Record does not determine legal correctness, provide legal advice,
or replace court records, legal citators, or legal research platforms.

## Purpose

The purpose of Judicial Record is to provide a durable record structure for
judicial reasoning and dependency.

Judicial Record defines constraints on:

- case records
- decision records
- opinion records
- claim records
- holding records
- citation records
- dependency records
- later treatment records
- source spans
- review status
- rendered reports

These constraints exist to prevent specific failure modes
that arise when legal information systems collapse
distinct categories of record into one:

- treating citation as dependency
- treating dependency as legal validity
- treating later treatment as erasure
- treating authority as correctness
- treating explanation as proof
- recording majority claims as system commitments

## Versioning and Stability

Current versions are pre-v1.
The contract is being co-developed with its
implementations and verifiers;
dependencies track main during this phase.
Versioned releases will follow once the contract stabilizes.

v1 will commit to:

- the judicial record model shape
- claim vs. holding distinction
- citation vs. dependency distinction
- later treatment recording as additive
- record-vs-report relationship

v1 does not claim closure over legal meaning, doctrine, authority,
or future judicial interpretation.

## Extension Policy

Extension policy applies once v1 stabilizes.
Until then, the contract is in active development
and changes occur on main.
Extension is permitted under a new version of the record model
or through declared profile extensions.

Any extension MUST:

- preserve conformance with the Accountable Record contract
- preserve source traceability
- preserve the distinction between citation and dependency
- preserve the distinction between later treatment and historical rewrite
- preserve the distinction between legal reasoning records and legal correctness
- declare prohibited inferences for new record types or fields
- be explicit, traceable, and verifiable

## Scope

This system defines:

- case, decision, and opinion records
- claim and holding records
- citation and dependency records
- later treatment records
- source span and review status conventions
- human-readable judicial record reports
- export bundles for verification

This system does NOT define:

- legal advice
- legal correctness
- binding authority
- judicial legitimacy
- automatic legal reasoning
- legal outcome prediction
- replacements for court record publication or legal research platforms

## Relationship to Other Work

- Judicial Record implements the Accountable Record contract for judicial materials.
- Other implementations could organize judicial records differently
  while still satisfying the contract.
- Judicial Record may consume public court records, legal metadata, or citation data.
- Judicial Record may interoperate with legal-informatics standards such as
  Akoma Ntoso, LegalRuleML, and ELI,
  or consume data from sources such as
  CourtListener, court websites, and citator services.
- Judicial Record does not replace those standards or services.
- Judicial Record produces export bundles that may be checked by
  `se-verification-judicial-record-spec`.
- SE verification checks whether Judicial Record preserves SE-relevant
  distinctions without determining legal correctness.

## Clarifying Statement

Judicial Record records the structure of legal reasoning,
not its correctness.

A judicial record may show that an opinion cited an authority, relied on a
holding, or was later treated by another decision.
It does not assert that the reasoning was correct, that the authority was
legitimate, that the outcome was justified, or that later treatment erases
the historical record.

Judicial Record exists so that judicial reasoning and dependency can remain
inspectable across disagreement, reinterpretation, and time.

## Repository Contents

- [README.md](./README.md) - Project overview
- [DECISIONS.md](./DECISIONS.md) - Founding design decisions
- [RECORD_MODEL.md](./RECORD_MODEL.md) - Judicial record model
- [EXPORTS.md](./EXPORTS.md) - Export bundle description
- [ANNOTATIONS.md](./ANNOTATIONS.md) - Annotation standards
- [LICENSE](./LICENSE) - Licensing terms
- [CITATION.cff](./CITATION.cff) - Citation metadata
- [CHANGELOG.md](./CHANGELOG.md) - Version history
- [data/examples](./data/examples) - Example judicial records
- [data/records](./data/records) - Record fixtures
- [data/exports](./data/exports) - Verification-ready exports

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/structural-explainability/judicial-record-spec

cd judicial-record-spec
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv sync --extra dev --extra docs --upgrade

# install git hooks once per clone
uvx pre-commit install

# autofix and manual fix issues
git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# validate Markdown sources and generated specification artifacts
uv run se-validate

# generate machine-readable specification artifacts under data/spec/
uv run se-ref-export

# check that generated data/spec/ artifacts are current
uv run se-ref-export --check

# validate reference artifacts and registry consistency
uv run se-ref-validate

# run strict validation, including all standard source and export checks
uv run se-validate --strict

# do chores
uv run python -m pyright
uv run python -m pytest

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)

## Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)
