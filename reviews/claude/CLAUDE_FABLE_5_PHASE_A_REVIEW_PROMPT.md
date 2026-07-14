# Claude Fable 5 Review Prompt — Phase A Foundation Baseline

Status: active
Status-date: 2026-07-14
Review-baseline: `7dd2629d7aab1d9166b02bb5a2b19cf180d6e382`
Repository: `vfi64/agentic-project-kit-dpa-lab`

## Prompt

You are reviewing the Phase A foundation baseline of the private architecture laboratory `vfi64/agentic-project-kit-dpa-lab`.

Review exactly commit:

`7dd2629d7aab1d9166b02bb5a2b19cf180d6e382`

Do not review an unpinned branch tip. Do not infer current `vfi64/agentic-project-kit` behavior from memory or model knowledge.

Read completely, in this order:

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
13. `traceability/PHASE_A_TRACEABILITY.md`
14. `reviews/README.md`
15. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
16. `integration/IMPORT_PLAN.md`

The lab is non-authoritative for runtime facts. The recorded main-repository baseline is contextual evidence only. Any concrete claim about current main-repository modules, schemas, fields, readers, writers, checks, gates or behavior must remain `NEEDS_MAIN_REPO_VALIDATION` unless exact-ref evidence is present.

Evaluate the baseline against these binding invariants:

- canonical state owns no rendering logic;
- renderers own no write logic and return only text or bytes;
- lifecycle validates, plans, locally locks and writes;
- workflow orchestration serializes across branches and pull requests;
- registry describes bounded contracts, not arbitrary plugins;
- renderer resolution is static and fail-loud;
- one renderer computes one registered target and triggers no renderer;
- evidence is never runtime authority;
- no parallel registry, lifecycle, freshness, evidence, Workspace or gate system;
- no new canonical history source merely for migration convenience;
- no automatic historical-prose merge on drift;
- time alone never causes a hard failure.

Review questions:

1. Are DPA-000 and DPA-100 internally coherent and RFC-like?
2. Are all authority terms precise enough to prevent a projection from silently becoming canonical state?
3. Is the renderer/lifecycle/workflow responsibility split complete and non-overlapping?
4. Does any wording imply a second governance or document-management subsystem?
5. Are freshness, drift and time semantics sufficiently separated for later DPA-500 work?
6. Are local locks and cross-PR serialization clearly distinguished?
7. Does the migration decision hierarchy avoid inventing canonical history?
8. Are repository-specific claims classified correctly?
9. Does the Phase A traceability table distinguish normative design, planned implementation and verified implementation?
10. Which ambiguities would block DPA-200 through DPA-500?
11. Which findings require a maintainer decision rather than editorial correction?
12. Which proposed changes would violate an earlier invariant and therefore must be rejected?

Return one Markdown review document with exactly these sections:

1. `Review metadata`
   - repository
   - reviewed commit
   - model/version
   - reviewed files
2. `Executive assessment`
   - `PASS`, `PASS_WITH_CHANGES`, or `BLOCK`
   - concise rationale
3. `Findings`
   - identifier `CF5-A-###`
   - severity: `BLOCKER`, `MAJOR`, `MINOR`, `EDITORIAL`
   - classification: `INTERNAL_CONSISTENCY`, `ARCHITECTURE`, `TERMINOLOGY`, `TRACEABILITY`, `NEEDS_MAIN_REPO_VALIDATION`, or `MAINTAINER_DECISION`
   - affected file and section
   - exact problem
   - recommended change
   - invariant impact
4. `Accepted strengths`
5. `Repository facts requiring validation`
6. `Maintainer decisions required`
7. `Proposed normative changes`
8. `Rejected alternatives`
9. `Phase A exit recommendation`

Do not edit normative files directly. Do not present review consensus as evidence. Every recommendation must be adjudicated before incorporation.
