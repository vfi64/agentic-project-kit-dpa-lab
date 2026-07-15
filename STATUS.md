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

`specs/dpa/DPA-200-DOCUMENT-MODEL.md` is now `draft`.

The initial draft defines:

- manual, full-projection, split-projection, managed-head and hybrid forms;
- complete-target and registered-region identity;
- target semantics and normalization requirements;
- canonical-source, configuration and historical-region authority;
- exclusive write ownership;
- consumer trust states from computed through accepted;
- compatibility for manual documents;
- invalid document-model states;
- DP1 form-selection prerequisites;
- delegated obligations for DPA-300 through DPA-800;
- traceability to stable invariants and accepted ADRs.

No production candidate has been assigned a document form. Region support, concrete schemas, readers, writers, lifecycle paths and consumer gate placement remain `NEEDS_MAIN_REPO_VALIDATION`.

## Next DPA-200 planning steps

1. Audit the draft against every stable `DPA-INV-*` and accepted ADR.
2. Add a document-form decision matrix with explicit allowed and prohibited combinations.
3. Add region-boundary and ownership state diagrams.
4. Extend Phase B traceability with DPA-200 requirements, tests, gates, evidence and rollback.
5. Record unresolved DPA-200 decisions in `DECISIONS.md` only where alternatives change normative meaning.
6. Produce an exact-ref primary review prompt when the draft satisfies its review-ready criteria.

## Phase B restrictions

- No production kit code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No registry-field or module-name claims without exact main-repository evidence.
- No preselection of a production migration form before DP1.
- No DPA-300 detail may bypass DPA-200 authority, ownership or trust-state rules.
- No review finding becomes normative without adjudication.

Phase B may continue. DPA-200 is not yet review-ready.