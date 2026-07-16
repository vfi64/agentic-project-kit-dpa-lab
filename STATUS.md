# Status

Status: active

Status-date: 2026-07-16

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is active on branch `spec/dpa-300-registry-lifecycle`.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200 and DPA-300 are `review-ready`.

## DP1 Discovery

DP1 Discovery is complete for the explicitly inspected scope at:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed.

DISC-003b established:

- `transfer chat-switch-complete` does not write `CURRENT_HANDOFF.md` in the inspected code at that ref;
- `transfer admin-refresh-pr` through `_refresh_operational_handoff_docs()` is an observed writer path;
- global writer-set completeness is not claimed and must be revalidated at Probe time.

No main-repository mutation occurred and no production form was selected.

## DPA-300 review and promotion

Primary review baseline:

`6682485e3809d42bb17a90b62582b15e4d8fd467`

Primary architecture review: `ACCEPT_WITH_CHANGES`.

Secondary technical verification: `ACCEPT_WITH_CHANGES`.

Maintainer adjudication accepted ADR-016 and ADR-017 and synchronized DPA-100, DPA-200, DPA-300, evidence language, traceability and diagrams.

Independent post-adjudication verification initially reported a narrow mechanical FAIL because `boundary drift` remained in DPA-200. The bounded synchronization commit corrected that residue, retired the obsolete DPA-200 amendment companion, repaired the canonical file map and added the DISC-003b cross-reference.

The diff-scoped re-check is recorded in:

`reviews/consolidated/DPA-300_POST_ADJUDICATION_DIFF_RECHECK.md`

Result: `PASS`.

DPA-300 is therefore promoted to `review-ready`. Stability remains blocked on applicable DP1 Probe evidence and later governed revalidation.

## Accepted DPA-300 decisions

- DPA-ADR-016 — lifecycle-owned acceptance state and interrupted-refresh recovery;
- DPA-ADR-017 — parent-entry partition contract.

Maintainer dispositions:

1. acceptance state is Workspace-resolved `.agentic/` lifecycle state, not evidence, canonical state, registry authority or target metadata;
2. crashed-after-Write bytes may be re-verified only against an exactly recovered still-valid plan, otherwise they are regenerated;
3. one partition contract lives on the parent registry entry;
4. DISC-003b is executed now rather than left as an ownerless gap;
5. DPA-100 owns the closed drift vocabulary and `partition drift` replaces `boundary drift`.

## Sequencing decision

The next architecture work is DPA-400 and then DPA-500.

During the current no-Mac period, both may be drafted and reviewed to `review-ready`, with every repository-dependent claim fenced as `NEEDS_MAIN_REPO_VALIDATION`.

Neither DPA-400 nor DPA-500 may become `stable` before the applicable DP1 Probe evidence exists.

PROBE-001 is governed by DPA-300 and ADR-017. It does not wait for DPA-400. The fixture may carry a syntactically plausible renderer identifier because DPA-300 already defines that registry field; actual renderer resolution and behavior remain DPA-400 and later Probe concerns.

Portability literal fixes in the main repository are a separate maintenance stream and may run in parallel with Probe work during the later Mac phase. The `CURRENT_HANDOFF.md` writer must not be treated as a portability quick fix because its governed replacement is part of DPA/DP2 architecture.

Independent-context verification is retained only as deferred future scope for DPA-800/DPA-900 and later kit governance. It is not a new active specification slice.

## Next governed step

1. complete the DPA-300 branch closeout and place the review-ready result on `main`;
2. start a clean DPA-400 branch from updated `main`;
3. draft the renderer contract, traceability and diagrams;
4. prepare PROBE-001 and the DPA-300-owned subset of PROBE-002 as non-executed fixtures and expected-result contracts;
5. keep all Probe execution deferred until a suitable main-repository environment is available.

## Restrictions

- No production code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe before its governing contract is reviewable.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without adjudication.

Phase B may continue. The active architecture task is DPA-400 preparation.