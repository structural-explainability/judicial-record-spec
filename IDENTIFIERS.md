# Judicial Record Identifiers (JR)

This document defines the stable requirement identifiers used by the
Judicial Record (JR) specification.

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

## Overview

Defines domain profile identifiers for judicial accountable record systems.

JR represents judicial reasoning artifacts including cases, decisions,
opinions, claims, holdings, citations, dependencies, later treatment,
source spans, and review status.

JR does not define legal correctness, legal advice, binding authority,
judicial legitimacy, court record publication, or legal research replacement.

## Identifier Semantics and Ordering

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

Identifiers are listed in strict alphabetical order to remove editorial
discretion and ensure deterministic placement.

## Identifier Naming Rules

All identifiers follow this pattern:

All identifiers begin with `JR.` and use uppercase dot-separated semantic terms.

Identifiers are:

- semantic, not positional
- stable across versions
- reusable across prose, code, reports, and verification traces
- language-agnostic
- suitable for direct mapping to verification rule names

Identifiers MUST NOT be renamed or repurposed.
New identifiers MAY be added only in a new major version of this document.

## Identifier Notes

Each identifier MUST be followed by exactly one note.

- The note MUST be expressed as a single bullet.
- The bullet text MAY wrap across lines.
- No additional bullets, sublists, or structural markers are permitted.
- Notes are explanatory only and do not introduce additional requirements.

## Canonical Identifier List (Alphabetical, with Notes)

JR.CASE.RECORD

- Defines case records as procedural units within which judicial decisions and opinions occur.

JR.CITATION.RECORD

- Defines citation records as references from an opinion or decision to an authority.

JR.CLAIM.RECORD

- Defines claim records as assertions made within an opinion.

JR.COLLAPSE.PROHIBITED

- Prohibits judicial category collapses such as citation-to-dependency or claim-to-holding.

JR.CONFORMANCE.AR.REQUIRED

- Requires conformance with Accountable Record.

JR.CONFORMANCE.SE.REQUIRED

- Requires conformance with Structural Explainability.

JR.DECISION.RECORD

- Defines decision records as dispositions of cases by courts.

JR.DEFINITION.CORE

- Defines JR as the judicial domain profile of AR.

JR.DEPENDENCY.RECORD

- Defines dependency records as declared reliance of one or more judicial
  records on a cited authority through a specific source.

JR.HOLDING.RECORD

- Defines holding records as controlling determinations of decisions.

JR.LATER_TREATMENT.RECORD

- Defines later treatment records as additive records of subsequent treatment.

JR.OPINION.RECORD

- Defines opinion records as reasoning offered in support of decisions.

JR.REVIEW_STATUS.RECORD

- Defines review status records for procedural posture with respect to review.

JR.SCOPE.EXCLUSIONS

- Defines what JR explicitly does not specify.

JR.SOURCE_SPAN.REFERENCE

- Defines source span references to locations within source documents.

JR.VERSIONING

- Defines JR versioning requirements.

## Cross-Artifact Consistency Rule

Each identifier in this list MUST appear:

- exactly once in SPEC.md
- exactly once in CONFORMANCE.md
- exactly once in generated requirements artifacts
- exactly once in generated conformance-check artifacts where applicable

Alphabetical order SHOULD be preserved across all artifacts.
