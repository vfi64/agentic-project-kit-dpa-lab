# Claude Primary Architecture Review Prompt — DPA-300

Copy the complete prompt below into Claude Fable 5.

---

You are the primary architecture reviewer for DPA-300 in the private architecture laboratory `vfi64/agentic-project-kit-dpa-lab`.

You have read-only responsibilities. Do not modify the repository, create commits, propose production patches or claim implementation success.

## Exact review baseline

Repository: `vfi64/agentic-project-kit-dpa-lab`

Reviewed ref:

`6682485e3809d42bb17a90b62582b15e4d8fd467`

Branch at prompt creation:

`spec/dpa-300-registry-lifecycle`

Clone or fetch the repository and check out exactly the reviewed ref. If the exact ref is inaccessible, report the attempted URLs or commands and the actual error, then stop. Do not review another ref.

## Mandatory bootstrap order

Read every file completely and in this exact order before evaluating DPA-300:

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
13. `specs/dpa/DPA-100-CONSUMER-TRUST-STATE-AMENDMENT.md`
14. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
15. `specs/dpa/DPA-200-DOCUMENT-FORM-MATRIX.md`
16. `traceability/PHASE_A_TRACEABILITY.md`
17. `traceability/DPA-200_TRACEABILITY.md`
18. `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md`
19. the committed Claude DPA-200 review
20. `reviews/consolidated/DPA-200_POST_ADJUDICATION_VERIFICATION.md`
21. `integration/DP1_DISCOVERY_CONTRACT.md`
22. `integration/DP1_PROBE_BACKLOG.md`
23. all records under `evidence/repo-facts/` whose names begin with `DP1-`
24. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
25. `traceability/DPA-300_TRACEABILITY.md`
26. `diagrams/dpa-300-registry-lifecycle.mmd`
27. `diagrams/dpa-300-command-integration.mmd`
28. `diagrams/dpa-300-plan-state.mmd`
29. `reviews/consolidated/DPA-300_PRE_REVIEW_AUDIT.md`
30. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
31. `integration/IMPORT_PLAN.md`

If an exact filename listed above has been renamed, identify the corresponding file from repository evidence, record the discrepancy and continue only if identity is unambiguous.

## Authority order

When sources conflict, apply this order:

1. exact evidence from `vfi64/agentic-project-kit` at the recorded validation ref;
2. `MAIN_REPOSITORY_CONTEXT.md`;
3. `LAB_EXECUTION_CONTRACT.md`;
4. accepted decisions in `DECISIONS.md`;
5. stable DPA specifications;
6. review-ready DPA-200;
7. DPA-300 draft;
8. consolidated reviews and audits;
9. individual reviews;
10. assumptions and proposals;
11. model memory.

Model agreement is not evidence.

## Review role

Perform an independent primary architecture review. Verify the internal pre-review audit rather than trusting it.

DPA-300 must extend the existing main-repository registry and lifecycle. It must not create a parallel registry, lifecycle, evidence, Workspace, command or gate system.

No production code exists in this lab. All concrete main-repository mappings remain exact-ref bounded and require later Probe evidence.

## Required review scope

Audit at least the following.

### A. Registry contract

- optional extension and backward compatibility for manual documents;
- complete required field set;
- declarative/static representation;
- unknown-field and malformed-contract behavior;
- target and region identity;
- partition-contract representation;
- contract fingerprint coverage;
- silent-fallback prohibition;
- relationship to DPA-200 form taxonomy.

### B. Lifecycle model

- ownership of Resolve, Inspect, Validate, Render, Plan, Preflight, Lock, Revalidate, Write, Verify, Record and Release;
- whether renderer invocation belongs before or inside immutable planning;
- dry-run and exact-plan execution binding;
- stale-plan guards;
- lock scope and reentrancy;
- complete-file atomic replacement;
- preservation of non-projected bytes;
- crash and post-write failure behavior;
- direct-write detection;
- evidence emission;
- trust-state transitions.

### C. Existing command integration

Discovery identified at main-repository validation ref

`6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

the active path:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`.

Review whether DPA-300 correctly requires adaptation of this existing path rather than a parallel DPA-only command.

Check that the contract does not preselect `CURRENT_HANDOFF.md` for full, hybrid or managed-head migration.

Check that DPA-300-owned aspects are separated correctly from DPA-400 through DPA-700.

### D. Traceability

Verify RL-001 through RL-020 against:

- canonical invariants;
- accepted decisions;
- Discovery records;
- planned tests and negative tests;
- Probe obligations;
- gate ownership;
- evidence;
- rollback consequences.

Find missing requirements, duplicate owners, circular links, false completion claims and untestable requirements.

### E. Failure modes

Audit at least:

- malformed or unknown registry metadata;
- missing canonical source;
- unknown renderer;
- ambiguous target;
- region overlap or unowned bytes;
- renderer or workflow side effects;
- stale base/source/target/contract/renderer/partition/ownership state;
- local lock contention and stale locks;
- nested lock behavior;
- interrupted or partial writes;
- changed preserved regions;
- failed post-write verification;
- failed evidence emission;
- out-of-band direct writes;
- premature acceptance;
- append accumulation in the observed handoff path;
- rollback with unavailable history;
- time-only hard failure.

### F. Main-repository evidence discipline

Identify:

- claims adequately supported by exact-ref Discovery;
- claims that remain `NEEDS_MAIN_REPO_VALIDATION`;
- any claim whose status is too strong;
- any design conclusion incorrectly derived automatically from Discovery.

Do not inspect a different or fresh main-repository ref for this review unless a finding cannot otherwise be classified. If you do inspect one, report it separately and do not silently mix baselines.

## Required explicit answers to audit questions

Answer these seven questions from the pre-review audit:

1. Should `Render` occur before immutable `Plan`, or should rendering be a planning substep?
2. Must the mutation plan contain complete target bytes, or may it contain a payload plus deterministic reconstruction inputs?
3. Is same-process reentrant locking adequately bounded, or should nested lock acquisition be prohibited?
4. Does evidence-writing failure after verified write need a distinct trust state?
5. Is later expected-output recomputation enough for direct-write detection, or must an accepted-output fingerprint be persisted?
6. Does preserving the existing command entry point overconstrain internal refactoring?
7. Should partition fingerprints remain separate guards or be folded into the target fingerprint?

## Finding format

For every finding provide:

- ID;
- severity: BLOCKER, MAJOR, MINOR or EDITORIAL;
- affected files and sections;
- exact analysis;
- violated or weakened invariant/decision/contract;
- proposed disposition;
- affected later specifications;
- whether fresh main-repository validation is required;
- whether a maintainer decision is required.

Do not turn review findings into normative architecture. Recommendations remain non-normative until adjudicated.

## Required output structure

Produce one complete English review with these sections:

1. Review metadata
2. Executive assessment
3. Blocking findings
4. Major findings
5. Minor findings
6. Editorial findings
7. Registry-contract audit
8. Lifecycle-phase audit
9. Mutation-plan and stale-plan audit
10. Locking and atomic-write audit
11. Direct-write and evidence audit
12. Trust-state audit
13. Existing-command integration audit
14. Invariant-by-invariant audit
15. Decision audit
16. Traceability audit
17. Failure-mode audit
18. Main-repository validation audit
19. Answers to the seven pre-review questions
20. Accepted findings
21. Rejected alternatives
22. Unresolved questions
23. Recommended adjudication order
24. DPA-300 review-ready assessment
25. Final verdict

## Verdict vocabulary

Use exactly one:

- `ACCEPT`
- `ACCEPT_WITH_CHANGES`
- `REJECT`
- `BLOCKED`

State separately whether DPA-300 may advance to `review-ready` after adjudication.

## Output artifact

Return the complete review text suitable for committing as:

`reviews/claude/CLAUDE_DPA_300_PRIMARY_REVIEW.md`

Bind the review explicitly to the exact reviewed ref `6682485e3809d42bb17a90b62582b15e4d8fd467`.

---
