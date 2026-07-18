# Status

Status: active

Status-date: 2026-07-18

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is review-complete through DPA-500 and merged through PR #3 at merge commit `1f3e5a64f4be5a974bf979f066d9434505a1d74c`.

Phase C — Operational completion has begun on branch `spec/dpa-600-concurrency` with DPA-600 at `draft`. This branch remains a remote architecture-preparation branch and does not establish main-repository implementation or Probe evidence.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence.

`MASTERPLAN.md` is the canonical execution plan for the remaining revalidation, Probe, bounded-amendment, DP2 and external-habitability work. `MASTERPLAN_REMOTE_PREPARATION.md` governs Package A preparation.

## DP1 Discovery

DP1 Discovery is complete for the explicitly inspected scope at:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed. Global writer-set completeness is not claimed and must be rebuilt at the Probe validation ref.

No main-repository mutation occurred and no production form was selected.

Every observation from `6a9da7d…` is historical exact-ref evidence and MUST be revalidated against current `origin/main` before mutation.

## DPA-300 lineage and bounded amendment

DPA-300 completed primary review, secondary verification, Maintainer adjudication, independent post-adjudication verification and bounded synchronization re-check.

The later review-ready restructure was independently compared against the certified text and received `PASS_WITH_EXPLICIT_RATIFICATION`. The Maintainer ratification restored the dropped target identity, generic required-field rejection, partition encoding declaration, policy identifiers and normative MUST force; it accepted the enumerated strengthenings and restored Probe and conformance pointers.

DPA-300 remains `review-ready`. ADR-021 adds a bounded synchronized amendment for conditional accepted-base persistence and layered post-acceptance comparison of registered-region projections. That amendment was included in the DPA-500 independent post-adjudication verification and passed without blocking findings. DPA-300 stability remains blocked on applicable DP1 Probe evidence and later governed revalidation.

## DPA-400 closeout

DPA-400 completed primary review, adjudication, governed amendment, independent post-adjudication verification and status-only promotion.

Independent verification at exact ref `6050d0664d9c1ac8bd1a2eb9d6409593046ede9c` returned `PASS` with zero blocking findings. DPA-400 is `review-ready` and was merged through PR #2 at merge commit `7de43fff8debe5c0b9b0c8276a21723d5bc12da6`.

Repository-specific renderer mappings and enforcement mechanisms remain `NEEDS_MAIN_REPO_VALIDATION`; no production implementation, Probe success or main-repository conformance is claimed.

## DPA-500 closeout

The immutable primary-review baseline was:

`60d6457f0473365789ece4f885a48ea5320b01ff`

The primary architecture review returned `ACCEPT_WITH_CHANGES` with three majors, four minors and three editorial findings. All findings were accepted and adjudicated through ADR-021.

The immutable post-adjudication verification ref was:

`bb3db42e49db0ce9a38e0a019962cdd61f51785c`

Independent verification returned `PASS_WITH_NON_BLOCKING_FINDINGS` with zero blocking findings, zero majors, zero minors and two editorial findings. It confirmed complete closure of all adjudicated findings, DPA-300/DPA-500 synchronization, derived traceability anchors, diagram consistency, authority boundaries and the absence of parallel systems.

DPA-500 is `review-ready`. This status does not establish production implementation, Probe success, adoption or main-repository conformance.

The two remaining editorials V5-e01 and V5-e02 are parked in `MASTERPLAN.md` for the next otherwise-required bounded amendment.

## DPA-600 active draft

The first bounded DPA-600 slice defines:

- renderer, lifecycle, workflow and repository-integration concurrency domains;
- local Workspace-lock ownership and same-process reentrancy limits;
- independent base, source, target, contract, renderer, partition, ownership, gate-set and acceptance-state guards;
- branch and pull-request revalidation and serialization semantics;
- stale-plan rejection and regeneration from an exact current ref;
- acceptance-state and interrupted-recovery interaction;
- fail-loud, evidence and rollback obligations.

The draft introduces no new runtime authority and selects no concrete main-repository workflow or locking implementation. All concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-600 is not `review-ready`. Package A review preparation requires completion of DPA-600, an internal DPA-000 through DPA-500 audit, DPA-700, synchronized Package A artifacts and an immutable review ref.

## Probe relationship

PROBE-001 remains governed by DPA-300 and ADR-017. It does not depend on DPA-400 or DPA-500 runtime completion.

DPA-400 requires exact-ref evidence for static renderer mapping, capability restriction, determinism, renderer versioning and lifecycle integration before `stable`.

DPA-500 requires exact-ref evidence for findings, severities, conditional base persistence, re-acceptance, ownership provenance, layered freshness, gate integration, recovery and staged strict adoption before `stable`.

DPA-600 concrete lock, guard and workflow mappings require exact-ref validation and later Probe evidence. The architecture draft does not establish current implementation capability.

Probe fixtures may be prepared during the no-Mac period but must not be represented as executed.

## Active work order

Follow `MASTERPLAN.md` and `MASTERPLAN_REMOTE_PREPARATION.md`:

1. complete the bounded DPA-600 concurrency and guard-ownership draft;
2. synchronize DPA-600 traceability, diagram and project-control surfaces;
3. run the read-only Lab gates and internal DPA-000 through DPA-500 consistency audit;
4. resolve any architecture contradiction or missing Maintainer decision;
5. begin DPA-700 only after DPA-600 is coherent;
6. prepare closed Package A artifacts and an exact immutable review ref;
7. request bounded independent verification without asking the reviewer to redesign the architecture;
8. preserve the separate exact-ref main-repository revalidation and Probe work order under `MASTERPLAN.md`.

## Restrictions

- No production code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without adjudication.
- No quick fix to handoff writers, lifecycle Apply, acceptance state, re-acceptance, layered acceptance or projection gates before PROBE-002 and subsequent architecture revalidation.
- A promotion commit changes status surfaces only and MUST NOT change normative text.
- DPA-600 MUST NOT treat a local lock, acceptance state or evidence as cross-ref serialization authority.

Phase B through DPA-500 remains review-complete. Phase C remote architecture preparation is active through the bounded DPA-600 draft; exact-ref main-repository revalidation and Probe execution remain separate governed work.