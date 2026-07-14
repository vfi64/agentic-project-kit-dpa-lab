# agentic-project-kit-dpa-lab

> **Non-authoritative architecture planning repository**

This repository is the temporary architecture laboratory for the Document Projection Architecture (DPA) of `vfi64/agentic-project-kit`.

It is not a runtime dependency and is not authoritative for the current state of the main repository.

Repository facts marked `VERIFIED` remain subject to revalidation against the current `origin/main` before implementation.

After adoption, the authoritative architecture and runtime contracts live only in `vfi64/agentic-project-kit`.

## Mandatory session entrypoint

Every human or LLM session MUST begin with:

1. `LAB_BOOTSTRAP.md`
2. `MAIN_REPOSITORY_CONTEXT.md`
3. `LAB_EXECUTION_CONTRACT.md`

Then follow the complete read order defined by `LAB_BOOTSTRAP.md`.

Do not start work from chat memory or from an isolated review document.

## Mission

Develop a complete, reviewable and implementation-ready DPA specification that extends the existing document registry, lifecycle, freshness, evidence, workspace and gate architecture without creating a parallel document-management system.

## Repository roles

### This lab

- develops normative DPA specifications,
- stores model reviews separately,
- records decisions and assumptions,
- prepares traceability, validation and import plans,
- contains no production kit code,
- remains non-authoritative for main-repository runtime state.

### Main repository

`vfi64/agentic-project-kit` remains authoritative for implementation, Direction, registry, lifecycle, tests, gates, releases and handoff state.

## Working status vocabulary

- `VERIFIED`
- `ASSUMPTION`
- `NORMATIVE`
- `PROPOSAL`
- `REJECTED`
- `NEEDS_MAIN_REPO_VALIDATION`

## Current phase

The lab is in the pre-adoption architecture phase.

DPA-000 through at least DPA-500 must be stable before the lab is adopted with `agentic-project-kit`. Until then, no `.agentic/` state may be created or simulated here.

## Primary documents

- `LAB_BOOTSTRAP.md` — mandatory session bootstrap and authority order
- `MAIN_REPOSITORY_CONTEXT.md` — evidenced main-repository context snapshot
- `LAB_EXECUTION_CONTRACT.md` — complete working, review, commit and completion contract
- `GOVERNANCE.md` — authority and prohibitions
- `STATUS.md` — current lab state and next action
- `ROADMAP.md` — DPA-000 through DPA-900 sequence
- `DECISIONS.md` — accepted and provisional architecture decisions
- `ASSUMPTIONS.md` — facts requiring main-repository validation
- `specs/dpa/` — normative DPA specification series
- `reviews/` — non-normative model reviews
- `integration/` — validation and controlled import planning
