# Judicial Record Model

Status: Working Draft

This document defines the working record model for `judicial-record-spec`.

Judicial Record (JR) is an Accountable Record domain profile for judicial
reasoning and dependency.
It records cases, decisions, opinions, claims, holdings, citations,
dependencies, later treatment, source spans, review status, claims,
interpretations, provenance, and reports without asserting legal correctness,
binding authority, judicial legitimacy, or the substantive merit of any
judicial reasoning.

## Model Purpose

The purpose of this record model is to make judicial reasoning and dependency
inspectable without collapsing source records, citations, dependencies, and
later treatment into stronger interpretive claims.

The model supports:

- stable identity-bearing records
- source-span-backed claim and holding records
- explicit citation and dependency separation
- additively recorded later treatment
- declared opinion types
- derived reports that do not replace underlying records
- export bundles suitable for SE verification

The model does not define:

- legal advice
- legal correctness
- binding authority
- judicial legitimacy
- court record publication
- legal research replacement
- automatic legal reasoning
- legal outcome prediction

## Record Model Overview

Judicial Record uses the following primary record families:

- source records
- case records
- decision records
- opinion records
- claim records
- holding records
- citation records
- dependency records
- later treatment records
- source span references
- review status records
- claim records
- interpretation records
- provenance records
- report records

Each record must have a stable identifier, a declared record type, and enough
source or provenance information to support inspection and verification.

## Common Record Fields

All judicial records should use this common structure where applicable:

```json
{
  "id": "jr:record:example",
  "record_type": "example_record",
  "schema_version": "0.1.0",
  "created_at": "2026-05-16",
  "updated_at": "2026-05-16",
  "source_refs": [],
  "provenance_refs": [],
  "review_status": "draft",
  "notes": []
}
```

Common fields:

- `id`: stable record identifier
- `record_type`: declared record type
- `schema_version`: JR record model version
- `created_at`: record creation date where available
- `updated_at`: last update date where available
- `source_refs`: source records or source spans supporting the record
- `provenance_refs`: provenance records describing derivation
- `review_status`: review status value
- `notes`: non-normative implementation notes

Common fields do not imply that all records have the same meaning.
The declared `record_type` controls the role of the record.

## Source Record

A source record identifies an external source, document, court record,
reporter, database entry, or other material used by the system.

```json
{
  "id": "source:courtlistener:opinion:example",
  "record_type": "source_record",
  "source_system": "CourtListener",
  "source_identifier": "example",
  "source_url": "https://example.invalid/source",
  "retrieved_at": "2026-05-16",
  "description": "Example source opinion text."
}
```

A source record:

- identifies source material
- remains distinct from interpretations of that source
- does not assert that source content is correct, complete, current, or
  authoritative by default

## Case Record

A case record represents the procedural unit within which judicial decisions
and opinions occur.

```json
{
  "id": "case:example-court:2024:001",
  "record_type": "case_record",
  "case_name": "Example v. Example",
  "case_number": "2024-001",
  "issuing_court_ref": "court:example-court",
  "filed_date": "2024-01-15",
  "source_refs": ["source:courtlistener:case:example"]
}
```

A case record:

- conforms to `JR.CASE.RECORD`
- uses a stable identifier
- identifies the issuing court or tribunal
- remains distinct from decision and opinion records
- does not assert legal correctness or outcome legitimacy

## Decision Record

A decision record represents the disposition of a case by a court.

```json
{
  "id": "decision:case:example-court:2024:001",
  "record_type": "decision_record",
  "case_ref": "case:example-court:2024:001",
  "deciding_court_ref": "court:example-court",
  "decided_date": "2024-10-15",
  "disposition_type": "affirmed",
  "source_refs": ["source:courtlistener:decision:example"]
}
```

A decision record:

- conforms to `JR.DECISION.RECORD`
- references the case record
- identifies the deciding court or tribunal
- remains distinct from opinion records and later treatment records
- does not assert legal correctness, legitimacy, or binding authority

## Opinion Record

An opinion record represents the reasoning offered in support of a decision.

```json
{
  "id": "opinion:case:example-court:2024:001:majority",
  "record_type": "opinion_record",
  "decision_ref": "decision:case:example-court:2024:001",
  "opinion_type": "majority",
  "authoring_actor_refs": ["judge:example-judge"],
  "source_refs": ["source:courtlistener:opinion:example"]
}
```

Opinion type values may include:

- `majority`
- `concurring`
- `dissenting`
- `plurality`
- `per curiam`

An opinion record:

- conforms to `JR.OPINION.RECORD`
- references the decision it supports
- declares opinion type
- remains distinct from decision, claim, and holding records
- does not assert that the reasoning is correct or that the opinion is
  authoritative beyond its declared type

## Claim Record

A claim record represents an assertion made within an opinion.

```json
{
  "id": "claim:opinion:example:001",
  "record_type": "claim_record",
  "opinion_ref": "opinion:case:example-court:2024:001:majority",
  "claim_text": "Example legal claim text drawn from the opinion.",
  "source_refs": ["source-span:opinion:example:para:12"]
}
```

A claim record:

- conforms to `AR.CLAIM.RECORD` and `JR.CLAIM.RECORD`
- identifies the opinion in which the claim was made
- remains distinct from holding records
- does not assert that the claim is correct, binding, or controlling

## Holding Record

A holding record represents a controlling determination of a decision.

```json
{
  "id": "holding:decision:example:001",
  "record_type": "holding_record",
  "decision_ref": "decision:case:example-court:2024:001",
  "holding_text": "Example holding text drawn from the decision.",
  "source_refs": ["source-span:opinion:example:para:34"]
}
```

A holding record:

- conforms to `JR.HOLDING.RECORD`
- references the decision in which the holding was issued
- remains distinct from claim records and citation records
- does not assert that the holding is correct or remains controlling in
  subsequent contexts

## Citation Record

A citation record represents a reference from an opinion or decision to an
authority.

```json
{
  "id": "citation:opinion:example:to:precedent:001",
  "record_type": "citation_record",
  "citing_record_ref": "opinion:case:example-court:2024:001:majority",
  "cited_authority_ref": "case:precedent-court:2010:042",
  "citation_text": "Example v. Precedent, 100 Example 42 (2010)",
  "source_refs": ["source-span:opinion:example:para:18"]
}
```

A citation record:

- conforms to `JR.CITATION.RECORD`
- identifies the citing record and the cited authority
- remains distinct from dependency records
- does not imply that the citing record relied on the cited authority
- does not imply that the cited authority is correct, binding, or legitimate

## Dependency Record

A dependency record represents declared reliance of one or more judicial
records on a cited authority through a specific source.

```json
{
  "id": "dependency:opinion:example:on:precedent:001",
  "record_type": "dependency_record",
  "record_slug": "example-case-slug",
  "source_id": "source:opinion:example",
  "citation_id": "citation:opinion:example:to:precedent:001",
  "dependency_type": "precedent-binding",
  "supports": [
    "holding:decision:example:001",
    "claim:opinion:example:003"
  ],
  "status": "draft"
}
```

A dependency record:

- conforms to `AR.DEPENDENCY.RECORD` and `JR.DEPENDENCY.RECORD`
- identifies the originating source
- identifies the citation that grounds the dependency
- declares the dependency type
- identifies the judicial records that the dependency supports
- remains distinct from citation records
- does not modify the citation record or the supporting records
- does not imply that the cited authority is correct, binding, or legitimate
- does not imply that the supporting records are valid

A citation records that a reference was made.
A dependency records that one or more judicial records rely on that citation
in a declared way.
The dependency type identifies the kind of reliance.
The supported records identify what the dependency upholds.

## Later Treatment Record

A later treatment record represents how a judicial record was subsequently
referenced, distinguished, followed, limited, overruled, or otherwise treated
by later decisions.

```json
{
  "id": "later-treatment:precedent:001:by:later-decision:002",
  "record_type": "later_treatment_record",
  "treating_record_ref": "decision:later-court:2024:002",
  "treated_record_ref": "case:precedent-court:2010:042",
  "treatment_type": "distinguished",
  "treatment_text": "Example treatment description.",
  "source_refs": ["source-span:opinion:later-court:para:7"]
}
```

Treatment type values may include:

- `followed`
- `distinguished`
- `limited`
- `criticized`
- `overruled`
- `superseded`
- `cited-without-comment`

A later treatment record:

- conforms to `JR.LATER_TREATMENT.RECORD`
- identifies the treating record and the treated record
- declares the treatment type
- is recorded additively
- does not modify or replace the treated record
- does not assert that later treatment erases the historical record
- does not assert that the treating record is correct

## Source Span Reference

A source span reference identifies a specific location within a source
document.

```json
{
  "id": "source-span:opinion:example:para:12",
  "record_type": "source_span_reference",
  "source_ref": "source:courtlistener:opinion:example",
  "location_type": "paragraph",
  "location_value": "12",
  "excerpt": null
}
```

A source span reference:

- conforms to `JR.SOURCE_SPAN.REFERENCE`
- identifies the source document and the location within it
- is referenceable from claim, holding, citation, and dependency records
- remains distinct from interpretations of the referenced text
- is not modified to reflect interpretation of the referenced text

## Review Status Record

A review status record identifies review state for a judicial record.

```json
{
  "id": "review-status:opinion:case:example-court:2024:001:majority",
  "record_type": "review_status_record",
  "record_ref": "opinion:case:example-court:2024:001:majority",
  "status": "curated",
  "assigned_by": "curator:example",
  "assigned_at": "2026-05-16"
}
```

Review status values may include:

- `draft`
- `machine-suggested`
- `curated`
- `reviewed`
- `disputed`
- `deprecated`
- `superseded`

A review status record:

- conforms to `JR.REVIEW_STATUS.RECORD`
- does not assert correctness, legitimacy, or binding authority of the
  underlying record
- remains distinct from governance, interpretation, and provenance records

## Interpretation Record

An interpretation record attaches interpretive content to judicial records.

```json
{
  "id": "interpretation:example-doctrinal-reading",
  "record_type": "interpretation_record",
  "interpretive_inference_type": "doctrinal reading",
  "depends_on_record_refs": [
    "opinion:case:example-court:2024:001:majority",
    "holding:decision:example:001"
  ],
  "interpretation_text": "The referenced opinion and holding may support a contestable doctrinal reading.",
  "asserting_actor": "analyst:example",
  "review_status": "draft"
}
```

An interpretation record:

- conforms to `AR.INTERPRETATION.RECORD`
- identifies grounding records
- identifies the asserting actor
- remains distinct from claim records, holding records, citation records, and
  dependency records
- does not modify substrate records
- does not assert correctness, authority, legitimacy, obligation, or
  enforcement

## Source Provenance Record

A source provenance record traces a source document to one or more derived
judicial records.

```json
{
  "id": "provenance:source:opinion:example",
  "record_type": "source_provenance_record",
  "originating_source_ref": "source:courtlistener:opinion:example",
  "derived_record_refs": [
    "opinion:case:example-court:2024:001:majority",
    "claim:opinion:example:001",
    "citation:opinion:example:to:precedent:001"
  ],
  "derivation_method": "manual extraction with curator review",
  "asserting_actor": "curator:example",
  "review_status": "draft"
}
```

A source provenance record:

- conforms to `AR.PROVENANCE`
- identifies the originating source document
- identifies derived records
- does not certify correctness, completeness, authority, legitimacy, or
  binding effect of the derivation

## Report Record

A report record represents a derived human-readable or machine-readable view.

```json
{
  "id": "report:example-judicial-summary",
  "record_type": "report_record",
  "report_type": "judicial-reasoning-summary",
  "derived_from_record_refs": [
    "decision:case:example-court:2024:001",
    "opinion:case:example-court:2024:001:majority",
    "claim:opinion:example:001",
    "holding:decision:example:001",
    "citation:opinion:example:to:precedent:001"
  ],
  "generated_at": "2026-05-16"
}
```

A report record:

- is a derived view
- does not replace the records it summarizes
- does not assert legal correctness, binding authority, judicial legitimacy,
  or proof

## Prohibited Collapses

The record model must preserve these distinctions:

- citation is not dependency
- dependency is not legal validity
- later treatment is not erasure of the historical record
- authority is not correctness
- claim is not holding
- explanation is not proof
- majority opinion claim is not system commitment
- source span is not interpretation
- review status is not legitimacy of the underlying record
- source provenance is not source correctness
- interpretation is not source-backed claim

## Verification Readiness

A judicial record system should be able to export a bundle containing:

- manifest metadata
- record type counts
- source records
- case, decision, and opinion records
- claim and holding records
- citation and dependency records
- later treatment records
- source span references
- review status records where used
- interpretation records where used
- provenance records where used
- version declarations for JR and AR

The exported bundle should be suitable for checking by
`se-verification-judicial-record-spec`.

## Clarifying Statement

Judicial Record records the structure of legal reasoning, not its correctness.

It may show that an opinion cited an authority, relied on a holding, or was
later treated by another decision. It does not assert that the reasoning was
correct, that the authority was legitimate, that the outcome was justified,
or that later treatment erases the historical record.
