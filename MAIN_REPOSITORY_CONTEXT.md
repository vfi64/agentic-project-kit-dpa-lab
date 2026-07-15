# Main Repository Context

Status: active
Status-date: 2026-07-15
Superseded-by: n/a

## Purpose

This document records the last evidenced context of the main repository `vfi64/agentic-project-kit` that is relevant to work in this lab.

It is a context snapshot, not a substitute for fresh verification. Before implementation in the main repository, every fact here must be revalidated against the then-current `origin/main`.

## Evidence baseline

### VERIFIED

- Repository: `vfi64/agentic-project-kit`
- Default branch: `main`
- Current DP1 Discovery validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`
- Commit subject: `Refresh handoff state after PR1863 (#1864)`
- Latest evidenced substantive commit immediately before that refresh: `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`
- Substantive commit subject: `Add post-L5 lifecycle audit evidence (#1863)`
- Latest evidenced completed implementation milestone before the post-L5 evidence: PR #1860, `L5: add workspace hygiene baseline`
- Current verified release recorded by the refreshed handoff state: `0.4.12`
- Current release tag recorded there: `v0.4.12`

Evidence refs used for this snapshot:

- main commit `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`
- substantive commit `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`
- L5 commit `8c970adf2a18debe329bd29df6b5c15d89cf4719`
- bounded DP1 Discovery records under `evidence/repo-facts/DP1-DISC-*6A9DA7D.md`

## Masterplan Q2 status

### VERIFIED_AT_RECORDED_BASELINE

The Q2 implementation series reached its planned L5 endpoint and was followed by post-L5 lifecycle evidence and an administrative handoff refresh.

The following major capability families existed at the recorded baseline and must be inspected and extended, not recreated:

- command manifest governance,
- instruction and chat-entrypoint contracts,
- lock reentrancy and mutation-lock coverage,
- repository identity and active-literal enforcement,
- remote branch hygiene,
- Workspace/self-hosting foundations,
- document-lifecycle metadata and signals,
- lifecycle sweep and staged strict adoption,
- workspace hygiene baseline.

This list is contextual, not a substitute for module-level evidence.

## DP1 Discovery findings relevant to DPA-300

### VERIFIED AT `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

1. The documentation registry is document-wide and schema-bounded. No registered-region identity, boundary representation or projection-contract block was observed. Compatibility of a future optional projection structure remains a Probe question.
2. The documentation lifecycle already provides structured findings, dry-run triage and planning, staged strict blockers and bounded evidence-report writing. No projection-target content writer, atomic replacement path or projection-specific drift vocabulary was observed in the inspected lifecycle path.
3. Workspace is the existing path-resolution authority for registry, status, handoff, reports, lock and `.agentic/` paths. Relevant direct literals still exist in some helpers.
4. `CURRENT_HANDOFF.md` is read as a full mandatory boot source. No section selector or enforced current-first read order was observed.
5. `CURRENT_HANDOFF.md` contains a marked generated current-state block plus accumulated historical prose.
6. `.agentic/operational_handoff_state.yaml` is an observed semantic input for that generated block; it is not a complete authority for all surrounding historical/manual bytes.
7. The active writer path is `agentic-kit transfer admin-refresh-pr` through `_refresh_operational_handoff_docs()`. It updates state and handoff artifacts and appends or regex-replaces standardized refresh-history sections.
8. A safe single-block replacement primitive already exists in `operational_handoff_projection.py`, but the active `CURRENT_HANDOFF.md` admin-refresh path does not use it for the document update at this ref.
9. Local concurrency uses a PID-based, same-process-reentrant Workspace lock. Transfer workflows add branch guards, full-SHA PR guards, remote-head verification and administrative refresh branch/PR serialization.
10. The primary CI workflow runs Ruff, the complete pytest suite and CLI smoke checks. Projection-specific required checks and drift gates do not yet exist.
11. Git history retains prior candidate, state and writer versions. No separate canonical history database or automatic historical-prose merge mechanism was observed.

These facts are bounded by the individual DISC records. They do not establish suitability, schema compatibility or a production migration form.

## Existing document-management direction

### VERIFIED_AT_RECORDED_BASELINE

The main repository already has an integrated document-management stack including:

- `docs/DOCUMENTATION_REGISTRY.yaml`,
- document scope and coverage contracts,
- document lifecycle implementation,
- lifecycle findings and sweep commands,
- freshness and drift checks,
- Workspace-resolved paths,
- gate integration,
- registered evidence and reports.

Therefore the DPA MUST extend this stack. It MUST NOT introduce a second registry, lifecycle, freshness, evidence, Workspace or gate architecture.

## Why the DPA lab exists

### NORMATIVE

A specific handoff-document problem exposed a broader architecture question:

- current state and historical prose may coexist in the same document,
- refresh logic may update or append a valid later section while the beginning remains historically stale,
- bootloaders and humans usually read from the beginning,
- marker-presence checks may not prove that the consumed projection is current,
- local mutation locks do not serialize concurrent branches or pull requests.

The lab exists to design a durable extension of the existing document-management system before production implementation begins.

## DPA objective

### NORMATIVE

The DPA shall enable registered documents to be deterministic views of canonical repository-backed state while preserving these boundaries:

- canonical state owns facts,
- renderers compute text or bytes only,
- the document lifecycle validates, plans, locks and writes,
- workflow orchestration serializes across branches and pull requests,
- evidence is not runtime authority,
- the existing documentation registry holds the eventual runtime projection contract.

## Known candidate documents

### NEEDS_MAIN_REPO_VALIDATION BEFORE IMPLEMENTATION

Observed or planned candidates include:

- `docs/handoff/CURRENT_HANDOFF.md`
- `docs/handoff/NEXT_CHAT_BOOTSTRAP.md`
- `docs/handoff/START_NEW_CHAT_PROMPT.md`
- `docs/STATUS.md`
- selected files under `docs/reports/handoff-packages/latest/`

No candidate is approved for migration solely because it appears in this list. Discovery evidence does not select a document form.

## Lab versus main repository responsibilities

### Lab may decide

- normative DPA principles,
- terminology,
- contracts,
- alternatives,
- migration strategies,
- evidence requirements,
- DP1–DP5 implementation specification,
- review and traceability structure.

### Lab may not decide without main-repository validation

- exact schema compatibility,
- suitability of observed findings and locks,
- actual migration mode for a production document,
- test and CI success for an implementation,
- completed implementation status.

## Revalidation rule

Any session that needs a current main-repository fact must:

1. identify the exact fact,
2. identify the required repository ref,
3. fetch or inspect the corresponding main-repository evidence,
4. record the result under `evidence/repo-facts/`,
5. update this document only when the new context is relevant to subsequent lab work.

If verification is unavailable, use `NEEDS_MAIN_REPO_VALIDATION`; never upgrade an assumption from model consensus alone.

## Current next step for the lab

### NORMATIVE

The lab shall now:

1. complete the Discovery record-set review and Probe backlog synchronization,
2. draft DPA-300 from exact-ref evidence,
3. create DPA-300 traceability and integration diagrams,
4. obtain primary architecture review and secondary technical verification against one immutable DPA-300 baseline,
5. execute DP1 Probe only after a reviewable DPA-300 contract exists,
6. continue through DPA-500 before considering kit adoption of this lab.
