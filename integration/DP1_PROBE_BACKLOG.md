# DP1 Probe Backlog

Status: active

Status-date: 2026-07-15

Authority: DPA-ADR-015

## 1. Purpose

This backlog records compatibility, sufficiency and conformance questions that Discovery is not permitted to answer. Each item requires a reviewable normative contract and an exact main-repository validation ref before execution.

Discovery evidence remains non-normative. A Probe result may confirm or falsify compatibility with a proposed contract but MUST NOT silently create architecture.

## 2. Entry conditions

A Probe item may execute only when:

- its governing DPA specification is reviewable;
- the exact main-repository validation ref is recorded;
- the proposed contract and expected result are explicit;
- the probe is bounded and reproducible;
- mutation is absent or separately authorized by the later implementation phase;
- output is recorded as evidence rather than chat-only judgment.

## 3. Active Probe items

### PROBE-001 — Registry projection-schema compatibility

Evidence source: `evidence/repo-facts/DP1-DISC-001-REGISTRY-6A9DA7D.md`

Governing contract required: reviewable DPA-300 registry schema.

Question: Does the real registry parser and validator accept the proposed optional projection contract without weakening existing validation or breaking existing entries?

Required evidence:

- exact parser and validator invocation;
- existing-entry regression result;
- unknown-field and malformed-contract negative results;
- exact-ref output record.

### PROBE-002 — CURRENT_HANDOFF governed bounded replacement

Evidence source: `evidence/repo-facts/DP1-DISC-003-WRITER-GRAPH-6A9DA7D.md`

Observed command path:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

Governing contracts required:

- DPA-300 lifecycle and registry integration;
- DPA-400 renderer purity and payload contract;
- DPA-500 marker, drift and acceptance findings;
- DPA-600 stale-plan and competing-PR guards;
- DPA-700 preservation and rollback rules.

Question: Can the proposed DPA contract replace the observed append-based `CURRENT_HANDOFF.md` mutation with lifecycle-owned bounded replacement of the marked operational handoff region?

The Probe MUST demonstrate:

1. the command updates declared source state before rendering;
2. the renderer returns only the target-region payload or contract-defined bytes and performs no write;
3. the lifecycle validates exactly one ordered marker pair before mutation;
4. missing, duplicated or misordered markers fail loud without changing the target;
5. bytes outside the governed region remain byte-identical;
6. the generated region is replaced rather than appended;
7. the write is planned, locked and atomic;
8. stale source, target, base or contract state invalidates the plan;
9. post-write validation and evidence are emitted;
10. direct target writes outside the lifecycle are detectable;
11. competing administrative refreshes cannot silently overwrite one another;
12. rollback restores the prior target from recoverable repository history without merging historical prose.

The Probe MUST NOT preselect `CURRENT_HANDOFF.md` as full, hybrid or managed-head. Form eligibility is an Assessment decision after the Probe evidence exists.

### PROBE-003 — Lifecycle finding compatibility

Evidence source: future DISC-005 record.

Governing contracts required: reviewable DPA-300 and DPA-500.

Question: Can the existing finding structures represent the required DPA drift, marker, ownership, stale-plan and acceptance failures without creating a parallel finding system?

### PROBE-004 — Gate and CI compatibility

Evidence source: future DISC-009 record.

Governing contract required: reviewable DPA-500.

Question: Can existing gate and CI mechanisms carry staged DPA enforcement while preserving the rule that time alone cannot cause a hard failure?

### PROBE-005 — Concurrency and serialization compatibility

Evidence source: future DISC-008 record.

Governing contract required: reviewable DPA-600.

Question: Can existing local locks and branch/PR workflows enforce the proposed local and cross-ref serialization contract?

### PROBE-006 — Rollback-input sufficiency

Evidence source: future DISC-010 record.

Governing contract required: reviewable DPA-700.

Question: Are the observed Git and repository inputs sufficient to execute the proposed rollback contract without introducing a new canonical history source?

## 4. Review boundary

This backlog MUST be reviewed for completeness after DISC-001 through DISC-010 are committed and assumptions are synchronized.

Claude primary architecture review is not requested for raw Discovery records. Claude should review the first exact-ref, reviewable DPA-300 contract together with:

- all DISC records;
- synchronized `ASSUMPTIONS.md`;
- synchronized `MAIN_REPOSITORY_CONTEXT.md`;
- this Probe backlog;
- the proposed DPA-300 traceability and Probe mapping.

A separate Claude review is required after a material DPA-300 redesign or before DPA-300 is promoted from `review-ready` to `stable` if the first review was performed against an earlier semantic baseline.
