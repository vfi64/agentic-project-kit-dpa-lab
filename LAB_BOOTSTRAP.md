# DPA Lab Bootstrap

Status: active
Status-date: 2026-07-15
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
8. `DECISIONS.md`
9. `ASSUMPTIONS.md`
10. `specs/dpa/README.md`
11. every DPA specification whose document status is `active`, `draft`, `review-ready` or required by the assigned task
12. relevant primary reviews, technical verification audits and consolidated adjudications under `reviews/`
13. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
14. `integration/IMPORT_PLAN.md`

Do not begin work until this read order is complete.

## Authority hierarchy

When sources conflict, use this order:

1. Current evidence from the real `vfi64/agentic-project-kit` repository at an exact validation ref.
2. `MAIN_REPOSITORY_CONTEXT.md` for the last recorded and evidenced main-repository context.
3. `LAB_EXECUTION_CONTRACT.md` for how the lab must be operated.
4. Accepted decisions in `DECISIONS.md`.
5. Normative DPA specifications under `specs/dpa/`.
6. Consolidated adjudications and reviews.
7. Primary architecture reviews and secondary technical verification audits.
8. Assumptions and proposals.
9. Chat memory.

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

The lab is in the pre-adoption architecture phase.

Current work order:

1. stabilize DPA-000 through DPA-500,
2. maintain review inputs separately from normative text,
3. build traceability and decision records,
4. prepare DPA-600 through DPA-900,
5. validate all main-repository assumptions before implementation,
6. adopt this lab with the kit only after the architecture baseline is stable.

Until that adoption point, do not create or simulate `.agentic/` state in this lab.

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
