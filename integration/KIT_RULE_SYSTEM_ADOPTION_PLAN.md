# Kit Rule-System Adoption Plan — Proactive Specialist Gap Escalation

Status: active

Status-date: 2026-07-19

Superseded-by: n/a

## 1. Purpose

This document defines how the newly identified proactive specialist-gap obligation must be transferred from the DPA Lab into the existing Agentic Project Kit rule system and, through that system, into repositories governed by the Kit.

It prevents a parallel-rule failure: the obligation MUST NOT be implemented only as free prose in the Lab, an isolated `AGENTS.md` sentence, a prompt convention, or a new rule framework. It must be adopted through the Kit's existing governed rule-mechanism registry, test-coverage metadata, migrations, reports, acknowledgements and enforcement surfaces after exact-ref validation and review.

This plan is non-authoritative for production runtime state. It authorizes planning and read-only inspection only.

## 2. Existing rule authority to extend

Current exact-ref remote inspection establishes an existing governed rule system with these primary artifacts:

- `.agentic/rule_mechanism_inventory.yaml`;
- `.agentic/rule_migrations.yaml`;
- `.agentic/rule_test_coverage.yaml`;
- `.agentic/rule_direct_test_plan.yaml`;
- `agentic-kit rule-registry check`;
- `agentic-kit rule-registry report`;
- `agentic-kit rule-registry register`.

The current validator recognizes mechanism categories:

- `communication`;
- `execution`;
- `governance`;
- `workflow`;
- `preflight`.

It recognizes enforcement phases:

- `runtime`;
- `guard`;
- `preflight`.

The proposed obligation must extend these existing authorities. No second rule registry, policy engine, acknowledgement system or enforcement framework may be created.

## 3. Proposed rule intent

Working title:

`proactive-specialist-gap-escalation`

Protected rule intent:

> During Kit development and work in Kit-governed repositories, an agent or reviewer with materially greater specialist knowledge than the Maintainer must surface material architecture, safety, governance, correctness or operability gaps that would leave the stated project goal or motivating failure class unmet, even when the Maintainer did not know to ask about them.

The obligation is not permission to expand scope without control. Every surfaced concern must be classified as exactly one of:

1. confirmed architecture or governance gap;
2. suspected gap requiring evidence;
3. implementation defect under an adequate existing contract;
4. editorial or synchronization inconsistency;
5. optional out-of-scope improvement.

The agent must explain the consequence of inaction, the evidence status and the correct authority path. It must not silently implement an unrelated improvement.

## 4. Applicability levels

### 4.1 Kit self-development

The rule applies while developing `vfi64/agentic-project-kit` itself. It covers architecture, rules, commands, generators, lifecycle, handoff, status, gates, evidence, GUI and portability work.

### 4.2 Kit-managed repositories

The rule must be available to repositories adopted or initialized by the Kit. Its exact activation model must be determined through the existing project contract, profile and policy-pack system rather than by unconditional prose injection.

Candidate integration surfaces requiring exact-ref assessment include:

- an existing governance or agentic-development policy pack;
- a documentation-governed or safety-oriented policy pack;
- generated or adopted agent instructions;
- project execution contracts and successor handoff packages;
- rule acknowledgement and reporting;
- advisory architecture or plan-review surfaces;
- preflight or guard checks for missing disposition of recorded material concerns.

No profile or policy-pack placement is selected by this Lab plan. Selection requires current main-repository inventory and Maintainer adjudication.

### 4.3 Project-specific specialization

A governed repository may define domain-specific specialist obligations, but they must inherit the common classification and evidence discipline. Project rules must not weaken the Kit-level obligation silently.

## 5. Rule-mechanism registration requirements

Before production adoption, the proposed mechanism must have a reviewed registration record containing at least:

- stable mechanism ID;
- allowed mechanism category;
- compatible enforcement phase;
- owner;
- priority from the existing closed range;
- conflict domains;
- covered surfaces;
- direct source path;
- required source anchor terms;
- direct regression test paths;
- protected rule intent;
- direct assertion statement and supported assertion kind;
- test-evidence references;
- migration and compatibility disposition.

The exact category, phase, priority and owner remain `NEEDS_MAIN_REPO_VALIDATION` until the current rule inventory and conflict model are fully inspected.

## 6. Required behavioral boundaries

The rule must require proactive escalation but also prevent uncontrolled agent autonomy.

A conforming mechanism must enforce or verify that:

- material concerns are surfaced before implementation or closure when reasonably discoverable;
- concerns identify evidence and uncertainty honestly;
- the motivating goal or failure class is named;
- concerns are classified using the closed disposition set;
- architecture gaps are routed to planning or decision authority before implementation;
- implementation defects are routed to the existing implementation workflow;
- optional improvements do not become hidden scope expansion;
- Maintainer decisions are preserved;
- rejected or deferred concerns remain traceable without repeatedly blocking unrelated work;
- no model's specialist assertion becomes production truth without repository-backed evidence and the required review path.

## 7. Human-knowledge amplification objective

The rule exists to increase the effective knowledge available to the human Maintainer while preserving human authority.

The intended interaction is:

```text
human goal and constraints
→ agent/reviewer specialist analysis
→ explicit gap or risk classification
→ evidence and consequence
→ existing planning/decision/rule authority
→ Maintainer adjudication
→ governed implementation or documented deferral
```

The mechanism must not replace Maintainer judgment. It must make relevant specialist knowledge visible early enough to be useful.

## 8. Remote iPhone work

The following work is safe remotely:

1. inspect the complete current rule inventory and migration model;
2. identify existing mechanisms with overlapping intent;
3. map conflict domains and priority ordering;
4. inspect acknowledgement and enforcement paths;
5. inspect how profiles and policy packs activate rules in managed repositories;
6. identify generated instruction and handoff surfaces affected by the rule;
7. prepare a proposed registration record without executing registration;
8. prepare direct positive and negative tests;
9. prepare migration behavior for existing Kit and adopted workspaces;
10. prepare an independent governance review package.

Remote inspection remains provisional until locally confirmed against the exact installed ref.

## 9. Local validation and implementation sequence

After Mac access and exact-ref equality:

1. run the existing rule-registry check and report commands;
2. capture the complete inventory, coverage, migrations and direct-test-plan state;
3. confirm no existing mechanism already owns the protected intent;
4. validate conflicts, category, phase, owner and priority;
5. add or amend the canonical source rule through the approved planning slice;
6. register the mechanism using the existing `rule-registry register` path when its contract fits;
7. add direct tests and negative cases;
8. update policy-pack or project-contract activation only through existing authorities;
9. update generated instructions and handoff projections through their generators, not by durable direct patches;
10. run rule-registry validation, focused tests, instruction lint, docs gates and standard audit gates;
11. verify behavior in the Kit repository and at least one disposable managed repository;
12. preserve migration and rollback evidence.

If the existing registration command cannot represent the required mechanism safely, that is a bounded rule-system capability gap to be planned and reviewed. It is not permission to bypass the registry manually.

## 10. Relationship to DPA and document commands

The rule-system adoption and DPA command-integration tracks reinforce each other:

- the proactive rule requires agents to surface ungoverned document writers and duplicate semantic authority;
- DPA command integration defines how those writers are classified and corrected;
- the existing rule registry governs the obligation to detect and escalate such gaps;
- generated rule, instruction, status and handoff artifacts remain subject to DPA mutation-authority rules;
- neither track may create a parallel registry or authority.

## 11. Exit criteria

Planning is complete when:

- the current rule system is fully inventoried for the inspected exact ref;
- overlap and conflict analysis is documented;
- the proposed mechanism record is complete;
- activation across Kit self-development and Kit-managed repositories is specified;
- direct positive, negative and non-overreach tests are designed;
- migration, acknowledgement, reporting and rollback are covered;
- an independent review has assessed knowledge amplification, Maintainer authority, scope-control and parallel-system risk.

Production adoption is complete only after registration or approved bounded rule-system extension, direct tests, all applicable gates, migration evidence and validation in both the Kit and a disposable Kit-managed repository.