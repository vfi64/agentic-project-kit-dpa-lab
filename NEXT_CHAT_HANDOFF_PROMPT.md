# Next Chat Handoff Prompt

We are developing the Document Projection Architecture in the private architecture Lab `vfi64/agentic-project-kit-dpa-lab`.

Work only from the current remote repositories and documented contracts. Do not work from chat memory.

## Mandatory bootstrap

Read fully and in this order:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `MASTERPLAN.md`
9. `MASTERPLAN_REMOTE_PREPARATION.md`
10. `DECISIONS.md`
11. `ASSUMPTIONS.md`
12. `specs/dpa/README.md`
13. `specs/dpa/DPA-000-VISION.md`
14. `specs/dpa/DPA-100-FOUNDATIONS.md`
15. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
16. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
17. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
18. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`
19. `specs/dpa/DPA-600-CONCURRENCY.md`
20. relevant accepted ADRs, especially ADR-016, ADR-017, ADR-019, ADR-020 and ADR-021
21. relevant traceability and diagrams
22. `probes/README.md`
23. `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`
24. `probes/PROBE-001-MANUAL.md`
25. `probes/PROBE-001-FIXTURE-MANIFEST.md`
26. `probes/PROBE-002-MANUAL.md`
27. `probes/PROBE-002-FIXTURE-MANIFEST.md`
28. `probes/DPA-400-RENDERER-PROBE-MANUAL.md`
29. `probes/DPA-400-RENDERER-FIXTURE-MANIFEST.md`
30. `probes/EXACT_REF_FREEZE_PROCEDURE.md`
31. `probes/EVIDENCE_CAPTURE_PROCEDURE.md`
32. `probes/PROBE_ADJUDICATION_PROCEDURE.md`
33. `reviews/claude/CLAUDE_PACKAGE_P_REVIEW.md`
34. `reviews/adjudication/PACKAGE_P_REVIEW_ADJUDICATION.md`
35. `reviews/claude/CLAUDE_PACKAGE_P_PPR_M03_REREVIEW.md`
36. `reviews/adjudication/PACKAGE_P_FINAL_CLOSURE.md`
37. `evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`
38. `integration/MAIN_REPO_REMOTE_SURFACE_INVENTORY_20260719.md`
39. `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`
40. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
41. `integration/PORTABILITY_SLICE_PLAN.md`
42. this handoff prompt

Do not begin substantive work before completing the bootstrap.

## Authority and evidence

- Current exact-ref main-repository evidence outranks Lab proposals.
- Normative DPA contracts and accepted ADRs outrank planning documents.
- `MASTERPLAN.md` is the canonical execution plan.
- The current remote main-repository ref was freshly read on 2026-07-19 as `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`.
- That equality with the historical Discovery baseline does not remove the requirement for a fresh read immediately before local work.
- Local equality, cleanliness, environment identity and executable behavior remain unconfirmed.
- No repository-specific claim is `VERIFIED` without current exact-ref inspection and required local confirmation.

## Current Lab state

- DPA-000 and DPA-100: `stable`.
- DPA-200 through DPA-500: `review-ready`.
- DPA-400 and DPA-500 remain blocked from `stable` pending applicable Probe evidence and adjudication.
- Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft.
- DPA-600 remains `draft` and frozen.
- DPA-700 is `planned` and has not started.
- The Lab contains no production kit code and has not been adopted by the main repository.

## Package P state

Package P — Remote Probe Preparation is finally closed.

Completed:

- primary independent verdict `ACCEPT_WITH_CHANGES`;
- 0 blockers, 3 majors, 4 minors and 3 editorials adjudicated and corrected;
- limited PPR-M03 rereview completed;
- its sole editorial numbering finding corrected;
- final Maintainer closure recorded;
- no further Package-P independent rereview required.

No executable fixture has been materialized. No Probe has run. No implementation or main-repository conformance is claimed.

## Active work package

The active work is **Package M — Local Fixture Materialization Planning and Exact-Ref Reality Contact**.

Remote planning already completed:

1. fresh current-main record;
2. exact-ref remote source inventory;
3. governed local fixture-materialization plan;
4. status and roadmap synchronization.

Remote inspection confirms concrete current surfaces for Workspace/path resolution, documentation-registry loading and validation, lifecycle reporting, Workspace mutation locking, operational evidence tooling and CLI routing.

Remote inspection does not yet establish a complete DPA renderer, ProjectionContract/PartitionContract serialization, DPA lifecycle mutation sequence, authoritative acceptance state, re-acceptance, layered acceptance, recovery or staged enforcement. Those must remain absent, partial or blocked until local exact-ref evidence exists. Do not invent them.

## Current immediate task

On the Mac and in the real `vfi64/agentic-project-kit` checkout:

1. reread `origin/main` and record the exact SHA;
2. record local HEAD and require equality;
3. record `git status --short` and require the permitted clean baseline;
4. record Python, virtual environment, package version and Workspace profile/manifest identity;
5. create a disposable fixture root and isolated evidence root;
6. prove path containment, sentinel cleanup and unchanged protected-path hashes;
7. execute only the read-only inventory stages in `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`;
8. produce Workspace, registry, reader, writer, lifecycle, lock, renderer, state/acceptance, gate/freshness, recovery and evidence inventories;
9. classify every Probe case by materialization class;
10. stop before fixture bytes if any entry gate, isolation proof or inventory boundary fails;
11. do not execute any Probe;
12. do not mutate frozen DPA-critical production paths.

## Required distinction

The following are different states and MUST NOT be collapsed:

- semantic fixture prepared;
- concrete fixture materialized;
- fixture set frozen;
- Probe case executed;
- evidence captured;
- result interpreted;
- Maintainer adjudication completed;
- architecture revalidated;
- implementation authorized.

The current state is planning complete remotely, local baseline and inventories pending.

## DPA-600 and main-repository mutation freeze

Until applicable Probe execution, adjudication and architecture revalidation:

- do not materially expand or promote DPA-600;
- do not begin DPA-700;
- do not select concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanisms;
- do not implement quick fixes to handoff writers, Doc Lifecycle Apply, writer semantics, immutable-plan execution, acceptance state, recovery, re-acceptance, layered acceptance, freshness or gate integration;
- do not represent portability candidates as verified without exact source inspection;
- do not materialize fake implementation state to make a Probe executable.

## Merge discipline

Governed batches whose assurance depends on commit sequence MUST NOT be squash-merged. Preserve source commit SHAs, review refs and the selected merge method durably.

Do not claim Probe execution, implementation, adoption or main-repository conformance.
