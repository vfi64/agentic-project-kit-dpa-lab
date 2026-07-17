# DPA-500 Primary Review Adjudication

Status: complete
Status-date: 2026-07-17

## Scope

This record adjudicates the findings in `reviews/claude/CLAUDE_DPA_500_PRIMARY_REVIEW.md`, bound to exact review ref `60d6457f0473365789ece4f885a48ea5320b01ff`.

The review verdict was `ACCEPT_WITH_CHANGES` with three major, four minor and three editorial findings. Review prose is non-normative until dispositioned here and applied through a governed amendment batch.

## Overall adjudication

All three major findings are accepted. All four minor findings and all three editorial findings are accepted.

The accepted correction set is bounded and does not redesign DPA-500, introduce a new runtime authority, create a parallel gate or freshness system, claim implementation, or claim main-repository conformance.

DPA-500 remains `draft`. Promotion to `review-ready` is not authorized by this adjudication alone.

## Major findings

### R5-M01 — Base-context freshness after acceptance

Disposition: **ACCEPTED**.

Decision:

- Base/ref identity is operation-scoped unless the projection contract explicitly declares base dependence.
- DPA-500 §5.9 will compare the base/ref context required by the governing plan or requested operation.
- Acceptance state will persist an accepted base identity only when the accepted projection contract declares base dependence.
- A post-acceptance audit without a live plan must remain evaluable when no base-dependent contract applies.

Rationale:

Attempt-scoped plans cannot serve as the sole persistent comparator after Release. Conditional persistence preserves evaluability without turning every repository base into semantic projection state.

### R5-M02 — Gate-set re-evaluation without target mutation

Disposition: **ACCEPTED**.

Decision:

DPA-500 will define a lifecycle-owned gate-set re-evaluation operation that:

- is permitted only when every applicable freshness dimension except gate-set freshness is `fresh`;
- evaluates the complete current required gate set against the existing accepted bytes;
- performs no renderer invocation and no target write;
- updates only the acceptance-state gate-set identity and accepted outcome after a complete `pass`;
- emits findings and leaves acceptance state unchanged on `warning`, `failure` or evaluation unavailability;
- remains governed by the existing lifecycle sole-writer, persistence and crash-safety rules.

Rationale:

Policy-only changes must not require semantically pointless regeneration. Re-acceptance is a lifecycle state transition, not a second write path or a bypass of mandatory gates.

### R5-M03 — Governed manual-region evolution

Disposition: **ACCEPTED — layered acceptance selected**.

Decision:

For registered-region projections:

- post-acceptance freshness compares lifecycle-owned projected payload bytes and lifecycle-owned partition bytes;
- preserved-region and complete-target fingerprints remain mandatory plan-time guards and Write/Verify acceptance-integrity checks;
- a post-acceptance change made by the governed non-lifecycle owner to its own region, while preserving the registered partition contract, is not projection drift and does not make the projected payload stale;
- such an owned-region evolution may produce bounded informational evidence but must not be represented as out-of-band drift;
- unauthorized change to lifecycle-owned payload bytes remains `target drift`;
- unauthorized change to lifecycle-owned partition bytes or boundaries remains `partition drift`;
- ambiguous ownership, malformed boundaries or unverifiable ownership fail closed.

A synchronized governed amendment to DPA-300 §12.2 is required. The complete-target comparator remains authoritative for complete-target projections; region projections use owned-byte comparators for post-acceptance freshness while retaining complete-target fingerprints as mutation guards and acceptance-integrity evidence.

Rationale:

Hybrid documents exist specifically to permit governed manual-region evolution alongside a stable projected region. Strict complete-target acceptance would turn legitimate document evolution into permanent false-positive staleness and would undermine the primary candidate use case.

## Minor findings

### R5-m01

Disposition: **ACCEPTED**.

A failed renderer attempt affects the evaluated attempt context and may end `abandoned`; it does not automatically reclassify previously accepted bytes. Previously accepted bytes remain classified from the current DPA-500 freshness comparisons.

### R5-m02

Disposition: **ACCEPTED**.

Contract-declared configuration change maps deterministically to `contract drift`. Target-semantics changes map to `contract drift`, except partition-owned semantics changes which map to `partition drift`. No open source/contract disjunction remains.

### R5-m03

Disposition: **ACCEPTED**.

Every DPA-500 traceability invariant anchor will be re-derived from the canonical DPA-000 invariant register. New rows and tests will cover base-context evaluability, gate-set re-acceptance and governed-region evolution versus out-of-band writes.

### R5-m04

Disposition: **ACCEPTED**.

Gate evidence will distinguish mandatory identity-critical fields from contextual fields. Evaluated ref/tree, target identity, freshness classification, drift classes and finding subreasons, gate decision and enforcement stage are mandatory when applicable. Contextual diagnostics remain `SHOULD`.

## Editorial findings

R5-e01 through R5-e03 are accepted for the amendment batch:

- replace ambiguous adjective use around malformed acceptance-state records;
- make the diagram's acceptance edge conditional on an acceptance-bearing operation;
- state complete-target and registered-region target comparators explicitly.

## Required amendment batch

The governed amendment batch must synchronize at least:

1. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`;
2. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`;
3. `traceability/DPA-500_TRACEABILITY.md`;
4. `diagrams/dpa-500-freshness-gates.mmd`;
5. applicable decision and status surfaces only where the new decision ownership requires it.

The batch must add conformance coverage for:

- post-acceptance base-context evaluation without a live plan;
- conditionally persisted base identity;
- gate-set re-evaluation success and failure;
- governed manual-region evolution;
- unauthorized lifecycle-owned payload change;
- unauthorized partition change;
- attempt-scoped renderer failure without retroactive reclassification.

## Verification and promotion boundary

After the amendment batch:

1. durable Lab gates must pass;
2. a bounded internal consistency audit must verify the adjudicated changes;
3. an independent post-adjudication verification must evaluate the exact amendment ref;
4. only after zero blocking findings may a separate status-only promotion commit move DPA-500 to `review-ready`.

No step in this adjudication establishes Probe success, production implementation, strict-mode activation or main-repository conformance.
