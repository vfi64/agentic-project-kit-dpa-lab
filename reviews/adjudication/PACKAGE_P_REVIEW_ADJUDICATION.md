# Package P Independent Review Adjudication

Status: active

Status-date: 2026-07-19

Reviewed evidence: `reviews/claude/CLAUDE_PACKAGE_P_REVIEW.md`

Reviewed immutable ref: `18d0fd08b27d97aef1b06b5a75079527290ca8e4`

Independent verdict: `ACCEPT_WITH_CHANGES`

Maintainer decision: accept all findings and apply only the bounded corrections recorded below.

## 1. Authority and scope

This adjudication accepts independent review findings as evidentiary input. It does not treat the review as normative architecture, Probe execution, implementation conformance or mutation authority.

No normative DPA specification, accepted ADR, traceability artifact or diagram changes are authorized by this adjudication. No main-repository mutation is authorized. DPA-600 remains frozen and DPA-700 remains unstarted.

## 2. Finding dispositions

| Finding | Decision | Primary class | Disposition | Rereview |
|---|---|---|---|---|
| PPR-M01 | accepted | fixture-or-harness-defect | make P001-C020 rejection unconditional and prohibit inferred defaults | no |
| PPR-M02 | accepted | fixture-or-harness-defect | separate unknown check location from mandatory fail-loud outcome; absent complete stage proof is `PARTIAL`, never `PASS` | no |
| PPR-M03 | accepted | architecture-package coverage defect | add two explicit PROBE-002 cases and fixtures for staged fail-closed new projections and gate-set-change-triggered re-acceptance | limited independent rereview required |
| PPR-m01 | accepted | planning precision defect | relabel `6a9da7d…` as last recorded Discovery baseline and require fresh remote read | no |
| PPR-m02 | accepted | completeness-check defect | require bidirectional case/fixture mapping and explicit case totals in all three Probe packages | no |
| PPR-m03 | accepted | normative-anchor precision defect | qualify renderer secret isolation by the accepted-future bounded-need exception | no |
| PPR-m04 | accepted | cross-Probe evidence-bound defect | state that divergent refs bound or invalidate combined conclusions unless justified and accepted | no |
| PPR-e01 | accepted | editorial | explain why the shared contract remains `draft` before first execution | no |
| PPR-e02 | accepted | editorial | ensure the review request exists at the corrected review ref | no |
| PPR-e03 | accepted | editorial | cite DPA-300 §7 as the lifecycle-order source | no |

## 3. Correction boundaries

The accepted correction set may change only:

- Probe manuals and fixture manifests;
- Probe preparation README/status explanation;
- freeze/adjudication cross-references;
- portability-plan wording;
- review-navigation artifacts;
- project-control and handoff surfaces required to record the new review state.

It MUST NOT:

- change a normative DPA requirement;
- select concrete main-repository serialization, parser, writer, lock, renderer, state, evidence or gate mechanisms;
- materialize executable fixtures;
- execute any Probe;
- release DPA-600;
- begin DPA-700;
- claim main-repository conformance.

## 4. PPR-M03 accepted semantics

Two explicit cases are required:

1. `P002-C059` — in `block-new` and `strict`, a new projection or new acceptance attempt fails closed when mandatory safety cannot be established, while previously accepted legacy content may remain readable according to the declared compatibility stage; compatibility MUST NOT authorize the new mutation or acceptance.
2. `P002-C060` — a gate-set identity change on otherwise unchanged accepted bytes is the trigger that makes gate-set re-acceptance required; the re-acceptance path does not render or mutate target bytes and remains subject to all non-gate context guards.

Matching fixtures:

- `F002-STAGE-BLOCK-NEW-VS-LEGACY`;
- `F002-REACCEPT-GATESET-TRIGGER`.

These additions expand preparation test surface only. They do not assert that the main repository implements either behavior.

## 5. Refreeze and rereview

After all accepted corrections and a successful Lab gate:

1. preserve a new immutable Lab review ref;
2. retain the original review ref and review evidence unchanged as historical evidence;
3. request independent rereview limited to PPR-M03 and synchronization consequences of the two added cases;
4. do not ask the limited reviewer to reopen accepted mechanical findings unless a direct contradiction is discovered.

## 6. Materialization-planning decision

Local executable-fixture materialization planning may begin only after:

- all accepted corrections are present at the new immutable ref;
- the limited PPR-M03 rereview is dispositioned;
- the Maintainer records final Package P closure;
- the current main-repository remote ref is freshly read and locally confirmed.

Probe execution remains prohibited until all freeze, identity, isolation, observation, cleanup and safety preconditions are satisfied.

## 7. Maintainer conclusion

All independent findings are accepted. The review contains no blocker and requires no architecture amendment. Package P remains in correction and limited-rereview state. DPA-600 remains frozen; DPA-700 remains unstarted.
