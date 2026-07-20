# ROS Operating Model

Status: bootstrap proposal
Status-date: 2026-07-20

## Roles

Minimum role vocabulary:

- Maintainer: final local authority and adjudicator;
- Planner: prepares bounded work and dependencies;
- Implementer: performs authorized repository mutations;
- Reviewer: challenges correctness, completeness and risk;
- Verifier: evaluates exact evidence and gates;
- Successor agent: continues from a validated handoff.

A person or model may hold multiple roles, but each action must declare the active role when authority differs.

## Work-package lifecycle

- `CAPTURED`
- `TRIAGED`
- `PLANNED`
- `READY`
- `IN_PROGRESS`
- `BLOCKED`
- `UNDER_REVIEW`
- `VERIFIED`
- `CLOSED`
- `SUPERSEDED`

Capture and planning remain distinct: a captured idea cannot enter `READY` without promotion into the repository's governed planning system.

## Session entry

A session begins only after:

1. repository and exact ref are known;
2. authority and applicable profile are known;
3. required bootstrap and context projections are validated;
4. local plan or authorized exploratory scope is identified;
5. stop conditions are understood.

## Execution contract

Each executable work package identifies:

- target repository and branch policy;
- governing local plan item;
- permitted mutations;
- required tests, gates and evidence;
- protected boundaries;
- blocking conditions;
- review and closeout requirements;
- required successor-handoff update.

## Multi-repository coordination

A coordinating work package may declare dependencies in other repositories, but it cannot mutate or reprioritize them without local adoption. Cross-repository status is represented as referenced evidence, not copied local truth.

## Escalation

Stop and escalate when:

- authority is ambiguous;
- exact evidence conflicts;
- a protected boundary would be crossed;
- a required local planning or lifecycle command is unavailable;
- a change would create dual authority;
- a repository-specific decision is required.

## Closeout

Closeout requires:

- implementation or analysis result;
- exact evidence references;
- unresolved risks and follow-ups;
- updated local authoritative state;
- validated successor context where continuation is expected.

A chat summary alone is never sufficient closeout evidence.