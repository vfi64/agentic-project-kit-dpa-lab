# Claude Primary Architecture Review Prompt — DPA-400 Renderer Contract

Review repository: `vfi64/agentic-project-kit-dpa-lab`
Review exact immutable ref: `8c9b6892540895e58be53038c6064648d49a2b57`
Branch at prompt creation: `spec/dpa-400-renderer-contract`
Review role: primary architecture reviewer under DPA-ADR-012

## Access and mutation boundary

Clone or fetch the repository and check out the exact ref above.

Do not review a moving branch head.

Do not write, commit, patch or modify the repository. Do not inspect the main repository directly. Repository-specific facts may use only the exact-ref Discovery evidence committed in the lab and must retain its limitations.

If the exact ref is inaccessible, stop and report the attempted access method and actual error. Do not invent content.

## Mandatory bootstrap order

Read fully and in this order before reviewing DPA-400:

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
16. `decisions/DPA-ADR-003-RENDERER-LIFECYCLE-WORKFLOW-BOUNDARIES.md`
17. `decisions/DPA-ADR-004-DERIVATIONAL-FRESHNESS.md`
18. `decisions/DPA-ADR-005-STATIC-RENDERER-RESOLUTION.md`
19. `decisions/DPA-ADR-013-DOCUMENT-FORM-PARTITION-AND-BOUNDARIES.md`
20. `decisions/DPA-ADR-014-CONSUMER-TRUST-STATE-MODEL.md`
21. `decisions/DPA-ADR-016-ACCEPTANCE-STATE-AND-INTERRUPTED-RECOVERY.md`
22. `decisions/DPA-ADR-017-PARENT-ENTRY-PARTITION-CONTRACT.md`
23. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
24. `traceability/DPA-400_TRACEABILITY.md`
25. `diagrams/dpa-400-renderer-boundary.mmd`
26. `reviews/consolidated/DPA-400_PRE_REVIEW_AUDIT.md`
27. `integration/DP1_PROBE_BACKLOG.md`
28. all `DP1-*` records under `evidence/repo-facts/`
29. `reviews/README.md`
30. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
31. `integration/IMPORT_PLAN.md`

Read the internal pre-review audit last among the DPA-400 architecture artifacts and verify it independently rather than trusting it.

## Authority order

When statements conflict, apply:

1. exact main-repository evidence at a concrete ref;
2. `MAIN_REPOSITORY_CONTEXT.md`;
3. `LAB_EXECUTION_CONTRACT.md`;
4. accepted decisions;
5. stable/review-ready normative DPA specifications;
6. DPA-400 draft;
7. consolidated review artifacts;
8. individual reviews;
9. assumptions and proposals;
10. chat memory.

Chat memory is never authority.

## Required review objectives

Independently determine whether DPA-400:

- defines exactly one coherent renderer authority boundary;
- preserves the registry/renderer/lifecycle/workflow separation;
- creates no plugin framework, parallel renderer subsystem, command path, state authority or gate authority;
- uses one closed static renderer mapping and fail-loud unknown-identifier behavior;
- permits only declared semantic sources and contract-declared configuration;
- defines a capability-bounded invocation context with no ambient authority;
- returns only text or immutable bytes for exactly one registered target;
- returns payload-only bytes for registered regions and no partition bytes;
- prohibits writes, state mutation, locks, network, subprocesses, workflows, evidence authority, acceptance assignment and renderer chaining;
- defines determinism and reproducibility strongly enough for DPA-300 plan and acceptance-state fingerprints;
- defines renderer-version identity strongly enough to invalidate stale plans without using raw current HEAD as semantic identity;
- handles failure and resource bounds without truncated or partially accepted output;
- delegates findings, gates, serialization and rollback to DPA-500 through DPA-700 without redefining them;
- remains exact-ref fenced and makes no implementation-success claim;
- may advance to `review-ready` after adjudication while remaining blocked from `stable` before applicable Probe evidence.

## Mandatory special questions

Answer each explicitly:

1. DPA-400 §4 says a renderer may read declared canonical sources, while §§6–7 say the lifecycle resolves and fingerprints sources and the invocation context is sufficient without ambient reads. Must the renderer receive immutable values/content-addressed snapshots only, or may it open lifecycle-resolved paths? What exact rule avoids a fingerprint/read race?
2. DPA-400 §15 requires deterministic resource limits but includes execution duration. How should semantic deterministic bounds be separated from operational safety timeouts whose firing may vary by host load?
3. Does the renderer contract need a bounded diagnostics/result envelope in addition to the single semantic payload? If so, how is it prevented from becoming a second target, finding authority or evidence authority?
4. Is side-effect conformance satisfied by prevention, post-hoc detection, or either mechanism with equivalent negative evidence? Which minimum architecture contract belongs in DPA-400 versus Probe/implementation?
5. Is renderer-version identity sufficiently defined? Assess the relation among canonical renderer identifier, semantic renderer version, implementation fingerprint and source-commit evidence.
6. Does allowing reviewed aliases create a second identity surface or weaken stale-plan comparison?
7. Is permitting contract-declared fixed-seed randomness coherent with the deterministic renderer contract, or should pseudorandom generation be described as deterministic configuration-driven computation rather than randomness?
8. Are renderer failures and trust-state consequences owned consistently, especially the transition to `abandoned` and preservation of prior accepted bytes?
9. Does the resource policy create any semantic dependency on host capacity or scheduling?
10. Are all invalid renderer states owned once, traceable and testable?

## Required review sections

Produce one commit-ready English Markdown review with exactly these sections:

1. Review metadata
2. Executive assessment
3. Blocking findings
4. Major findings
5. Minor findings
6. Editorial findings
7. Renderer authority audit
8. Static-resolution audit
9. Invocation-context and input audit
10. Output and partition-boundary audit
11. Determinism and reproducibility audit
12. Purity and side-effect audit
13. Renderer-version and fingerprint audit
14. Failure and resource-bound audit
15. Existing-command integration audit
16. Invariant-by-invariant audit
17. Decision audit
18. Traceability audit
19. Diagram audit
20. Failure-mode audit
21. Main-repository validation audit
22. Answers to the ten mandatory special questions
23. Accepted findings
24. Rejected alternatives
25. Unresolved questions
26. Recommended adjudication order
27. DPA-400 review-ready assessment
28. Final verdict

## Finding format

Every finding must include:

- stable ID;
- severity: BLOCKING, MAJOR, MINOR or EDITORIAL;
- exact file and section;
- analysis;
- violated or weakened invariant, decision or contract;
- proposed disposition;
- affected later specifications or DP slices;
- whether fresh main-repository validation is required;
- whether a Maintainer decision is required.

Do not make review prose normative. Do not propose production code. Do not claim implementation conformance.

## Verdict scale

Use exactly one:

- `ACCEPT`
- `ACCEPT_WITH_CHANGES`
- `REJECT`
- `BLOCKED`

State separately whether DPA-400 may advance to `review-ready` after adjudication.

A verdict of `ACCEPT_WITH_CHANGES` is appropriate when corrections are bounded and do not require a foundational redesign. A contradiction with canonical invariants, a hidden parallel subsystem, a new runtime authority or an unresolved ownership failure should produce `REJECT` or a blocking finding.

## Output destination

The review must be ready to save as:

`reviews/claude/CLAUDE_DPA_400_PRIMARY_REVIEW.md`

Bind every conclusion to exact reviewed ref:

`8c9b6892540895e58be53038c6064648d49a2b57`