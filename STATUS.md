# Status

Status: active

Status-date: 2026-07-18

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is review-complete through DPA-500 and merged through PR #3 at merge commit `1f3e5a64f4be5a974bf979f066d9434505a1d74c`.

Phase C remote preparation is active. The immediate priority is **Package P — Remote Probe Preparation** under `MASTERPLAN.md` and the corrected `MASTERPLAN_REMOTE_PREPARATION.md`.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence and adjudication.

## DP1 Discovery evidence

The recorded Discovery baseline is:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed for the inspected scope. Global writer-set completeness is not claimed.

Every observation from `6a9da7d…` is historical exact-ref evidence and MUST be revalidated against current `origin/main` and locally confirmed before mutation.

## DPA-300 through DPA-500

DPA-300 completed its review, adjudication, verification and later restructure-ratification path. ADR-021 contains the synchronized bounded amendment for conditional accepted-base persistence and layered post-acceptance comparison.

DPA-400 completed primary review, adjudication, amendment, independent verification and status-only promotion. It is `review-ready`; repository-specific renderer mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-500 completed primary review, adjudication, independent post-adjudication verification and promotion to `review-ready`. Editorials V5-e01 and V5-e02 remain parked for the next otherwise-required bounded amendment.

The DPA-500 landing on `main` used a squash merge. The governed branch commit sequence therefore remains relevant evidence. Future governed batches whose assurance depends on commit sequence MUST use a merge method that preserves that sequence and MUST record durable source commit SHAs outside a deletable branch.

## DPA-600 frozen draft

Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft covering concurrency domains, lifecycle-owned local Workspace locking, same-process reentrancy boundaries, independent drift guards, cross-ref revalidation, stale-plan rejection, acceptance-state interaction and fail-loud evidence obligations.

The draft introduces no new runtime authority and selects no concrete main-repository workflow or locking implementation. Concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-600 is frozen while Package P is active:

- status remains `draft`;
- no `review-ready` promotion;
- no material expansion into concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanics;
- only sequencing, status, evidence-boundary and defect-correction edits are allowed;
- DPA-700 is `planned` and MUST NOT begin.

## Package P progress

Completed at the remote semantic-preparation level:

1. shared Probe execution and evidence contract;
2. PROBE-001 manual, fixture manifest and internal contract audit — `PASS_AFTER_CORRECTION`;
3. PROBE-002 manual, fixture manifest and internal contract audit — `PASS_AFTER_CORRECTION`;
4. DPA-400 renderer Probe manual, fixture manifest and internal contract audit — `PASS_AFTER_CORRECTION`;
5. exact-ref freeze procedure;
6. bounded evidence-capture procedure;
7. Maintainer adjudication procedure;
8. expanded canonical CSC, namespace-profile and external-habitability checklist.

None of these artifacts records Probe execution, frozen current main-repository refs, materialized executable fixtures, adoption or main-repository conformance.

## Active work order — remaining Package P

The next binding work is:

1. specify Probe-independent portability slices;
2. prove for each slice that registry schema, lifecycle semantics, writer semantics, acceptance state and gate authority are unchanged;
3. synchronize project-control and handoff surfaces;
4. prepare a closed Package P review set and immutable Lab review ref;
5. request bounded independent verification;
6. keep DPA-600 frozen and DPA-700 unstarted until the package is dispositioned.

Probe preparation MUST remain distinct from Probe execution.

## Probe relationship

PROBE-001 tests registry parser and validator compatibility against DPA-300 and ADR-017.

PROBE-002 tests lifecycle planning, Workspace resolution, locks, reentrancy, stale-plan handling, Write–Verify–Record–Release ordering, acceptance state, recovery, conditional base persistence, gate-set re-acceptance, layered acceptance, findings and staged enforcement.

The DPA-400 renderer Probe package tests closed static resolution, interface and version behavior, immutable inputs, source-as-data and secret boundaries, determinism, output scope, lifecycle-only invocation, prohibited capabilities, resource behavior and failure semantics.

DPA-600 concrete lock, guard, workflow and integration mappings require exact-ref validation and applicable Probe evidence. The current draft does not establish implementation capability.

## Restrictions

- No production code in the Lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without adjudication.
- No quick fix to handoff writers, lifecycle Apply, writer semantics, acceptance state, recovery completion, re-acceptance, layered acceptance or projection gates before PROBE-002 and subsequent architecture revalidation.
- No DPA-700 work while Package P is active.
- No squash merge for governed batches whose verification depends on preserved commit sequence.

Phase B through DPA-500 remains review-complete. Package P is active. DPA-600 remains a frozen bounded draft in PR #5; DPA-700 has not started.
