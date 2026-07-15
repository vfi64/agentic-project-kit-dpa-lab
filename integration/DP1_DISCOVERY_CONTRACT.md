# DP1 Discovery Contract

Status: active

Status-date: 2026-07-15

Authority: DPA-ADR-015

## 1. Purpose

This contract governs the early read-only Discovery stage of the single DP1 slice. It collects exact-ref facts needed to write DPA-300 against the real main-repository architecture instead of unchecked assumptions.

Discovery is evidence collection only. It is not implementation, migration, adoption, conformance testing or architecture adjudication.

## 2. Repository and validation ref

Target repository: `vfi64/agentic-project-kit`

Before execution, the operator MUST record one exact fetched `origin/main` commit as the validation ref. Every evidence record MUST name that ref.

No claim may be generalized beyond that validation ref without separate evidence.

## 3. Hard governance boundary

Discovery MUST be strictly read-only.

Discovery MUST NOT:

- modify the main repository;
- create commits, branches, pull requests or tags;
- create or modify registry entries;
- create production code or runtime files;
- initialize or simulate `.agentic/` state;
- run migrations or projection writes;
- change document contents;
- execute mutation-capable commands except in a proven no-write inspection mode;
- determine that an observed mechanism is sufficient for a future DPA contract;
- select a production document form;
- create, modify, accept or reject an architecture decision.

Discovery MAY replace an assumption with exact-ref evidence. Evidence remains non-normative.

## 4. Evidence method

Each fact family MUST produce a bounded static record under `evidence/repo-facts/` containing:

- repository and validation ref;
- inspection date;
- fact-family identifier;
- factual question;
- inspected paths, symbols or commands;
- observed result;
- limitations and unresolved questions;
- related assumption IDs;
- later Probe or Assessment obligation;
- mandatory no-generalization note.

Records MUST follow DPA-ADR-011 discipline and MUST NOT form a parallel evidence database or runtime service.

## 5. Discovery questions

All questions below are factual inventory questions. Words such as `sufficient`, `compatible`, `safe`, `supports the DPA`, or `conforms` are prohibited in Discovery conclusions.

### DISC-001 — Registry representation

Record:

- registry source files and loaders;
- entry structure and validation path;
- extension points already present;
- handling of unknown fields;
- document and region identity representations, if any;
- parser and validator entry points;
- tests that exercise registry parsing.

Do not conclude whether a proposed projection block is compatible. That is a Probe question.

### DISC-002 — Candidate reader graph

For each candidate document named by existing lab planning, record:

- every repository reader found;
- human, LLM, GUI, CLI, bootloader and workflow readers where evidenced;
- read order and section assumptions where evidenced;
- whether readers consume the full document or a bounded region;
- exact source locations.

Do not select a document form.

### DISC-003 — Candidate writer graph

Record:

- every code, workflow and documented manual writer;
- mutation commands and write paths;
- ownership and locking calls observed;
- generated, current, historical and manual regions where evidenced;
- direct writes that bypass the lifecycle, if observed.

Do not judge whether existing ownership is acceptable under DPA-200.

### DISC-004 — Authority inputs

Record:

- state files, registries, reports and other repository-backed inputs currently used to produce candidate document facts;
- which readers or writers treat each input as authoritative in observed code or contracts;
- unresolved authority ambiguity.

Do not promote evidence, generated targets or historical prose to canonical state.

### DISC-005 — Lifecycle findings

List every relevant existing finding type with:

- identifier;
- severity or category;
- producer;
- data fields;
- consumer or gate mapping;
- tests and documentation;
- lifecycle phase in which it is emitted.

Do not conclude whether these findings can absorb DPA projection drift. That is a Probe and later DPA-500 question.

### DISC-006 — Lifecycle mutation path

Record:

- planning and dry-run interfaces;
- validation sequence;
- mutation-lock acquisition and release;
- atomic-write mechanism as observed;
- post-write validation and evidence emission;
- crash or interrupted-write handling as observed;
- Workspace path-resolution calls.

Do not define the future DPA lifecycle contract.

### DISC-007 — Workspace and path APIs

Record:

- Workspace class or equivalent abstraction;
- path fields and resolver methods relevant to documentation, registry, evidence, temporary files and transfer;
- direct path literals that bypass the abstraction in relevant code;
- tests covering path resolution.

### DISC-008 — Locking and concurrency inventory

Record:

- mutation-lock API and scope;
- reentrancy behavior where documented or tested;
- branch and pull-request refresh workflows;
- base-SHA, target-hash or stale-plan checks already present;
- merge queue, required checks or other integration serialization mechanisms.

Do not conclude whether local locking or workflows satisfy DPA-600.

### DISC-009 — Gate and CI inventory

Record:

- existing lifecycle and documentation gates;
- severity-to-result mapping;
- warning and failure behavior;
- staged or strict modes;
- required-check integration;
- relevant CI recipes and tests.

Do not define future projection-gate policy.

### DISC-010 — Candidate history and rollback inputs

Record:

- tracked prior document states available through Git;
- existing historical regions or append behavior;
- scripts or workflows that reconstruct current or historical content;
- rollback inputs already authoritative or recoverable;
- gaps where rollback source is not observable.

Do not invent a new history source.

## 6. Assumption handling

For each related assumption:

- mark it `VERIFIED` only for the exact validation-ref claim supported by the record;
- mark it falsified or narrow its scope when evidence contradicts it;
- retain `NEEDS_MAIN_REPO_VALIDATION` for unanswered questions;
- create a Probe obligation when the remaining question asks whether an observed mechanism satisfies a proposed contract.

Discovery MUST NOT convert an observation directly into `NORMATIVE` architecture.

## 7. Required output set

The Discovery stage is complete only when:

- one validation ref is recorded;
- DISC-001 through DISC-010 each have a record or an explicit `not-observable` record with attempted method;
- `ASSUMPTIONS.md` is synchronized;
- `MAIN_REPOSITORY_CONTEXT.md` is updated only where later work depends on the new exact-ref facts;
- unresolved compatibility and sufficiency questions are transferred to a DP1 Probe backlog;
- no main-repository mutation occurred;
- no production form or architecture outcome was selected.

## 8. Probe boundary

The following are explicitly outside Discovery and require a reviewable DPA-300 or later contract:

- whether an optional projection schema is accepted by the actual parser and validator;
- whether existing finding structures are sufficient for projection drift;
- whether lifecycle hooks can enforce the proposed ownership and trust transitions;
- whether region representation can implement DPA-200 semantics;
- whether existing gate and workflow mechanisms satisfy DPA-500 and DPA-600;
- whether a candidate document may adopt a specific migration form.

## 9. Stop conditions

Stop and record a bounded diagnosis if:

- the exact validation ref cannot be established;
- inspection would require mutation;
- secrets or private runtime state would need to be copied into the lab;
- an observed fact cannot be separated from an architectural judgment;
- the requested question belongs to Probe, Assessment or implementation;
- evidence would require a parallel evidence service or maintained mirror.

## 10. Traceability

This contract implements DPA-ADR-015 and supports DPA-ADR-001, DPA-ADR-002, DPA-ADR-007 and DPA-ADR-011.

Its outputs inform DPA-300, DPA-400, DPA-500, DPA-600, DPA-700 and future DPA-800 without changing their normative authority.
