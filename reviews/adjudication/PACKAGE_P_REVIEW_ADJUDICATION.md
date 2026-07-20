# Package P Independent Review Adjudication

Status: complete

Status-date: 2026-07-19

Reviewed evidence:

- `reviews/claude/CLAUDE_PACKAGE_P_REVIEW.md`
- `reviews/claude/CLAUDE_PACKAGE_P_PPR_M03_REREVIEW.md`

Original reviewed immutable ref: `18d0fd08b27d97aef1b06b5a75079527290ca8e4`

Limited rereview ref: `c12eb19acb07325958e06800f5591aa3bf5f03c7`

Independent primary verdict: `ACCEPT_WITH_CHANGES`

Limited rereview verdict: `ACCEPT_WITH_CHANGES` with one editorial record correction

Maintainer decision: accept all primary-review findings and the limited-rereview editorial finding; apply only the bounded corrections recorded below.

## 1. Authority and scope

This adjudication accepts independent review findings as evidentiary input. It does not treat either review as normative architecture, Probe execution, implementation conformance or mutation authority.

No normative DPA specification, accepted ADR, traceability artifact or diagram change is authorized by this adjudication. No main-repository mutation is authorized. DPA-600 remains frozen and DPA-700 remains unstarted.

## 2. Primary-review finding dispositions

| Finding | Decision | Primary class | Disposition | Rereview |
|---|---|---|---|---|
| PPR-M01 | accepted | fixture-or-harness-defect | make P001-C020 rejection unconditional and prohibit inferred defaults | no |
| PPR-M02 | accepted | fixture-or-harness-defect | separate unknown check location from mandatory fail-loud outcome; absent complete stage proof is `PARTIAL`, never `PASS` | no |
| PPR-M03 | accepted | architecture-package coverage defect | add two explicit PROBE-002 cases and fixtures for staged fail-closed new projections and gate-set-change-triggered re-acceptance | limited independent rereview completed |
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
- project-control and handoff surfaces required to record the review state.

It MUST NOT:

- change a normative DPA requirement;
- select concrete main-repository serialization, parser, writer, lock, renderer, state, evidence or gate mechanisms;
- materialize executable fixtures;
- execute any Probe;
- release DPA-600;
- begin DPA-700;
- claim main-repository conformance.

## 4. PPR-M03 accepted semantics

Two explicit cases are required and are now present:

1. `P002-C059` — a gate-set identity change on otherwise unchanged accepted bytes is the trigger that makes gate-set re-acceptance required; the re-acceptance path does not render or mutate target bytes and remains subject to all non-gate context guards.
2. `P002-C060` — in `block-new` and `strict`, a new projection or new acceptance attempt fails closed when mandatory safety cannot be established, while previously accepted legacy content may remain readable according to the declared compatibility stage; compatibility MUST NOT authorize the new mutation or acceptance.

Matching fixtures:

- `F002-REACCEPT-GATESET-TRIGGER` for P002-C059;
- `F002-STAGE-BLOCK-NEW-VS-LEGACY` for P002-C060.

These additions expand preparation test surface only. They do not assert that the main repository implements either behavior.

## 5. Limited rereview disposition

The limited independent rereview confirmed that PPR-M03 is substantively resolved and that all ten requested checks pass.

It found one editorial synchronization defect:

| Finding | Decision | Class | Disposition | Further rereview |
|---|---|---|---|---|
| PPR-M03-RR-e01 | accepted and corrected | editorial | correct the transposed C059/C060 labels in this adjudication record | no |

The correction above is the complete disposition. It changes no Probe artifact, fixture, normative contract or mechanism.

## 6. Refreeze and review history

The following immutable refs remain preserved as historical evidence:

- original Package-P review ref: `18d0fd08b27d97aef1b06b5a75079527290ca8e4`;
- corrected limited-rereview ref: `c12eb19acb07325958e06800f5591aa3bf5f03c7`.

The final closure ref MUST include this corrected adjudication and the limited-rereview report. No further independent rereview is required for PPR-M03-RR-e01.

## 7. Materialization-planning decision

After final Package-P closure and a fresh read plus local confirmation of the current main-repository ref, local executable-fixture materialization planning MAY begin.

This permits planning only. Materialized executable fixtures still require exact current mappings, immutable revisions and hashes, safe isolation, observation hooks and verified cleanup.

Probe execution remains prohibited until all freeze, identity, isolation, observation, cleanup and safety preconditions are satisfied.

## 8. Maintainer conclusion

All primary-review and limited-rereview findings are accepted and corrected. There is no blocker and no required architecture amendment. PPR-M03 is fully resolved. Package P is ready for final Maintainer closure on a new green immutable ref.

DPA-600 remains frozen. DPA-700 remains unstarted.