# Status

Status: active

Status-date: 2026-07-19

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is review-complete through DPA-500 and merged through PR #3 at merge commit `1f3e5a64f4be5a974bf979f066d9434505a1d74c`.

Phase C remote preparation has completed **Package P — Remote Probe Preparation**. The independent primary review, Maintainer adjudication, all bounded corrections, limited PPR-M03 rereview and final editorial correction are complete. Package P is finally closed at the Lab preparation level.

The active phase is now **Package M — exact-ref materialization preparation plus document mutation authority and command integration**. The current remote main-repository ref has been freshly read. A bounded remote surface inventory, local materialization plan and binding command-integration planning addendum are committed. Local equality, local cleanliness, complete inventories and executable materialization remain unverified.

The Lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence and adjudication.

## Current main-repository evidence

Fresh remote read on 2026-07-19:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Commit subject:

`Refresh handoff state after PR1863 (#1864)`

The freshly read ref equals the historical DP1 Discovery baseline, but is recorded as a new remote observation in:

`evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`

DISC-001 through DISC-010 and DISC-003b remain historical evidence for the inspected scope. Global writer-set and document-command completeness are not claimed.

Local HEAD equality, worktree cleanliness, environment identity and actual command behavior remain to be confirmed on the Mac. If remote `main` moves before local confirmation, a new current-ref record is required.

## Newly identified architecture gap

The DPA already defines registry, renderer, lifecycle, workflow, evidence, freshness, gate and acceptance boundaries. It does not yet completely define the mutation authority of every Agentic Kit command and internal entry point that creates, refreshes, rewrites, reconciles, appends, moves, archives or deletes document-like artifacts.

That gap matters because the motivating handoff and status drift failure class cannot be excluded while commands may independently write the same semantic fact, update generated artifacts outside one governed plan, write beyond declared scope or return success without post-write verification.

The binding planning artifact is:

`integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`

A non-normative decision proposal is recorded as:

`decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`

ADR-022 is `DEFERRED PROPOSAL`. It does not yet amend normative DPA specifications or authorize main-repository changes.

Expected later bounded amendment surfaces are DPA-200, DPA-300, DPA-400 and DPA-500, with later synchronized consequences for DPA-600, DPA-700 and DPA-800 when their sequencing permits work.

## DPA-300 through DPA-500

DPA-300 completed review, adjudication, verification and restructure-ratification. ADR-021 contains the synchronized bounded amendment for conditional accepted-base persistence and layered post-acceptance comparison.

DPA-400 completed primary review, adjudication, amendment, independent verification and status-only promotion. It remains `review-ready`; repository-specific renderer mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-500 completed primary review, adjudication, independent post-adjudication verification and promotion to `review-ready`. Editorials V5-e01 and V5-e02 remain parked for the next otherwise-required bounded amendment.

The command-integration gap does not silently reopen these specifications. It creates a bounded amendment proposal that must first be supported by complete command inventory, exact-ref evidence, independent review and Maintainer adjudication.

## DPA-600 frozen draft

Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft. It introduces no new runtime authority and selects no concrete main-repository workflow or locking implementation. Concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-600 remains frozen:

- status remains `draft`;
- no `review-ready` promotion;
- no material expansion into concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanics;
- only sequencing, status, evidence-boundary and defect-correction edits are allowed;
- DPA-700 is `planned` and MUST NOT begin.

The proposed command-integration consequences for DPA-600 and DPA-700 are recorded only as later dependencies, not as present specification work.

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

## Remote surface inventory and Package-M plans

Committed planning artifacts:

1. `evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`;
2. `integration/MAIN_REPO_REMOTE_SURFACE_INVENTORY_20260719.md`;
3. `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`;
4. `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`;
5. `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`.

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
- DPA staged-enforcement mechanism;
- command-to-document mutation-authority inventory;
- generated-artifact ownership map;
- proof that declared and actual command output scopes are equal;
- proof that handoff, status and related semantic facts have no unauthorized duplicate writers.

Those surfaces remain `VERIFICATION_BLOCKED` or `REMOTE_PARTIAL`. Their absence must be recorded honestly; no fixture or architecture text may invent them and then attribute them to the implementation.

## Active remote iPhone work order

Before Mac access, the next binding work is:

1. inventory every CLI command mode and internal entry point that may create, update, move, archive or delete document-like artifacts;
2. record canonical inputs, declared targets, discovered write paths, Workspace resolution, lock and lifecycle ownership for each;
3. classify every command mode provisionally as CMA-1 through CMA-8 under the command-integration plan;
4. build a semantic-fact overlap matrix for handoff, status, planning, registry, command-reference, lifecycle, transfer and evidence families;
5. build the generated-artifact ownership matrix, including direct-edit policy and regeneration authority;
6. map command integration to existing Probe cases and identify bounded additions or amendments;
7. prepare exact proposed DPA-200/300/400/500 clauses, traceability updates and diagrams without yet making them normative;
8. prepare an independent architecture-review package for ADR-022 and the bounded amendment proposal;
9. complete the provisional materializability classification of all Probe cases;
10. refine the exact-ref, isolation, cleanup and fixture-freeze schemas;
11. prepare the complete local Mac execution contract.

This work is planning and read-only main-repository inspection. It must not claim global completeness until local confirmation.

## Later local Mac work order

After Mac access:

1. reread current remote `origin/main` immediately before local work;
2. record local HEAD, remote HEAD, equality and worktree cleanliness;
3. record Python, virtual-environment, package and Workspace-profile identity;
4. enumerate the installed CLI and compare it with the remote command inventory;
5. create a disposable fixture root and isolated evidence root;
6. test containment, sentinel cleanup and protected-path hash checks;
7. build the complete local Workspace, registry, reader, writer, command, lifecycle, lock, renderer, state, gate, recovery and evidence inventories;
8. execute only approved read-only or disposable-repository command observations;
9. compare each command's declared and actual changed-path scope;
10. classify every Probe case as executable, observation-only, implementation-absent, unsafe, ambiguous, harness-required or inventory-blocked;
11. materialize only bounded fixtures whose current implementation surfaces and isolation are proven;
12. preserve immutable fixture revisions and hashes;
13. run exact-ref freeze only after all materialization exit conditions pass;
14. execute PROBE-001, PROBE-002 and the renderer Probe only after freeze and all safety preconditions;
15. capture and adjudicate evidence;
16. review and adjudicate ADR-022 and the bounded normative amendment package;
17. revalidate DPA-300 through DPA-500;
18. only then reconsider evidence-bounded DPA-600 continuation.

Local fixture-materialization planning is permitted. Executable materialization is conditional on the local entry gates. Probe execution remains blocked.

## Probe relationship

PROBE-001 tests registry parser and validator compatibility against DPA-300 and ADR-017.

PROBE-002 tests lifecycle planning, Workspace resolution, locks, reentrancy, stale-plan handling, Write–Verify–Record–Release ordering, acceptance state, recovery, conditional base persistence, gate-set-change-triggered re-acceptance, layered acceptance, findings and staged enforcement.

The DPA-400 renderer Probe package tests closed static resolution, interface and version behavior, immutable inputs, source-as-data and bounded secret boundaries, determinism, output scope, lifecycle-only invocation, prohibited capabilities, resource behavior and failure semantics.

Command integration must additionally establish or explicitly classify command mutation authority, canonical inputs, generated-artifact ownership, declared-versus-actual output scope, duplicate semantic writers, composed-command behavior and post-write verification. Existing Probe contracts may require bounded synchronized amendments after review; no silent case change is permitted.

DPA-600 concrete mappings require exact-ref validation and applicable Probe evidence. The current draft does not establish implementation capability.

## Restrictions

- No production code in the Lab.
- No `.agentic/` initialization or simulated adoption in the Lab.
- No production-form selection from historical Discovery evidence.
- No executable fixture materialization before local ref, environment, containment and cleanup gates pass.
- No Probe execution without its reviewed contract, immutable freeze and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No quick fix to handoff writers, status writers, lifecycle Apply, writer semantics, acceptance state, recovery completion, re-acceptance, layered acceptance or projection gates before PROBE-002 execution, adjudication and subsequent architecture revalidation.
- No direct patch to a generated artifact may be represented as the durable fix unless its authority and regeneration contract explicitly permit direct maintenance.
- No new command registry, writer authority, lifecycle, state store, evidence service or gate system.
- No DPA-600 continuation before applicable Probe evidence and revalidation.
- No DPA-700 work while DPA-600 remains frozen.
- No squash merge for governed batches whose verification depends on preserved commit sequence.

## Proactive architecture-gap obligation

During future work, material gaps that would leave the motivating failure class possible must be surfaced even when the Maintainer did not know to ask about them.

Each concern must be classified as a confirmed architecture gap, suspected gap requiring evidence, implementation defect under an adequate contract, editorial inconsistency or out-of-scope improvement.