# Status

Status: active

Status-date: 2026-07-18

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is review-complete through DPA-500 and merged through PR #3 at merge commit `1f3e5a64f4be5a974bf979f066d9434505a1d74c`.

Phase C remote preparation is active. **Package P — Remote Probe Preparation is internally prepared and awaiting bounded independent verification.**

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence and adjudication.

## DP1 Discovery evidence

The recorded Discovery baseline is:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed for the inspected scope. Global writer-set completeness is not claimed.

Remote inspection during Package-P preparation observed the same current `main` SHA. This does not replace local equality, cleanliness or concrete path confirmation before Probe execution or mutation.

## DPA-300 through DPA-500

DPA-300 completed its review, adjudication, verification and later restructure-ratification path. ADR-021 contains the synchronized bounded amendment for conditional accepted-base persistence and layered post-acceptance comparison.

DPA-400 completed primary review, adjudication, amendment, independent verification and status-only promotion. It is `review-ready`; repository-specific renderer mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-500 completed primary review, adjudication, independent post-adjudication verification and promotion to `review-ready`. Editorials V5-e01 and V5-e02 remain parked for the next otherwise-required bounded amendment.

The DPA-500 landing on `main` used a squash merge. Future governed batches whose assurance depends on commit sequence MUST preserve that sequence and record durable source commit SHAs outside a deletable branch.

## DPA-600 frozen draft

Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft covering concurrency domains, lifecycle-owned local Workspace locking, same-process reentrancy boundaries, independent drift guards, cross-ref revalidation, stale-plan rejection, acceptance-state interaction and fail-loud evidence obligations.

The draft introduces no new runtime authority and selects no concrete main-repository workflow or locking implementation. Concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-600 remains frozen:

- status remains `draft`;
- no `review-ready` promotion;
- no material expansion into concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanics;
- only sequencing, status, evidence-boundary and defect-correction edits are allowed;
- DPA-700 is `planned` and MUST NOT begin.

## Package P prepared set

Prepared and internally synchronized:

1. shared Probe execution and evidence contract;
2. PROBE-001 manual, fixture manifest and internal audit — `PASS_AFTER_CORRECTION`;
3. PROBE-002 manual, fixture manifest and internal audit — `PASS_AFTER_CORRECTION`;
4. DPA-400 renderer Probe manual, fixture manifest and internal audit — `PASS_AFTER_CORRECTION`;
5. exact-ref freeze procedure;
6. bounded evidence-capture procedure;
7. Maintainer adjudication procedure;
8. expanded canonical CSC, namespace-profile and external-habitability checklist;
9. Probe-independent portability slice plan;
10. Package-P internal consistency audit — `PASS_AFTER_CORRECTION`;
11. synchronized successor handoff.

No executable fixture has been materialized. No Probe has run. No implementation, adoption or main-repository conformance is claimed.

## Active work order

The next binding work is:

1. preserve an immutable Package-P Lab review ref;
2. request bounded independent verification against that exact ref;
3. preserve review method, reviewed files, findings and limitations;
4. perform Maintainer adjudication;
5. correct only accepted findings on the working branch;
6. keep DPA-600 frozen and DPA-700 unstarted until Package P is dispositioned.

## Probe relationship

PROBE-001 tests registry parser and validator compatibility against DPA-300 and ADR-017.

PROBE-002 tests lifecycle planning, Workspace resolution, locks, reentrancy, stale-plan handling, Write–Verify–Record–Release ordering, acceptance state, recovery, conditional base persistence, gate-set re-acceptance, layered acceptance, findings and staged enforcement.

The DPA-400 renderer Probe package tests closed static resolution, interface and version behavior, immutable inputs, source-as-data and secret boundaries, determinism, output scope, lifecycle-only invocation, prohibited capabilities, resource behavior and failure semantics.

DPA-600 concrete lock, guard, workflow and integration mappings require exact-ref validation and applicable Probe evidence. The current draft does not establish implementation capability.

## Restrictions

- No production code in the Lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its governing reviewed contract, immutable freeze and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without Maintainer adjudication.
- No quick fix to handoff writers, lifecycle Apply, writer semantics, acceptance state, recovery completion, re-acceptance, layered acceptance or projection gates before PROBE-002 execution, adjudication and subsequent architecture revalidation.
- No DPA-600 continuation before Package-P review disposition.
- No DPA-700 work while Package P remains undispositioned.
- No squash merge for governed batches whose verification depends on preserved commit sequence.
