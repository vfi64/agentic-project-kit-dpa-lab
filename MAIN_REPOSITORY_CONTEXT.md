# Main Repository Context

Status: active
Status-date: 2026-07-14
Superseded-by: n/a

## Purpose

This document records the last evidenced context of the main repository `vfi64/agentic-project-kit` that is relevant to work in this lab.

It is a context snapshot, not a substitute for fresh verification. Before implementation in the main repository, every fact here must be revalidated against the then-current `origin/main`.

## Evidence baseline

### VERIFIED

- Repository: `vfi64/agentic-project-kit`
- Default branch: `main`
- Current evidenced administrative main commit at the time this context was written: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`
- Commit subject: `Refresh handoff state after PR1863 (#1864)`
- Latest evidenced substantive commit immediately before that refresh: `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`
- Substantive commit subject: `Add post-L5 lifecycle audit evidence (#1863)`
- Latest evidenced completed implementation milestone before the post-L5 evidence: PR #1860, `L5: add workspace hygiene baseline`
- Current verified release recorded by the refreshed handoff state: `0.4.12`
- Current release tag recorded there: `v0.4.12`
- The post-L5 lifecycle audit evidence was registered in the central documentation registry.
- The post-L5 lifecycle audit evidence recorded warn-mode lifecycle findings with zero blocking findings and strict adoption intentionally left maintainer-gated.
- `docs/architecture/P5C_PHYSICAL_MIGRATION_PLAN.md` existed as a proposed plan awaiting maintainer decision.
- The main repository already contained evidence for command-manifest hardening, mutation-lock coverage, path-literal enforcement, remote-branch hygiene and lifecycle work.

Evidence refs used for this snapshot:

- main commit `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`
- substantive commit `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`
- L5 commit `8c970adf2a18debe329bd29df6b5c15d89cf4719`

## Masterplan Q2 status

### VERIFIED AT THE RECORDED BASELINE

The Q2 implementation series reached its planned L5 endpoint and was followed by post-L5 lifecycle evidence and an administrative handoff refresh.

The following major capability families were implemented during that series and must be treated as existing architecture to be inspected and extended, not recreated:

- command manifest governance,
- command selection support,
- instruction linting and chat entrypoint contracts,
- lock inventory, reentrancy decision and lock-coverage remediation,
- repository identity derivation and active-literal enforcement,
- remote branch hygiene evidence,
- workspace manifest/self-hosting foundations,
- legacy-profile deprecation,
- physical-migration planning,
- GUI project-root support and operating-layer guidance,
- negative-path hardening,
- document-lifecycle metadata,
- lifecycle signals,
- lifecycle sweep workflows,
- staged strict adoption,
- workspace hygiene baseline.

This list is contextual, not a substitute for module-level verification.

## Existing document-management direction

### VERIFIED AT THE RECORDED BASELINE

The main repository already had an integrated document-management stack including:

- `docs/DOCUMENTATION_REGISTRY.yaml`,
- document scope and coverage contracts,
- document lifecycle implementation,
- lifecycle findings and sweep commands,
- document freshness and drift checks,
- workspace-resolved paths,
- standard-gate integration,
- documentation architecture contracts,
- registered evidence and reports.

Therefore the DPA MUST extend this stack. It MUST NOT introduce a second registry, lifecycle, freshness, evidence, workspace or gate architecture.

## Why the DPA lab exists

### NORMATIVE

A specific handoff-document problem exposed a broader architecture question:

- current state and historical prose may coexist in the same document,
- refresh logic may update a valid later section while the beginning remains historically stale,
- bootloaders and humans usually read from the beginning,
- marker-presence checks may not prove that the consumed projection is current,
- local mutation locks do not serialize concurrent branches or pull requests.

The lab exists to design a durable extension of the existing document-management system before any production implementation begins.

## DPA objective

### NORMATIVE

The DPA shall enable registered documents to be deterministic views of canonical repository-backed state while preserving these boundaries:

- canonical state owns facts,
- renderers compute text or bytes only,
- the document lifecycle validates, plans, locks and writes,
- workflow orchestration serializes across branches and pull requests,
- evidence is not runtime authority,
- the documentation registry holds the eventual runtime projection contract.

## Known candidate documents

### NEEDS_MAIN_REPO_VALIDATION BEFORE IMPLEMENTATION

The planning discussion identified these likely candidates:

- `docs/handoff/CURRENT_HANDOFF.md`
- `docs/handoff/NEXT_CHAT_BOOTSTRAP.md`
- `docs/handoff/START_NEW_CHAT_PROMPT.md`
- `docs/STATUS.md`
- selected files under `docs/reports/handoff-packages/latest/`

No candidate is approved for migration solely because it appears in this list. DP1 must build the real reader/writer/source graph and determine the correct classification.

## Known open maintainer decisions outside the lab

### VERIFIED OR RECORDED AS MAINTAINER-GATED AT THE BASELINE

- execution decision for the P5c physical migration plan,
- lifecycle backlog clearance before strict adoption is made fully blocking,
- any explicit strict-lifecycle switch for the kit repository,
- any proposal-delete execution,
- first real adoption of an external/private repository such as Comm-SCI-Control-private,
- later 2.0-line decisions including removal of legacy compatibility.

These are not automatically part of DPA work. DPA may affect their sequencing, but it must not silently execute them.

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

- actual current module names and field names,
- exact registry schema compatibility,
- real reader/writer relationships,
- real state authority,
- real checks and gate behavior,
- actual migration mode for any production document,
- test and CI success,
- completed implementation status.

## Revalidation rule

Any session that needs a current main-repository fact must:

1. identify the exact fact,
2. identify the required repository ref,
3. fetch or inspect the corresponding main-repository evidence,
4. record the result under `evidence/repo-facts/`,
5. update this document only when the new context is relevant to subsequent lab work.

If verification is unavailable, use `NEEDS_MAIN_REPO_VALIDATION`; never upgrade an assumption to `VERIFIED` from model consensus alone.

## Current next step for the lab

### NORMATIVE

The lab shall now:

1. complete and stabilize DPA-000,
2. create DPA-100 with exact terminology,
3. establish traceability and review templates,
4. continue through DPA-500 before considering kit adoption of this lab,
5. draft DPA-600 through DPA-900 under the same governance,
6. prepare DP1 as proof-of-architecture against a future fresh main.
