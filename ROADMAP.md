# Roadmap

Status: active

Status-date: 2026-07-15

## Specification sequence

1. DPA-000 — Vision and principles — stable
2. DPA-100 — Foundations and terminology — stable, consolidated
3. DPA-200 — Document model — review-ready
4. DPA-300 — Registry and lifecycle integration — draft after adjudication; independent verification pending
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
- normative and derived artifact consolidation.

Pending:

1. independent post-adjudication verification by a verifier that did not apply the changes;
2. DPA-300 `review-ready` promotion if verification passes;
3. preparation and execution of PROBE-001 and the DPA-300-owned subset of PROBE-002;
4. DPA-400 drafting from DPA-300 and Probe evidence;
5. DPA-500 drafting with accepted-state, recovery and drift findings.

Early Discovery does not constitute adoption, implementation or migration.

## DPA-300 adjudicated architecture

DPA-300 now defines:

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
- payload-only purity;
- declared sources/configuration;
- no partition bytes or nested renderer invocation.

### DPA-500

- findings and gates for all drift classes;
- acceptance-state absence/tamper;
- interrupted refresh and evidence failure;
- transition to `accepted` only after complete gates;
- no time-only hard failure.

### DPA-600

- base and cross-ref revalidation;
- competing-PR serialization;
- interaction with local plan/recovery state.

### DPA-700

- migration/no-migration outcome;
- preservation and rollback;
- no automatic historical-prose merge;
- recovery when re-verification is impossible.

### DPA-800

- DP1 stage exit criteria;
- exact-ref Probe recipes;
- DP2 implementation of acceptance state, partition contracts and recovery;
- CURRENT_HANDOFF writer inventory and command adaptation.

## Prohibitions

- No production code or main-repository mutation in the lab.
- No `.agentic/` initialization before adoption.
- No production-form selection from Discovery or Probe capability alone.
- No parallel registry, lifecycle, state, evidence, command or gate system.
- No Probe before DPA-300 review-ready.
- No review prose becomes normative without adjudication.
