# Judicial Record Conformance Checklist

This document defines the criteria for determining whether an artifact conforms
to the Judicial Record specification.

Identifiers referenced in this document are the sole normative reference.
Section ordering, formatting, and presentation are non-normative.

An artifact may be a judicial record system, export bundle, repository, domain
profile, or other deliverable claiming conformance.

## Conformance Overview

An artifact CONFORMS if and only if:

- all mandatory requirements are satisfied
- no prohibited assertions are present
- conformance with Accountable Record is preserved
- conformance with Structural Explainability is preserved
- judicial records remain source-backed, inspectable, and contestable
- judicial records do not assert legal correctness, binding authority,
  judicial legitimacy, or substantive merit by default

Failure of any single check constitutes non-conformance.

## JR.CASE.RECORD

- [ ] Case records use stable identifiers.
- [ ] Case records identify the issuing court or tribunal as a referenced entity.
- [ ] Case records remain distinguishable from decision records.
- [ ] Case records remain distinguishable from opinion records.
- [ ] Case records do not assert legal correctness or outcome legitimacy.
- Fail if: a case record is treated as decision, opinion, legal correctness, or outcome legitimacy.

## JR.CITATION.RECORD

- [ ] Citation records identify the citing record.
- [ ] Citation records identify the cited authority.
- [ ] Citation records remain distinguishable from dependency records.
- [ ] Citation records do not imply that the citing record relied on the cited authority.
- [ ] Citation records do not imply that the cited authority is correct, binding, or legitimate.
- Fail if: citation is treated as dependency, correctness, binding authority, legitimacy, or reliance.

## JR.CLAIM.RECORD

- [ ] Claim records conform to AR.CLAIM.RECORD.
- [ ] Claim records identify the opinion in which the claim was made.
- [ ] Claim records remain distinguishable from holding records.
- [ ] Claim records do not assert that the claim is correct, binding, or controlling.
- Fail if: a claim is treated as holding, correctness, binding authority, or controlling determination.

## JR.COLLAPSE.PROHIBITED

- [ ] Citation remains distinct from dependency.
- [ ] Dependency remains distinct from legal validity.
- [ ] Later treatment remains distinct from historical rewrite.
- [ ] Authority remains distinct from correctness.
- [ ] Claim remains distinct from holding.
- [ ] Explanation remains distinct from proof.
- [ ] Majority opinion claims remain distinct from system commitments.
- Fail if: a judicial record collapses any prohibited judicial category.

## JR.CONFORMANCE.AR.REQUIRED

- [ ] The artifact declares conformance with AR.
- [ ] The artifact preserves all AR constraints.
- [ ] The artifact does not weaken, override, or reinterpret AR.
- Fail if: JR conformance is asserted while weakening, overriding, or reinterpreting AR.

## JR.CONFORMANCE.SE.REQUIRED

- [ ] The artifact declares conformance with SE.
- [ ] The artifact preserves SE neutrality constraints.
- [ ] The artifact does not weaken, override, or reinterpret SE.
- Fail if: JR conformance is asserted while weakening, overriding, or reinterpreting SE neutrality.

## JR.DECISION.RECORD

- [ ] Decision records reference the case record.
- [ ] Decision records identify the deciding court or tribunal.
- [ ] Decision records remain distinguishable from opinion records.
- [ ] Decision records remain distinguishable from later treatment records.
- [ ] Decision records do not assert legal correctness, legitimacy, or binding authority.
- Fail if: a decision record is treated as opinion, later treatment, correctness,
  legitimacy, or binding authority.

## JR.DEFINITION.CORE

- [ ] The artifact treats JR as a domain profile of AR.
- [ ] The artifact limits JR to judicial reasoning artifacts and prohibited collapses.
- [ ] The artifact does not define legal advice, legal correctness, binding authority,
  judicial legitimacy, court record publication, legal research replacement,
  automatic legal reasoning, or legal outcome prediction.
- Fail if: JR is treated as legal advice, legal correctness validator, citator,
  court record publisher, legal research replacement, automatic legal reasoning engine,
  or outcome predictor.

## JR.DEPENDENCY.RECORD

- [ ] Dependency records conform to AR.DEPENDENCY.RECORD.
- [ ] Dependency records identify the dependent record.
- [ ] Dependency records identify the depended-upon record.
- [ ] Dependency records remain distinguishable from citation records.
- [ ] Dependency records do not imply that the depended-upon record is correct, binding, or legitimate.
- [ ] Dependency records do not imply that the dependent record is valid.
- Fail if: dependency is treated as citation, validity, correctness,
- binding authority, legitimacy, or proof.

## JR.HOLDING.RECORD

- [ ] Holding records reference the decision record in which the holding was issued.
- [ ] Holding records remain distinguishable from claim records.
- [ ] Holding records remain distinguishable from citation records.
- [ ] Holding records remain distinguishable from dependency records.
- [ ] Holding records do not assert that the holding is correct.
- [ ] Holding records do not assert that the holding remains controlling in subsequent contexts.
- Fail if: a holding is treated as claim, citation, dependency, correctness, or
  current controlling status.

## JR.LATER_TREATMENT.RECORD

- [ ] Later treatment records identify the treating record.
- [ ] Later treatment records identify the treated record.
- [ ] Later treatment records identify the nature of treatment as a declared treatment type.
- [ ] Later treatment records are recorded additively.
- [ ] Later treatment records do not modify or replace the treated record.
- [ ] Later treatment records do not assert that later treatment erases the historical record.
- [ ] Later treatment records do not assert that the treating record is correct.
- Fail if: later treatment rewrites, erases, replaces, or mutates the treated record or
  asserts correctness of the treating record.

## JR.OPINION.RECORD

- [ ] Opinion records reference the decision record they support.
- [ ] Opinion records identify the opinion type as a declared type.
- [ ] Opinion records remain distinguishable from decision records.
- [ ] Opinion records remain distinguishable from claim records.
- [ ] Opinion records remain distinguishable from holding records.
- [ ] Opinion records do not assert that the reasoning is correct.
- [ ] Opinion records do not assert authority beyond declared type.
- Fail if: an opinion is treated as decision, claim, holding, correctness, or undeclared authority.

## JR.REVIEW_STATUS.RECORD

- [ ] Review status records identify the record whose status is being described.
- [ ] Review status records identify the review status as a declared status type.
- [ ] Review status records remain distinguishable from decision records.
- [ ] Review status records remain distinguishable from later treatment records.
- [ ] Review status records do not assert correctness of the underlying decision.
- [ ] Review status records do not assert that any review outcome is legitimate.
- Fail if: review status is treated as decision, later treatment, correctness, or legitimacy.

## JR.SCOPE.EXCLUSIONS

Verify that the artifact does not define:

- [ ] legal advice
- [ ] legal correctness
- [ ] binding authority
- [ ] judicial legitimacy
- [ ] court record publication
- [ ] legal research replacement
- [ ] automatic legal reasoning
- [ ] legal outcome prediction
- [ ] replacements for court record publication or legal research platforms

Presence of any excluded concern as a JR-defined construct constitutes non-conformance.

## JR.SOURCE_SPAN.REFERENCE

- [ ] Source span references identify the source document.
- [ ] Source span references identify the location within the source document.
- [ ] Source span references are referenceable from claim records.
- [ ] Source span references are referenceable from holding records.
- [ ] Source span references are referenceable from citation records.
- [ ] Source span references are referenceable from dependency records.
- [ ] Source span references remain distinguishable from interpretations of referenced text.
- [ ] Source span references are not modified to reflect interpretation of referenced text.
- Fail if: source span references are missing, unstable, unreferenceable,
  interpreted as meaning, or modified by interpretation.

## JR.VERSIONING

- [ ] JR versioning conforms to AR.VERSIONING.
- [ ] JR identifies the JR version.
- [ ] JR identifies the underlying AR version.
- [ ] JR does not allow silent or implicit change.
- Fail if: JR or AR versioning is missing, implicit, unstable, or silently changed.

## Final Determination

An artifact CONFORMS if:

- all checks above pass
- no prohibited assertions are present
- conformance with Accountable Record is preserved
- conformance with Structural Explainability is preserved
- judicial records remain source-backed, inspectable, and contestable
- legal correctness, binding authority, judicial legitimacy, and substantive
  merit remain outside substrate records

Otherwise, the artifact is NON-CONFORMANT.

## Conformance Declaration

Artifacts claiming conformance SHOULD include a declaration of the form:

```text
Conforms to: JR Specification vX.Y
Conforms to: AR Specification vX.Y
Conforms to: SE Specification vX.Y
```
