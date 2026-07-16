# Roadmap

Status: active

Status-date: 2026-07-16

## Specification sequence

1. DPA-000 — Vision and principles — stable
2. DPA-100 — Foundations and terminology — stable, consolidated
3. DPA-200 — Document model — review-ready
4. DPA-300 — Registry and lifecycle integration — review-ready
5. DPA-400 — Renderer contract — planned
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
- evidence-based DPA-300 draft;
- primary architecture review and secondary technical verification;
- maintainer adjudication through ADR-016 and ADR-017;
- independent post-adjudication verification, bounded synchronization fix and diff-scoped PASS re-check;
- DPA-300 `review-ready` promotion.

Pending:

1. complete the DPA-300 branch closeout and update `main`;
2. draft and review DPA-400 to no more than `review-ready` before applicable Probe evidence;
3. draft and review DPA-500 to no more than `review-ready` before applicable Probe evidence;
4. prepare PROBE-001 and the DPA-300-owned subset of PROBE-002 as bounded fixtures and expected-result contracts;
5. execute PROBE-001/002 when a suitable main-repository environment is available;
6. revalidate DPA-300–500 against Probe evidence before any stability promotion;
7. continue DPA-600–900 only after the Probe evidence has bounded the correction surface.

Early Discovery and fixture preparation do not constitute adoption, implementation or migration.

## Probe and specification relationship

PROBE-001 tests the real registry parser and validator against the DPA-300/ADR-017 `ProjectionContract` and `PartitionContract` serialization proposal.

DPA-400 does not gate PROBE-001. A PROBE-001 fixture needs only a syntactically plausible renderer identifier because DPA-300 already defines that field. Renderer resolution and runtime behavior remain DPA-400 concerns.

DPA-400 and DPA-500 may be fully drafted and reviewed during the no-Mac period. Repository-dependent claims MUST remain `NEEDS_MAIN_REPO_VALIDATION`, and neither specification may become `stable` before the relevant Probe evidence is available and adjudicated.

## Parallel main-repository maintenance stream

Verified kit deficiencies fall into separate work classes:

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

## DPA-300 adjudicated architecture

DPA-300 defines:

- optional projection contracts in the existing registry;
- one parent-entry partition contract for multi-region documents;
- fail-loud static validation;
- Recover → Resolve → Inspect → Validate → Render → Plan → Preflight → Lock → Revalidate → Write → Verify → Record → Release;
- dry-run and exact-plan-bound execution;
- distinct payload, preserved-region, partition and complete-target fingerprints;
- no nested projection mutation;
- lifecycle-owned atomic complete-file Write;
- immediate `written-unverified` after Write;
- Workspace-resolved acceptance-state lifecycle state;
- independent multi-class drift detection;
- interrupted-refresh and stale-lock recovery;
- bounded non-authoritative evidence;
- adaptation of every existing candidate writer rather than a parallel command.

Accepted decisions:

- ADR-016 — acceptance state and interrupted recovery;
- ADR-017 — parent-entry partition contract.

## CURRENT_HANDOFF command obligation

Exact-ref Discovery established an observed writer:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

DISC-003b established that the inspected `transfer chat-switch-complete` path does not write `CURRENT_HANDOFF.md` at the same ref.

If the candidate is later approved, every then-known writer must be routed through the lifecycle. Global writer-set completeness must be rebuilt at the Probe validation ref.

No production form is selected.

## Later-spec obligations

### DPA-400

- static renderer resolution;
- declared canonical sources and contract-declared configuration;
- pure payload-only output;
- exactly one registered target per invocation;
- no partition bytes, writes, locks, workflow calls, evidence authority or nested renderer invocation;
- deterministic and reproducible output contracts;
- fail-loud behavior for unknown identifiers and undeclared inputs.

### DPA-500

- findings and gates for all drift classes;
- acceptance-state absence or tamper;
- interrupted refresh and evidence failure;
- transition to `accepted` only after complete gates;
- staged enforcement and no time-only hard failure.

### DPA-600

- base and cross-ref revalidation;
- competing-PR serialization;
- interaction with local plan and recovery state.

### DPA-700

- migration/no-migration outcome;
- preservation and rollback;
- no automatic historical-prose merge;
- recovery when re-verification is impossible.

### DPA-800

- DP1 stage exit criteria;
- exact-ref Probe recipes;
- DP2 implementation of acceptance state, partition contracts and recovery;
- CURRENT_HANDOFF writer inventory and command adaptation;
- possible later risk-based independent-verification rule for evidence-bearing DP2–DP5 workflows.

### DPA-900

- future independent-context verification as governed gate policy;
- scope, cost controls and relationship to deterministic tests, Maintainer adjudication and real-repository Probes;
- no current normative expansion from this future-scope note.

## Prohibitions

- No production code or main-repository mutation in the lab.
- No `.agentic/` initialization before adoption.
- No production-form selection from Discovery or Probe capability alone.
- No parallel registry, lifecycle, state, evidence, command or gate system.
- No Probe before its governing specification is reviewable.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No new active specification slice solely for independent-context verification during DPA-400 work.
- No review prose becomes normative without adjudication.