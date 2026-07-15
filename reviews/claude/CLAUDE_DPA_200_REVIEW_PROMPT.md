# Claude Primary Architecture Review Prompt — DPA-200 Document Model

You are performing the primary architecture review of DPA-200 for the Document Projection Architecture laboratory.

You have READ-ONLY access.

Do not modify files.
Do not create commits or patches.
Do not propose production implementation code.
Your output is one review document only.

## Repository and exact reviewed ref

Repository:

`vfi64/agentic-project-kit-dpa-lab`

Review exactly this immutable commit:

`44a87127fca7f482bc2991f0c258af0a386a7048`

Branch at prompt creation:

`spec/dpa-200-document-model`

Do not review a newer branch tip. Clone or fetch the repository and check out the exact commit before reading files.

## Mandatory bootstrap

Read completely and in this order:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `DECISIONS.md`
9. `ASSUMPTIONS.md`
10. `specs/dpa/README.md`
11. `specs/dpa/DPA-000-VISION.md`
12. `specs/dpa/DPA-100-FOUNDATIONS.md`
13. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
14. `specs/dpa/DPA-200-DOCUMENT-FORM-MATRIX.md`
15. `traceability/PHASE_A_TRACEABILITY.md`
16. `traceability/DPA-200_TRACEABILITY.md`
17. `diagrams/architecture.mmd`
18. `diagrams/dpa-200-region-ownership.mmd`
19. `diagrams/dpa-200-trust-states.mmd`
20. `reviews/consolidated/PHASE_A_ADJUDICATION.md`
21. `reviews/consolidated/DPA-200_PRE_REVIEW_AUDIT.md`
22. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
23. `integration/IMPORT_PLAN.md`

The pre-review audit is non-normative. Verify it rather than trusting it.

## Authority order

Use this authority order:

1. exact evidence from the real main repository at a concrete Git ref;
2. `MAIN_REPOSITORY_CONTEXT.md` for its recorded baseline only;
3. `LAB_EXECUTION_CONTRACT.md`;
4. accepted decisions in `DECISIONS.md`;
5. stable DPA-000 and DPA-100;
6. draft DPA-200 and its owned matrix;
7. consolidated reviews and audits;
8. individual reviews;
9. assumptions and proposals;
10. model memory.

Model memory is never authoritative.

Do not invent current main-repository facts. Concrete registry fields, modules, candidate documents, readers, writers and implementation behavior remain `NEEDS_MAIN_REPO_VALIDATION` unless exact evidence exists.

## Review objective

Independently determine whether DPA-200 is internally coherent and eligible to become `review-ready`.

Audit in particular:

- document-form taxonomy;
- distinction between split projection and hybrid document;
- full-projection completeness requirements;
- managed-head exceptional constraints;
- complete-target and registered-region identity;
- boundary representation and malformed-boundary behavior;
- exhaustive, non-overlapping byte ownership;
- canonical source, configuration, evidence and historical-region authority;
- write-owner exclusivity;
- target semantics and normalization;
- consumer trust states and accepted-state boundary;
- backwards compatibility for manual documents;
- invalid-state coverage;
- DP1 form-selection hierarchy;
- delegation to DPA-300 through DPA-800;
- invariant and ADR conformance;
- test, gate, evidence and rollback traceability;
- hidden parallel systems or new runtime authority;
- false implementation or validation claims.

Do not optimize for agreement with the internal pre-review audit.

## Required output

Produce one Markdown document with exactly these sections:

1. Review metadata
2. Executive assessment
3. Blocking findings
4. Major findings
5. Minor findings
6. Editorial findings
7. Document-form taxonomy audit
8. Region identity and boundary audit
9. Authority and write-ownership audit
10. Target-semantics audit
11. Consumer trust-boundary audit
12. Invariant-by-invariant audit
13. Decision audit
14. Traceability audit
15. Failure-mode audit
16. Main-repository validation audit
17. Accepted findings
18. Rejected alternatives
19. Unresolved questions
20. Recommended adjudication order
21. DPA-200 review-ready assessment
22. Final verdict

For every finding include:

- stable finding ID;
- severity;
- exact file and section;
- analysis;
- weakened or violated contract;
- proposed disposition;
- affected later specifications;
- whether main-repository validation is required;
- whether a maintainer decision is required.

The final verdict must be exactly one of:

- `ACCEPT`
- `ACCEPT_WITH_CHANGES`
- `MAJOR_REWORK`
- `REJECT`

Also state separately whether DPA-200 may advance to `review-ready` after adjudication.

## Constraints

- No repository writes.
- No production implementation.
- No `.agentic/` state.
- No assumed region support in the real registry.
- No production-document form selection.
- No model agreement treated as evidence.
- Review prose remains non-normative until maintainer adjudication.

Return the complete review in English, suitable for storage under `reviews/claude/`.
