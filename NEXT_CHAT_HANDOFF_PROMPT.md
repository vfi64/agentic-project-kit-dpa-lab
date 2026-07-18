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
20. relevant accepted ADRs, especially ADR-016, ADR-017, ADR-019, ADR-020 and ADR-021
21. relevant traceability and diagrams
22. `probes/README.md`
23. `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`
24. `probes/PROBE-001-MANUAL.md`
25. `probes/PROBE-001-FIXTURE-MANIFEST.md`
26. `probes/PROBE-001-INTERNAL-CONTRACT-AUDIT.md`
27. `probes/PROBE-002-MANUAL.md`
28. `probes/PROBE-002-FIXTURE-MANIFEST.md`
29. `probes/PROBE-002-INTERNAL-CONTRACT-AUDIT.md`
30. `probes/DPA-400-RENDERER-PROBE-MANUAL.md`
31. `probes/DPA-400-RENDERER-FIXTURE-MANIFEST.md`
32. `probes/DPA-400-RENDERER-INTERNAL-CONTRACT-AUDIT.md`
33. `probes/EXACT_REF_FREEZE_PROCEDURE.md`
34. `probes/EVIDENCE_CAPTURE_PROCEDURE.md`
35. `probes/PROBE_ADJUDICATION_PROCEDURE.md`
36. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
37. `integration/PORTABILITY_SLICE_PLAN.md`
38. `reviews/PACKAGE_P_INTERNAL_CONSISTENCY_AUDIT.md`
39. this handoff prompt

Do not begin substantive work before completing the bootstrap.

## Authority and evidence

- Current exact-ref main-repository evidence outranks Lab proposals.
- Normative DPA contracts and accepted ADRs outrank planning documents.
- `MASTERPLAN.md` is the canonical execution plan.
- `MASTERPLAN_REMOTE_PREPARATION.md` defines the corrected remote sequence and cannot override the Masterplan.
- The currently observed remote main-repository head is `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`; local equality and cleanliness remain unconfirmed until Mac execution.
- No repository-specific claim is `VERIFIED` without current exact-ref inspection and required local confirmation.

## Current Lab state

- DPA-000 and DPA-100: `stable`.
- DPA-200 through DPA-500: `review-ready`.
- DPA-400 and DPA-500 remain blocked from `stable` pending applicable Probe evidence and adjudication.
- Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft.
- DPA-600 remains `draft` and frozen.
- DPA-700 is `planned` and has not started.
- The Lab contains no production kit code and has not been adopted by the main repository.

## Package P state

Package P — Remote Probe Preparation is internally prepared and awaiting bounded independent verification.

Prepared artifacts:

1. shared Probe execution and evidence contract;
2. PROBE-001 manual and fixture manifest;
3. PROBE-001 internal audit: `PASS_AFTER_CORRECTION`;
4. PROBE-002 manual and fixture manifest;
5. PROBE-002 internal audit: `PASS_AFTER_CORRECTION`;
6. DPA-400 renderer Probe manual and fixture manifest;
7. renderer internal audit: `PASS_AFTER_CORRECTION`;
8. exact-ref freeze procedure;
9. evidence-capture procedure;
10. Maintainer adjudication procedure;
11. canonical CSC, namespace-profile and external-habitability checklist;
12. Probe-independent portability slice plan;
13. closed Package-P internal consistency audit.

No executable fixtures have been materialized. No Probe has run. No implementation or main-repository conformance is claimed.

## Current immediate task

1. read the immutable Package-P review ref recorded in `reviews/PACKAGE_P_REVIEW_REQUEST.md`;
2. perform bounded independent verification of Package P against the listed normative contracts;
3. classify findings as blocker, major, minor or editorial;
4. do not edit the immutable review ref;
5. record whether Package P is `ACCEPT`, `ACCEPT_WITH_CHANGES` or `REJECT`;
6. after Maintainer adjudication, correct only accepted findings on the working branch;
7. do not continue DPA-600 until Package-P review and adjudication are complete.

## DPA-600 and main-repository mutation freeze

Until Package-P review and Maintainer adjudication release the next step:

- do not materially expand or promote DPA-600;
- do not begin DPA-700;
- do not select concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanisms;
- do not implement quick fixes to handoff writers, Doc Lifecycle Apply, writer semantics, immutable-plan execution, acceptance state, recovery, re-acceptance, layered acceptance, freshness or gate integration;
- do not represent portability candidates as verified without exact source inspection.

## Merge discipline

Governed batches whose assurance depends on commit sequence MUST NOT be squash-merged. Preserve source commit SHAs, review refs and the selected merge method durably.

Do not claim Probe execution, implementation, adoption or main-repository conformance.
