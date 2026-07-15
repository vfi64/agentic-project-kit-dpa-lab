# DPA-200 Pre-Review Audit

Status: active
Status-date: 2026-07-15
Scope: internal exact-tree consistency audit before external primary review

## 1. Audit scope

This audit checks the current DPA-200 draft, its document-form matrix, traceability and diagrams against stable DPA-000 invariants and accepted decisions. It is not an external review and does not make DPA-200 stable.

Audited artifacts:

- `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
- `specs/dpa/DPA-200-DOCUMENT-FORM-MATRIX.md`
- `traceability/DPA-200_TRACEABILITY.md`
- `diagrams/dpa-200-region-ownership.mmd`
- `diagrams/dpa-200-trust-states.mmd`

## 2. Invariant audit

| Invariant | Result | DPA-200 treatment |
|---|---|---|
| DPA-INV-001 | PASS | Canonical state owns facts; no rendering logic is assigned to it. |
| DPA-INV-002 | PASS | Renderers are never write owners. |
| DPA-INV-003 | PASS | Renderer output is text or bytes only. |
| DPA-INV-004 | PASS | The existing lifecycle owns validation, planning, locking and projected writes. |
| DPA-INV-005 | PASS / DELEGATED | Cross-ref serialization is required and delegated to DPA-600. |
| DPA-INV-006 | PASS | Document forms do not create executable registry plugins. |
| DPA-INV-007 | PASS / DELEGATED | Static renderer resolution is preserved and delegated to DPA-400. |
| DPA-INV-008 | PASS | One contract resolves to one complete target or one registered region. |
| DPA-INV-009 | PASS | No renderer chaining is authorized. |
| DPA-INV-010 | PASS | Evidence and historical prose are excluded from runtime authority by default. |
| DPA-INV-011 | PASS | Runtime contracts remain in the existing main-repository system. |
| DPA-INV-012 | PASS | No parallel registry, lifecycle, evidence, Workspace, freshness or gate system is introduced. |
| DPA-INV-013 | PASS / DELEGATED | Time-only failure remains prohibited and is delegated to DPA-500. |
| DPA-INV-014 | PASS | Automatic historical-prose merge is explicitly prohibited. |
| DPA-INV-015 | PASS / DELEGATED | Dry-run remains required through DPA-300 lifecycle planning. |
| DPA-INV-016 | PASS / DELEGATED | Concrete paths remain Workspace-bound after validation. |
| DPA-INV-017 | PASS | All concrete schema, module, candidate and behavior claims remain `NEEDS_MAIN_REPO_VALIDATION`. |

No invariant contradiction was found.

## 3. ADR audit

| Decision | Result | DPA-200 treatment |
|---|---|---|
| DPA-ADR-001 | PASS | Existing document-management mechanisms are extended, not duplicated. |
| DPA-ADR-002 | PASS | The lab remains planning authority only. |
| DPA-ADR-003 | PASS | Renderer, lifecycle and workflow responsibilities remain separated. |
| DPA-ADR-004 | PASS | Trust and freshness rely on reproducibility, not timestamps. |
| DPA-ADR-005 | PASS / DELEGATED | Static fail-loud renderer resolution is preserved for DPA-400. |
| DPA-ADR-006 | PASS / DELEGATED | Local ownership and cross-ref serialization remain distinct. |
| DPA-ADR-007 | PASS | No new canonical history source is created; form selection follows evidence. |
| DPA-ADR-008 | PASS / DELEGATED | Time-only hard failure remains prohibited. |
| DPA-ADR-009 | PASS | Classification, document status, progress and access outcome remain separated. |
| DPA-ADR-010 | PASS | Stable invariant IDs are referenced without re-owning them. |
| DPA-ADR-011 | PASS | Main-repository claims require exact evidence and later validation. |
| DPA-ADR-012 | PASS | Review artifacts are role-based and exact-ref-bound. |

No accepted-decision contradiction was found.

## 4. Document-model completeness audit

| Area | Result | Note |
|---|---|---|
| Manual documents | PASS | Backwards-compatible behavior is preserved. |
| Full projection | PASS | Complete reproducibility and exclusive lifecycle ownership are required. |
| Split projection | PASS | Current projection and historical material have separate identity or regions. |
| Managed-head projection | PASS WITH EXCEPTION LABEL | Exceptional status, explicit ownership, rollback and serialization are required. |
| Hybrid documents | PASS | Non-overlap and exhaustive byte ownership are required. |
| Target semantics | PASS | Replacement, encoding, normalization, boundaries and fingerprint domain are defined. |
| Registered regions | PASS WITH MAIN-REPO VALIDATION | Abstract contract is complete; actual registry compatibility remains unverified. |
| Consumer trust boundary | PASS | Only accepted output may be represented as accepted repository state. |
| Invalid states | PASS | Ambiguous authority, identity, ownership, input and rollback states fail loud. |
| Form-selection hierarchy | PASS | Full, split, exceptional managed-head, then no migration. |
| Later-spec delegation | PASS | DPA-300 through DPA-800 obligations are explicit. |

## 5. Traceability audit

- Requirements DM-001 through DM-010 have invariant and decision anchors.
- Negative tests cover ambiguous identity, overlapping regions, missing ownership, undeclared inputs, evidence-as-runtime-input, premature trust, automatic history merge and unavailable rollback.
- Gate, evidence and rollback obligations are planned rather than represented as implemented.
- No production candidate is assigned a document form.

Result: PASS for review-ready planning scope.

## 6. Diagram audit

- The ownership diagram preserves lifecycle-only writes for projected targets.
- Manual and historical regions have explicit bounded owners.
- Workflow orchestration authorizes and serializes but does not own semantics.
- Evidence has no runtime-authority edge.
- The trust-state diagram prevents computed, planned and written-unverified bytes from being represented as accepted state.

Result: PASS.

## 7. Open review questions

The external reviewer should focus on:

1. whether `split projection` is sufficiently distinct from the general hybrid form;
2. whether managed-head projection is constrained strongly enough to remain exceptional;
3. whether exhaustive byte ownership is practical and correctly stated for non-content bytes such as delimiters and boundaries;
4. whether `written-unverified` is a useful architectural state or belongs wholly to DPA-300;
5. whether the consumer trust boundary needs additional reader classes;
6. whether the decision matrix contains any permitted combination that can still produce ambiguous authority;
7. whether delegated obligations are placed in the correct later specification.

## 8. Result

Internal pre-review result: **PASS_WITH_EXTERNAL_REVIEW_REQUIRED**.

DPA-200 may advance to an exact-ref primary architecture review. It MUST NOT become `stable` from this audit alone.
