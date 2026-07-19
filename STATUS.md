# Status

Status: active

Status-date: 2026-07-19

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is review-complete through DPA-500 and merged through PR #3 at merge commit `1f3e5a64f4be5a974bf979f066d9434505a1d74c`.

Phase C remote preparation has completed **Package P — Remote Probe Preparation**. The independent primary review, Maintainer adjudication, all bounded corrections, limited PPR-M03 rereview and final editorial correction are complete. Package P is finally closed at the Lab preparation level.

The next active phase is **local fixture-materialization planning and exact-ref reality contact**. The current remote main-repository ref has been freshly read and a bounded exact-ref remote surface inventory plus a governed local materialization plan are committed. Local equality, local cleanliness, complete inventories and executable materialization remain unverified.

The Lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence and adjudication.

## Current main-repository evidence

Fresh remote read on 2026-07-19:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Commit subject:

`Refresh handoff state after PR1863 (#1864)`

The freshly read ref equals the historical DP1 Discovery baseline, but is recorded as a new remote observation in:

`evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`

DISC-001 through DISC-010 and DISC-003b remain historical evidence for the inspected scope. Global writer-set completeness is not claimed.

Local HEAD equality, worktree cleanliness, environment identity and actual command behavior remain to be confirmed on the Mac. If remote `main` moves before local confirmation, a new current-ref record is required.

## DPA-300 through DPA-500

DPA-300 completed review, adjudication, verification and restructure-ratification. ADR-021 contains the synchronized bounded amendment for conditional accepted-base persistence and layered post-acceptance comparison.

DPA-400 completed primary review, adjudication, amendment, independent verification and status-only promotion. It remains `review-ready`; repository-specific renderer mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-500 completed primary review, adjudication, independent post-adjudication verification and promotion to `review-ready`. Editorials V5-e01 and V5-e02 remain parked for the next otherwise-required bounded amendment.

## DPA-600 frozen draft

Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft. It introduces no new runtime authority and selects no concrete main-repository workflow or locking implementation. Concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-600 remains frozen:

- status remains `draft`;
- no `review-ready` promotion;
- no material expansion into concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanics;
- only sequencing, status, evidence-boundary and defect-correction edits are allowed;
- DPA-700 is `planned` and MUST NOT begin.

## Package P final state

Primary independent review:

- exact reviewed ref: `18d0fd08b27d97aef1b06b5a75079527290ca8e4`;
- verdict: `ACCEPT_WITH_CHANGES`;
- findings: 0 blockers, 3 majors, 4 minors, 3 editorials;
- all findings accepted and corrected.

Limited PPR-M03 rereview:

- exact reviewed ref: `c12eb19acb07325958e06800f5591aa3bf5f03c7`;
- substantive PPR-M03 result: resolved;
- finding: one editorial C059/C060 numbering transposition in the adjudication record;
- final disposition: accepted and corrected;
- further independent rereview required: no.

Final closure:

- `reviews/adjudication/PACKAGE_P_FINAL_CLOSURE.md`;
- open Package-P review findings: 0;
- architecture amendments required by Package-P review: 0;
- executable fixtures materialized: no;
- Probes executed: no;
- implementation, adoption or main-repository conformance claimed: no.

## Remote surface inventory and materialization plan

Committed planning artifacts:

1. `evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`;
2. `integration/MAIN_REPO_REMOTE_SURFACE_INVENTORY_20260719.md`;
3. `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`.

Remote evidence currently establishes concrete existing surfaces for:

- Workspace and path resolution;
- documentation-registry loading and validation entry points;
- documentation lifecycle reporting and findings;
- Workspace mutation locking and its audit;
- operational evidence tooling;
- top-level CLI routing.

Remote evidence does not yet establish a complete DPA-compatible:

- static renderer map and callable boundary;
- ProjectionContract or PartitionContract serialization;
- Render–Plan–Preflight–Lock–Revalidate–Write–Verify–Record–Release implementation;
- authoritative acceptance state;
- gate-set re-acceptance;
- layered acceptance;
- target-write recovery state machine;
- DPA staged-enforcement mechanism.

Those surfaces remain `VERIFICATION_BLOCKED` or `REMOTE_PARTIAL`. Their absence must be recorded honestly during local inventory; no fixture may invent them and then attribute them to the implementation.

## Active work order

The next binding work is now local and read-only first:

1. reread current remote `origin/main` immediately before local work;
2. record local HEAD, remote HEAD, equality and worktree cleanliness;
3. record Python, virtual-environment, package and Workspace-profile identity;
4. create a disposable fixture root and isolated evidence root;
5. test containment, sentinel cleanup and protected-path hash checks;
6. build the complete local Workspace, registry, reader, writer, lifecycle, lock, renderer, state, gate, recovery and evidence inventories defined by `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`;
7. classify every Probe case as executable, observation-only, implementation-absent, unsafe, ambiguous, harness-required or inventory-blocked;
8. materialize only bounded fixtures whose current implementation surfaces and isolation are proven;
9. preserve immutable fixture revisions and hashes;
10. run exact-ref freeze only after all materialization exit conditions pass;
11. execute PROBE-001, PROBE-002 and the renderer Probe only after freeze and all safety preconditions;
12. capture and adjudicate evidence;
13. revalidate DPA-300 through DPA-500;
14. only then reconsider evidence-bounded DPA-600 continuation.

Local fixture-materialization planning is permitted. Executable materialization is conditional on the local entry gates. Probe execution remains blocked.

## Probe relationship

PROBE-001 tests registry parser and validator compatibility against DPA-300 and ADR-017.

PROBE-002 tests lifecycle planning, Workspace resolution, locks, reentrancy, stale-plan handling, Write–Verify–Record–Release ordering, acceptance state, recovery, conditional base persistence, gate-set-change-triggered re-acceptance, layered acceptance, findings and staged enforcement.

The DPA-400 renderer Probe package tests closed static resolution, interface and version behavior, immutable inputs, source-as-data and bounded secret boundaries, determinism, output scope, lifecycle-only invocation, prohibited capabilities, resource behavior and failure semantics.

DPA-600 concrete mappings require exact-ref validation and applicable Probe evidence. The current draft does not establish implementation capability.

## Restrictions

- No production code in the Lab.
- No `.agentic/` initialization or simulated adoption in the Lab.
- No production-form selection from historical Discovery evidence.
- No executable fixture materialization before local ref, environment, containment and cleanup gates pass.
- No Probe execution without its reviewed contract, immutable freeze and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No quick fix to handoff writers, lifecycle Apply, writer semantics, acceptance state, recovery completion, re-acceptance, layered acceptance or projection gates before PROBE-002 execution, adjudication and subsequent architecture revalidation.
- No DPA-600 continuation before applicable Probe evidence and revalidation.
- No DPA-700 work while DPA-600 remains frozen.
- No squash merge for governed batches whose verification depends on preserved commit sequence.
