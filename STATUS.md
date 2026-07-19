# Status

Status: active

Status-date: 2026-07-19

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is review-complete through DPA-500 and merged through PR #3 at merge commit `1f3e5a64f4be5a974bf979f066d9434505a1d74c`.

Phase C remote preparation is active. **Package P received independent verdict `ACCEPT_WITH_CHANGES`; all findings are Maintainer-adjudicated and corrected, and a limited PPR-M03 rereview is pending.**

The Lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence and adjudication.

## DP1 Discovery evidence

The recorded Discovery baseline is:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed for the inspected scope. Global writer-set completeness is not claimed.

The Discovery SHA is historical evidence only. Current remote `origin/main` MUST be freshly read and locally confirmed before Probe materialization, execution or main-repository mutation.

## DPA-300 through DPA-500

DPA-300 completed review, adjudication, verification and restructure-ratification. ADR-021 contains the synchronized bounded amendment for conditional accepted-base persistence and layered post-acceptance comparison.

DPA-400 completed primary review, adjudication, amendment, independent verification and status-only promotion. It remains `review-ready`; repository-specific renderer mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-500 completed primary review, adjudication, independent post-adjudication verification and promotion to `review-ready`. Editorials V5-e01 and V5-e02 remain parked for the next otherwise-required bounded amendment.

The DPA-500 landing on `main` used a squash merge. Future governed batches whose assurance depends on commit sequence MUST preserve that sequence and record durable source commit SHAs outside a deletable branch.

## DPA-600 frozen draft

Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft. It introduces no new runtime authority and selects no concrete main-repository workflow or locking implementation. Concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-600 remains frozen:

- status remains `draft`;
- no `review-ready` promotion;
- no material expansion into concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanics;
- only sequencing, status, evidence-boundary and defect-correction edits are allowed;
- DPA-700 is `planned` and MUST NOT begin.

## Package P review and correction state

Independent review:

- exact reviewed ref: `18d0fd08b27d97aef1b06b5a75079527290ca8e4`;
- verdict: `ACCEPT_WITH_CHANGES`;
- findings: 0 blockers, 3 majors, 4 minors, 3 editorials;
- report: `reviews/claude/CLAUDE_PACKAGE_P_REVIEW.md`;
- Maintainer adjudication: all findings accepted;
- adjudication record: `reviews/adjudication/PACKAGE_P_REVIEW_ADJUDICATION.md`.

Corrections completed:

1. PROBE-001 P001-C020 now enforces unconditional encoding/normalization/line-ending declaration rejection;
2. PROBE-001 P001-C023 now requires ultimate fail-loud unknown-renderer rejection while leaving the owning stage provisional;
3. PROBE-002 now has 60 cases, including gate-set-change-triggered re-acceptance and block-new/strict fail-closed behavior for new projections while legacy accepted content may remain readable;
4. all three Probe packages require explicit case totals and bidirectional case/fixture mapping;
5. renderer secret isolation contains the accepted-future bounded-need qualifier;
6. cross-Probe conclusions are bounded across divergent refs;
7. portability planning labels the Discovery SHA as historical and requires a fresh current ref;
8. shared-contract status and lifecycle-order navigation are clarified;
9. correction audit result is `PASS_AFTER_CORRECTION`.

No executable fixture has been materialized. No Probe has run. No implementation, adoption or main-repository conformance is claimed.

## Active work order

The next binding work is:

1. obtain a successful Lab gate for the corrected package;
2. preserve a new immutable corrected Package-P review ref;
3. request independent rereview limited to PPR-M03 and direct synchronization consequences;
4. perform Maintainer disposition of that limited rereview;
5. only then close Package P and permit local fixture-materialization planning;
6. keep Probe execution blocked until exact current main-repository ref, local equality, immutable fixture revisions, isolation, observation and cleanup preconditions are established.

## Probe relationship

PROBE-001 tests registry parser and validator compatibility against DPA-300 and ADR-017.

PROBE-002 tests lifecycle planning, Workspace resolution, locks, reentrancy, stale-plan handling, Write–Verify–Record–Release ordering, acceptance state, recovery, conditional base persistence, gate-set-change-triggered re-acceptance, layered acceptance, findings and staged enforcement.

The DPA-400 renderer Probe package tests closed static resolution, interface and version behavior, immutable inputs, source-as-data and bounded secret boundaries, determinism, output scope, lifecycle-only invocation, prohibited capabilities, resource behavior and failure semantics.

DPA-600 concrete mappings require exact-ref validation and applicable Probe evidence. The current draft does not establish implementation capability.

## Restrictions

- No production code in the Lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its reviewed contract, immutable freeze and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without Maintainer adjudication.
- No quick fix to handoff writers, lifecycle Apply, writer semantics, acceptance state, recovery completion, re-acceptance, layered acceptance or projection gates before PROBE-002 execution, adjudication and subsequent architecture revalidation.
- No DPA-600 continuation before final Package-P disposition.
- No DPA-700 work while Package P remains undispositioned.
- No squash merge for governed batches whose verification depends on preserved commit sequence.
