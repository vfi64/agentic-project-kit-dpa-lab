# Authority and Interchange Model

Status: draft baseline
Status-date: 2026-07-20

## Authority matrix

| Repository | Owns | Does not own |
|---|---|---|
| AGF | reusable governance method, accepted framework decisions, common object vocabulary | downstream implementation, planning or domain truth |
| DPA Lab | DPA architecture specifications and review records until controlled import | Kit runtime state |
| Agentic Project Kit | executable tooling, workspace state, registries, gates, releases and local implementation evidence | universal governance truth or application-domain truth |
| ROS | repository operating-model specifications and adopted operational profiles | Kit implementation or application-domain truth |
| Application repository | its domain rules, scientific claims, plans, runtime and adoption state | upstream framework definitions |

## Interchange contract

Repositories exchange versioned records, never implicit authority. Each exchanged object must identify:

- schema and schema version;
- producing repository;
- object identifier;
- exact source ref;
- authority scope;
- lifecycle and evidence state where applicable;
- intended consumer and adoption status;
- freshness or revalidation requirement.

## Adoption states

- `NOT_EVALUATED`
- `EVALUATING`
- `ADAPTED_PROPOSAL`
- `ADOPTED`
- `REJECTED`
- `SUPERSEDED`
- `REVALIDATION_REQUIRED`

Listing a consumer or creating an integration document does not constitute adoption.

## Conflict rules

1. A repository-local runtime fact overrides an upstream assumption about that runtime.
2. An upstream framework definition controls only within its declared framework scope.
3. A local adaptation must be explicit and traceable; silent term redefinition is prohibited.
4. Conflicting adopted versions require an explicit compatibility or migration decision.
5. Chat memory may explain intent but cannot resolve authority conflicts.

## Planning boundary

A cross-repository masterplan may coordinate dependency milestones. It may not replace repository-local planning, task state or release authority.

## Kit hold

No Agentic Project Kit documentation or planning artifact may be changed for this system initiative until the Maintainer is back at the Mac and the repository's own Agentic-Kit document-lifecycle and planning commands can be run. The pending work is recorded in the AGF masterplan and must later be introduced through the Kit's established planning system.