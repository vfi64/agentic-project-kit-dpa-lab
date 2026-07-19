# Roadmap

Status: active

Status-date: 2026-07-19

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

The active sequence remains Probe-first, but remote preparation is now complete:

1. Package P shared Probe contract, three Probe packages, freeze/evidence/adjudication procedures, CSC checklist and portability planning — complete and finally closed;
2. fresh current-main remote read and exact-ref remote surface inventory — complete for the 2026-07-19 observation;
3. local ref/environment/isolation baseline — next;
4. complete local reader/writer/lifecycle/lock/renderer/state/gate/recovery/evidence inventories — next;
5. semantic-to-concrete fixture reconciliation and bounded materialization — after inventory gates;
6. exact Probe-ref and fixture freeze — after materialization exits;
7. PROBE-001, PROBE-002 and renderer Probe execution — only after freeze;
8. evidence capture and Maintainer adjudication;
9. DPA-300 through DPA-500 revalidation and bounded amendments where required;
10. evidence-bounded continuation of DPA-600;
11. DPA-700 through DPA-900, controlled import and implementation after upstream release decisions.

DPA-600 through DPA-900 MUST NOT displace the active reality-contact sequence. DPA-600 remains frozen and DPA-700 remains unstarted.

## Current package

**Package P — Remote Probe Preparation** is finally closed.

The active work package is now:

**Package M — Local Fixture Materialization Planning and Exact-Ref Reality Contact**

Governing artifacts:

- `evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`;
- `integration/MAIN_REPO_REMOTE_SURFACE_INVENTORY_20260719.md`;
- `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`;
- existing Package-P Probe contracts and procedures.

Package M is planning and inventory first. It authorizes no Probe execution and no main-repository implementation change.

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
- bounded initial DPA-600 draft, traceability and diagram in Draft PR #5;
- complete Package-P preparation, independent review, correction, limited rereview and final closure;
- fresh 2026-07-19 remote read of main-repository `main` at `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`;
- bounded exact-ref remote surface inventory;
- governed local fixture-materialization plan.

Pending under `MASTERPLAN.md`:

1. local equality, cleanliness, environment and isolation baseline;
2. complete local exact-ref surface inventories;
3. concrete fixture materialization with immutable revisions and hashes;
4. exact Probe-ref freeze;
5. Probe execution and evidence adjudication;
6. bounded DPA-300 through DPA-500 revalidation and amendments where required;
7. independent verification of normative amendments to review-ready specifications;
8. evidence-bounded continuation of DPA-600 through DPA-900;
9. DP2 implementation through existing registry, lifecycle, Workspace, findings, gate and evidence authorities;
10. external-repository habitability validation;
11. sustainable-governance and review-economics closeout.

Remote inspection currently confirms concrete Workspace, registry, lifecycle-reporting, lock, evidence and CLI surfaces. It does not yet confirm a complete DPA renderer, acceptance state, re-acceptance, recovery or staged-enforcement implementation. Missing surfaces must be recorded as absent or blocked, not invented.

Early Discovery, remote source inspection, fixture preparation and exploratory drafting do not constitute adoption, implementation, migration or Probe success.

## Probe and specification relationship

PROBE-001 tests the real registry parser and validator against the DPA-300/ADR-017 `ProjectionContract` and `PartitionContract` serialization proposal.

PROBE-002 tests lifecycle, immutable planning, Workspace, locks, Write, Verify, acceptance-state, recovery, conditional base persistence, gate-set re-acceptance and layered acceptance against an exact main-repository ref.

The DPA-400 renderer Probe package tests renderer mapping, interface compatibility, version behavior, deterministic execution, immutable inputs, output scope and prohibited capabilities.

DPA-400 and DPA-500 remain `review-ready`. Repository-dependent claims MUST remain `NEEDS_MAIN_REPO_VALIDATION`, and neither specification may become `stable` before relevant Probe evidence is available and adjudicated.

DPA-600 remains `draft`. Its concrete concurrency and workflow mappings require exact-ref validation and applicable Probe evidence before promotion can be considered.

## Merge discipline

Governed batches whose assurance depends on commit sequence MUST NOT be squash-merged. Their source commit SHAs, review refs and selected merge method MUST be recorded durably. The DPA-500 governed branch should be retained until its sequence is preserved outside the branch.
