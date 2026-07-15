# Status

Status: active

Status-date: 2026-07-15
Superseded-by: n/a

## Current

Phase A — Foundation is closed on `main` at commit `a1b81beaf8f8a065d8a869d15bbf39d0e6459aae`.

Phase B — Core document-management integration is active on branch `discovery/dp1-main-repository`.

The lab remains non-authoritative for the runtime state of `vfi64/agentic-project-kit`, contains no production kit code and has not been adopted with the kit.

## DPA-200 review and adjudication

Review baseline:

`44a87127fca7f482bc2991f0c258af0a386a7048`

- Claude primary architecture review: `ACCEPT_WITH_CHANGES`; no blockers.
- ChatGPT secondary technical verification: `ACCEPT_WITH_CHANGES`.
- Maintainer adjudication: complete.
- Post-adjudication verification: `PASS`.

DPA-200 and its matrix are `review-ready`.

## Accepted DPA-200 decisions

- DPA-ADR-013 — unique document-form classifier and lifecycle-owned partition bytes.
- DPA-ADR-014 — closed consumer trust-state model.

The consolidated model provides:

1. one primary form per document;
2. split projection only for multiple independently registered target identities;
3. hybrid classification for one mixed document;
4. managed-head as an exceptional hybrid subtype;
5. lifecycle-owned partition contracts and exhaustive byte ownership;
6. renderer payload-only output;
7. trust states `computed`, `plan-captured`, `written-unverified`, `accepted`, `abandoned`;
8. explicit drift and acceptance-scope semantics;
9. one normative invalid-state catalog;
10. DM-011 target-semantics completeness;
11. `no migration` as the fail-safe outcome.

## Accepted sequencing decision

DPA-ADR-015 — Permit early read-only DP1 discovery — is accepted.

DP1 remains one formal slice with internal stages:

1. Discovery
2. Probe
3. Assessment

Only Discovery may execute in Phase B before DPA-300 and before lab adoption.

The governing contract is `integration/DP1_DISCOVERY_CONTRACT.md`.

Discovery:

- is strictly read-only;
- uses one exact validation ref;
- records facts rather than suitability judgments;
- may verify or falsify assumptions only after committed records exist;
- performs no mutation, migration, adoption, conformance judgment, form selection or architecture decision.

## Active DP1 Discovery

Target repository:

`vfi64/agentic-project-kit`

Validation ref:

`6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Completed records:

- DISC-001 — registry representation;
- DISC-002 — candidate reader graph;
- DISC-003 — candidate writer graph;
- DISC-004 — authority inputs;
- DISC-006 — lifecycle mutation path;
- DISC-007 — Workspace and path APIs.

Pending records:

- DISC-005 — lifecycle findings;
- DISC-008 — locking and concurrency;
- DISC-009 — gates and CI;
- DISC-010 — history and rollback inputs.

No main-repository mutation has occurred.

## Confirmed CURRENT_HANDOFF command-path finding

Exact-ref Discovery identified the active mutation path as:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

The observed implementation updates handoff state and generated artifacts, but for `CURRENT_HANDOFF.md` it removes only one narrowly matched prior refresh section and appends a new historical refresh section. It does not route that target through the existing bounded `replace_generated_operational_handoff_block()` primitive.

This is now an explicit planning obligation in `ROADMAP.md` and an exact Probe item in `integration/DP1_PROBE_BACKLOG.md`.

Required later result:

- DPA-300 defines lifecycle-owned bounded mutation;
- DPA-400 defines renderer payload purity;
- DPA-500 defines marker/drift findings and gates;
- DPA-600 preserves stale-plan and competing-PR protection;
- DPA-700 defines outside-region preservation and rollback;
- DP1 Probe demonstrates replacement rather than append behavior without preselecting a production form.

Primary evidence:

`evidence/repo-facts/DP1-DISC-003-WRITER-GRAPH-6A9DA7D.md`

## Next governed step

Complete the remaining read-only Discovery packages:

1. DISC-005 and DISC-009 — lifecycle findings, gates and CI;
2. DISC-008 and DISC-010 — locking, concurrency, history and rollback.

Then:

1. review all ten records for exact-ref scope and limitations;
2. synchronize `ASSUMPTIONS.md` only where committed evidence supports reclassification;
3. update `MAIN_REPOSITORY_CONTEXT.md` only for facts needed by later design;
4. finalize `integration/DP1_PROBE_BACKLOG.md`;
5. create the first evidence-based DPA-300 draft and traceability baseline;
6. bind a Claude primary architecture review prompt to that exact DPA-300 commit.

DP1 Probe and Assessment remain deferred until the DPA-300 contract is reviewable.

## Claude review timing

Claude is not required for individual raw Discovery records. The next primary Claude review is required when all of the following exist at one immutable lab commit:

- DISC-001 through DISC-010 records;
- synchronized `ASSUMPTIONS.md`;
- synchronized `MAIN_REPOSITORY_CONTEXT.md`;
- finalized `integration/DP1_PROBE_BACKLOG.md`;
- a reviewable DPA-300 draft;
- DPA-300 traceability and diagrams sufficient to audit registry, lifecycle, writer ownership, command integration and Probe coverage.

Claude must specifically verify that the proposed DPA-300 contract accounts for the observed `transfer admin-refresh-pr` / `CURRENT_HANDOFF.md` writer path and does not merely specify a parallel replacement command.

## Validation boundary

Concrete region support, marker syntax, candidate readers and writers, lifecycle hooks, finding suitability, gate mapping, concurrency mechanisms and rollback behavior remain `NEEDS_MAIN_REPO_VALIDATION` until the appropriate Discovery, Probe or Assessment evidence exists.

No production candidate has been assigned a form.

## Phase B restrictions

- No production kit code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No registry-field or module-name claim without exact evidence.
- No production-form selection before DP1 evidence.
- No DPA-300 rule may bypass DPA-200 authority, ownership or trust-state contracts.
- No Discovery conclusion may make an architecture decision.
- No review finding becomes normative without adjudication.

Phase B may continue. DPA-200 is review-ready; early DP1 Discovery is active and governed.
