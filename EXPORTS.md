# Judicial Record Exports

Status: Working Draft

This document describes the export structure produced by `judicial-record-spec`
for validation, inspection, and SE verification.

Judicial Record exports are designed to make judicial records portable,
inspectable, and verifiable without requiring downstream systems to reuse the
internal implementation.

## Export Purpose

Exports provide machine-readable evidence of the record system's structure.

They support:

- record inspection
- source traceability
- citation and dependency inspection
- later treatment inspection
- provenance inspection
- conformance checking
- SE verification
- derived reporting
- cross-system review

Exports do not determine:

- legal correctness
- legal advice
- binding authority
- judicial legitimacy
- substantive merit of any judicial reasoning
- predicted legal outcome
- recommendation or decision outcome

## Export Directory

Generated and curated exports should live under:

```text
data/exports/
```

Specification-level generated artifacts live under:

```text
data/spec/
```

Example structure:

```text
data/
  spec/
    requirements.json
    conformance-checks.json
    scope-exclusions.json
  examples/
    example-judicial-record-specs.json
  records/
    example-records.json
  exports/
    judicial-record-spec-bundle.json
```

## Export Bundle

The primary export artifact is a judicial record bundle.

Suggested filename:

```text
data/exports/judicial-record-spec-bundle.json
```

Suggested top-level shape:

```json
{
  "schema": "judicial-record-spec-bundle-1",
  "bundle_id": "jr-bundle:example",
  "generated_at": "2026-05-16",
  "versions": {
    "judicial_record_spec": "0.1.0",
    "accountable_record": "0.1.0"
  },
  "conformance": {
    "jr": true,
    "ar": true,
    "se": true
  },
  "manifest": {
    "record_count": 0,
    "record_type_counts": {}
  },
  "records": []
}
```

## Required Bundle Fields

A judicial record bundle must identify:

- bundle schema
- bundle identifier
- generation time where available
- JR version
- AR version
- conformance declarations
- record manifest
- included records

## Manifest

The manifest summarizes the bundle contents.

Example:

```json
{
  "record_count": 8,
  "record_type_counts": {
    "source_record": 1,
    "case_record": 1,
    "decision_record": 1,
    "opinion_record": 1,
    "claim_record": 1,
    "holding_record": 1,
    "citation_record": 1,
    "source_span_reference": 1
  }
}
```

The manifest is used for integrity checks. It does not define the meaning of
the records.

## Records Array

The `records` array contains the exported judicial records.

Example:

```json
{
  "records": [
    {
      "id": "source:courtlistener:opinion:example",
      "record_type": "source_record",
      "source_system": "CourtListener",
      "source_identifier": "example"
    },
    {
      "id": "case:example-court:2024:001",
      "record_type": "case_record",
      "case_name": "Example v. Example",
      "issuing_court_ref": "court:example-court",
      "source_refs": ["source:courtlistener:case:example"]
    }
  ]
}
```

Each record must declare its record type.

## Source References

Records that depend on source material should include stable source references.

Example:

```json
{
  "source_refs": [
    "source:courtlistener:opinion:example"
  ]
}
```

Source references identify source material. They do not assert that source
content is correct, complete, current, or authoritative by default.

## Source Span References

Records that reference specific locations within source documents should
include source span references rather than ambiguous citations.

Example:

```json
{
  "source_refs": [
    "source-span:opinion:example:para:12"
  ]
}
```

Source span references identify specific locations within a source document.
They remain distinct from interpretations of the referenced text.

## Provenance References

Derived records should include provenance references where provenance is
available or required.

Example:

```json
{
  "provenance_refs": [
    "provenance:source:opinion:example"
  ]
}
```

Provenance describes how a record was produced. It does not certify
correctness, completeness, authority, legitimacy, binding effect, or
substantive merit.

## Review Status

Records may include review status directly or through review status records.

Inline example:

```json
{
  "id": "opinion:case:example-court:2024:001:majority",
  "record_type": "opinion_record",
  "review_status": "curated"
}
```

Separate record example:

```json
{
  "id": "review-status:opinion:case:example-court:2024:001:majority",
  "record_type": "review_status_record",
  "record_ref": "opinion:case:example-court:2024:001:majority",
  "status": "curated"
}
```

Review status does not assert correctness, legitimacy, or binding authority of
the underlying record.

## Citation and Dependency Exports

Citation records and dependency records must remain distinct in the export.

Citation example:

```json
{
  "id": "citation:opinion:example:to:precedent:001",
  "record_type": "citation_record",
  "citing_record_ref": "opinion:case:example-court:2024:001:majority",
  "cited_authority_ref": "case:precedent-court:2010:042",
  "citation_text": "Example v. Precedent, 100 Example 42 (2010)"
}
```

Dependency example:

```json
{
  "id": "dependency:opinion:example:on:precedent:001",
  "record_type": "dependency_record",
  "record_slug": "example-case-slug",
  "source_id": "source:opinion:example",
  "citation_id": "citation:opinion:example:to:precedent:001",
  "dependency_type": "precedent-binding",
  "supports": [
    "holding:decision:example:001"
  ],
  "status": "draft"
}
```

A citation record asserts that a reference was made.
A dependency record asserts that one or more judicial records rely on a
citation in a declared way, with the kind of reliance declared as the
dependency type.
These are separate records.

## Later Treatment Exports

Later treatment records must be recorded additively and must not modify the
treated records.

Example:

```json
{
  "id": "later-treatment:precedent:001:by:later-decision:002",
  "record_type": "later_treatment_record",
  "treating_record_ref": "decision:later-court:2024:002",
  "treated_record_ref": "case:precedent-court:2010:042",
  "treatment_type": "distinguished",
  "treatment_text": "Example treatment description."
}
```

Later treatment is additive history. It does not erase or rewrite the treated
record.

## Claim and Holding Exports

Claim records and holding records must remain distinct in the export.

Claim example:

```json
{
  "id": "claim:opinion:example:001",
  "record_type": "claim_record",
  "opinion_ref": "opinion:case:example-court:2024:001:majority",
  "claim_text": "Example legal claim text drawn from the opinion.",
  "source_refs": ["source-span:opinion:example:para:12"]
}
```

Holding example:

```json
{
  "id": "holding:decision:example:001",
  "record_type": "holding_record",
  "decision_ref": "decision:case:example-court:2024:001",
  "holding_text": "Example holding text drawn from the decision.",
  "source_refs": ["source-span:opinion:example:para:34"]
}
```

A claim is what the opinion says.
A holding is what the decision decides.
These are separate records.

## Interpretation Exports

Systems that record interpretive readings of judicial materials should export
interpretation records separately from claim, holding, citation, and
dependency records.

Example:

```json
{
  "id": "interpretation:example-doctrinal-reading",
  "record_type": "interpretation_record",
  "interpretive_inference_type": "doctrinal reading",
  "depends_on_record_refs": [
    "opinion:case:example-court:2024:001:majority",
    "holding:decision:example:001"
  ],
  "asserting_actor": "analyst:example"
}
```

An interpretation record does not become a claim, holding, citation, or
dependency record.

## Export Validation

An export is valid when:

- required bundle fields are present
- record identifiers are stable and unique
- record types are declared
- referenced records resolve within the bundle or to declared external sources
- manifest counts match included records
- JR and AR versions are declared
- citation records and dependency records are distinguishable
- claim records and holding records are distinguishable
- later treatment records are recorded additively
- interpretation records do not mutate substrate records
- provenance records do not certify source correctness
- citation records do not imply correctness of the cited authority

## Verification Handoff

The export bundle is the handoff artifact for:

```text
se-verification-judicial-record-spec
```

The verifier checks whether the exported bundle preserves the distinctions
required by JR, AR, and SE.

Verification may check:

- source traceability
- record type declarations
- citation and dependency separation
- claim and holding separation
- later treatment additivity
- authority and correctness separation
- explanation and proof separation
- majority claim non-commitment
- interpretation non-mutation
- source provenance chain discipline
- export bundle integrity

## Generated Specification Artifacts

The repository also exports generated specification artifacts under:

```text
data/spec/
```

Expected artifacts:

```text
data/spec/requirements.json
data/spec/conformance-checks.json
data/spec/scope-exclusions.json
```

These artifacts are generated from:

```text
SPEC.md
IDENTIFIERS.md
CONFORMANCE.md
```

They support consistency checks and machine-readable inspection of the
specification itself.

## Clarifying Statement

A judicial record export makes records inspectable.

It does not certify legal correctness, prove binding authority, establish
judicial legitimacy, or determine the substantive merit of any reasoning.
Those questions may be represented as explicit claims or interpretations, but
they remain separate from source-backed records, citations, and holdings.
