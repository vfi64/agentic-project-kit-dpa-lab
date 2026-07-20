# Document Mutation Authority and Command Integration Plan

Status: active

Status-date: 2026-07-19

Superseded-by: n/a

## 1. Purpose

This document is the binding planning addendum for integrating every Agentic Kit command that creates, refreshes, rewrites, reconciles, appends, moves, archives or deletes document-like artifacts into the Document Projection Architecture.

It closes a planning gap: the current DPA already separates registry, renderer, lifecycle, workflow, evidence, freshness and gates, but it does not yet provide a complete command-to-mutation-authority contract for all existing document-producing and document-updating Agentic Kit commands.

This plan is not production implementation and does not claim that current commands conform. It defines the investigation, architecture-amendment, Probe and implementation work required to make that claim possible.

## 2. Problem statement

The failure class that motivated the DPA cannot be excluded merely by adding pure renderers or projection metadata.

A handoff, status, planning, reference or report artifact can still drift when:

- more than one command writes the same semantic fact independently;
- a generated document is manually edited instead of changing its canonical source;
- a command writes both authoritative state and derived prose without one governed mutation plan;
- the declared output scope differs from the actual changed-path set;
- a refresh command silently preserves stale sections;
- a report or evidence writer becomes an accidental state authority;
- a command bypasses Workspace resolution or writes a legacy path under a namespace profile;
- one command updates a source while another command updates only a projection;
- generated files are accepted without post-write verification against their declared sources;
- command composition causes a later subcommand to overwrite a correct earlier projection.

The DPA must therefore govern not only documents and renderers, but the complete mutation authority graph of document-producing commands.

## 3. Governing principles

### 3.1 Mutation intent before file write

A command MUST express a governed mutation intent before any document write occurs.

A file path or CLI verb alone is not mutation authority.

### 3.2 One semantic fact, one canonical authority

The same semantic fact MUST NOT be authored independently by multiple commands or files.

Multiple projections MAY display the fact, but they MUST derive it from the same declared canonical authority.

### 3.3 Generated artifacts are not primary edit surfaces

A generated or projected artifact MUST NOT be treated as the normal source of a semantic change.

The responsible canonical source, mutation command and regeneration path MUST be known before editing.

### 3.4 Existing authority families remain authoritative

The DPA SHALL extend the existing registry, lifecycle, Workspace, state, workflow, evidence and gate systems. It SHALL NOT create a second command registry, second writer authority, second lifecycle or second state store.

### 3.5 Actual write scope must equal authorized write scope

Every mutating command MUST have a declared output scope and MUST verify the actual changed-path set against that scope.

Unexpected changed paths are a failure, not an informational warning.

### 3.6 Post-write verification is mandatory for governed outputs

A command success return code does not prove document correctness.

Governed document outputs require reread, byte or semantic comparison as appropriate, source/contract fingerprint verification and bounded evidence.

## 4. Command mutation classes

Every relevant Agentic Kit command and internal entry point MUST receive exactly one primary class and zero or more constrained secondary effects.

### CMA-1 — Canonical source mutator

May change an accepted canonical authority such as reviewed registry data, explicit state or another approved source.

It MUST NOT directly invent independent projection prose.

### CMA-2 — Lifecycle projection mutator

May write a registered full projection or registered region only through the governed lifecycle sequence.

It MUST use declared sources, contracts, immutable planning, locking, post-write verification and acceptance handling.

### CMA-3 — State transition mutator

May change lifecycle-owned or workflow-owned state but MUST NOT independently author projected target content.

### CMA-4 — Evidence and report writer

May write logs, reports and evidence. Its output MUST NOT become canonical state, implicit acceptance or authorization for later mutation.

### CMA-5 — Derived reference generator

May generate command references, indexes, summaries or other derived documentation from declared authoritative inputs.

It MUST declare whether the output is a governed projection, disposable report or reviewable generated reference.

### CMA-6 — Migration or archival mutator

May move, archive, split or retire documents only under an approved migration plan with source preservation, rollback and authority-transfer rules.

### CMA-7 — Cleanup or garbage-collection mutator

May delete only artifacts whose retention policy explicitly permits deletion. It MUST fail closed for unknown document ownership.

### CMA-8 — Read-only inspector

May read and report but performs no repository or document mutation.

A command with materially different modes MUST classify each mode separately. A dry-run mode is not evidence that execute mode has the same authority boundary.

## 5. Required command-to-document authority record

For every document-producing or document-updating command, the inventory MUST record:

- public CLI path and aliases;
- internal entry point and delegated call chain;
- command mode, including dry-run and execute variants;
- primary mutation class;
- canonical input authorities;
- registry and Workspace resolution paths;
- declared target paths or target classes;
- actual discovered write paths;
- complete-file, region, append, replace, rename, move or delete semantics;
- whether output is canonical, projected, generated-reference, state, evidence, temporary or historical;
- renderer identity where applicable;
- lifecycle ownership where applicable;
- lock ownership and scope;
- workflow serialization requirements;
- preflight and stale-plan behavior;
- post-write verification behavior;
- acceptance or trust-state effect;
- evidence emitted;
- cleanup and rollback behavior;
- legacy-profile behavior;
- namespace-profile behavior;
- known callers and composed commands;
- Probe coverage;
- implementation disposition.

Unknown fields MUST remain explicit `NEEDS_MAIN_REPO_VALIDATION` or `verification-blocked`; they MUST NOT be inferred from command names.

## 6. Required architecture amendments

The command integration work is expected to require a bounded amendment package after exact-ref evidence and review.

### DPA-200

Add or clarify:

- generated document and generated region classification;
- canonical source versus generated target distinction;
- document mutation owner and command mutation authority;
- complete-byte and semantic-fact ownership;
- manual-edit prohibition for generated surfaces;
- authority transfer during migration.

### DPA-300

Add or clarify:

- command-to-mutation-authority contract;
- adaptation of existing commands into governed lifecycle entry points;
- declared versus actual output-scope equality;
- composed-command behavior;
- prohibition of independent multi-writer semantic facts;
- generator/source relationship;
- post-write verification for non-renderer generated references where applicable;
- fail-loud behavior for unknown ownership or unclassified mutators.

### DPA-400

Clarify:

- pure renderer boundary versus generator command;
- a generator command may orchestrate lifecycle work but the renderer remains pure;
- existing commands that both render and write must be decomposed or wrapped through lifecycle authority;
- renderer output alone cannot update status, handoff, evidence or acceptance state.

### DPA-500

Add or clarify:

- freshness for command-generated documents;
- command identity, command-contract version and declared input-set identity where output semantics depend on them;
- stale generated-reference and stale projection findings;
- gate behavior for unauthorized writers, unexpected output scope and direct edits;
- staged enforcement for newly classified command writers.

### DPA-600

After its freeze is released by applicable evidence, add:

- serialization of composed document-mutating commands;
- cross-ref regeneration ownership;
- prevention of concurrent commands independently rewriting the same semantic projection;
- command-plan identity and stale-plan invalidation.

### DPA-700

When permitted to begin, add:

- migration of existing command writers;
- compatibility wrappers and deprecation;
- rollback from adapted commands;
- removal of direct-write paths only after replacement evidence.

DPA-800 must convert the accepted architecture into bounded implementation slices and command migration order.

## 7. Remote iPhone work package

The following work is safe before Mac access because it is read-only against the main repository and planning-only in the Lab.

### C1 — Complete command discovery

Inspect all CLI groups, aliases and internal entry points that may create or modify document-like files.

Search families include:

- `write_`, `_write_`, `render_`, `generate_`, `refresh_`, `reconcile`, `compile`, `finalize`, `archive`, `move`, `rename`, `replace`, `unlink` and `rmtree`;
- direct `Path.write_text`, `write_bytes`, `open(..., "w")`, `yaml.safe_dump` and JSON writers;
- Git restore or checkout operations that replace generated documents;
- composed commands that invoke other mutators.

### C2 — Build command-to-document inventory

Produce one row per command mode and one row per internal mutator that has no direct CLI surface.

Do not collapse different execute, dry-run, repair, refresh, post-merge or cleanup modes.

### C3 — Build semantic-fact overlap matrix

For handoff, status, planning, command reference, registry, lifecycle and evidence families, record where the same semantic fact is read or written by multiple paths.

Classify each overlap as:

- legitimate shared read;
- one source with multiple projections;
- composed mutation under one authority;
- duplicate writer;
- conflicting authority;
- unknown pending local evidence.

### C4 — Build generated-artifact ownership matrix

For each artifact family, identify:

- canonical source;
- generated target;
- generating command;
- direct-edit policy;
- regeneration trigger;
- freshness rule;
- acceptance rule;
- retention rule;
- migration requirement.

### C5 — Map command coverage to Probes

Extend Probe planning so that relevant cases cover:

- command output-scope enforcement;
- generator determinism;
- direct-edit detection;
- duplicate-writer detection;
- composed-command ordering;
- Workspace profile resolution;
- post-write verification;
- stale generation inputs;
- failure after partial command composition;
- evidence that generated targets were not manually authored.

### C6 — Prepare amendment and review package

Prepare exact proposed clauses, traceability changes, diagram changes and a bounded independent-review prompt.

Normative DPA files MUST NOT be amended until the proposal is reviewed against the complete remote inventory and later bounded by local exact-ref evidence where required.

## 8. Local Mac validation package

Before command adaptation or normative repository-specific claims:

1. confirm remote/local exact-ref equality;
2. enumerate CLI commands from the installed local package;
3. run read-only help and manifest commands;
4. trace candidate command call chains locally;
5. execute only approved commands in a disposable fixture repository;
6. capture complete before/after file inventories and hashes;
7. compare declared and actual write scope;
8. verify Workspace profile behavior;
9. test composed-command ordering and failure paths;
10. classify every command as conforming, adaptable, replaceable, deprecated or blocked;
11. preserve exact command, environment, repository and fixture refs.

No production workspace may be used as the first execution target.

## 9. Implementation requirements

No command is considered integrated merely because it calls a shared helper.

Integration requires:

- explicit mutation class;
- declared authority and input set;
- Workspace-resolved targets;
- exact output scope;
- lifecycle routing where target bytes are governed projections;
- lock and workflow boundaries appropriate to the mutation;
- post-write verification;
- bounded findings and evidence;
- focused tests;
- namespace-profile negative tests;
- compatibility and migration disposition;
- removal or fail-loud blocking of superseded direct-write paths.

Commands that currently generate correct output but lack authority, scope or verification controls still require adaptation.

## 10. Hard restrictions

Until PROBE-002 execution, adjudication and architecture revalidation:

- no quick fix to current handoff, status or lifecycle writers;
- no replacement of existing command semantics merely to satisfy the proposed architecture;
- no invented command registry or second lifecycle;
- no direct manual patch presented as the durable fix for a generated artifact;
- no DPA-600 continuation;
- no DPA-700 work;
- no claim that the command inventory is globally complete without local confirmation.

Read-only inventory and planning are permitted and required.

## 11. Exit criteria

This planning package is complete when:

- the remote command-to-document inventory is complete for the inspected ref;
- semantic-fact overlaps and generated-artifact ownership are mapped;
- every command mode has a provisional mutation class;
- unresolved paths are explicit;
- the proposed ADR and bounded DPA amendment package are prepared;
- Probe coverage changes are mapped;
- the local exact-ref validation procedure is executable;
- an independent review has assessed authority completeness and parallel-system risk.

Architecture completion requires the later reviewed normative amendments. Implementation completion requires exact-ref main-repository changes, tests, migration evidence and removal or blocking of superseded direct-write paths.

## 12. Proactive architecture-gap rule

During all future DPA work, the working agent MUST surface material architecture gaps when repository evidence, command behavior or cross-document relationships reveal that the current plan would not exclude the motivating failure class.

The agent MUST distinguish:

- a confirmed architecture gap;
- a suspected gap requiring evidence;
- an implementation defect under an already adequate contract;
- an editorial inconsistency;
- an out-of-scope improvement.

Silence is not appropriate merely because the Maintainer did not know to ask about a specialist concern.