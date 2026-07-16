# DPA-300 Restructure Ratification Record

Status: ACCEPTED
Date: 2026-07-16

## 1. Authority and scope

This record is the Maintainer disposition required by DPA-ADR-020 after the independent equivalence verification comparing:

- certified baseline `a86aa49851c96c39380a8eb4afad17763263fe00`;
- restructured promotion state `e3f8b85c5eb76b8c6cae76dde317fd33f236ce88`.

The verification result was `PASS_WITH_EXPLICIT_RATIFICATION`.

This record does not ratify silent weakening. It chooses explicit reinstatement for safety-relevant lost obligations and explicit acceptance only where coverage remains complete or a strengthening was introduced.

## 2. Disposition of weakened details

### R-W1 — target identity

**Disposition: REINSTATE.**

A mutation plan MUST contain an explicit target identity in addition to registry-entry identity and contract fingerprint. This is required for region-level targets and interrupted-refresh recovery for the same target.

### R-W2 — missing required fields

**Disposition: REINSTATE.**

Validation MUST reject any projection or partition contract missing a required field.

### R-W3 — partition-byte encoding

**Disposition: REINSTATE AND RETAIN LINE ENDINGS.**

A PartitionContract MUST declare encoding, normalization and line-ending behavior for partition bytes.

### R-W4 — policy identifiers

**Disposition: RESTORE IDENTIFIER SEMANTICS.**

ProjectionContract lifecycle, freshness and evidence policies MUST be represented by reviewed policy identifiers rather than unrestricted inline policy bodies. Exact serialized representation remains `NEEDS_MAIN_REPO_VALIDATION`.

## 3. Changed coverage

### R-C1 — undeclared versus missing canonical sources

**Disposition: RATIFY OWNERSHIP SPLIT WITH EXPLICIT VALIDATION.**

DPA-300 validation rejects missing declared canonical sources. DPA-400 owns prohibition and detection of undeclared source consumption. DPA-300 additionally rejects contracts whose declared-source set is absent or internally inconsistent; runtime undeclared access is not silently accepted.

### R-C2 — review-ready self-assessment

**Disposition: REWORD.**

The unconditional sentence asserting all criteria were already satisfied is replaced with a statement that review-ready lineage is complete only after the equivalence verification, this ratification record and the governed amendment synchronization are complete.

## 4. Removed consolidated sections

### R-R1 — planned DP1 Probes

**Disposition: REINSTATE NORMATIVE POINTER.**

DPA-300 MUST point to the DP1 Probe backlog and traceability as the owning detailed views and MUST retain the rule that a falsified compatibility mapping returns the affected contract to adjudication.

### R-R2 — conformance checklist

**Disposition: REINSTATE.**

The consolidated conformance-demonstration checklist is restored because it provides direct DP2 implementation and review value. Derived traceability remains non-owning.

## 5. Normative keyword relaxations

**Disposition: RESTORE NORMATIVE FORCE.**

DPA-300 must state explicitly that:

1. the existing documentation registry MUST remain the sole registry authority for projection and partition contracts;
2. validation MUST be side-effect free;
3. failure before Write MUST leave target bytes unchanged;
4. validation MUST reject unknown contract or partition schema versions;
5. later inspection MUST compare current observations independently with accepted lifecycle state.

## 6. Accepted strengthenings

The Maintainer explicitly accepts the following additions as consistent strengthenings:

- the 27-item invalid-state catalog;
- source-drift anti-mislabeling;
- prohibition of a second render for the same still-valid plan;
- explicit Workspace path coverage and hard-coded-path prohibition after validated implementation;
- DISC-003b writer-inventory rebuild at the Probe validation ref;
- added schema, ordered-configuration, ownership, acceptance-scope and gate-set fields;
- identity-critical evidence as `MUST` and contextual evidence as `SHOULD`;
- expanded fail-loud conditions;
- stronger parent-entry partition and complete-byte ownership rules.

## 7. Required synchronization

The governed amendment batch MUST:

1. apply the dispositions above to DPA-300;
2. apply DPA-ADR-019 renderer vocabulary consistently to DPA-100, DPA-300 and DPA-400;
3. update DPA-400 traceability and diagram artifacts;
4. update status and roadmap without changing normative content in a later promotion commit;
5. receive independent post-adjudication verification by a context that did not apply the amendment.

## 8. Consequence

After the governed amendment and independent verification pass, the DPA-300 verification lineage extends to the restructured text and R4-M04 is closed.

DPA-300 remains `review-ready`, not `stable`; stability still requires applicable exact-ref Probe evidence and governed revalidation.
