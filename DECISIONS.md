# Decisions

This document records founding decisions.

## Decision 1: Define Judicial Record as an Accountable Record system

Decision: `judicial-record-spec` implements the Accountable Record contract for
judicial reasoning and dependency.

Rationale: Judicial materials span cases, decisions, opinions, claims,
holdings, citations, dependencies, later treatment, source spans, and review
status. The system needs a durable record model that can represent those
structures without collapsing them into legal correctness, binding authority,
judicial legitimacy, or substantive merit.

Consequences:

- The repository depends on `accountable-record`.
- Judicial Record keeps domain vocabulary separate from SE substrate
  commitments.
- SE verification can check whether the exported records preserve required
  distinctions.

## Decision 2: Separate citation records from dependency records

Decision: Citation records and dependency records are separate record types.

Rationale: A citation records that a reference was made. A dependency
records that one or more judicial records rely on a citation in a declared
way. Collapsing these into one record loses the distinction between what
an opinion mentioned and what one or more judicial records rely on, which
is load-bearing for inspection and contestation.

Consequences:

- Citation records identify the citing record and the cited authority.
- Dependency records identify the originating source, the grounding citation,
  the kind of dependency, and the records the dependency supports.
- Citation records do not imply reliance.
- Dependency records do not imply correctness of the cited authority or
  validity of the supporting records.
- Citation records and dependency records carry different defining fields
  and remain distinguishable in records, exports, and verification.

## Decision 3: Separate claim records from holding records

Decision: Claim records and holding records are separate record types.

Rationale: A claim is what an opinion says. A holding is what a decision
decides. Treating opinion claims as if they were holdings overstates the
controlling status of the claim; treating holdings as ordinary claims
understates their procedural role.

Consequences:

- Claim records reference the opinion in which the claim was made.
- Holding records reference the decision in which the holding was issued.
- Claim records do not assert that the claim is controlling.
- Holding records do not assert that the holding is correct or remains
  controlling in subsequent contexts.

## Decision 4: Record later treatment additively

Decision: Later treatment records are added to the system as new records.
They do not modify or replace the records they treat.

Rationale: Judicial doctrine evolves through subsequent decisions that follow,
distinguish, limit, criticize, overrule, or supersede earlier decisions. If
the historical record is overwritten to reflect later treatment, the original
state becomes inaccessible, and contestation of the later treatment itself
becomes harder.

Consequences:

- Later treatment records identify the treating record, the treated record,
  and the declared treatment type.
- The treated record is not modified to reflect later treatment.
- The historical record remains accessible after later treatment is recorded.
- Later treatment does not assert that the treating record is correct.

## Decision 5: Use source span references for precise location

Decision: Records that reference specific locations within source documents
use source span references rather than ambiguous source citations.

Rationale: Judicial work requires pinpoint references — a paragraph, a
section, a page — to support claim, holding, citation, and dependency records.
Loose source references cannot be verified for accuracy of attribution.

Consequences:

- Source span references identify the source document and the location within
  it.
- Claim, holding, citation, and dependency records may reference source spans.
- Source span references remain distinct from interpretations of the
  referenced text.

## Decision 6: Keep judicial records source-traceable

Decision: Records derived from source documents should preserve source
references and provenance where available.

Rationale: Inspection, contestation, and audit depend on knowing which source
supports each record and how the record was derived.

Consequences:

- Source records remain distinct from derived records.
- Source provenance may be represented through `AR.PROVENANCE`.
- Provenance does not certify correctness, completeness, authority,
  legitimacy, or binding effect.

## Decision 7: Keep the implementation verifiable

Decision: The record model and exports are designed for verification by
`se-verification-judicial-record-spec`.

Rationale: The purpose of the system is not only to store judicial records,
but to make the record discipline externally checkable.

Consequences:

- Export bundles identify versions, record types, manifests, and references.
- Records use stable identifiers.
- Verification reports can trace failures to JR, AR, and SE constraints.

## Decision 8: Do not replace court records, citators, or legal research platforms

Decision: Judicial Record does not replace CourtListener, court websites,
legal citators, legal research platforms, or other source systems.

Rationale: The repository is an accountable record layer. It references and
derives from source systems; it does not become the authoritative source
system.

Consequences:

- Source records identify external systems and documents.
- Source content is not treated as correct, complete, current, or
  authoritative by default.
- The project can remain lightweight and inspectable.

## Decision 9: Use working draft status

Decision: The initial version is a working draft specification.

Rationale: The contract and domain model will be stress-tested through
implementation and verification.

Consequences:

- Version `0.1.0` is appropriate for the initial release.
- Breaking changes may occur before a stable major release.
- Identifier changes should still be treated as serious and diff-visible.
