# Claude Prompt — DPA-400 Independent Post-Adjudication Verification

You are working in repository `vfi64/agentic-project-kit-dpa-lab`.

Work only from the repository and the exact ref below. Do not work from chat memory or prior review conclusions.

## Role

Act as the independent post-adjudication verifier under DPA-ADR-012 and DPA-ADR-020.

You MUST NOT write to the repository, adjudicate new architecture, redesign DPA-400 or inspect the main repository.

Disclose whether this context authored any amendment being verified. If it did, return `INDEPENDENCE_BLOCKED`.

## Exact verification ref

Checkout and verify exactly:

`055aee9f892fcd321686267804931bd3379ab4f6`

The primary-review baseline was:

`8c9b6892540895e58be53038c6064648d49a2b57`

## Bootstrap order

Read fully, in order:

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
14. `specs/dpa/DPA-200-DOCUMENT-FORM-MATRIX.md`
15. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
16. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
17. `traceability/DPA-300_TRACEABILITY.md`
18. `traceability/DPA-400_TRACEABILITY.md`
19. `diagrams/dpa-300-registry-lifecycle.mmd`
20. `diagrams/dpa-300-plan-state.mmd`
21. `diagrams/dpa-300-command-integration.mmd`
22. `diagrams/dpa-400-renderer-boundary.mmd`
23. `decisions/DPA-ADR-019-RENDERER-INPUT-RESOURCE-AND-VERSION-MODEL.md`
24. `decisions/DPA-ADR-020-PROMOTION-COMMIT-AND-EQUIVALENCE-VERIFICATION.md`
25. `reviews/claude/CLAUDE_DPA_400_PRIMARY_REVIEW.md`
26. `reviews/consolidated/DPA-400_ADJUDICATION_RECORD.md`
27. `reviews/claude/CLAUDE_DPA_300_RESTRUCTURE_EQUIVALENCE_VERIFICATION.md`
28. `reviews/consolidated/DPA-300_RESTRUCTURE_RATIFICATION_RECORD.md`
29. `reviews/consolidated/DPA-400_ADJUDICATION_AMENDMENT_BASELINE.md`

Verify rather than trust all review and adjudication records.

## Verification objective

Determine whether the governed amendment batch correctly closes every accepted DPA-400 primary-review finding and the DPA-300 lineage issue without introducing a new contradiction, parallel authority, false implementation claim or unreviewed semantic change.

This is a closure verification, not a new architecture review. Report newly discovered defects only when they prevent truthful closure or promotion.

## Required checks

### A. DPA-300 lineage and ratification

Verify that:

1. the plan again contains explicit target identity;
2. generic missing-required-field rejection is restored;
3. partition-byte encoding is restored alongside normalization and line endings;
4. lifecycle, freshness and evidence policies are identifiers;
5. registry sole authority, side-effect-free validation, pre-Write preservation and acceptance-state comparison use normative MUST force;
6. Probe obligations and the consolidated conformance demonstration are restored;
7. all strengthenings enumerated in the equivalence report remain consistent;
8. the review-ready statement is explicitly bound to the equivalence verification and ratification record;
9. DPA-300 uses renderer identifier, interface version and semantic version consistently in contract, plan and acceptance state.

### B. R4-M01 — immutable renderer inputs

Verify that:

1. renderers consume only lifecycle-resolved immutable values or content-addressed immutable snapshots;
2. renderer-visible bytes are exactly the lifecycle-fingerprinted bytes;
3. renderers cannot reopen, reread or resolve mutable repository paths;
4. the invocation-context list is closed and contains no open extension slot;
5. traceability and tests cover the mutation-between-fingerprint-and-invocation race.

### C. R4-M02 — semantic bounds versus operational aborts

Verify that:

1. deterministic semantic bounds are contract-declared and fingerprinted where output- or validity-relevant;
2. wall-clock and host-memory termination are operational controls rather than semantic results;
3. operational aborts produce `abandoned`, findings and no truncated accepted output;
4. operational aborts do not enter semantic fingerprint domains;
5. DPA-500 obligations and traceability distinguish both classes.

### D. R4-M03 — renderer identity and versions

Verify a single coherent four-part model:

1. renderer identifier;
2. renderer interface version;
3. renderer semantic version;
4. renderer implementation evidence.

Check that:

- DPA-100 is the sole vocabulary owner;
- only semantic version is output/fingerprint relevant;
- interface version governs callable compatibility;
- implementation evidence is evidence only;
- DPA-300 and DPA-400 use identical terms;
- plans, acceptance state, evidence and drift semantics are consistent.

### E. Minor and editorial closure

Verify that:

1. failure diagnostics are bounded, failure-only and lifecycle-translated;
2. diagnostics cannot coexist with success output or become authority;
3. capability conformance requires the closed invocation boundary and deterministic prohibited-capability tests;
4. hard OS/process isolation remains optional and Probe-assessed;
5. invocation identity is explicitly defined for memoization;
6. template/import/traversal/shell injection has a requirement, tests and invalid-state coverage;
7. the renderer diagram consumes target bytes, plan/state fingerprints and acceptance state rather than implying a target-only gate;
8. the decision index includes ADR-013 through ADR-020 and marks ADR-018 non-normative;
9. no temporary workflow or helper file remains in the tree.

### F. Cross-artifact audit

Run repository-wide targeted searches for at least:

- `renderer contract version`
- `renderer-version identity`
- `implementation version`
- `MAY read declared canonical sources`
- `representation-only context explicitly permitted`
- `execution duration`
- `A resource limit MUST be deterministic`
- stale DPA-400 primary-review planning language in STATUS or ROADMAP
- any residual temporary one-shot workflow

Classify every occurrence as valid historical prose, current normative text or defect.

### G. Authority and claim audit

Verify:

- no renderer write, lock, workflow, state, evidence or acceptance authority;
- no second registry, lifecycle, renderer map, command, state, evidence or gate subsystem;
- no production-form selection;
- all repository-specific implementation details remain `NEEDS_MAIN_REPO_VALIDATION`;
- DPA-400 remains `draft` at the verification ref;
- no Probe is represented as executed;
- no status promotion is mixed into the normative amendment batch.

## Required report

Produce a commit-ready English report with:

1. metadata and exact ref;
2. independence disclosure;
3. method and reviewed files;
4. overall `PASS`, `FAIL` or `INDEPENDENCE_BLOCKED`;
5. closure table for R4-M01 through R4-M04;
6. closure table for R4-m01 through R4-m06 and editorial findings;
7. DPA-300 ratification verification;
8. DPA-100/300/400 vocabulary consistency audit;
9. traceability and diagram audit;
10. targeted-search results;
11. remaining main-repository validation obligations;
12. promotion recommendation.

Return `PASS` only if DPA-400 can truthfully be promoted to `review-ready` by a later status-only commit. If any residual requires normative text change, return `FAIL` with the smallest bounded correction set.
