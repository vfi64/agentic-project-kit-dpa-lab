# Agentic System Architecture

Status: draft baseline
Status-date: 2026-07-20

## Purpose

This document defines the cross-repository target architecture for long-term human–LLM collaboration. It is authoritative only for the AGF system model. Each repository remains authoritative for its own implementation and adoption state.

## Layer model

1. **AGF — meta-governance and scientific reasoning method**
   Defines governance objects, evidence classes, falsification, review, adjudication, adoption, simplification and retirement.
2. **DPA — knowledge, document and projection architecture**
   Defines canonical structured knowledge, document regions, lifecycle, rendering, freshness, provenance and bounded context projections.
3. **Agentic Project Kit — executable repository and agent runtime**
   Implements workspaces, registries, validators, renderers, gates, handoffs, evidence capture and GitHub integration.
4. **ROS — repository operating model**
   Defines roles, work packages, operating states, agent-session rules, multi-repository coordination and closeout semantics. ROS uses Kit capabilities and must not duplicate the Kit runtime.
5. **Applications**
   Wrapper, Comm-SCI-Control-private, Comm-SCI-Control and future repositories adopt selected profiles while retaining domain authority.

## Authority invariant

Upstream layers define reusable method or representation contracts. They do not own downstream runtime facts, plans, scientific truth or adoption state.

## Federated memory model

Long-term repository memory combines:

- append-only capture events for provenance;
- canonical governed graph objects for current accepted knowledge;
- Git history for change lineage;
- repository-local plans and decisions for control;
- execution and evidence records for observed outcomes;
- bounded DPA projections for humans and LLM sessions.

No projection, capture entry or upstream repository may silently become a second authority for a downstream plan or fact.

## Federated graph domains

The system uses connected but authority-separated graph domains:

- reasoning and governance: capture, hypothesis, evidence, counterargument, review, decision, rule;
- planning: requirement, plan item, dependency, work package, milestone;
- execution and evidence: branch, commit, pull request, gate run, validation record, release;
- representation: canonical object, projection, source region, freshness record;
- operation: repository, role, agent session, operating state, handoff.

Typed relations connect these domains, for example `promoted_to`, `scheduled_by`, `realized_by`, `verified_by`, `projected_as`, `adopted_by` and `operated_by`.

## LLM context principle

An LLM session should receive a validated bounded context projection, not an unfiltered repository or whole graph dump. A context projection identifies exact sources, authority, freshness, unresolved conflicts and token-budget decisions.

## Non-goals

- no monorepo merger of AGF, DPA, Kit, ROS and applications;
- no universal central planner;
- no replacement of domain-specific scientific authority;
- no immediate removal of Markdown;
- no automatic adoption across repositories.