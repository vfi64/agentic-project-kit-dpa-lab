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
7. DPA-600 — Concurrency and workflow serialization — planned
8. DPA-700 — Migration and rollback — planned
9. DPA-800 — DP1–DP5 implementation specification — planned
10. DPA-900 — Future evolution — planned
11. reversible lab adoption with `agentic-project-kit`
12. controlled import into `vfi64/agentic-project-kit`

The normative specification order is unchanged.

`MASTERPLAN.md` owns the detailed execution sequence, parallel work streams, mutation freezes, Probe preparation, amendment verification and external-habitability path.

## Evidence-first DP1 sequencing

DP1 remains one slice with internal stages Discovery → Probe → Assessment.

Completed:

- DPA-200 adjudication and review-ready promotion;
- DP1 read-only Discovery at `6a9da7d…`;
- DISC-001 through DISC-010 and DISC-003b;
- assumptions, main-repository context and Probe backlog synchronization;
- DPA-300 review, verification, adjudication, correction and review-ready promotion;
- DPA-300 independent restructure-equivalence verification and explicit Maintainer ratification;
- DPA-400 normative contract, traceability, diagram, primary review, amendment, verification and promotion;
- DPA-500 normative contract, traceability, diagram, primary review, ADR-021 amendment, verification and promotion;
- merge of the DPA-500 slice through PR #3 at `1f3e5a64f4be5a974bf979f066d9434505a1d74c`;
- durable read-only Lab gates for the reviewed architecture slices.

Pending under `MASTERPLAN.md`:

1. current remote-main revalidation of historical findings;
2. complete preparation of PROBE-001, PROBE-002 and DPA-400 renderer Probes;
3. complete CSC/namespace-profile checklist;
4. remote specification of Probe-independent portability slices;
5. local confirmation and exact Probe-ref freeze;
6. Probe execution and evidence adjudication;
7. bounded DPA-300 through DPA-500 revalidation and amendments where required;
8. independent verification of normative amendments to review-ready specifications;
9. DP2 implementation through existing registry, lifecycle, Workspace, findings, gate and evidence authorities;
10. external-repository habitability validation;
11. continuation of DPA-600 through DPA-900 with the Probe evidence constraining the correction surface;
12. completion of the DPA-900 sustainable-governance and review-economics contract before final DPA closeout.

Early Discovery and fixture preparation do not constitute adoption, implementation or migration.

## Probe and specification relationship

PROBE-001 tests the real registry parser and validator against the DPA-300/ADR-017 `ProjectionContract` and `PartitionContract` serialization proposal.

DPA-400 does not gate PROBE-001. A PROBE-001 fixture needs only a syntactically plausible renderer identifier because DPA-300 already defines that field. Renderer resolution and runtime behavior remain DPA-400 concerns.

PROBE-002 tests lifecycle, immutable planning, Workspace, locks, Write, Verify, acceptance-state, recovery, conditional base persistence, gate-set re-acceptance and layered acceptance against an exact main-repository ref.

DPA-400 and DPA-500 are `review-ready`. Repository-dependent claims MUST remain `NEEDS_MAIN_REPO_VALIDATION`, and neither specification may become `stable` before relevant Probe evidence is available and adjudicated.

## Parallel main-repository streams

### Architecture and Probe stream

- exact-ref main-repository revalidation;
- PROBE-001 and PROBE-002;
- DPA-400 renderer Probes;
- evidence classification and adjudication;
- bounded DPA revalidation and amendments;
- independent verification of normative amendments.

### Portability maintenance stream

- hard-coded registry paths that bypass Workspace;
- boot-source and profile assumptions requiring namespace-profile review;
- direct path literals in protected planning, GUI readiness and removed-source audit paths;
- internal helpers that reconstruct Workspace-owned paths directly.

These slices may be specified remotely after revalidation and implemented in parallel during the Mac/Codex phase only when they do not alter Probe subjects, registry schema, lifecycle semantics, writer semantics, acceptance state or gate authority.

### DPA-critical implementation stream

- governed content writer;
- lifecycle-owned bounded replacement for candidate projections;
- acceptance state and recovery;
- conditional base persistence;
- gate-set re-acceptance;
- layered acceptance and owner provenance;
- semantic freshness and projection gates;
- `CURRENT_HANDOFF.md` writer adaptation through DP2.

This stream remains frozen until PROBE-002 and subsequent architecture revalidation. The handoff writer MUST NOT be patched as an isolated portability quick fix.

### Adoption and project-maturity stream

- namespace-profile habitability;
- first external-repository adoption evidence;
- bus-factor and repeatability concerns;
- CSC validation.

## CURRENT_HANDOFF command obligation

Exact-ref Discovery established one observed writer:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

DISC-003b established that the inspected `transfer chat-switch-complete` path does not write `CURRENT_HANDOFF.md` at the same ref.

Global writer-set completeness MUST be rebuilt read-only at the Probe validation ref. If the candidate is later approved, every then-known writer must be routed through the lifecycle.

No production form is selected.

## Amendment governance

Every normative bounded amendment to a `review-ready` DPA-300, DPA-400 or DPA-500 contract follows the established exact-ref, Maintainer-adjudication and independent post-adjudication verification path unless the change is proven to be non-normative metadata or purely editorial without contract effect.

The two DPA-500 verification editorials remain parked for the next suitable bounded amendment:

- V5-e01 — clarify re-acceptance as an acceptance-record update for already-accepted unchanged bytes;
- V5-e02 — show or annotate re-acceptance eligibility before gate evaluation in the diagram.

## Required future objective — sustainable governance and review economics

The DPA closeout MUST include a DPA-900 contract showing how future architecture and governance changes become cheaper to validate without weakening correctness, evidence discipline, authority clarity, rollback safety or Maintainer control.

DPA-900 must define:

- risk-based review depth;
- high-risk triggers requiring the full review path;
- diff-scoped equivalence verification for semantic-preserving refactors;
- bounded fast paths for low-risk editorial or deterministic generated changes;
- selective independent-context verification for evidence-bearing high-risk changes;
- machine-checkable consistency checks;
- explicit cost controls and fallback to full review when equivalence cannot be proven;
- measurable success criteria for reduced review cost and reduced synchronization defects.

## Later-spec obligations

### DPA-600

- base and cross-ref revalidation;
- competing-PR serialization;
- interaction with renderer-derived plans and local recovery state.

### DPA-700

- migration/no-migration outcome;
- preservation and rollback;
- rollback when renderer semantic versions change or disappear;
- no automatic historical-prose merge.

### DPA-800

- DP1 stage exit criteria;
- exact-ref Probe recipes;
- DP2 implementation of registry, lifecycle, renderer, acceptance-state and partition contracts;
- CURRENT_HANDOFF writer inventory and command adaptation;
- evidence-qualified DP2–DP5 implementation sequence.

### DPA-900

- future independent-context verification as governed gate policy;
- sustainable governance and review economics;
- risk classification and cost controls;
- mechanically checked consistency and equivalence paths;
- measurable reduction of future review cost without reduced assurance.

## Prohibitions

- No production code or main-repository mutation in the lab.
- No `.agentic/` initialization before adoption.
- No production-form selection from Discovery or Probe capability alone.
- No parallel registry, lifecycle, state, evidence, command, renderer or gate system.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No quick fix to the frozen DPA-critical paths before PROBE-002 adjudication.
- No review prose becomes normative without adjudication.
- Promotion commits change status surfaces only and MUST NOT alter normative text.