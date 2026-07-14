# DPA Lab Bootstrap

Status: active
Status-date: 2026-07-14
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
11. every DPA specification whose status is `active`, `draft` or needed by the assigned task
12. relevant reviews under `reviews/`
13. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
14. `integration/IMPORT_PLAN.md`

Do not begin work until this read order is complete.

## Authority hierarchy

When sources conflict, use this order:

1. Current evidence from the real `vfi64/agentic-project-kit` repository at an exact Git ref.
2. `MAIN_REPOSITORY_CONTEXT.md` for the last recorded and evidenced main-repository context.
3. `LAB_EXECUTION_CONTRACT.md` for how the lab must be operated.
4. Accepted decisions in `DECISIONS.md`.
5. Normative DPA specifications under `specs/dpa/`.
6. Consolidated reviews.
7. Individual model reviews.
8. Assumptions and proposals.
9. Chat memory.

Chat memory is never an authoritative source.

## Classification requirement

Every repository-specific statement must be marked or clearly treated as one of:

- `VERIFIED`
- `ASSUMPTION`
- `NORMATIVE`
- `PROPOSAL`
- `REJECTED`
- `NEEDS_MAIN_REPO_VALIDATION`

A statement is `VERIFIED` only when the exact main-repository ref and the validating source or reproduction method are recorded.

## Repository separation

### Lab repository

May contain:

- normative architecture specifications,
- diagrams,
- decisions,
- assumptions,
- model reviews,
- consolidation records,
- traceability,
- implementation plans,
- import and validation plans.

Must not contain:

- production kit code,
- live private state copied from another repository,
- secrets,
- fabricated gate or test evidence,
- a second runtime authority for the main repository.

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
2. maintain reviews separately from normative text,
3. build traceability and decision records,
4. prepare DPA-600 through DPA-900,
5. validate all main-repository assumptions before implementation,
6. adopt this lab with the kit only after the architecture baseline is stable.

Until that adoption point, do not create or simulate `.agentic/` state in this lab.

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
- a proposal creates a new runtime truth source without explicit approved architecture authority,
- review conclusions are being copied into normative documents without adjudication,
- the requested work would introduce production kit code into the lab,
- the assigned task is outside the active lab phase.
