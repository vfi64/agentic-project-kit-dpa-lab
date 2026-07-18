# Roadmap

Status: active

Status-date: 2026-07-18

## Specification sequence

1. DPA-000 — Vision and principles — stable
2. DPA-100 — Foundations and terminology — stable, synchronized through ADR-019
3. DPA-200 — Document model — review-ready
4. DPA-300 — Registry and lifecycle integration — review-ready, restructure lineage ratified and ADR-021 amendment verified
5. DPA-400 — Renderer contract — review-ready after independent post-adjudication verification
6. DPA-500 — Freshness and gates — review-ready after independent post-adjudication verification
7. DPA-600 — Concurrency and workflow serialization — bounded draft frozen in PR #5
8. DPA-700 — Migration and rollback — planned, not started
9. DPA-800 — DP1–DP5 implementation specification — planned
10. DPA-900 — Future evolution — planned
11. reversible Lab adoption with `agentic-project-kit`
12. controlled import into `vfi64/agentic-project-kit`

The normative DPA-number sequence is unchanged. It does not determine the immediate execution order.

`MASTERPLAN.md` owns the canonical execution sequence. `MASTERPLAN_REMOTE_PREPARATION.md` defines the corrected remote order and cannot override the Masterplan.

## Immediate execution order

The active sequence is Probe-first:

1. shared Probe execution and evidence contract;
2. PROBE-001 manual and fixtures;
3. PROBE-002 manual and fixtures;
4. DPA-400 renderer Probe manual and fixtures;
5. current-ref revalidation and exact Probe-ref freeze procedures;
6. CSC and namespace-profile checklist;
7. Probe-independent portability slice specifications;
8. bounded DPA-600 and DPA-700 drafting only within the remaining evidence-independent surface;
9. controlled import, DPA-800 and DPA-900 work after their upstream dependencies permit it.

DPA-600 through DPA-900 MAY receive bounded exploratory drafts before Probe execution only when they remain `draft`, make no repository-specific `VERIFIED` claim, retain `NEEDS_MAIN_REPO_VALIDATION` for concrete mappings and do not displace Probe preparation.

## Current package

**Package P — Remote Probe Preparation** is active.

Branch `spec/dpa-600-concurrency` and Draft PR #5 preserve the bounded initial DPA-600 draft. That draft is frozen while Package P is active. DPA-700 MUST NOT begin.

## Evidence-first DP1 sequencing

Completed:

- DPA-200 adjudication and review-ready promotion;
- DP1 read-only Discovery at `6a9da7d…`;
- DISC-001 through DISC-010 and DISC-003b;
- assumptions, main-repository context and Probe backlog synchronization;
- DPA-300 review, verification, adjudication, correction and review-ready promotion;
- DPA-300 restructure-equivalence verification and Maintainer ratification;
- DPA-400 normative contract, traceability, diagram, review, amendment, verification and promotion;
- DPA-500 normative contract, traceability, diagram, review, ADR-021 amendment, verification and promotion;
- merge of the DPA-500 slice through PR #3 at `1f3e5a64f4be5a974bf979f066d9434505a1d74c`;
- durable read-only Lab gates for the reviewed architecture slices;
- bounded initial DPA-600 draft, traceability and diagram in Draft PR #5.

Pending under `MASTERPLAN.md`:

1. current remote-main revalidation of historical findings;
2. shared Probe contract;
3. complete preparation of PROBE-001, PROBE-002 and DPA-400 renderer Probes;
4. complete CSC/namespace-profile checklist;
5. remote specification of Probe-independent portability slices;
6. local confirmation and exact Probe-ref freeze;
7. Probe execution and evidence adjudication;
8. bounded DPA-300 through DPA-500 revalidation and amendments where required;
9. independent verification of normative amendments to review-ready specifications;
10. evidence-bounded continuation of DPA-600 through DPA-900;
11. DP2 implementation through existing registry, lifecycle, Workspace, findings, gate and evidence authorities;
12. external-repository habitability validation;
13. sustainable-governance and review-economics closeout.

Early Discovery, fixture preparation and exploratory drafting do not constitute adoption, implementation, migration or Probe success.

## Probe and specification relationship

PROBE-001 tests the real registry parser and validator against the DPA-300/ADR-017 `ProjectionContract` and `PartitionContract` serialization proposal.

PROBE-002 tests lifecycle, immutable planning, Workspace, locks, Write, Verify, acceptance-state, recovery, conditional base persistence, gate-set re-acceptance and layered acceptance against an exact main-repository ref.

The DPA-400 renderer Probe package tests renderer mapping, interface compatibility, version behavior, deterministic execution, immutable inputs, output scope and prohibited capabilities.

DPA-400 and DPA-500 remain `review-ready`. Repository-dependent claims MUST remain `NEEDS_MAIN_REPO_VALIDATION`, and neither specification may become `stable` before relevant Probe evidence is available and adjudicated.

DPA-600 remains `draft`. Its concrete concurrency and workflow mappings require exact-ref validation and applicable Probe evidence before promotion can be considered.

## Merge discipline

Governed batches whose assurance depends on commit sequence MUST NOT be squash-merged. Their source commit SHAs, review refs and selected merge method MUST be recorded durably. The DPA-500 governed branch should be retained until its sequence is preserved outside the branch.