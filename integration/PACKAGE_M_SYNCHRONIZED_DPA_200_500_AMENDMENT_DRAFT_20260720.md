# Package M Synchronized DPA-200–DPA-500 Amendment Draft

Status: review-candidate

Status-date: 2026-07-20

Authority: non-normative bounded amendment draft prepared after Maintainer adjudication for independent review

Depends-on:

- `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`;
- `reviews/adjudication/PACKAGE_M_MAINTAINER_ADJUDICATION_20260720.md`;
- `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`;
- `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`;
- `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_V2_20260720.md`;
- `integration/PACKAGE_M_INDEPENDENT_REVIEW_DISPOSITION_20260720.md`.

## 1. Purpose and boundary

This document consolidates the accepted Package M proposal and both correction addenda into one synchronized candidate amendment for DPA-200, DPA-300, DPA-400 and DPA-500.

It is not normative. It does not modify the four review-ready specifications, promote ADR-022 beyond its recorded proposal status, authorize implementation, execute or amend a Probe, claim complete command coverage or change DPA-600 or DPA-700 sequencing.

Repository-specific runtime homes, schemas, command mappings, finding identifiers and enforcement points remain `NEEDS_MAIN_REPO_VALIDATION`.

The clauses below are written as insertion-ready normative candidates. They become normative only through a later governed amendment, synchronized traceability and diagram update, independent verification and Maintainer acceptance.

## 2. Shared proposal terms

### 2.1 Document mutation authority

A **document mutation authority** is an already-governed registry, lifecycle, state, workflow, evidence, migration or retention authority under which one command mode may cause one declared class of document-like mutation.

A CLI path, alias, helper function or file path is not authority by itself.

### 2.2 Command mutation contract

A **command mutation contract** is a reviewed declaration binding one authority-bearing command mode or independently schedulable or independently recoverable composed mutation step to:

- exactly one primary command mutation class;
- zero or more constrained secondary effects;
- canonical input authorities;
- Workspace-resolved target identities;
- a plan-bound changed-path conformance relation;
- write semantics;
- lifecycle, lock and workflow ownership;
- verification, trust-state and evidence effects;
- recovery, compatibility and migration disposition.

The contract MUST be represented through a reviewed extension of exactly one existing main-repository authority selected after exact-ref validation. Candidate homes may include an existing command manifest, existing command metadata or a statically reviewed code mapping. No new DPA-owned command registry or persistence surface is authorized.

The same command-mode contract MUST NOT be duplicated in independently editable stores. Derived references MAY project it but MUST identify their source and MUST NOT become runtime authority.

### 2.3 Inherited subordinate path

An internal helper, lifecycle method, adapter or delegated function that cannot independently broaden authority, select additional targets, persist independent authoritative state, be invoked outside the owning operation or produce an independently recoverable result inherits the owning command mutation contract.

An inherited path MUST NOT broaden the owning contract's target set, changed-path boundary, source authority, secondary effects, lock scope, verification obligations or recovery authority.

### 2.4 Synchronized projection set

A **synchronized projection set** is two or more generated targets whose contracts require derivation from one immutable, plan-bound source-snapshot identity and whose orchestration requires one bounded aggregate attempt result.

Each member retains exactly one registered target identity, one renderer invocation and one lifecycle-owned target result. The aggregate attempt result is workflow-orchestration output only. It MUST NOT create a consumer trust state, acceptance-state record, canonical authority, target write owner or independent persistent state.

Aggregate success may be reported only when every required member has completed its own lifecycle-owned verification, required gates and target-scoped acceptance, and every declared secondary effect and cleanup obligation has verified success.

Aggregate failure preserves every member's actual lifecycle and trust-state outcome and creates one bounded orchestration recovery identity. It MUST NOT downgrade, promote or replace a target's lifecycle-owned acceptance state.

### 2.5 Secondary writer effect

A **secondary writer effect** is a mutation performed by a command mode in addition to its primary effect.

Every secondary writer effect MUST be declared, authorized, plan-bound and verified. A mode is not read-only when an option or delegated path writes an outbox, report, state file, prompt, package or target.

### 2.6 Generated edit surface

A **generated edit surface** is a generated or projected artifact whose semantic facts derive from declared canonical authorities.

It is not a normal primary edit surface. A durable correction MUST change an authorized canonical source, contract or governed generator path and then regenerate or re-accept the target as applicable.

## 3. Candidate DPA-200 amendments

### 3.1 Insert after DPA-200 §6.4

#### 6.5 Semantic-fact authority

Every semantic fact represented in a generated or projected target MUST have exactly one declared canonical authority.

Multiple targets MAY represent the same semantic fact only as projections of that authority. A generated target, evidence record, mutation plan, report, review or historical region MUST NOT become an independent authority for the fact through repetition, convenience or direct repair.

When two writers appear able to author the same semantic fact, the document model is invalid until one of the following is established:

1. one is the canonical source mutator and the other only projects it;
2. both are subordinate steps of one governed composed mutation;
3. one is a compatibility alias with behavior equivalent to the canonical command;
4. one path is deprecated, blocked or migrated.

Unknown or ambiguous semantic-fact authority MUST fail loud before governed mutation or acceptance.

### 3.2 Insert after DPA-200 §7

#### 7.1 Command mutation ownership

Write ownership and command mutation authority are distinct.

The document lifecycle remains the sole write owner for projected targets, projected regions, partition bytes and lifecycle-owned acceptance state. A command may request or orchestrate that write only through a command mutation contract and the governed lifecycle.

A command that directly writes lifecycle-owned bytes is non-conforming even when its output is currently correct.

Manual, historical, migration, evidence, report and cleanup writers MUST remain within their declared owner class and MUST NOT acquire projection ownership through an implementation shortcut.

#### 7.2 Generated-surface edit rule

Direct editing of a generated edit surface MUST NOT be represented as a durable semantic correction.

Where emergency repair is separately permitted, the repair MUST:

- be explicitly classified as temporary and non-accepted;
- preserve the prior and repaired byte identities;
- identify the canonical correction still required;
- prevent the repaired target from silently becoming canonical input;
- require governed regeneration or re-acceptance before accepted use.

### 3.3 Add to DPA-200 §12 invalid states

18. one semantic fact has two independent canonical writers;
19. a command directly writes projected or partition bytes outside lifecycle ownership;
20. a generated target is treated as the normal semantic edit source;
21. a secondary writer effect is undeclared or outside the plan-bound changed-path conformance relation;
22. a compatibility alias has materially different mutation authority from its canonical command without an independent reviewed contract;
23. a synchronized projection set combines members generated from different plan-bound source snapshots while claiming one completed aggregate attempt;
24. a command mutation contract is duplicated in independently editable runtime-authority stores.

## 4. Candidate DPA-300 amendments

### 4.1 Insert in DPA-300 §4 Responsibility boundaries

#### 4.6 Command integration

Every externally invocable command mode, compatibility alias with materially distinct behavior, and independently schedulable or independently recoverable composed mutation step that can authorize document-like mutation MUST resolve through one reviewed command mutation contract before mutation.

An internal helper, lifecycle method, adapter or delegated function that cannot independently broaden authority, select additional targets, persist independent authoritative state, be invoked outside the owning operation or produce an independently recoverable result inherits the owning command mutation contract and MUST NOT define a competing command mutation contract.

Delegation MUST remain statically reviewable. An inherited internal path MUST NOT broaden the owning contract's target set, changed-path boundary, source authority, secondary effects, lock scope, verification obligations or recovery authority.

Each materially different authority-bearing mode MUST be classified separately. Dry-run, execute, repair, refresh, normalize, cleanup, post-merge and compatibility-alias modes MUST NOT be collapsed when their effects differ.

A command mutation contract MUST identify:

- public command and aliases;
- delegated internal entry point or inherited subordinate boundary;
- primary command mutation class;
- constrained secondary effects;
- canonical input authorities;
- Workspace-resolved targets;
- maximum authorized changed-path boundary;
- required, conditional and temporary path outcomes;
- lifecycle, state, workflow, evidence, migration or retention owner;
- lock scope and composed-command ordering;
- verification and acceptance effects;
- recovery and compatibility disposition.

Unknown classification, runtime home, target ownership or changed-path boundary MUST prevent mutation.

#### 4.7 Alias equivalence

A compatibility alias MAY delegate to a canonical command only when both resolve to the same command mutation contract and produce equivalent authority, target, changed-path, verification, acceptance and evidence behavior for equivalent inputs.

Alias choice alone MUST NOT alter target freshness when the alias is proven contract-equivalent and the accepted target contract does not distinguish it.

A deprecated alias remains a live mutator until execution is blocked or removed. Deprecation text alone does not reduce its authority or Probe obligations.

### 4.2 Insert in DPA-300 §8 Mutation plan

#### 8.4 Command-bound mutation intent

For a command-initiated governed mutation, the immutable plan MUST additionally bind:

- command identity;
- command-contract schema and semantic version;
- invocation mode;
- declared primary class and secondary effects;
- maximum authorized changed-path boundary;
- required changes and conditional path predicates;
- temporary-path cleanup or retention outcomes;
- composed-command identity and ordered authority-bearing child-step identities where applicable;
- source-snapshot identity for a synchronized projection set;
- expected per-step and derived aggregate completion conditions.

A generic execute request, alias invocation or later orchestration step MUST NOT broaden the plan's authority.

Any output-affecting or authority-affecting change in command identity, command-contract semantics, invocation mode, target set, secondary effects, path predicates or composed ordering invalidates the active plan.

### 4.3 Insert after DPA-300 §10

#### 10.5 Plan-bound changed-path conformance

Every mutating command MUST bind a plan-scoped changed-path conformance relation before mutation.

The plan MUST distinguish, directly or through equivalent predicates:

- the maximum authorized changed-path boundary;
- paths or path classes required to change after plan-bound preconditions are resolved;
- conditionally permitted paths whose change or non-change is governed by explicit plan-bound predicates;
- declared temporary paths and their required cleanup or retention outcome.

The actual changed-path set MUST be a subset of the maximum authorized boundary. Every required change MUST occur. Every conditional path outcome MUST satisfy its bound predicate. Every temporary path MUST satisfy its cleanup or retention contract.

Any unauthorized changed path, missing required change, violated conditional predicate or unexplained residual temporary path is mutation failure.

A verified no-op is one explicitly declared conditional outcome. It is not a blanket exception and MUST NOT broaden authority or suppress missing required work.

Changed-path conformance does not replace content, semantic, ownership, lifecycle, acceptance or recovery verification.

### 4.4 Insert in DPA-300 §11 Post-write verification

#### 11.x Command and aggregate verification

Post-write verification for a command mutation MUST verify, as applicable:

- every lifecycle-owned target under its own target contract;
- every canonical state mutation under its state contract;
- every secondary writer effect;
- plan-bound changed-path conformance;
- command-contract identity;
- source-snapshot identity;
- alias equivalence when an alias was used;
- per-target completion and derived aggregate completion for a synchronized projection set.

Command success, child-step success or the existence of expected files is insufficient.

A synchronized projection set MUST NOT be reported as aggregate success when any required member failed generation, write, verification, acceptance or cleanup. Partial completion creates an explicit orchestration recovery obligation and MUST NOT be normalized by regenerating only the visibly stale member without a new governed plan.

### 4.5 Insert in DPA-300 recovery provisions

Target recovery remains lifecycle-owned per registered target.

For a composed mutation or synchronized projection set, workflow orchestration MUST record one bounded aggregate recovery identity that references, but does not replace, the actual per-target lifecycle outcomes and declared secondary effects.

Recovery MUST NOT:

- infer aggregate success from a subset of accepted members;
- silently rerun one member under stale source assumptions;
- use a generated member as the source for another member;
- erase evidence of an unauthorized changed path;
- convert a temporary direct repair into accepted state;
- fabricate all-or-nothing rollback where target-specific contracts do not provide it.

A new aggregate attempt requires a new plan-bound source-snapshot identity and current per-target plans. Already accepted target results may be reused only when their current contracts explicitly permit reuse and all required freshness and aggregate-snapshot conditions are revalidated.

New mutation remains blocked until every unresolved member, secondary effect and changed-path failure is dispositioned.

### 4.6 Add DPA-300 abstract failure semantics

DPA-300 owns abstract lifecycle and mutation-attempt failure semantics for:

- unclassified mutation-authority boundary;
- unauthorized direct writing;
- unauthorized changed path;
- missing required output;
- violated conditional-path predicate;
- undeclared or failed secondary writer effect;
- alias or delegated-path authority divergence;
- command-contract mismatch or invalidation;
- composed-step ordering or recovery failure.

These are command-plan, mutation-attempt, verification or recovery failures. They MUST NOT automatically classify previously accepted target bytes as stale.

Concrete production finding identifiers, severities, serialization and wording remain owned by the existing main-repository finding authority.

## 5. Candidate DPA-400 amendments

### 5.1 Insert after DPA-400 §18

#### 18.1 Generator command and renderer separation

A generator command and a renderer are not synonymous.

A generator command MAY resolve inputs, request lifecycle work, coordinate several target refreshes and emit bounded reports. The renderer remains a pure deterministic function for exactly one registered target and MUST NOT:

- write any target or state;
- select or broaden command authority;
- trigger another renderer;
- update handoff, status, evidence, acceptance or workflow state;
- decide derived aggregate success for a synchronized projection set.

An existing implementation that combines rendering and writing MUST be decomposed or bounded so that target writes occur only through lifecycle ownership. Calling a combined function a renderer does not make it conforming.

#### 18.2 Generator determinism

Generator determinism is evaluated over the declared command contract, canonical inputs, configuration, child-target contracts, plan-bound source snapshot and orchestration order.

Renderer determinism for individual targets does not prove generator determinism, changed-path conformance or aggregate snapshot consistency.

Variable evidence fields, timestamps and temporary paths MUST be excluded or normalized only by explicit contract.

## 6. Candidate DPA-500 amendments

### 6.1 Insert in DPA-500 §5 or §7

Where an accepted target contract declares command identity or command semantics output-affecting or acceptance-affecting, freshness evaluation MUST include:

- command-contract identity, schema and semantic version;
- invocation mode when semantically relevant;
- target and secondary-effect declarations relevant to acceptance;
- composed-command order when relevant;
- synchronized source-snapshot identity where applicable.

A change in output-affecting command semantics is `contract drift` unless an accepted later decision introduces a more specific existing DPA-100 drift mapping. It MUST NOT be hidden as renderer-only or target-only drift.

A command-contract change that broadens authority, target set, source set, secondary effects, ordering or verification obligations invalidates an active mutation plan even when current target bytes remain equal.

Plan validity, target freshness, consumer trust state, command conformance and derived aggregate attempt outcome remain distinct dimensions.

### 6.2 Insert in DPA-500 finding and gate provisions

DPA-500 owns projection-freshness and gate consequences only when:

- an accepted target contract declares command semantics output-affecting or acceptance-affecting;
- a registered projection has a mixed source snapshot;
- a synchronized projection attempt is only partially complete;
- a generated surface was edited directly in a way relevant to registered target evaluation;
- a generated reference is stale under the registered projection contract;
- a DPA-300 failure prevents safe projection evaluation, mutation or acceptance.

DPA-500 MUST preserve the distinction between:

- DPA-300 mutation-attempt failure;
- target freshness classification;
- consumer trust state;
- gate decision;
- enforcement stage;
- derived aggregate attempt outcome.

A DPA-300 command failure may produce a DPA-500 gate `failure` for the active projection operation without making independently verifiable, previously accepted bytes stale.

Unknown mutation authority, unauthorized lifecycle-byte writing, unauthorized changed paths, mixed source snapshots and false aggregate completion affect mutation safety and MUST fail closed for new mutation and acceptance.

Staged adoption MAY initially observe or warn for already-existing legacy readers and non-mutating references, but it MUST NOT authorize a new unclassified write, a direct generated-surface repair as accepted state or acceptance of an incompletely verified synchronized projection set.

All proposal-local diagnostic labels remain abstract subreasons. Concrete identifiers, severity mappings, serialization, suppression and user-facing wording remain owned by the existing main-repository finding authority and remain `NEEDS_MAIN_REPO_VALIDATION`.

## 7. Synchronized traceability candidates

The later normative amendment should add one traceability row per requirement group rather than one row per repository command.

| Proposal-local ID | Requirement group | Normative owner |
|---|---|---|
| `DMA-001` | one semantic fact, one canonical authority | DPA-200 |
| `DMA-002` | generated surfaces are not normal edit sources | DPA-200 |
| `DMA-003` | write ownership distinct from command orchestration | DPA-200 / DPA-300 |
| `DMA-004` | one contract per authority-bearing mode or independently recoverable step; helpers inherit | DPA-300 |
| `DMA-005` | alias equivalence or independent classification | DPA-300 |
| `DMA-006` | immutable plan binds command authority, path predicates and target set | DPA-300 |
| `DMA-007` | plan-bound changed-path conformance | DPA-300 |
| `DMA-008` | secondary writer effects are declared and verified | DPA-300 |
| `DMA-009` | synchronized set preserves per-target acceptance and derived aggregate result | DPA-300 |
| `DMA-010` | renderer remains pure under generator orchestration | DPA-400 |
| `DMA-011` | generator determinism distinct from renderer determinism | DPA-400 |
| `DMA-012` | command-aware projection freshness and gate consequences | DPA-500 |

These identifiers remain proposal-local until a governed normative amendment assigns stable traceability identities. They do not create a second invariant namespace.

## 8. Diagram amendment candidate

A synchronized diagram amendment should add only these relationships to the existing architecture:

1. `CLI command mode -> command mutation contract`;
2. `command mutation contract -> one existing authority family`;
3. `inherited helper -> owning command mutation contract`;
4. `generator orchestration -> lifecycle request(s)`;
5. `lifecycle -> one target write and target-scoped acceptance result per target`;
6. `workflow orchestration -> derived aggregate attempt result`;
7. `changed-path verifier -> command result`.

The diagram MUST NOT introduce a DPA command registry, aggregate acceptance database, aggregate trust state, DPA writer service, DPA state store or second lifecycle.

## 9. Review and acceptance gates

This consolidated draft is ready for independent review only when the reviewer can determine:

1. every clause extends an existing authority rather than creating a parallel system;
2. command-contract granularity excludes subordinate helper proliferation without allowing bypass;
3. command-contract runtime authority is singular and not duplicated;
4. DPA-200, DPA-300, DPA-400 and DPA-500 ownership is correctly divided;
5. synchronized projection sets preserve one-renderer/one-target and target-scoped acceptance;
6. derived aggregate outcome does not become acceptance authority or persistent state;
7. alias, secondary-writer, path-conformance and recovery rules are testable;
8. DPA-300 mutation-attempt failures remain distinct from DPA-500 freshness and gates;
9. repository-specific claims remain appropriately provisional;
10. DPA-600 remains frozen and DPA-700 remains unstarted.

## 10. Remaining blocked work

Before any normative amendment or main-repository implementation:

- exact-ref local command, helper, writer, state, lock, lifecycle, recovery and finding inventories must be completed;
- the existing runtime home for command mutation contracts must be selected and validated;
- proposed Probe consequences must be adjudicated without silently changing immutable Probe identities;
- DPA-200 through DPA-500 traceability and diagrams must be amended synchronously;
- independent review and Maintainer adjudication of the exact amendment text must complete;
- applicable Probe evidence and later post-amendment verification remain required.

No statement in this draft claims current main-repository conformance.