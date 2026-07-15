# Status

Status: active

Status-date: 2026-07-15
Superseded-by: n/a

## Current

Phase A — Foundation is closed on `main` at commit `a1b81beaf8f8a065d8a869d15bbf39d0e6459aae`.

Phase B — Core document-management integration is active on branch `spec/dpa-300-registry-lifecycle`.

The lab remains non-authoritative for the runtime state of `vfi64/agentic-project-kit`, contains no production kit code and has not been adopted with the kit.

DPA-200 and its matrix are `review-ready`; DPA-ADR-013 through DPA-ADR-015 are accepted.

## DP1 Discovery

DP1 Discovery is complete against:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010, synchronized `ASSUMPTIONS.md`, synchronized `MAIN_REPOSITORY_CONTEXT.md` and the DP1 Probe backlog are present.

No main-repository mutation occurred and no production document form was selected.

## DPA-300 baseline

The first evidence-based DPA-300 baseline now contains:

- `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`;
- `traceability/DPA-300_TRACEABILITY.md`;
- `diagrams/dpa-300-registry-lifecycle.mmd`;
- `diagrams/dpa-300-command-integration.mmd`;
- `diagrams/dpa-300-plan-state.mmd`;
- `reviews/consolidated/DPA-300_PRE_REVIEW_AUDIT.md`.

DPA-300 defines:

1. an optional declarative projection contract in the existing registry;
2. fail-loud registry validation;
3. Resolve → Inspect → Validate → Render → Plan → Preflight → Lock → Revalidate → Write → Verify → Record → Release;
4. deterministic plan identity and stale-plan invalidation;
5. existing workspace-lock use;
6. lifecycle-only atomic target and partition writes;
7. exact preservation of non-projected bytes;
8. post-write verification before acceptance;
9. direct-write detection by expected-output recomputation;
10. bounded non-authoritative evidence;
11. adaptation of existing mutating commands rather than creation of a parallel DPA command.

## Confirmed command integration obligation

Exact-ref Discovery identified:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

as the active handoff mutation path at the validation ref.

DPA-300 requires this existing path to be adapted through the registry and lifecycle if `CURRENT_HANDOFF.md` is later selected as a projection target. It prohibits a parallel DPA-only writer and requires governed bounded replacement instead of append accumulation.

This requirement remains conditional and does not select a full, hybrid or managed-head production form.

## Internal audit

`reviews/consolidated/DPA-300_PRE_REVIEW_AUDIT.md` result:

`PASS_WITH_REVIEW_QUESTIONS`

No foundational contradiction, hidden parallel system, new runtime authority or false implementation claim was found.

The audit records seven explicit reviewer questions concerning render/plan ordering, plan payload strength, lock reentrancy, evidence failure, direct-write fingerprints, command-contract preservation and partition fingerprints.

## Next governed step

1. create a Claude primary architecture review prompt bound to one immutable DPA-300 baseline commit;
2. obtain Claude's read-only review;
3. commit the review under `reviews/claude/`;
4. perform secondary technical verification;
5. adjudicate accepted findings before normative changes;
6. promote DPA-300 to `review-ready` only after corrections and post-adjudication verification.

DP1 Probe and Assessment remain deferred until the governing specifications are reviewable.

## Phase B restrictions

- No production kit code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No DPA-300 rule may bypass DPA-200 authority, ownership or trust-state contracts.
- No Probe may execute before its governing contract is reviewable.
- No review finding becomes normative without adjudication.

Phase B may continue. DPA-300 is a complete draft suitable for primary architecture review; it is not yet `review-ready`.