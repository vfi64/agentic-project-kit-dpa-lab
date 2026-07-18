# DPA Lab Bootstrap

Status: active
Status-date: 2026-07-18
Superseded-by: n/a

## Purpose

This file is the mandatory entrypoint for every new human or LLM session working in `vfi64/agentic-project-kit-dpa-lab`.

The lab is a temporary, versioned architecture workspace for the Document Projection Architecture (DPA) of `vfi64/agentic-project-kit`. It is not a runtime dependency and is not authoritative for the current implementation state of the main repository.

## Mandatory read order

Before proposing, editing, committing, reviewing or consolidating any work, read these files completely in this exact order:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `MASTERPLAN.md`
9. `DECISIONS.md`
10. `ASSUMPTIONS.md`
11. `specs/dpa/README.md`
12. every DPA specification whose document status is `active`, `draft`, `review-ready` or required by the assigned task
13. relevant primary reviews, technical verification audits and consolidated adjudications under `reviews/`
14. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
15. `integration/IMPORT_PLAN.md`

Do not begin work until this read order is complete.

## Authority hierarchy

When sources conflict, use this order:

1. Current evidence from the real `vfi64/agentic-project-kit` repository at an exact validation ref.
2. `MAIN_REPOSITORY_CONTEXT.md` for the last recorded and evidenced main-repository context.
3. `LAB_EXECUTION_CONTRACT.md` for how the lab must be operated.
4. Accepted decisions in `DECISIONS.md`.
5. Normative DPA specifications under `specs/dpa/`.
6. `MASTERPLAN.md` for the canonical remaining-work sequence, subject to the higher authorities above.
7. Consolidated adjudications and reviews.
8. Primary architecture reviews and secondary technical verification audits.
9. Assumptions and proposals.
10. Chat memory.

Chat memory is never an authoritative source.

## Classification and status requirement

Repository or architecture claims MUST use exactly one classification defined by DPA-100:

- `VERIFIED`
- `VERIFIED_AT_RECORDED_BASELINE`
- `ASSUMPTION`
- `NORMATIVE`
- `PROPOSAL`
- `REJECTED`
- `NEEDS_MAIN_REPO_VALIDATION`

Document status, progress status and access outcome are separate namespaces and MUST NOT be used as repository-fact classifications.

A statement is `VERIFIED` only when the exact main-repository validation ref and the validating source or reproduction method are recorded. `VERIFIED_AT_RECORDED_BASELINE` additionally requires a minimal static record under `evidence/repo-facts/` and never removes the requirement for fresh implementation validation.

## Repository separation

### Lab repository

May contain:

- normative architecture specifications,
- diagrams,
- decisions,
- assumptions,
- review and verification artifacts,
- consolidation records,
- traceability,
- implementation plans,
- import and validation plans,
- minimal static repo-fact evidence records.

Must not contain:

- production kit code,
- live private state copied from another repository,
- secrets,
- fabricated gate or test evidence,
- a second runtime authority for the main repository,
- a parallel evidence database or evidence execution system.

### Main repository

The real `vfi64/agentic-project-kit` remains authoritative for:

- implementation,
- runtime contracts,
- Direction state,
- documentation registry contents,
- lifecycle behavior,
- tests and gates,
- release and handoff state.

## Current phase

The lab is in the pre-adoption architecture and exact-ref validation phase.

Current work order:

1. use `MASTERPLAN.md` as the canonical execution sequence;
2. revalidate historical main-repository findings against a current exact ref;
3. prepare and execute PROBE-001, PROBE-002 and the DPA-400 renderer Probe package;
4. adjudicate Probe evidence and perform bounded DPA-300 through DPA-500 amendments where required;
5. independently verify normative amendments to review-ready specifications;
6. release and implement DP2 only after Probe-driven revalidation;
7. validate external-repository habitability before controlled adoption.

Until governed adoption, do not create or simulate `.agentic/` state in this lab.

## Review roles

Phase reviews are evidence-qualified roles, not vendor requirements:

1. primary architecture review,
2. secondary technical verification,
3. maintainer adjudication,
4. consolidated review record.

An access failure is recorded as `ACCESS_BLOCKED`; it is not a review verdict.

## Session start report

After completing the mandatory read order, report exactly:

- lab repository and branch/ref,
- current lab phase,
- current normative documents,
- current task,
- unresolved blocking decisions,
- main-repository facts used and their evidence status,
- whether work may proceed.

## Stop conditions

Stop and diagnose instead of guessing when:

- a main-repository fact is required but cannot be evidenced,
- two normative documents contradict each other,
- a proposal would create a parallel registry, lifecycle, freshness, evidence, workspace or gate system,
- a proposal creates a new runtime authority without explicit approved architecture authority,
- review conclusions are being copied into normative documents without adjudication,
- the requested work would introduce production kit code into the lab,
- the assigned task is outside the active lab phase.