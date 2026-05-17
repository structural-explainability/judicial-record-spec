# Judicial Record Specification (JR)

Status: Working Draft Specification

This document defines the normative requirements for conformance with the
Judicial Record (JR).

JR is a domain profile of the Accountable Record (AR) specification.
All AR constraints apply.

JR is a downstream specification that conforms to Structural Explainability (SE).
All SE neutrality constraints apply.

JR specifies record types and prohibited collapses for judicial reasoning
artifacts including opinions, claims, holdings, citations, dependencies,
later treatment, source spans, and review status.

JR does not define legal correctness, legal advice, binding authority,
judicial legitimacy, court record publication, or legal research
replacement.

## How to Read This Spec

Keywords MUST, MUST NOT, SHOULD, and MAY
are to be interpreted as described in RFC 2119.

Use of terms such as "canonical" denotes structural role only and
does not imply epistemic, causal, or normative preference.

This specification does not prescribe editorial structure,
terminology preference, or documentation layout beyond identifier semantics.

## Representation vs Constraint Classes

Some requirements describe what judicial record structures MAY represent,
while others constrain how such representations MUST NOT be interpreted.

Overlap between these classes is intentional:
representation permissions do not imply legal, epistemic, causal, normative,
authoritative, or enforcement commitment.

## Identifier Semantics and Stability

Each requirement in this document is identified by a stable identifier
of the form `JR.*`.

Identifiers are the sole normative reference for conformance.
Textual wording MAY be clarified over time without changing meaning;
any change that alters the requirement MUST result in a new identifier.

Renaming, reordering, or relocating identifiers constitutes a semantic
change and is therefore intentionally diff-visible.

Repository paths, filenames, and section ordering are non-normative and
do not affect identifier meaning.

---

## JR.CASE.RECORD

JR MUST provide a structural form for case records that represent the
procedural unit within which judicial decisions and opinions occur.

Case records:

- MUST use stable identifiers
- MUST identify the issuing court or tribunal as a referenced entity
- MUST be distinguishable from decision records and opinion records
- MUST NOT assert legal correctness or outcome legitimacy

## JR.CITATION.RECORD

JR MUST provide a structural form for citation records that represent
references from an opinion or decision to an authority.

Citation records:

- MUST identify the citing record and the cited authority
- MUST be distinguishable from dependency records
- MUST NOT imply that the citing record relied on the cited authority
- MUST NOT imply that the cited authority is correct, binding, or legitimate

A citation record records that a reference was made.
It does not record that the reference established dependency.

## JR.CLAIM.RECORD

JR MUST provide a structural form for claim records that represent assertions
made within an opinion.

Claim records:

- MUST conform to AR.CLAIM.RECORD
- MUST identify the opinion in which the claim was made
- MUST be distinguishable from holding records
- MUST NOT assert that the claim is correct, binding, or controlling

A claim is what the opinion says.
A holding is what the decision decides.
These are separate records.

## JR.COLLAPSE.PROHIBITED

JR MUST prohibit structural collapse of the following distinct judicial record
categories into a single record:

- citation and dependency
- dependency and legal validity
- later treatment and historical rewrite
- authority and correctness
- claim and holding
- explanation and proof
- majority opinion claims and system commitments

These prohibitions apply in addition to those declared in AR.COLLAPSE.PROHIBITED.

## JR.CONFORMANCE.AR.REQUIRED

Any system claiming conformance with this specification MUST also conform to
the Accountable Record (AR) specification.

JR MUST NOT weaken, override, or reinterpret any AR constraint.

## JR.CONFORMANCE.SE.REQUIRED

Any system claiming conformance with this specification MUST also conform to
the Structural Explainability (SE) specification.

JR MUST NOT weaken, override, or reinterpret any SE neutrality constraint.

## JR.DECISION.RECORD

JR MUST provide a structural form for decision records that represent the
disposition of a case by a court.

Decision records:

- MUST reference the case record
- MUST identify the deciding court or tribunal
- MUST be distinguishable from opinion records
- MUST be distinguishable from later treatment records
- MUST NOT assert legal correctness, legitimacy, or binding authority

A decision record records that a disposition was made.
It does not assert that the disposition was correct or that it is binding.

## JR.DEFINITION.CORE

Judicial Record defines a domain profile of AR for representing judicial
reasoning artifacts as durable, inspectable records.

JR specifies structural forms for:

- case records
- decision records
- opinion records
- claim records
- holding records
- citation records
- dependency records
- later treatment records
- source span references
- review status references
- rendered judicial reports

JR does not define:

- legal advice
- legal correctness
- binding authority
- judicial legitimacy
- court record publication
- legal research replacement
- automatic legal reasoning
- legal outcome prediction

## JR.DEPENDENCY.RECORD

JR MUST support a structural form for dependency records that represents
declared reliance of one or more judicial records on a cited authority.

Dependency records:

- MUST conform to AR.DEPENDENCY.RECORD
- MUST identify the originating source
- MUST identify the citation that grounds the dependency
- MUST declare the dependency type
- MUST identify the judicial records that the dependency supports
- MUST be distinguishable from citation records
- MUST NOT modify the citation record or the supporting records
- MUST NOT assert correctness, authority, legitimacy, or enforcement of
the cited authority

A citation records that a reference was made.
A dependency records that one or more judicial records rely on
that citation in a declared way.
The dependency type identifies the kind of reliance
(constitutional authority, precedent, doctrinal foundation, etc.).
The supports list identifies the records the dependency upholds.

## JR.HOLDING.RECORD

JR MUST provide a structural form for holding records that represent the
controlling determinations of a decision.

Holding records:

- MUST reference the decision record in which the holding was issued
- MUST be distinguishable from claim records
- MUST be distinguishable from citation and dependency records
- MUST NOT assert that the holding is correct or that it remains controlling
  in subsequent contexts

## JR.LATER_TREATMENT.RECORD

JR MUST provide a structural form for later treatment records that represent
how a judicial record was subsequently referenced, distinguished, followed,
limited, overruled, or otherwise treated by later decisions.

Later treatment records:

- MUST identify the treating record and the treated record
- MUST identify the nature of the treatment as a declared treatment type
- MUST be recorded additively
- MUST NOT modify or replace the treated record
- MUST NOT assert that later treatment erases the historical record
- MUST NOT assert that the treating record is correct

Later treatment is additive history, not historical revision.

## JR.OPINION.RECORD

JR MUST provide a structural form for opinion records that represent the
reasoning offered in support of a decision.

Opinion records:

- MUST reference the decision record they support
- MUST identify the opinion type as a declared type
  (such as majority, concurring, dissenting, plurality, per curiam)
- MUST be distinguishable from decision records
- MUST be distinguishable from claim and holding records
- MUST NOT assert that the reasoning is correct or that the opinion is
  authoritative beyond its declared type

## JR.REVIEW_STATUS.RECORD

JR MUST provide a structural form for review status records that represent
the procedural posture of a case or decision with respect to appellate or
collateral review.

Review status records:

- MUST identify the record whose status is being described
- MUST identify the review status as a declared status type
  (such as pending, decided, denied, dismissed, vacated, remanded)
- MUST be distinguishable from decision records and later treatment records
- MUST NOT assert correctness of the underlying decision
- MUST NOT assert that any review outcome is legitimate

## JR.SCOPE.EXCLUSIONS

This specification does not define:

- legal advice
- legal correctness
- binding authority
- judicial legitimacy
- court record publication
- legal research replacement
- automatic legal reasoning
- legal outcome prediction
- replacements for court record publication or legal research platforms

These concerns are explicitly out of scope.

## JR.SOURCE_SPAN.REFERENCE

JR MUST provide a structural form for source span references that identify
specific locations within a source document.

Source span references:

- MUST identify the source document and the location within it
- MUST be referenceable from claim, holding, citation, and dependency records
- MUST be distinguishable from interpretations of the referenced text
- MUST NOT be modified to reflect interpretation of the referenced text

## JR.VERSIONING

JR MUST define versioning rules for the specification and for judicial record
systems claiming conformance.

Versioning:

- MUST conform to AR.VERSIONING
- MUST identify both the JR version and the underlying AR version
- MUST NOT allow silent or implicit change
