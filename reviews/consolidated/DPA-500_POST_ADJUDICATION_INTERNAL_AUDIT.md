# DPA-500 Post-Adjudication Internal Audit

Status: complete

Status-date: 2026-07-17

## Scope

This audit evaluates the governed DPA-500 amendment batch after Maintainer adjudication of the primary architecture review.

Audited artifacts:

- `specs/dpa/DPA-100-FOUNDATIONS.md`;
- `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`;
- `specs/dpa/DPA-400-RENDERER-CONTRACT.md`;
- `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`;
- `decisions/DPA-ADR-021-FRESHNESS-REACCEPTANCE-AND-LAYERED-ACCEPTANCE.md`;
- `traceability/DPA-500_TRACEABILITY.md`;
- `diagrams/dpa-500-freshness-gates.mmd`;
- `reviews/claude/CLAUDE_DPA_500_PRIMARY_REVIEW.md`;
- `reviews/consolidated/DPA-500_PRIMARY_REVIEW_ADJUDICATION.md`;
- `STATUS.md`.

The audit does not inspect or claim current main-repository implementation behavior.

## Result

**PASS**

No unresolved blocking contradiction was found in the adjudicated amendment scope. DPA-500 remains `draft`; this result authorizes independent post-adjudication verification, not promotion.

## Major-finding closure

### R5-M01 — Base-context evaluability

Closed.

- DPA-500 §5 scopes base context to the governing plan or requested operation.
- DPA-500 §8 persists accepted base identity only for declared base dependence.
- DPA-300 §12.1 applies the same conditional persistence rule.
- Base-independent accepted state remains evaluable after attempt-plan cleanup.
- Traceability FG-013 and conformance tests cover base-independent and base-dependent cases.

No live accepted-plan dependency remains in ordinary base-independent post-acceptance evaluation.

### R5-M02 — Gate-set re-acceptance

Closed.

- DPA-500 §15.6 defines lifecycle-owned gate-set re-evaluation without renderer invocation or target mutation.
- Eligibility requires every non-gate-set dimension to be `fresh`.
- Gate `pass` permits only acceptance-state and bounded-evidence update through existing authority.
- Gate `warning` or `failure` preserves target bytes and prior acceptance state.
- The operation reuses the existing lifecycle, Workspace, lock policy, state writer and gate authority.
- Traceability FG-014 and conformance tests cover pass, non-pass and no-render/no-write behavior.

No second acceptance authority or policy-change regeneration requirement remains.

### R5-M03 — Layered acceptance

Closed.

- ADR-021 records the Maintainer choice of layered acceptance.
- DPA-300 §12.2 distinguishes complete-target projections from registered-region projections.
- DPA-500 §§5, 8, 10 and 17 apply the same ownership-aware comparison model.
- Lifecycle-owned payload changes remain `target drift`.
- Lifecycle-owned partition or boundary changes remain `partition drift`.
- Ownership-declaration changes remain `ownership drift`.
- Governed non-lifecycle-owner region evolution does not by itself create projection drift or staleness.
- Complete-target and preserved-region fingerprints remain mandatory plan, write, verification and recovery guards.
- Ambiguous ownership fails closed.
- Traceability FG-015 and conformance tests distinguish authorized owner evolution, out-of-band payload mutation, partition mutation and ambiguous ownership.

The amendment preserves mutation safety while removing the false-positive post-acceptance classification identified by the review.

## Minor-finding closure

### R5-m01 — Attempt scope

Closed. DPA-500 §6 states that a failed renderer attempt does not reclassify previously accepted bytes. Renderer consequences in §16 are explicitly scoped to the active attempt. FG-016 traces the rule.

### R5-m02 — Configuration mapping

Closed. DPA-500 §10 maps output-affecting configuration change deterministically to `contract drift`. The prior source/contract disjunction is removed.

### R5-m03 — Invariant anchors

Closed. Every DPA-500 traceability row was re-derived from DPA-000 §7. New rows cover base context, re-acceptance, layered acceptance and attempt scope. The traceability file remains non-normative.

### R5-m04 — Evidence field strength

Closed. DPA-500 §19 separates identity-critical `MUST` fields from contextual `SHOULD` fields, consistent with DPA-300 §14.

## Editorial closure

- Acceptance-state defects use `malformed or unusable` where token adjacency could confuse the `invalid` freshness classification.
- The diagram limits acceptance-state update to acceptance-bearing operations and records that read-only pass does not update state.
- Complete-target versus registered-region target comparators are explicit in normative text and diagram.

## Vocabulary and dimensional separation

PASS.

The following dimensions remain separate:

1. freshness classification: `fresh`, `stale`, `invalid`, `indeterminate`;
2. consumer trust state: DPA-100 closed vocabulary;
3. drift class: DPA-100 seven-class vocabulary;
4. finding subreason;
5. lifecycle attempt outcome;
6. gate decision: `pass`, `warning`, `failure`;
7. enforcement stage: `observe`, `warn`, `block-new`, `strict`;
8. severity and user-facing wording delegated to the main-repository finding system.

The stage token `warn` is not reused as gate `warning`. No new trust-state or drift token is introduced.

## Authority and parallel-system audit

PASS.

The amendment creates no second registry, lifecycle, freshness engine, finding taxonomy, gate runner, acceptance store, Workspace abstraction or runtime authority.

Re-acceptance is explicitly lifecycle-owned. Renderer authority remains unchanged. Evidence remains non-authoritative. Production strict activation remains outside lab authority.

## DPA-300 synchronization audit

PASS.

DPA-300 and DPA-500 agree on:

- conditional accepted-base persistence;
- attempt-scoped plan base capture;
- complete-target comparison for complete-target projections;
- lifecycle-owned payload comparison for registered-region projections;
- partition and ownership drift;
- complete-target and preserved-region fingerprints as mutation and recovery guards;
- governed non-lifecycle-owner evolution not being projection target drift;
- fail-closed ambiguous ownership;
- DPA-500 ownership of acceptance, including gate-set re-acceptance.

The DPA-300 status remains `review-ready`; the bounded ADR-021 amendment is included in the required independent DPA-500 verification scope.

## Renderer integration audit

PASS.

DPA-500 preserves DPA-400 distinctions among renderer identifier, interface version, semantic version and implementation evidence. Nondeterminism and prohibited capabilities fail the active attempt without overwriting the classification of prior accepted bytes. Operational aborts remain non-semantic and non-accepted.

## Recovery and persistence audit

PASS at architecture-contract level.

- `written-unverified` never implies acceptance.
- Acceptance state cannot be reconstructed from bytes or evidence alone.
- Failed re-acceptance cannot fabricate a new gate-set identity.
- Exact persistence order, lock integration and recovery representation remain `NEEDS_MAIN_REPO_VALIDATION`.

## Evidence and main-repository boundary

PASS.

Identity-critical gate evidence is mandatory. Repository-specific schemas, commands, finding identifiers, severity mappings, provenance representation, locking details, persistence order and CI integration remain fenced as `NEEDS_MAIN_REPO_VALIDATION`.

No implementation, Probe-success, adoption or main-repository-conformance claim was found.

## Diagram and traceability synchronization

PASS.

The diagram shows:

- operation-scoped base context;
- separate lifecycle-owned payload and partition inputs;
- complete-target and preserved-region guard roles;
- layered-acceptance note;
- mutation-free re-acceptance;
- read-only pass without state update;
- renderer authority prohibition.

Traceability includes direct rows and tests for every primary-review finding and remains subordinate to normative specifications and accepted decisions.

## Remaining obligations

Before any DPA-500 `review-ready` promotion:

1. freeze this amendment batch at an exact immutable ref;
2. obtain independent post-adjudication verification of the exact ref;
3. disposition every verification finding;
4. require a zero-blocker verification outcome;
5. perform any promotion as a separate status-only commit.

Before `stable`, applicable exact-ref Probes must validate finding mappings, conditional base persistence, ownership provenance, layered comparison, re-acceptance, locking, persistence order, recovery and staged strict adoption.

## Promotion boundary

This audit does not promote DPA-500 and does not establish production implementation, Probe success or main-repository conformance.
