# Roadmap

Status: active

Status-date: 2026-07-17

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
11. Reversible lab adoption with `agentic-project-kit`
12. Controlled import into `vfi64/agentic-project-kit`

The normative specification order is unchanged.

## Evidence-first DP1 sequencing

DP1 remains one slice with internal stages Discovery → Probe → Assessment.

Completed:

- DPA-200 adjudication and review-ready promotion;
- DP1 read-only Discovery at `6a9da7d…`;
- DISC-001 through DISC-010 and DISC-003b;
- assumptions, main-repository context and Probe backlog synchronization;
- DPA-300 review, verification, adjudication, correction and review-ready promotion;
- DPA-300 independent restructure-equivalence verification and explicit Maintainer ratification;
- DPA-400 normative contract, traceability, diagram and internal audit;
- DPA-400 primary review;
- ADR-019/ADR-020 decisions and governed amendment batch;
- durable read-only Lab gates and deterministic validator;
- independent DPA-400 post-adjudication verification at `6050d066…` with `PASS`;
- status-only DPA-400 promotion to `review-ready`;
- DPA-500 normative contract, traceability, diagram and pre-review audit;
- DPA-500 primary review at `60d6457…` with `ACCEPT_WITH_CHANGES`;
- ADR-021 and governed DPA-300/DPA-500 amendment batch;
- independent DPA-500 post-adjudication verification at `bb3db42…` with `PASS_WITH_NON_BLOCKING_FINDINGS`;
- status-only DPA-500 promotion to `review-ready`.

Pending:

1. merge PR #3 and close the DPA-500 branch;
2. preparation and execution of PROBE-001 and the DPA-300-owned subset of PROBE-002 against an exact main-repository validation ref;
3. preparation and execution of renderer-map, determinism, immutable-input and purity Probe work for DPA-400;
4. revalidation of DPA-300–500 against Probe evidence before any stability promotion;
5. continuation of DPA-600–900 under the documented phase sequence;
6. completion of the DPA-900 sustainable-governance and review-economics contract before final DPA closeout.

Early Discovery and fixture preparation do not constitute adoption, implementation or migration.

## Probe and specification relationship

PROBE-001 tests the real registry parser and validator against the DPA-300/ADR-017 `ProjectionContract` and `PartitionContract` serialization proposal.

DPA-400 does not gate PROBE-001. A PROBE-001 fixture needs only a syntactically plausible renderer identifier because DPA-300 already defines that field. Renderer resolution and runtime behavior remain DPA-400 concerns.

DPA-400 and DPA-500 are `review-ready`. Repository-dependent claims MUST remain `NEEDS_MAIN_REPO_VALIDATION`, and neither specification may become `stable` before relevant Probe evidence is available and adjudicated.

## DPA-400 adjudicated contract

The renderer contract owns:

- closed static renderer resolution;
- lifecycle-resolved immutable canonical-source values or content-addressed snapshots;
- immutable contract-declared configuration;
- renderer identifier, interface version, semantic version and implementation evidence as distinct concepts;
- text-or-immutable-bytes output;
- payload-only region output;
- exactly one registered target per invocation;
- no partition bytes, writes, locks, subprocesses, network access, workflow calls, state/evidence writes or nested renderer invocation;
- deterministic and reproducible output;
- deterministic semantic bounds separated from non-semantic operational aborts;
- bounded failure diagnostics translated by the lifecycle;
- mandatory closed invocation boundary and prohibited-capability negative tests;
- fail-loud input, output, resource and side-effect behavior.

DPA-400 completed:

1. immutable amendment ref;
2. independent post-adjudication verification;
3. zero-blocker PASS adjudication closeout;
4. status-only promotion to `review-ready`.

Its next milestone is exact-ref Probe evidence before any possible `stable` promotion.

## DPA-500 adjudicated contract

The freshness and gates contract owns:

- multidimensional derivational freshness;
- closed separation of freshness classification, trust state, drift, finding, gate decision and enforcement stage;
- operation-scoped base context with conditional accepted-base persistence;
- lifecycle-owned mutation-free gate-set re-acceptance;
- layered acceptance for registered-region projections;
- ownership-aware distinction between authorized region evolution and out-of-band lifecycle-byte mutation;
- fail-closed findings and gates;
- identity-critical evidence requirements;
- recovery and staged enforcement semantics.

DPA-500 completed:

1. immutable primary-review ref;
2. primary architecture review;
3. Maintainer adjudication and ADR-021;
4. governed DPA-300/DPA-500 amendment batch;
5. immutable post-adjudication verification ref;
6. independent zero-blocker verification;
7. status-only promotion to `review-ready`.

Its next milestone is exact-ref Probe evidence before any possible `stable` promotion.

## Parallel main-repository maintenance stream

### Architecture/DPA stream

- governed content writer;
- lifecycle-owned bounded replacement for candidate projections;
- semantic freshness and projection gates;
- `CURRENT_HANDOFF.md` writer adaptation through DP2.

These MUST follow DPA and Probe contracts. The handoff writer MUST NOT be patched as an isolated portability quick fix.

### Portability maintenance stream

- hard-coded registry paths that bypass Workspace;
- boot-source and profile assumptions requiring namespace-profile review;
- additional direct path literals in protected planning, GUI readiness and removed-source audit paths.

These are ordinary maintenance slices and may run in parallel with Probe work during the Mac/Codex phase, provided they do not pre-empt DPA architecture.

### Adoption and project-maturity stream

- namespace-profile habitability;
- first external-repository adoption evidence;
- bus-factor and repeatability concerns;
- later CSC validation.

## CURRENT_HANDOFF command obligation

Exact-ref Discovery established one observed writer:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

DISC-003b established that the inspected `transfer chat-switch-complete` path does not write `CURRENT_HANDOFF.md` at the same ref.

If the candidate is later approved, every then-known writer must be routed through the lifecycle. Global writer-set completeness must be rebuilt at the Probe validation ref.

No production form is selected.

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

This is a mandatory future planning item and a DPA closeout criterion. It creates no current DPA-400 or DPA-500 scope.

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
- possible later risk-based independent-verification rule for evidence-bearing DP2–DP5 workflows.

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
- No new active specification slice solely for independent-context verification during DPA-400 work.
- No review prose becomes normative without adjudication.
- Promotion commits change status surfaces only and MUST NOT alter normative text.
