# Limited Independent Rereview — PPR-M03 (Package P)

Status: complete

Status-date: 2026-07-19

Reviewer/model: Claude Fable 5

Reviewed exact ref: `c12eb19acb07325958e06800f5591aa3bf5f03c7`

Verdict: `ACCEPT_WITH_CHANGES`

## Confirmation

The reviewer confirmed that HEAD was exactly `c12eb19acb07325958e06800f5591aa3bf5f03c7`, completed the required bootstrap, and kept the rereview strictly limited to PPR-M03 and direct synchronization consequences of P002-C059 and P002-C060.

The prompt named `375d3d2aab65531229fd0432cd4bc35bda2c448d` as the corrected ref. The reviewer verified that `probes/PROBE-002-MANUAL.md` and `probes/PROBE-002-FIXTURE-MANIFEST.md` were byte-identical between that ref and the binding reviewed ref `c12eb19…`. DPA-300, DPA-500, ADR-016 and ADR-021 were unchanged from the audited baseline.

## Substantive result

PPR-M03 is substantively resolved.

The rereview confirmed all ten required questions:

1. P002-C059 correctly makes a gate-set identity change on otherwise unchanged accepted bytes the trigger for gate-set re-acceptance.
2. P002-C059 prohibits rendering and target mutation during re-acceptance.
3. P002-C059 remains subject to every non-gate context guard.
4. `F002-REACCEPT-GATESET-TRIGGER` is a sufficient semantic fixture without inventing implementation serialization.
5. P002-C060 correctly makes `block-new` and `strict` fail closed for new projection or acceptance attempts when mandatory safety cannot be established.
6. P002-C060 permits prior accepted legacy content to remain readable only under the declared compatibility stage and never lets compatibility authorize new mutation or acceptance.
7. `F002-STAGE-BLOCK-NEW-VS-LEGACY` is a sufficient semantic fixture without selecting implementation.
8. Manual and manifest contain exactly 60 distinct cases and require bidirectional case/fixture mapping.
9. P002-C059 and P002-C060 remain distinct from P002-C037, P002-C038, P002-C056 and the remaining case set.
10. No normative DPA text changed, no production mechanism was selected, no execution was claimed, and DPA-600/DPA-700 restrictions remain intact.

## Finding

### PPR-M03-RR-e01 — Adjudication record swaps C059 and C060

Severity: `EDITORIAL`

File: `reviews/adjudication/PACKAGE_P_REVIEW_ADJUDICATION.md`, §4.

The adjudication record assigned:

- C059 to block-new/strict fail-closed behavior;
- C060 to gate-set-triggered re-acceptance.

The manual, fixture manifest and rereview prompt consistently assign the opposite and authoritative mapping:

- C059 = gate-set-change-triggered re-acceptance;
- C060 = block-new/strict fail-closed for new attempts while legacy accepted content remains readable only under the declared compatibility stage.

The fixture names in the adjudication record were correct, so the Probe package itself was not affected. The defect was limited to the audit-trail numbering.

Smallest safe correction: swap the two case IDs in §4 of the adjudication record.

Further independent rereview required: no. The correction is a mechanical Maintainer-checkable relabel and does not alter a Probe case, fixture, normative contract or production mechanism.

## Disposition

- PPR-M03 fully resolved on substance: yes.
- Package P may proceed to final Maintainer closure after the editorial record correction: yes.
- Local executable-fixture materialization planning may begin after final closure and fresh current-main confirmation: yes.
- Probe execution remains blocked pending exact-ref freeze, immutable materialized fixtures, isolation, observation, cleanup and safety preconditions.
- DPA-600 remains frozen.
- DPA-700 remains unstarted.

## Method and limitations

Method included exact-ref verification, byte-identity comparison of the two PPR-M03 subject files, normative-anchor comparison, direct case/fixture inspection, 60-case uniqueness and bidirectional-mapping checks, distinctness analysis, reconciliation of manual/manifest/adjudication/prompt numbering, and remote Lab-gate verification.

No main-repository implementation behavior was inspected. No Probe was run. No executable fixture was materialized. No implementation or conformance conclusion is permitted.

Rereview bound to exact ref `c12eb19acb07325958e06800f5591aa3bf5f03c7`.