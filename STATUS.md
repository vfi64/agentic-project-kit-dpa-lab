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

## DPA-200 review baseline

`specs/dpa/DPA-200-DOCUMENT-MODEL.md` remains `draft` and owns the normative document model.

The exact primary-review baseline is:

`44a87127fca7f482bc2991f0c258af0a386a7048`

The Claude review prompt is stored at:

`reviews/claude/CLAUDE_DPA_200_REVIEW_PROMPT.md`

The prompt was committed after the baseline and instructs Claude to check out the exact baseline rather than the later branch tip.

Completed DPA-200 planning artifacts:

- complete initial document-model draft;
- document-form decision matrix;
- DPA-200 requirement traceability DM-001 through DM-010;
- region and write-ownership diagram;
- consumer trust-state diagram;
- full audit against `DPA-INV-001` through `DPA-INV-017`;
- full audit against accepted DPA-ADR-001 through DPA-ADR-012;
- exact-ref primary architecture review prompt.

No production candidate has been assigned a document form. Region support, concrete schemas, readers, writers, lifecycle paths, gate placement and rollback sources remain `NEEDS_MAIN_REPO_VALIDATION`.

## Pre-review assessment

The internal pre-review audit result is:

`PASS_WITH_EXTERNAL_REVIEW_REQUIRED`

No contradiction with stable DPA-000, DPA-100, canonical invariants or accepted decisions was found.

The external review must independently examine:

- split projection versus general hybrid form;
- managed-head exceptional constraints;
- exhaustive byte ownership;
- registered-region boundaries;
- target semantics and normalization;
- written-unverified trust state;
- consumer classes and accepted-state boundary;
- delegated specification ownership;
- hidden authority ambiguity or parallel-system implications.

## Active work

1. Obtain the Claude primary architecture review against exact ref `44a87127fca7f482bc2991f0c258af0a386a7048`.
2. Commit the review unchanged under `reviews/claude/`.
3. Produce a secondary technical verification after the Claude review is available.
4. Create a consolidated finding-by-finding maintainer adjudication.
5. Apply accepted normative corrections.
6. Decide whether DPA-200 may advance from `draft` to `review-ready`.

## DPA-200 review-readiness tracking

| Criterion | Progress |
|---|---|
| Complete document-form definitions | complete |
| Authority and write ownership rules | complete |
| Target semantics and invalidity rules | complete |
| Consumer trust boundary | complete |
| Decision matrix | complete |
| Tests, gates, evidence and rollback traceability | complete for review baseline |
| Region-boundary and trust-state diagrams | complete |
| Full invariant and ADR audit | complete |
| Exact-ref primary review baseline | complete |
| Claude primary review | pending external reviewer output |
| Secondary technical verification | pending primary review |
| Maintainer adjudication | pending reviews |

## Phase B restrictions

- No production kit code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No registry-field or module-name claims without exact main-repository evidence.
- No preselection of a production migration form before DP1.
- No DPA-300 detail may bypass DPA-200 authority, ownership or trust-state rules.
- No review finding becomes normative without adjudication.

Phase B may continue only through the governed review and adjudication sequence. DPA-200 is not yet `review-ready`.