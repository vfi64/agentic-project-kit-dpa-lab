# ADR-001: Layered Federated Agentic System

Status: proposed
Date: 2026-07-20

## Context

AGF, DPA, Agentic Project Kit, ROS and domain applications address different but connected parts of durable human–LLM collaboration. Combining them into one authority or one repository would create coupling, duplicated state and unclear ownership.

## Decision

Use a layered federated architecture:

- AGF defines reusable governance and scientific reasoning methodology;
- DPA defines knowledge, document and projection architecture;
- Kit implements executable repository and agent tooling;
- ROS defines the operating model using Kit capabilities;
- applications adopt selected profiles while retaining domain authority.

GitHub repositories form the durable declarative memory substrate. Canonical structured objects, append-only events, Git history, local plans, evidence and bounded context projections remain distinct but connected.

## Consequences

Positive:

- clear authority boundaries;
- independent evolution and versioned adoption;
- reuse without automatic control;
- traceable long-term memory for LLM sessions;
- bounded migration and pilot testing.

Costs and risks:

- cross-repository compatibility management;
- schema/version coordination;
- potential over-engineering;
- need for explicit adoption records and context projections.

## Rejected alternatives

- one monorepo and unified authority;
- Markdown-only memory;
- chat history as primary continuity mechanism;
- ROS as a duplicate Kit runtime;
- immediate full migration of application repositories.

## Reconsideration conditions

Reopen this decision if federation creates more operational ambiguity than it removes, if a simpler model provides equivalent evidence and continuity, or if independent pilot agents cannot use the contracts consistently.