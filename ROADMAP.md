# Roadmap

Status: active
Status-date: 2026-07-16

## Specification sequence

1. DPA-000 — Vision and principles — stable
2. DPA-100 — Foundations and terminology — stable, consolidated
3. DPA-200 — Document model — review-ready
4. DPA-300 — Registry and lifecycle integration — review-ready
5. DPA-400 — Renderer contract — draft
6. DPA-500 — Freshness and gates — planned
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
- DPA-300 primary review, verification, adjudication and correction;
- DPA-300 diff-scoped PASS re-check and `review-ready` promotion;
- DPA-300 branch closeout and fast-forward to `main` at `aaa60ef2…`;
- clean DPA-400 branch creation from updated `main`;
- first DPA-400 normative contract, traceability and boundary diagram.

Pending:

1. complete DPA-400 internal audit and review baseline;
2. review and adjudicate DPA-400 to no more than `review-ready` before applicable Probe evidence;
3. draft and review DPA-500 to no more than `review-ready` before applicable Probe evidence;
4. prepare PROBE-001 and the DPA-300-owned subset of PROBE-002 as bounded fixtures and expected-result contracts;
5. prepare renderer-map, determinism and purity fixtures for later DPA-400 Probe work;
6. execute Probes when a suitable main-repository environment is available;
7. revalidate DPA-300–500 against Probe evidence before any stability promotion;
8. continue DPA-600–900 only after Probe evidence has bounded the correction surface.

Early Discovery and fixture preparation do not constitute adoption, implementation or migration.

## Probe and specification relationship

PROBE-001 tests the real registry parser and validator against the DPA-300/ADR-017 `ProjectionContract` and `PartitionContract` serialization proposal.

DPA-400 does not gate PROBE-001. A PROBE-001 fixture needs only a syntactically plausible renderer identifier because DPA-300 already defines that field. Renderer resolution and runtime behavior remain DPA-400 concerns.

DPA-400 and DPA-500 may be fully drafted and reviewed during the no-Mac period. Repository-dependent claims MUST remain `NEEDS_MAIN_REPO_VALIDATION`, and neither specification may become `stable` before the relevant Probe evidence is available and adjudicated.

## DPA-400 active work

The renderer contract owns:

- closed static renderer resolution;
- declared canonical sources and contract-declared configuration;
- capability-bounded invocation context;
- text-or-immutable-bytes output;
- pure payload-only region output;
- exactly one registered target per invocation;
- no partition bytes, writes, locks, subprocesses, network access, workflow calls, state/evidence writes or nested renderer invocation;
- deterministic and reproducible output;
- renderer-version and fingerprint obligations;
- fail-loud input, output, resource and side-effect behavior.

Current artifacts:

- `specs/dpa/DPA-400-RENDERER-CONTRACT.md`;
- `traceability/DPA-400_TRACEABILITY.md`;
- `diagrams/dpa-400-renderer-boundary.mmd`.

Next DPA-400 milestones:

1. internal invariant, ADR, terminology, failure-mode and cross-artifact audit;
2. synchronization of any audit corrections;
3. immutable primary-review ref;
4. Claude primary architecture review;
5. secondary verification and Maintainer adjudication;
6. post-adjudication verification;
7. promotion to at most `review-ready` before renderer Probe evidence.

## Parallel main-repository maintenance stream

Verified kit deficiencies remain separated into work classes.

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

Exact-ref Discovery established an observed writer:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

DISC-003b established that the inspected `transfer chat-switch-complete` path does not write `CURRENT_HANDOFF.md` at the same ref.

If the candidate is later approved, every then-known writer must be routed through the lifecycle. Global writer-set completeness must be rebuilt at the Probe validation ref.

No production form is selected.

## Later-spec obligations

### DPA-500

- findings and gates for all drift classes;
- renderer identity, version, nondeterminism and side-effect findings;
- acceptance-state absence or tamper;
- interrupted refresh and evidence failure;
- transition to `accepted` only after complete gates;
- staged enforcement and no time-only hard failure.

### DPA-600

- base and cross-ref revalidation;
- competing-PR serialization;
- interaction with renderer-derived plans and local recovery state.

### DPA-700

- migration/no-migration outcome;
- preservation and rollback;
- rollback when renderer versions change or disappear;
- no automatic historical-prose merge.

### DPA-800

- DP1 stage exit criteria;
- exact-ref Probe recipes;
- DP2 implementation of registry, lifecycle, renderer, acceptance-state and partition contracts;
- CURRENT_HANDOFF writer inventory and command adaptation;
- possible later risk-based independent-verification rule for evidence-bearing DP2–DP5 workflows.

### DPA-900

- future independent-context verification as governed gate policy;
- scope and cost controls;
- no current normative expansion from this future-scope note.

## Prohibitions

- No production code or main-repository mutation in the lab.
- No `.agentic/` initialization before adoption.
- No production-form selection from Discovery or Probe capability alone.
- No parallel registry, lifecycle, state, evidence, command, renderer or gate system.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No new active specification slice solely for independent-context verification during DPA-400 work.
- No review prose becomes normative without adjudication.
