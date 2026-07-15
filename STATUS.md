# Status

Status: active
Status-date: 2026-07-15
Superseded-by: n/a

## Current

Phase A — Foundation is closed on `main` at commit `a1b81beaf8f8a065d8a869d15bbf39d0e6459aae`.

Phase B — Core document-management integration is active on branch `discovery/dp1-main-repository`.

The lab remains non-authoritative for the runtime state of `vfi64/agentic-project-kit`, contains no production kit code and has not been adopted with the kit.

DPA-200 and its matrix are `review-ready`; DPA-ADR-013 through DPA-ADR-015 are accepted.

## DP1 Discovery completion

Target repository: `vfi64/agentic-project-kit`

Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 now each have bounded records under `evidence/repo-facts/`.

Completed fact families:

1. registry representation;
2. candidate reader graph;
3. candidate writer graph;
4. authority inputs;
5. lifecycle findings;
6. lifecycle mutation path;
7. Workspace and path APIs;
8. locking and concurrency;
9. gates and CI;
10. history and rollback inputs.

Post-Discovery synchronization is complete:

- `ASSUMPTIONS.md` now distinguishes verified facts from remaining Probe questions;
- `MAIN_REPOSITORY_CONTEXT.md` records the exact-ref facts needed by DPA-300;
- `integration/DP1_PROBE_BACKLOG.md` is bound to the completed records;
- no main-repository mutation occurred;
- no production form was selected.

## Confirmed CURRENT_HANDOFF command path

The active mutation path is:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

At the validation ref, this path updates source state and handoff artifacts but handles `CURRENT_HANDOFF.md` through narrow regex cleanup plus appended refresh prose. It does not route the target update through the existing safe bounded block-replacement primitive.

This is an explicit cross-spec obligation:

- DPA-300: lifecycle-owned plan, validation, lock and write path;
- DPA-400: pure payload renderer and no boundary-byte ownership;
- DPA-500: marker, drift, direct-write and acceptance findings;
- DPA-600: stale-plan and competing-PR serialization;
- DPA-700: preservation and rollback without historical-prose merge;
- DP1 Probe: demonstrate governed replacement rather than append behavior.

The lab must extend this observed command path or provide a governed migration of it; it must not create a parallel operational refresh command.

## Next governed step

Create the first evidence-based DPA-300 baseline:

1. write the registry-extension contract from DISC-001;
2. define lifecycle planning, validation, trust transition, locking, atomic write and evidence boundaries from DISC-005/006/007/008;
3. specify integration of the observed `admin-refresh-pr` writer path;
4. define direct-write detection and failure ownership without importing DPA-500 gate policy;
5. create DPA-300 traceability and registry/lifecycle/command-flow diagrams;
6. perform an internal invariant/ADR/evidence audit;
7. commit one immutable review baseline;
8. generate the Claude primary architecture review prompt against that exact commit.

DP1 Probe and Assessment remain deferred until DPA-300 is reviewable.

## Claude review timing

Claude is not required for raw Discovery records. Claude returns when one immutable commit contains:

- the complete Discovery set;
- synchronized assumptions and main-repository context;
- finalized Probe backlog;
- a reviewable DPA-300 draft;
- DPA-300 traceability and diagrams;
- explicit evidence-to-requirement mapping.

Claude must verify that DPA-300 integrates the observed `transfer admin-refresh-pr` / `CURRENT_HANDOFF.md` path rather than specifying a parallel replacement workflow.

## Phase B restrictions

- No production kit code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No DPA-300 rule may bypass DPA-200 authority, ownership or trust-state contracts.
- No Probe may execute before its governing contract is reviewable.
- No review finding becomes normative without adjudication.

Phase B may continue. DP1 Discovery is complete; DPA-300 drafting is now the active task.
