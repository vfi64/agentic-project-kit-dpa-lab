# DP1 Probe Backlog

Status: active

Status-date: 2026-07-15

Authority: DPA-ADR-015, DPA-ADR-016, DPA-ADR-017

## 1. Purpose

This backlog records compatibility, sufficiency and conformance questions that Discovery cannot answer. Each Probe requires a reviewable governing contract, exact validation ref, explicit expected result and bounded reproducible evidence.

Discovery evidence is non-normative. Probe evidence may confirm or falsify an implementation mapping but MUST NOT silently create architecture.

## 2. Entry conditions

A Probe item may execute only when:

- its governing specification is `review-ready` or later;
- the exact main-repository validation ref is recorded;
- proposed serialized contracts and expected results are explicit;
- the Probe is bounded and reproducible;
- mutation is absent or separately authorized by the implementation phase;
- output is committed as evidence.

## 3. Active Probe items

### PROBE-001 — Registry projection and partition compatibility

Evidence source: `evidence/repo-facts/DP1-DISC-001-REGISTRY-6A9DA7D.md`

Governing contract: reviewable DPA-300.

Question: Can the real registry parser and validator represent an optional `ProjectionContract` and one parent-entry `PartitionContract` without breaking manual entries or weakening validation?

Required evidence:

- exact parser and validator invocation;
- existing-entry regression;
- optional extension behavior;
- unknown-field, unknown-version and unknown-fingerprint negatives;
- parent partition ordering and ownership representation;
- missing/dangling/inconsistent region reference negatives;
- exact-ref record.

### PROBE-002 — Governed CURRENT_HANDOFF replacement, lifecycle state and recovery

Evidence sources:

- DISC-002 reader graph;
- DISC-003 writer graph;
- DISC-003 correction and DISC-003b resolution;
- DISC-004 authority inputs;
- DISC-006 lifecycle mutation;
- DISC-007 Workspace;
- DISC-008 locking/concurrency;
- DISC-010 history/rollback.

Mandatory observed writer coverage:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

DISC-003b establishes that the inspected `chat-switch-complete` path does not write `CURRENT_HANDOFF.md` at the recorded ref. The Probe MUST rebuild the writer inventory at its own validation ref and include every then-known writer.

Governing contracts: DPA-300 through DPA-700 for their respective scopes.

The Probe MUST demonstrate, for the DPA-300-owned subset:

1. declared canonical state is updated before rendering;
2. renderer returns payload bytes only and performs no write;
3. parent partition contract resolves exactly one ordered marker model;
4. malformed, missing, duplicated or reordered boundaries fail loud without mutation;
5. payload, preserved-region, partition and expected complete-target fingerprints are captured;
6. outside-region bytes remain byte-identical;
7. generated content is replaced rather than appended;
8. Write is exact-plan-bound, locally locked and atomic;
9. nested projection mutation is refused;
10. source, target, base, contract, renderer, partition and ownership drift are classified independently;
11. Workspace resolves the acceptance-state path under `.agentic/` lifecycle state;
12. evidence is not used as the acceptance-state source;
13. out-of-band target writes are detected from accepted fingerprints;
14. stale-lock takeover identifies and abandons an interrupted instance;
15. crashed-after-Write bytes are re-verified only when the exact recovered plan and every guard remain valid, otherwise regenerated;
16. post-write verification and bounded evidence are emitted;
17. command behavior is adapted without a parallel DPA-only writer.

Later DPA-500 through DPA-700 add acceptance gates, cross-ref serialization and rollback requirements.

The Probe MUST NOT preselect a document form. Form eligibility is Assessment work.

### PROBE-003 — Lifecycle finding compatibility

Evidence: DISC-005 and DISC-006.

Governing contracts: reviewable DPA-300 and DPA-500.

Question: Can existing finding structures represent registry, partition, drift, acceptance-state, interrupted-refresh, stale-plan and direct-write failures without a parallel finding system?

### PROBE-004 — Gate and CI compatibility

Evidence: DISC-009.

Governing contract: reviewable DPA-500.

Question: Can existing gate and CI mechanisms carry staged DPA enforcement while preserving the rule that time alone cannot hard-fail?

### PROBE-005 — Concurrency and serialization compatibility

Evidence: DISC-008.

Governing contracts: reviewable DPA-300 and DPA-600.

Question: Can existing local locking and branch/PR workflows implement the no-nested-projection rule, plan guards and cross-ref serialization without conflating local lock and workflow authority?

### PROBE-006 — Rollback-input sufficiency

Evidence: DISC-010.

Governing contract: reviewable DPA-700.

Question: Are Git and repository inputs sufficient for rollback without a new canonical history source or automatic historical-prose merge?

## 4. Review boundary

The Discovery set is complete for the recorded scope after DISC-003b. Global writer-set completeness is not claimed and must be revalidated at Probe time.

DPA-300 Probe execution remains blocked until independent post-adjudication verification passes and DPA-300 becomes `review-ready`.
