# Claude Fable 5 Review Prompt — DPA Phase A Foundation

Status: active
Status-date: 2026-07-14
Review type: individual, non-normative
Reviewed repository: `vfi64/agentic-project-kit-dpa-lab`
Reviewed ref: `1a73ec435a09d0367cb7e9f123241d9f61550b0f`

## Prompt

You are reviewing the Phase A foundation of the Document Projection Architecture (DPA) in the private repository `vfi64/agentic-project-kit-dpa-lab`.

Work only from repository content at the exact commit:

`1a73ec435a09d0367cb7e9f123241d9f61550b0f`

Do not use chat memory as authority. Do not review a moving branch tip. Do not infer current implementation facts about `vfi64/agentic-project-kit` beyond evidence explicitly recorded in the lab.

### Mandatory read order

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

### Authority order

When sources conflict, use:

1. exact evidence from the real main repository at a concrete Git ref;
2. `MAIN_REPOSITORY_CONTEXT.md`;
3. `LAB_EXECUTION_CONTRACT.md`;
4. accepted decisions in `DECISIONS.md`;
5. normative DPA specifications;
6. consolidated reviews;
7. individual reviews;
8. assumptions and proposals;
9. model memory.

### Binding constraints

Your review must preserve these constraints unless you identify a direct internal contradiction:

- The DPA extends the existing main-repository document-management architecture; it does not create a parallel system.
- Canonical state has no render logic.
- Renderers have no write logic and return text or bytes only.
- The existing lifecycle validates, plans, locks and writes.
- Workflow orchestration serializes across branches and pull requests.
- Registry data describes reviewed contracts, not arbitrary executable plugins.
- Renderer identifiers resolve statically and fail loud.
- One renderer computes one registered target and triggers no other renderer.
- Evidence is never runtime authority.
- No new canonical history source is introduced merely for migration convenience.
- Historical prose is not automatically merged during drift recovery.
- Time passage alone cannot cause a hard failure.
- Repository-specific implementation claims require exact ref-bound evidence.

### Review objectives

Assess whether Phase A is internally coherent and review-ready. Specifically inspect:

1. contradictions among bootstrap, execution contract, decisions, DPA-000, DPA-100 and traceability;
2. terminology collisions, circular definitions or ambiguous authority ownership;
3. any hidden parallel registry, lifecycle, freshness, evidence, workspace, workflow or gate subsystem;
4. any path by which evidence or a projection target could silently become canonical runtime state;
5. renderer impurity, dynamic loading, nested rendering or write-boundary leakage;
6. whether local locking and cross-PR serialization are correctly separated;
7. whether freshness, drift and time-based signals are distinguished precisely enough for DPA-500 and DPA-600;
8. whether migration principles prejudge DP1 without evidence;
9. whether manual, full, split, hybrid and managed-head document forms are defined without prematurely accepting them;
10. whether status labels distinguish planning, review-ready, stable, adopted and implemented states;
11. whether every accepted decision has context, alternatives, rationale, consequences, validation status and affected scope;
12. whether traceability links motivation, invariants, decisions, DP1–DP5, tests, gates, evidence and rollback without claiming implementation completion;
13. missing negative requirements or failure modes that must be settled before DPA-200;
14. repository-specific claims that are insufficiently classified;
15. any Phase A exit criterion that is falsely marked satisfied.

### Required output structure

Write the review in English and use this exact structure:

```markdown
# Claude Fable 5 Review — DPA Phase A Foundation

Reviewed repository: vfi64/agentic-project-kit-dpa-lab
Reviewed ref: 1a73ec435a09d0367cb7e9f123241d9f61550b0f
Model: Claude Fable 5
Review status: COMPLETE | BLOCKED

## 1. Executive assessment

- Overall result: ACCEPT | ACCEPT_WITH_CHANGES | REJECT | BLOCKED
- Phase A may proceed to adjudication: YES | NO
- Foundational contradiction present: YES | NO
- Hidden parallel system implied: YES | NO

## 2. Blocking findings

For each finding:
- ID
- Severity: BLOCKER
- Files and sections
- Exact contradiction or failure mode
- Why it violates an authority or invariant
- Proposed resolution
- Whether maintainer decision is required

## 3. Major findings

For each finding:
- ID
- Severity: MAJOR
- Files and sections
- Analysis
- Proposed normative change
- Affected decisions and traceability
- Main-repository validation required: YES | NO

## 4. Minor findings

Use the same fields with severity MINOR.

## 5. Terminology audit

List:
- coherent terms;
- ambiguous terms;
- duplicate or circular terms;
- missing terms required before DPA-200.

## 6. Authority and boundary audit

Evaluate:
- canonical state;
- projection authority;
- registry;
- renderer;
- lifecycle;
- workflow orchestration;
- evidence;
- historical record;
- consumers.

## 7. Invariant-by-invariant audit

For each Phase A invariant, state:
- PASS | FAIL | NEEDS_CLARIFICATION
- supporting file/section
- conflicting file/section, if any
- required correction.

## 8. Decision audit

For DPA-ADR-001 through DPA-ADR-008:
- ACCEPT | REVISE | REJECT
- completeness of context/alternatives/rationale/consequences
- consistency with DPA-000 and DPA-100.

## 9. Traceability audit

Identify:
- missing links;
- false completion claims;
- tests/gates/evidence/rollback gaps;
- DP1–DP5 sequencing risks.

## 10. Main-repository validation obligations

Separate:
- claims adequately classified now;
- claims that must remain NEEDS_MAIN_REPO_VALIDATION;
- exact evidence required later.

Do not invent module names or implementation facts.

## 11. Accepted findings

List findings you recommend for adjudication and normative incorporation.

## 12. Rejected alternatives

List tempting changes you explicitly reject because they would violate the contracts.

## 13. Unresolved questions

Include only questions that genuinely block adjudication or DPA-200. Mark whether each requires a maintainer decision or fresh main-repository evidence.

## 14. Recommended adjudication order

Provide a bounded sequence for resolving findings.

## 15. Final verdict

State whether the reviewed ref is:
- not review-ready;
- review-ready with changes;
- ready for Phase A adjudication;
- eligible for Phase A stability after adjudication.
```

### Review discipline

- Do not modify normative files directly.
- Do not treat your review as normative.
- Do not claim implementation success.
- Do not upgrade assumptions from model consensus.
- Prefer precise blocking diagnoses over broad redesign.
- Flag any recommendation that would require a new runtime authority source or parallel governance subsystem as prohibited unless it first changes the accepted architecture through an explicit maintainer decision.

Return only the completed review document.