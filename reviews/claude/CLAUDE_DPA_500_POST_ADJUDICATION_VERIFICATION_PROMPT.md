# Claude DPA-500 Post-Adjudication Verification Prompt

## Role

Act as the independent post-adjudication technical verifier under DPA-ADR-012.

You are not asked to redesign DPA-500, repeat the primary review from scratch or inspect a moving branch head. Verify whether the adjudicated correction set is complete, internally consistent and semantically faithful at the exact immutable ref below.

## Repository and exact ref

Repository:

`vfi64/agentic-project-kit-dpa-lab`

Exact immutable verification ref:

`bb3db42e49db0ce9a38e0a019962cdd61f51785c`

Commit subject:

`Audit DPA-500 post-adjudication amendment batch`

Do not use a newer branch head as reviewed content.

## Durable Lab-gate evidence

Workflow: `DPA lab gates`

Run: `29603817974`

Result: `success`

This proves only repository-integrity checks at the exact ref. It is not architecture approval, Probe evidence, implementation evidence, adoption evidence or main-repository conformance.

## Required bootstrap

Read completely, at the exact verification ref, in this order:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `DECISIONS.md`
9. `ASSUMPTIONS.md`
10. `specs/dpa/README.md`
11. `specs/dpa/DPA-000-VISION.md`
12. `specs/dpa/DPA-100-FOUNDATIONS.md`
13. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
14. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
15. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
16. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`
17. `decisions/DPA-ADR-021-FRESHNESS-REACCEPTANCE-AND-LAYERED-ACCEPTANCE.md`
18. `traceability/DPA-500_TRACEABILITY.md`
19. `diagrams/dpa-500-freshness-gates.mmd`
20. `reviews/claude/CLAUDE_DPA_500_PRIMARY_REVIEW.md`
21. `reviews/consolidated/DPA-500_PRIMARY_REVIEW_ADJUDICATION.md`
22. `reviews/consolidated/DPA-500_POST_ADJUDICATION_INTERNAL_AUDIT.md`
23. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
24. `integration/IMPORT_PLAN.md`

Also read the accepted decision files needed to interpret DPA-300 through DPA-500, especially DPA-ADR-013, 014, 016, 017, 019 and 020.

Do not mutate either repository.

## Verification objective

Determine whether the exact ref completely and correctly implements the adjudicated bounded correction set from the DPA-500 primary review while preserving upstream contracts and authority boundaries.

The required corrections are:

1. R5-M01 — operation-scoped base context and conditional accepted-base persistence;
2. R5-M02 — lifecycle-owned gate-set re-evaluation and re-acceptance without rendering or target mutation;
3. R5-M03 — layered acceptance for registered-region projections with a synchronized DPA-300 amendment;
4. R5-m01 — attempt-scoped renderer failure classification;
5. R5-m02 — deterministic configuration-drift mapping;
6. R5-m03 — corrected invariant anchors and new traceability rows;
7. R5-m04 — mandatory identity-critical gate-evidence fields;
8. R5-e01 through R5-e03 — terminology and diagram corrections.

## Mandatory verification fields

### A. Exact-ref and artifact integrity

Verify:

- every reviewed file comes from the exact ref;
- the gate run is bound to that ref and succeeded;
- DPA-500 remains `draft`;
- no status-only promotion is mixed into the normative amendment;
- no implementation, Probe, adoption or main-repository-conformance claim appears.

### B. R5-M01 closure

Verify that:

- base context is evaluated against the governing plan or requested operation;
- ordinary base-independent post-acceptance audit does not depend on a surviving accepted plan;
- accepted base identity is persisted only when the contract declares base dependence;
- DPA-300 and DPA-500 state the same rule;
- conformance and traceability cover both base-independent and base-dependent cases;
- cross-ref serialization remains DPA-600 scope.

### C. R5-M02 closure

Verify that gate-set re-acceptance:

- is lifecycle-owned;
- uses existing Workspace, lock/state/persistence and gate authority;
- is eligible only when every non-gate-set freshness dimension is `fresh`;
- invokes no renderer;
- performs no target write;
- updates only acceptance state and bounded evidence on gate `pass`;
- preserves target bytes and prior acceptance state on `warning` or `failure`;
- creates no second acceptance path or gate runner;
- has explicit recovery and conformance coverage.

### D. R5-M03 closure

Verify that layered acceptance:

- compares complete-target bytes post-acceptance for complete-target projections;
- compares lifecycle-owned payload bytes for registered-region projections;
- keeps lifecycle-owned partition bytes, boundaries and ownership independently guarded;
- keeps complete-target and preserved-region fingerprints mandatory for plan, under-lock revalidation, atomic reconstruction, post-Write verification and recovery;
- treats proven governed non-lifecycle-owner region evolution as neither projection target drift nor projection staleness;
- continues to classify lifecycle-owned payload mutation as `target drift`;
- continues to classify partition/boundary mutation as `partition drift`;
- continues to classify owner-map change as `ownership drift`;
- fails closed when ownership or boundaries cannot be proven;
- is synchronized across ADR-021, DPA-300, DPA-500, traceability and diagram;
- does not select a production document form.

### E. Minor and editorial closure

Verify that:

- failed attempt classification does not overwrite prior accepted-byte classification;
- output-affecting configuration change maps deterministically to `contract drift`;
- every traceability invariant anchor is defensible from DPA-000 §7 rather than decorative;
- identity-critical gate evidence uses `MUST`, with contextual fields using `SHOULD`;
- acceptance-state defect wording does not collide ambiguously with freshness `invalid`;
- the diagram does not imply read-only pass updates acceptance state;
- target comparator wording is explicit for complete-target versus region projections.

### F. Vocabulary and dimension separation

Verify no accidental extension or collision among:

- freshness classification;
- DPA-100 consumer trust state;
- DPA-100 drift class;
- finding subreason;
- lifecycle attempt outcome;
- gate decision;
- enforcement stage;
- severity/user wording.

Search specifically for prohibited trust-state uses of `stale`, `invalid` or `indeterminate`; gate outcomes `warn`, `block` or `error`; and new drift tokens outside DPA-100.

### G. Authority and parallel-system boundary

Verify that no second registry, lifecycle, freshness engine, findings taxonomy, gate runner, acceptance store, Workspace abstraction, writer path or runtime authority is created.

Confirm renderers do not gain findings, gate, state, acceptance, write or recovery authority.

### H. Recovery and crash safety

Verify that:

- `written-unverified` cannot become accepted without complete governed checks;
- acceptance state cannot be reconstructed from bytes or evidence alone;
- failed re-acceptance cannot fabricate a new gate-set identity;
- persistence ordering details remain appropriately fenced for main-repository validation;
- prior accepted state remains distinguishable from a failed active attempt.

### I. Evidence and main-repository fence

Verify that exact schemas, paths, finding codes, severity mappings, ownership provenance, command integration, lock behavior, persistence order, CI placement and strict switches remain `NEEDS_MAIN_REPO_VALIDATION` where required.

### J. Traceability and diagram equivalence

Verify that traceability and diagram explain the normative contracts without creating competing meaning. Identify every mismatch, omission or overstatement.

### K. Internal-audit verification

Do not trust the internal audit. Independently verify each closure claim and list any inaccurate or incomplete claim.

## Required verdict vocabulary

Use exactly one:

- `PASS`
- `PASS_WITH_NON_BLOCKING_FINDINGS`
- `FAIL`
- `ACCESS_BLOCKED`
- `INDEPENDENCE_BLOCKED`

`PASS` requires zero blocking findings and no required normative correction.

`PASS_WITH_NON_BLOCKING_FINDINGS` permits only minor/editorial issues that do not require normative correction before a separate status-only promotion.

`FAIL` applies when any adjudicated major is not closed, upstream meaning is contradicted, authority is duplicated, the DPA-300 sync is incomplete, or a required normative correction remains.

## Finding format

For each finding provide:

- ID;
- severity: BLOCKING, MAJOR, MINOR or EDITORIAL;
- affected file and section;
- exact analysis;
- consequence;
- smallest bounded correction;
- whether fresh main-repository validation is required;
- whether Maintainer adjudication is required.

Do not convert suggestions into mandatory findings unless the contract is actually inconsistent or incomplete.

## Required report structure

Produce a complete English report suitable for committing as:

`reviews/claude/CLAUDE_DPA_500_POST_ADJUDICATION_VERIFICATION.md`

Use these sections:

1. Title
2. Metadata
3. Independence disclosure
4. Bootstrap completion statement
5. Method
6. Reviewed files
7. Exact verification ref
8. Overall verdict
9. Executive summary
10. Blocking and major findings
11. Minor and editorial findings
12. R5-M01 closure verification
13. R5-M02 closure verification
14. R5-M03 closure verification
15. Minor/editorial closure verification
16. Vocabulary and dimension audit
17. DPA-300/DPA-500 synchronization audit
18. Authority and parallel-system audit
19. Recovery and persistence audit
20. Evidence and main-repository boundary audit
21. Traceability and diagram audit
22. Internal-audit accuracy
23. Remaining `NEEDS_MAIN_REPO_VALIDATION` obligations
24. Limitations and access-blocked items
25. Promotion recommendation

End with this exact promotion boundary, adjusted only for the verdict:

> DPA-500 may be promoted to `review-ready` only through a separate status-only commit if this verification has no blocking finding and every required correction is complete. Such promotion does not establish production implementation, Probe success, adoption or main-repository conformance.

After the English report, provide a short German summary containing:

- overall verdict;
- counts by severity;
- whether normative changes remain required;
- whether DPA-500 may proceed to a separate status-only promotion;
- recommended next step.
