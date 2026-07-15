# Status

Status: active

Status-date: 2026-07-15

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is active on branch `spec/dpa-300-registry-lifecycle`.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200 and its matrix are `review-ready`.

## DP1 Discovery

DP1 Discovery is complete for the explicitly inspected scope at:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed.

DISC-003b established:

- `transfer chat-switch-complete` does not write `CURRENT_HANDOFF.md` in the inspected code at that ref;
- `transfer admin-refresh-pr` through `_refresh_operational_handoff_docs()` is an observed writer path;
- global writer-set completeness is not claimed and must be revalidated at Probe time.

No main-repository mutation occurred and no production form was selected.

## DPA-300 review

Primary review baseline:

`6682485e3809d42bb17a90b62582b15e4d8fd467`

Primary architecture review:

`ACCEPT_WITH_CHANGES`

Secondary technical verification:

`ACCEPT_WITH_CHANGES`

No blocker, hidden parallel subsystem, new runtime authority, false implementation claim or production-form preselection was found.

## Accepted DPA-300 decisions

- DPA-ADR-016 — lifecycle-owned acceptance state and interrupted-refresh recovery;
- DPA-ADR-017 — parent-entry partition contract.

Maintainer dispositions:

1. acceptance state is Workspace-resolved `.agentic/` lifecycle state, not evidence, canonical state, registry authority or target metadata;
2. crashed-after-Write bytes may be re-verified only against an exactly recovered still-valid plan, otherwise they are regenerated;
3. one partition contract lives on the parent registry entry;
4. DISC-003b is executed now rather than left as an ownerless gap;
5. DPA-100 owns the closed drift vocabulary and `partition drift` replaces `boundary drift`.

## Applied adjudication changes

Completed:

- folded consumer trust states and the expanded drift vocabulary into `DPA-100-FOUNDATIONS.md`;
- retired the temporary DPA-100 amendment as a normative source;
- added lifecycle state, acceptance state, interrupted refresh and partition contract terminology;
- revised DPA-300 for parent partition representation, acceptance state, multi-class drift detection and crash recovery;
- corrected `written-unverified` timing;
- prohibited nested projection mutation while retaining bounded outer orchestration reentrancy;
- added payload, preserved-region and complete-target fingerprints;
- updated command integration to `an observed writer path` and incorporated DISC-003b;
- regenerated DPA-300 traceability and diagrams;
- expanded PROBE-001 and PROBE-002;
- removed the duplicate DPA-300 stub and added a canonical file map;
- synchronized assumptions and main-repository context.

DPA-300 remains `draft` until independent post-adjudication verification passes.

## Next governed step

Run an independent post-adjudication verification against one immutable commit containing:

- DPA-100 consolidation;
- DPA-300 adjudicated contract;
- ADR-016 and ADR-017;
- DISC-003b and synchronized evidence language;
- DPA-300 traceability and diagrams;
- updated Probe backlog;
- primary review, secondary verification and consolidated adjudication record.

The verifier must not be the session that applied the changes.

If verification passes:

1. promote DPA-300 to `review-ready`;
2. update ROADMAP and STATUS;
3. prepare PROBE-001 and the DPA-300-owned subset of PROBE-002;
4. do not execute Probe until the review-ready gate is committed.

## Restrictions

- No production code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe before its governing contract is reviewable.
- No review finding becomes normative without adjudication.

Phase B may continue. The current gate is independent post-adjudication verification.
