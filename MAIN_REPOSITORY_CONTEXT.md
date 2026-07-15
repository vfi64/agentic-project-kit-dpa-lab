# Main Repository Context

Status: active

Status-date: 2026-07-15

Superseded-by: n/a

## Purpose

This document records the last evidenced context of `vfi64/agentic-project-kit` relevant to the lab. It is a context snapshot, not a maintained mirror or substitute for fresh verification.

Before implementation, every repository-specific fact must be revalidated against the then-current `origin/main`.

## Evidence baseline

### VERIFIED (scoped to validation ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`)

- Repository: `vfi64/agentic-project-kit`
- Default branch: `main`
- DP1 Discovery validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`
- Commit subject: `Refresh handoff state after PR1863 (#1864)`
- Latest evidenced substantive commit: `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`
- Substantive subject: `Add post-L5 lifecycle audit evidence (#1863)`
- Recorded release: `0.4.12`, tag `v0.4.12`

Evidence includes the validation-ref record and bounded DISC-001 through DISC-010 plus DISC-003b under `evidence/repo-facts/`.

## Masterplan Q2 status

### VERIFIED_AT_RECORDED_BASELINE

The Q2 series reached its planned L5 endpoint and was followed by post-L5 lifecycle evidence and an administrative handoff refresh.

Capability families present at the baseline and therefore to be inspected and extended rather than recreated include command governance, instruction/chat contracts, mutation-lock coverage, repository identity enforcement, Workspace/self-hosting foundations, document lifecycle, staged strict adoption and workspace hygiene.

This list is contextual, not module-level implementation evidence.

## DP1 Discovery findings relevant to DPA-300

### VERIFIED (scoped to validation ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`)

1. The documentation registry is document-wide and schema-bounded. No registered-region identity, partition contract or projection-contract block was observed. Compatibility remains PROBE-001 work.
2. The lifecycle provides structured findings, dry-run triage and planning, strict blockers and bounded evidence-report writing. No projection content writer, acceptance-state path or projection-specific recovery path was observed in the inspected lifecycle surface.
3. Workspace is the path-resolution authority for registry, status, handoff, reports, lock and `.agentic/` paths; some direct literals remain.
4. `CURRENT_HANDOFF.md` is read as a full mandatory boot source. No section selector or enforced current-first read order was observed.
5. The file contains a marked generated current-state block plus accumulated historical prose.
6. `.agentic/operational_handoff_state.yaml` is an observed input for the generated block but does not own all surrounding historical/manual bytes.
7. **An observed writer path** is `agentic-kit transfer admin-refresh-pr` through `_refresh_operational_handoff_docs()`. It updates handoff state and writes `CURRENT_HANDOFF.md` using narrow regex cleanup plus appended refresh prose.
8. DISC-003b verified that the inspected `agentic-kit transfer chat-switch-complete` path creates the successor package and canonical prompt projections but does not write `CURRENT_HANDOFF.md` at this ref.
9. A safe bounded block-replacement primitive exists but the observed `admin-refresh-pr` target update does not use it.
10. Local concurrency uses a PID-based same-process-reentrant Workspace lock. Transfer workflows add branch, SHA and remote-head guards plus administrative refresh PR serialization.
11. CI runs Ruff, the full pytest suite and CLI smoke. Projection-specific checks do not yet exist.
12. Git retains prior candidate, state and writer versions. No separate canonical history database or automatic historical-prose merger was observed.

These facts do not establish global writer-set completeness, schema compatibility, suitability or a production migration form.

## Existing document-management direction

### VERIFIED_AT_RECORDED_BASELINE

The main repository already has an integrated documentation registry, scope contracts, lifecycle implementation, findings, sweep commands, freshness/drift checks, Workspace paths, gate integration and registered evidence.

The DPA MUST extend this stack and MUST NOT introduce a second registry, lifecycle, freshness, evidence, Workspace, state or gate architecture.

## Why the DPA lab exists

### NORMATIVE

Current and historical prose may coexist in one document; refresh logic may update or append later content while leading content remains stale; consumers often read from the beginning; marker presence does not prove derivational freshness; and local locks do not serialize refs.

The lab designs a durable extension before production implementation.

## DPA objective

### NORMATIVE

The DPA shall enable registered documents to become deterministic views of canonical repository-backed state while preserving:

- canonical state ownership of facts;
- pure renderer computation;
- lifecycle-owned plan, local lock, Write, Verify and lifecycle state;
- workflow-owned cross-ref serialization;
- non-authoritative evidence;
- registry ownership of projection and partition contracts.

## Known candidate documents

### NEEDS_MAIN_REPO_VALIDATION BEFORE IMPLEMENTATION

Observed or planned candidates include:

- `docs/handoff/CURRENT_HANDOFF.md`
- `docs/handoff/NEXT_CHAT_BOOTSTRAP.md`
- `docs/handoff/START_NEW_CHAT_PROMPT.md`
- `docs/STATUS.md`
- selected files under `docs/reports/handoff-packages/latest/`

No candidate is approved for migration solely because it appears here.

## Lab versus main repository responsibilities

The lab may decide normative architecture, terminology, contracts, alternatives, migration strategies, evidence requirements, DP1–DP5 specifications and review structure.

Without main-repository validation it may not decide serialized schema compatibility, exact path mappings, suitability of findings/locks, actual migration form, implementation test success or completed implementation status.

## Revalidation rule

A session needing a current main-repository fact must identify the fact and ref, inspect the exact source, record the result under `evidence/repo-facts/`, and update this context only when later design depends on the result.

Unavailable verification remains `NEEDS_MAIN_REPO_VALIDATION` or `ASSUMPTION`; model consensus is never sufficient.

## Current next step for the lab

### NORMATIVE

The lab shall now:

1. complete DPA-300 adjudication under ADR-016 and ADR-017;
2. synchronize DPA-100, DPA-300, Traceability, diagrams and Probe mappings;
3. run independent post-adjudication verification;
4. promote DPA-300 to `review-ready` only if that verification passes;
5. prepare PROBE-001 and the DPA-300-owned subset of PROBE-002;
6. continue through DPA-500 before considering kit adoption.
