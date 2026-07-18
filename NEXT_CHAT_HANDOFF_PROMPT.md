# Next Chat Handoff Prompt

We are developing the Document Projection Architecture in the private architecture Lab `vfi64/agentic-project-kit-dpa-lab`.

Work only from the current remote repository and documented contracts. Do not work from chat memory.

## Mandatory bootstrap

Read fully and in this order:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `MASTERPLAN.md`
9. `MASTERPLAN_REMOTE_PREPARATION.md`
10. `DECISIONS.md`
11. `ASSUMPTIONS.md`
12. `specs/dpa/README.md`
13. `specs/dpa/DPA-000-VISION.md`
14. `specs/dpa/DPA-100-FOUNDATIONS.md`
15. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
16. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
17. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
18. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`
19. `specs/dpa/DPA-600-CONCURRENCY.md`
20. relevant accepted ADRs
21. relevant traceability and diagrams
22. `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`
23. review and integration contracts relevant to the task
24. this handoff prompt

Do not begin substantive work before completing the bootstrap.

## Authority and evidence

- Current exact-ref main-repository evidence outranks Lab proposals.
- Normative DPA contracts and accepted ADRs outrank planning documents.
- `MASTERPLAN.md` is the canonical execution plan.
- `MASTERPLAN_REMOTE_PREPARATION.md` defines the corrected remote sequence and cannot override the Masterplan.
- The historical Discovery baseline `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` is historical evidence only.
- No repository-specific claim is `VERIFIED` without validation against a current exact main-repository ref.

## Current Lab state

- DPA-000 and DPA-100: `stable`.
- DPA-200 through DPA-500: `review-ready`.
- DPA-400 and DPA-500 remain blocked from `stable` pending applicable Probe evidence and adjudication.
- Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft.
- DPA-600 remains `draft` and is frozen while Package P is active.
- DPA-700 is `planned` and has not started.
- The Lab contains no production kit code and has not been adopted by the main repository.

## Active work package

The active package is **Package P — Remote Probe Preparation**.

Work in this order:

1. shared Probe execution and evidence contract;
2. PROBE-001 manual and fixtures;
3. PROBE-002 manual and fixtures;
4. DPA-400 renderer Probe manual and fixtures;
5. current-ref revalidation, exact Probe-ref freeze and adjudication procedures;
6. CSC and namespace-profile checklist;
7. Probe-independent portability slice specifications.

Only after this package is complete may bounded DPA-600 continuation be reconsidered within the evidence-independent surface.

## DPA-600 freeze

While Package P is active:

- do not materially expand DPA-600;
- do not promote DPA-600 to `review-ready`;
- do not begin DPA-700;
- do not select concrete main-repository lock, workflow, branch-protection, merge-queue, recovery or rollback mechanisms;
- allow only sequencing, status, evidence-boundary and defect-correction edits required for consistency.

## Main-repository mutation freeze

Do not propose or implement quick fixes touching:

- `transfer_repo_actions._refresh_operational_handoff_docs()`;
- any writer of `docs/handoff/CURRENT_HANDOFF.md`;
- Doc Lifecycle Apply content-writing behavior;
- governed writer semantics;
- mutation-plan execution semantics;
- acceptance-state schema or persistence;
- recovery completion semantics;
- gate-set re-acceptance;
- layered acceptance;
- projection freshness or gate integration.

These remain frozen until PROBE-002 execution, adjudication and subsequent architecture revalidation.

## Merge discipline

Governed batches whose assurance depends on commit sequence MUST NOT be squash-merged. Record source commit SHAs, review refs and selected merge method durably. Retain `spec/dpa-500-freshness-gates` until its governed sequence is preserved outside the branch.

## Immediate task

Continue Package P from the current branch state.

First inspect `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md` for consistency with DPA-300 through DPA-500. Then prepare `probes/PROBE-001-MANUAL.md` and its fixture/case manifest. Synchronize status and planning surfaces only where required. Run the read-only Lab gates after each coherent slice.

Do not claim Probe execution, implementation, adoption or main-repository conformance.