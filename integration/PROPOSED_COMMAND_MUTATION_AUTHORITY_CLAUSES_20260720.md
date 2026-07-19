# Proposed Command Mutation Authority Clauses

Status: review-candidate

Status-date: 2026-07-20

Authority: non-normative Package M amendment proposal

Depends-on:

- `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`;
- `integration/REMOTE_COMMAND_MUTATION_INVENTORY_20260719.md`;
- `integration/REMOTE_HANDOFF_AND_TRANSFER_MUTATION_MAP_20260719.md`;
- `integration/SEMANTIC_FACT_OVERLAP_MATRIX_20260719.md`;
- `integration/GENERATED_ARTIFACT_OWNERSHIP_MATRIX_20260719.md`;
- `integration/COMMAND_MUTATION_PROBE_COVERAGE_MAP_20260719.md`;
- `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`.

## 1. Purpose and boundary

This document prepares exact candidate clauses for a later synchronized amendment of DPA-200, DPA-300, DPA-400 and DPA-500.

It is not normative. It does not change the status of ADR-022, amend any DPA specification, authorize implementation, execute a Probe or claim complete main-repository command coverage.

Every repository-specific mapping remains `NEEDS_MAIN_REPO_VALIDATION` until exact-ref local validation and Maintainer adjudication.

DPA-600 remains frozen. DPA-700 remains unstarted.

## 2. Closed terms proposed for shared use

### 2.1 Document mutation authority

A **document mutation authority** is the already-governed registry, lifecycle, state, workflow, evidence, migration or retention authority under which one command mode may cause one declared class of document-like mutation.

A CLI path, alias, helper function or file path is not authority by itself.

### 2.2 Command mutation contract

A **command mutation contract** is the reviewed declaration that binds one command mode to:

- exactly one primary command mutation class;
- zero or more constrained secondary effects;
- canonical input authorities;
- Workspace-resolved target identities;
- authorized changed-path scope;
- write semantics;
- lifecycle, lock and workflow ownership;
- verification, trust-state and evidence effects;
- compatibility and migration disposition.

The contract extends existing runtime authorities. It is not a second command registry or lifecycle.

### 2.3 Synchronized projection set

A **synchronized projection set** is two or more generated targets that represent one accepted source snapshot and whose contract requires generation, verification and acceptance as one logical result.

A synchronized projection set does not make one renderer invocation responsible for multiple independently registered projection targets. Each governed target retains its own target identity and lifecycle result. Orchestration may bind those results to one source-snapshot identity and one higher-level completion decision.

### 2.4 Secondary writer effect

A **secondary writer effect** is a mutation performed by a command mode in addition to its primary effect.

Every secondary writer effect must be declared, authorized and included in the actual changed-path comparison. A user-facing diagnostic or normalization mode is not read-only when an option or delegated path writes an outbox, report, state file, prompt, package or target.

### 2.5 Generated edit surface

A **generated edit surface** is a generated or projected artifact whose semantic facts derive from declared canonical authorities.

It is not a normal primary edit surface. A durable correction must change an authorized canonical source, contract or governed generator path and then regenerate the target.

## 3. Candidate DPA-200 amendments

### 3.1 Proposed addition after DPA-200 §6.4

#### 6.5 Semantic-fact authority

Every semantic fact represented in a generated or projected target MUST have exactly one declared canonical authority.

Multiple targets MAY represent the same semantic fact only as projections of that authority. A generated target, evidence record, mutation plan, report, review or historical region MUST NOT become an independent authority for the fact through repetition, convenience or direct repair.

When two writers appear able to author the same semantic fact, the document model is invalid until one of the following is established:

1. one is the canonical source mutator and the other only projects it;
2. both are subordinate steps of one governed composed mutation;
3. one is a compatibility alias with behavior equivalent to the canonical command;
4. one path is deprecated, blocked or migrated.

Unknown or ambiguous semantic-fact authority MUST fail loud before governed mutation or acceptance.

### 3.2 Proposed addition after DPA-200 §7

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

### 3.3 Proposed additions to DPA-200 §12 invalid states

Add the following invalid states:

18. one semantic fact has two independent canonical writers;
19. a command directly writes projected or partition bytes outside lifecycle ownership;
20. a generated target is treated as the normal semantic edit source;
21. a secondary writer effect is undeclared or outside the authorized changed-path scope;
22. a compatibility alias has materially different mutation authority from its canonical command without an independent reviewed contract;
23. a synchronized projection set combines members generated from different accepted source snapshots while claiming one completed refresh.

## 4. Candidate DPA-300 amendments

### 4.1 Proposed addition to DPA-300 §4 Responsibility boundaries

#### 4.6 Command integration

Every command mode and internal entry point that may create, rewrite, append, replace, move, archive or delete a document-like artifact MUST resolve through one reviewed command mutation contract before mutation.

Each materially different mode MUST be classified separately. Dry-run, execute, repair, refresh, normalize, cleanup, post-merge and compatibility-alias modes MUST NOT be collapsed when their effects differ.

A command mutation contract MUST identify:

- public command and aliases;
- delegated internal entry point;
- primary command mutation class;
- constrained secondary effects;
- canonical input authorities;
- Workspace-resolved targets;
- authorized changed-path scope;
- lifecycle, state, workflow, evidence, migration or retention owner;
- lock scope and composed-command ordering;
- verification and acceptance effects;
- recovery and compatibility disposition.

Unknown classification, target ownership or changed-path scope MUST prevent mutation.

#### 4.7 Alias equivalence

A compatibility alias MAY delegate to a canonical command only when both resolve to the same command mutation contract and produce equivalent authority, target, changed-path, verification, acceptance and evidence behavior for equivalent inputs.

A deprecated alias remains a live mutator until execution is blocked or removed. Deprecation text alone does not reduce its authority or Probe obligations.

### 4.2 Proposed addition to DPA-300 §8 Mutation plan

#### 8.4 Command-bound mutation intent

For a command-initiated governed mutation, the immutable plan MUST additionally bind:

- command identity;
- command-contract schema and semantic version;
- invocation mode;
- declared primary class and secondary effects;
- authorized target and changed-path set;
- composed-command identity and ordered child-step identities where applicable;
- source-snapshot identity for a synchronized projection set;
- expected per-step and aggregate completion conditions.

A generic execute request, alias invocation or later orchestration step MUST NOT broaden the plan's authority.

Any change in command identity, command-contract semantics, invocation mode, target set, secondary effects or composed ordering invalidates the plan.

### 4.3 Proposed addition after DPA-300 §10

#### 10.5 Declared and actual changed-path equality

Every mutating command MUST capture a pre-state path inventory appropriate to its authorized scope and MUST compare the actual post-operation changed-path set with the plan-authorized set.

Unexpected created, modified, moved, archived or deleted paths are mutation failure.

A missing expected path is also failure unless the command contract explicitly permits a no-op and the no-op condition is verified.

Temporary paths MAY be excluded only when their location, retention, cleanup and evidence treatment are contract-declared. Unexplained residual temporary state is failure.

Changed-path equality does not replace content, semantic, ownership or acceptance verification.

### 4.4 Proposed addition to DPA-300 §11 Post-write verification

#### 11.x Command and aggregate verification

Post-write verification for a command mutation MUST verify, as applicable:

- every lifecycle-owned target under its own target contract;
- every canonical state mutation under its state contract;
- every secondary writer effect;
- actual changed-path equality;
- command-contract identity;
- source-snapshot identity;
- alias equivalence when an alias was used;
- aggregate completion of a synchronized projection set.

Command success, child-step success or the existence of expected files is insufficient.

A synchronized projection set MUST NOT be reported as complete when any member failed generation, write, verification, acceptance or cleanup. Partial completion creates an explicit recovery obligation and MUST NOT be normalized by regenerating only the visibly stale member without a new governed plan.

### 4.5 Proposed addition to recovery provisions

Recovery for a composed mutation or synchronized projection set MUST classify each member and secondary effect separately while preserving one aggregate recovery identity.

Recovery MUST NOT:

- infer aggregate success from a subset of accepted members;
- silently rerun only one member under stale source assumptions;
- use a generated member as the source for another member;
- erase evidence of an undeclared changed path;
- convert a temporary direct repair into accepted state.

New mutation remains blocked until every unresolved member, secondary effect and changed path is dispositioned.

## 5. Candidate DPA-400 amendments

### 5.1 Proposed pure-renderer clarification

A generator command and a renderer are not synonymous.

A generator command MAY resolve inputs, request lifecycle work, coordinate several target refreshes and emit bounded reports. The renderer remains a pure deterministic function for exactly one registered target and MUST NOT:

- write any target or state;
- select or broaden command authority;
- trigger another renderer;
- update handoff, status, evidence, acceptance or workflow state;
- decide aggregate success for a synchronized projection set.

An existing implementation that combines rendering and writing MUST be decomposed or wrapped so that target writes occur only through lifecycle ownership. Calling the combined function a renderer does not make it conforming.

### 5.2 Proposed generator determinism clarification

Generator determinism is evaluated over the declared command contract, canonical inputs, configuration, child-target contracts and orchestration order.

Renderer determinism for individual targets does not prove generator determinism or aggregate snapshot consistency.

Variable evidence fields, timestamps and temporary paths MUST be excluded or normalized only by explicit contract.

## 6. Candidate DPA-500 amendments

### 6.1 Proposed freshness inputs

Where output semantics depend on command orchestration, freshness evaluation MUST include:

- command identity;
- command-contract schema and semantic version;
- invocation mode;
- authorized target and changed-path set;
- declared secondary effects;
- composed-command order;
- synchronized source-snapshot identity where applicable.

A change in any output-affecting command input is command-contract drift and MUST NOT be hidden as renderer-only or target-only drift.

### 6.2 Proposed findings

DPA-500 should define distinct findings for:

- `unclassified-command-mutator`;
- `unauthorized-direct-writer`;
- `unexpected-changed-path`;
- `missing-expected-output`;
- `undeclared-secondary-writer`;
- `alias-authority-divergence`;
- `direct-generated-surface-edit`;
- `mixed-source-snapshot`;
- `partial-synchronized-projection-set`;
- `stale-generated-reference`.

These findings MUST remain distinct from target freshness, trust state, gate decision and enforcement stage.

### 6.3 Proposed gate behavior

Unknown mutation authority, unauthorized lifecycle-byte writing, unexpected changed paths, mixed source snapshots and false aggregate completion affect mutation safety and MUST fail closed for new mutation and acceptance.

Staged adoption MAY initially observe or warn for already-existing legacy readers and non-mutating references, but it MUST NOT authorize a new unclassified write, a direct generated-surface repair as accepted state or acceptance of an incompletely verified synchronized projection set.

## 7. Candidate traceability additions

The later normative amendment should add one traceability row per requirement group, not one row per repository command.

Proposed stable requirement identifiers:

| Proposed ID | Requirement group | Normative owner |
|---|---|---|
| `DMA-001` | one semantic fact, one canonical authority | DPA-200 |
| `DMA-002` | generated surfaces are not normal edit sources | DPA-200 |
| `DMA-003` | write ownership distinct from command orchestration | DPA-200 / DPA-300 |
| `DMA-004` | one command mutation contract per materially distinct mode | DPA-300 |
| `DMA-005` | alias equivalence or independent classification | DPA-300 |
| `DMA-006` | immutable plan binds command authority and target set | DPA-300 |
| `DMA-007` | authorized and actual changed-path equality | DPA-300 |
| `DMA-008` | secondary writer effects are declared and verified | DPA-300 |
| `DMA-009` | synchronized projection-set snapshot and aggregate completion | DPA-300 |
| `DMA-010` | renderer remains pure under generator orchestration | DPA-400 |
| `DMA-011` | generator determinism is distinct from renderer determinism | DPA-400 |
| `DMA-012` | command-contract freshness and distinct findings | DPA-500 |

The identifiers are proposal-local until the amendment is accepted. They MUST NOT create a second invariant namespace or duplicate existing DPA invariants.

## 8. Candidate diagram change

A later diagram amendment should add only these edges to the existing architecture:

1. `CLI command mode -> command mutation contract`;
2. `command mutation contract -> existing authority family`;
3. `generator orchestration -> lifecycle request(s)`;
4. `lifecycle -> one target write and acceptance result per target`;
5. `aggregate coordinator -> synchronized projection-set completion decision`;
6. `changed-path verifier -> command result`.

The diagram MUST NOT introduce a DPA command registry, DPA state store, DPA writer service or second lifecycle box.

## 9. Probe consequences

The existing Probe manuals remain unchanged by this proposal.

Before a normative amendment is accepted, the six candidates in `integration/COMMAND_MUTATION_PROBE_COVERAGE_MAP_20260719.md` must be adjudicated as:

- new PROBE-002 cases;
- extensions of existing cases with preserved original meaning;
- a separate bounded command-integration Probe;
- or blocked pending exact-ref local discovery.

No existing PASS condition may be broadened after execution without a new immutable Probe identity.

## 10. Acceptance conditions for this clause package

This proposal is ready for independent review only when reviewers can determine:

1. whether every clause extends an existing authority rather than creating a parallel system;
2. whether DPA-200, DPA-300, DPA-400 and DPA-500 ownership is correctly divided;
3. whether synchronized projection sets preserve the one-renderer/one-target rule;
4. whether command contracts add required authority without becoming a competing runtime registry;
5. whether alias, secondary-writer and changed-path rules are testable;
6. whether repository-specific claims remain appropriately provisional;
7. whether DPA-600 and DPA-700 sequencing restrictions remain intact.
