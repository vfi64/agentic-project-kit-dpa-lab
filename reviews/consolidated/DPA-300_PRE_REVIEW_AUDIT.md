# DPA-300 Pre-Review Audit

Status: complete

Audit date: 2026-07-15

Audited branch: `spec/dpa-300-registry-lifecycle`

Audited artifacts:

- `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
- `traceability/DPA-300_TRACEABILITY.md`
- `diagrams/dpa-300-registry-lifecycle.mmd`
- `diagrams/dpa-300-command-integration.mmd`
- `diagrams/dpa-300-plan-state.mmd`
- DISC-001 through DISC-010 records
- `ASSUMPTIONS.md`
- `MAIN_REPOSITORY_CONTEXT.md`
- `integration/DP1_PROBE_BACKLOG.md`

## 1. Result

Overall result: `PASS_WITH_REVIEW_QUESTIONS`

- foundational contradiction: none found;
- hidden parallel registry or lifecycle: none found;
- new runtime authority: none found;
- false implementation claim: none found;
- premature production-form selection: none found;
- fresh main-repository evidence required before external review: no;
- external architecture review required before `review-ready`: yes.

## 2. Contract ownership audit

- Registry representation and validation: owned by DPA-300 and explicitly constrained to the existing registry.
- Renderer purity and static implementation: delegated to DPA-400.
- Gate severity and acceptance: delegated to DPA-500.
- Cross-branch and cross-PR serialization: delegated to DPA-600.
- Migration and rollback policy: delegated to DPA-700.
- Implementation sequencing and exact mapping: delegated to DPA-800.

No companion artifact is presented as a second normative owner. Traceability and diagrams are derived views.

## 3. Invariant audit

| Invariant | Result | DPA-300 treatment |
|---|---|---|
| DPA-INV-001 canonical state has no render logic | PASS | canonical sources are inputs; renderer selection remains registry contract |
| DPA-INV-002 renderers have no write logic | PASS | renderer returns bytes only; lifecycle is sole writer |
| DPA-INV-003 renderers return text/bytes only | PASS | explicit in §§4, 7 and command diagram |
| DPA-INV-004 lifecycle validates, plans, locks and writes | PASS | complete ordered lifecycle in §7 |
| DPA-INV-005 workflows serialize cross-ref work | PASS/DELEGATED | DPA-300 preserves workflow role; DPA-600 owns complete contract |
| DPA-INV-006 registry is declarative, not arbitrary plugins | PASS | executable paths and dynamic expressions prohibited |
| DPA-INV-007 renderer identifiers resolve statically | PASS/DELEGATED | required here, complete mapping in DPA-400 |
| DPA-INV-008 one invocation computes one target | PASS | one registered target per render/plan |
| DPA-INV-009 no renderer chaining | PASS/DELEGATED | not authorized; complete enforcement in DPA-400 |
| DPA-INV-010 evidence is not runtime authority | PASS | evidence excluded from semantic authority and source use |
| DPA-INV-011 runtime contracts live in existing main-repo system | PASS | existing registry/lifecycle only |
| DPA-INV-012 no parallel subsystem | PASS | explicit non-goal and command-adaptation requirement |
| DPA-INV-013 time alone cannot hard-fail | PASS | timestamp is evidence only |
| DPA-INV-014 no automatic historical prose merge | PASS | stale recovery regenerates; preservation is byte-level only |
| DPA-INV-015 mutation defaults dry-run | PASS | exact plan binding required for execution |
| DPA-INV-016 paths resolve through Workspace | PASS | existing Workspace required; concrete mapping remains Probe |
| DPA-INV-017 repo claims remain exact-ref bounded | PASS | all observed command/module claims bound to `6a9da7d…` |

## 4. Decision audit

- ADR-001: PASS — extension of existing stack only.
- ADR-002: PASS — lab evidence is non-authoritative.
- ADR-003: PASS — registry/renderer/lifecycle/workflow boundaries preserved.
- ADR-004: PASS — derivational fingerprints and drift invalidate plans.
- ADR-005: PASS — static renderer ID and fail-loud unknown values.
- ADR-006: PASS — local lock distinguished from cross-ref serialization.
- ADR-007: PASS — no new canonical history and no prose merge.
- ADR-008: PASS — no time-only hard failure.
- ADR-009: PASS — no undeclared status vocabulary introduced.
- ADR-010: PASS — canonical invariant IDs referenced without regrouping.
- ADR-011: PASS — exact-ref evidence claims remain bounded.
- ADR-012: PASS — review baseline and role prompt planned.
- ADR-013: PASS — lifecycle owns partition bytes; renderer payload excludes boundaries.
- ADR-014: PASS — lifecycle cannot assign `accepted`.
- ADR-015: PASS — Discovery informs the contract; Probe remains later.

## 5. Discovery evidence audit

The DPA-300 contract uses Discovery only for observed constraints:

- document-wide registry and parser baseline;
- dry-run lifecycle structures and missing projection writer;
- Workspace and reentrant local mutation lock;
- existing `admin-refresh-pr` mutation path;
- existing bounded block replacement helper not used by active append path;
- current CI shape;
- Git-backed prior target history.

It does not claim that these mechanisms conform to DPA-300. Compatibility remains in PROBE-001, PROBE-002, PROBE-003 and PROBE-005.

## 6. Command integration audit

The contract correctly requires adaptation of the existing command path rather than creation of a parallel DPA command.

The `CURRENT_HANDOFF.md` clause is conditional: it applies only if later Assessment selects that document as a projection target. No full, hybrid or managed-head form is selected.

## 7. Failure-mode audit

Covered:

- malformed registry contract;
- unknown renderer;
- missing authority input;
- ambiguous target;
- overlapping/unowned regions;
- stale plans across all fingerprint families;
- lock failure;
- renderer or workflow write bypass;
- in-place partial region writes;
- changed preserved bytes;
- post-write verification failure;
- evidence-writing failure;
- direct acceptance bypass;
- time-only hard failure;
- append-based accumulation after governed replacement adoption.

Delegated rather than omitted:

- exact finding severity and staged enforcement → DPA-500;
- cross-PR race mechanism → DPA-600;
- rollback execution mechanics → DPA-700;
- concrete module/CLI patching → DPA-800.

## 8. Review questions

The external reviewer should decide whether the following require normative amendments:

1. Is the lifecycle phase order correct when `Render` occurs before immutable `Plan`, or should the renderer invocation itself be represented as part of planning?
2. Is requiring complete planned target bytes in the mutation plan too strong for large targets, or is a payload plus deterministic reconstruction sufficient?
3. Is same-process lock reentrancy sufficiently bounded by the top-level-owner rule, or should DPA-300 prohibit nested lock acquisition entirely?
4. Does evidence-writing failure after a verified write require a distinct trust state, or is `written-unverified` plus an explicit finding sufficient?
5. Is direct-write detection based on later recomputation adequate as the minimum contract, or must DPA-300 require a stored accepted-output fingerprint in the registry/lifecycle state?
6. Does the command-adaptation requirement overconstrain future refactoring by preserving an exact CLI entry point, or correctly preserve the user-facing contract while allowing internal replacement?
7. Should partition fingerprints be part of the target fingerprint or remain a separately addressable guard as specified?

## 9. Required next action

1. update STATUS and ROADMAP to mark DPA-300 draft and review preparation active;
2. create a commit-ref-bound Claude primary architecture review prompt;
3. obtain the review without repository writes;
4. commit the review under `reviews/claude/`;
5. perform secondary technical verification and maintainer adjudication before normative changes.

DPA-300 is suitable for an external primary architecture review. It is not yet `review-ready`.