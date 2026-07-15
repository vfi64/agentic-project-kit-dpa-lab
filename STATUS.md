# Status

Status: active
Status-date: 2026-07-15
Superseded-by: n/a

## Current

Phase A — Foundation is closed on `main` at commit `a1b81beaf8f8a065d8a869d15bbf39d0e6459aae`.

Phase B — Core document-management integration is active on branch `spec/dpa-200-document-model`.

The lab remains non-authoritative for the runtime state of `vfi64/agentic-project-kit`, contains no production kit code and has not been adopted with the kit.

## Completed Phase A work

- DPA-000 and DPA-100 are stable.
- Claude primary architecture review is complete.
- ChatGPT secondary technical verification is complete.
- Maintainer adjudication is complete.
- DPA-ADR-009 through DPA-ADR-012 are accepted.
- Canonical invariants `DPA-INV-001` through `DPA-INV-017` are stable.
- Closed vocabulary, phase governance, review roles and minimal baseline evidence are synchronized.
- Phase A traceability and final consistency review are complete.

## Active DPA-200 work

`specs/dpa/DPA-200-DOCUMENT-MODEL.md` remains `draft` and owns the normative document model.

Completed DPA-200 planning artifacts:

- initial full document-model draft;
- `specs/dpa/DPA-200-DOCUMENT-FORM-MATRIX.md` with permitted, conditional, exceptional and prohibited form combinations;
- `traceability/DPA-200_TRACEABILITY.md` with requirement IDs DM-001 through DM-010;
- explicit form-to-test, gate, evidence and rollback mapping;
- explicit negative-test obligations for invalid authority, ownership, boundary, trust and rollback states.

The current model defines:

- manual, full-projection, split-projection, managed-head and hybrid forms;
- complete-target and registered-region identity;
- target semantics and normalization requirements;
- canonical-source, configuration and historical-region authority;
- exclusive byte-range and region write ownership;
- consumer trust states from computed through accepted;
- compatibility for manual documents;
- invalid document-model states;
- DP1 form-selection prerequisites;
- delegated obligations for DPA-300 through DPA-800;
- traceability to stable invariants and accepted ADRs.

No production candidate has been assigned a document form. Region support, concrete schemas, readers, writers, lifecycle paths, gate placement and rollback sources remain `NEEDS_MAIN_REPO_VALIDATION`.

## Next DPA-200 planning steps

1. Add region-boundary and ownership state diagrams.
2. Audit DPA-200 and its matrix against every stable `DPA-INV-*` and accepted ADR.
3. Decide whether any unresolved alternative requires a new ADR; do not create one for purely delegated implementation detail.
4. Harmonize the matrix terminology back into the owning DPA-200 text before review-ready promotion.
5. Produce one exact-ref primary architecture review prompt for DPA-200 and its traceability artifacts.
6. Adjudicate review findings before changing normative meaning.

## DPA-200 review-readiness tracking

| Criterion | Progress |
|---|---|
| Complete document-form definitions | complete |
| Authority and write ownership rules | complete |
| Target semantics and invalidity rules | complete |
| Consumer trust boundary | complete |
| Decision matrix | complete |
| Tests, gates, evidence and rollback traceability | complete for initial draft |
| Region-boundary diagrams | pending |
| Full invariant and ADR audit | pending |
| Exact-ref primary review baseline | pending |

## Phase B restrictions

- No production kit code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No registry-field or module-name claims without exact main-repository evidence.
- No preselection of a production migration form before DP1.
- No DPA-300 detail may bypass DPA-200 authority, ownership or trust-state rules.
- No review finding becomes normative without adjudication.

Phase B may continue. DPA-200 is not yet review-ready.
