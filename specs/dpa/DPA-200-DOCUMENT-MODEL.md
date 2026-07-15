# DPA-200 — Document Model

Status: draft
Status-date: 2026-07-15
Superseded-by: n/a

## 1. Purpose

This specification defines the normative document model for the Document Projection Architecture.

It classifies registered documents and registered regions, assigns authority and write ownership, defines target semantics and consumer trust boundaries, and constrains how later registry, lifecycle, renderer, freshness, concurrency and migration specifications may operate.

DPA-200 conforms to stable DPA-000 and DPA-100. It MUST NOT introduce a parallel registry, lifecycle, evidence, Workspace, freshness or gate system.

## 2. Scope

DPA-200 defines:

- document-form classifications;
- target identity and region identity;
- projected, manual and historical-region ownership;
- full-target and region-target semantics;
- source, configuration and target relationships;
- consumer trust states;
- compatibility expectations for manual documents;
- prerequisites for selecting a migration form;
- obligations delegated to DPA-300, DPA-400, DPA-500 and DPA-700.

Concrete main-repository schemas, field names, modules, commands and candidate-document classifications remain `NEEDS_MAIN_REPO_VALIDATION` until DP1 inspects an exact validation ref.

## 3. Non-goals

DPA-200 MUST NOT:

1. define executable renderer resolution;
2. define lifecycle write algorithms;
3. define gate severity mappings;
4. define cross-pull-request serialization mechanisms;
5. choose a production migration target or migration form before DP1;
6. establish evidence or historical prose as runtime authority;
7. invent a canonical history source for migration convenience;
8. permit overlapping or ambiguous region ownership;
9. permit unvalidated rendered bytes to be represented as accepted repository state.

## 4. Document identity

### 4.1 Registered document

A registered document is identified by the existing main-repository documentation registry after validated adoption.

Its concrete registry identity representation is `NEEDS_MAIN_REPO_VALIDATION`.

### 4.2 Registered region

A registered region is a non-overlapping, precisely bounded region within one registered document.

A conforming registered-region contract MUST define:

- parent document identity;
- region identity;
- boundary representation;
- target semantics;
- write owner;
- normalization rules;
- drift comparison domain;
- behavior when boundaries are absent, duplicated or malformed.

Region-level registration compatibility with the existing registry remains `NEEDS_MAIN_REPO_VALIDATION`.

### 4.3 Target identity

A projection contract MUST resolve to exactly one target identity:

- one complete registered document; or
- one registered region inside one registered document.

A renderer invocation MUST NOT target multiple documents or multiple independently owned regions.

## 5. Document forms

### 5.1 Manual document

A manual document has no projection contract.

Its existing lifecycle behavior MUST remain unchanged unless a separate accepted contract explicitly changes it. DPA adoption MUST be backwards compatible for manual documents.

### 5.2 Full projection

A full projection owns the complete target bytes of one registered document.

Full projection MAY be selected only when every byte required by the target is reproducible from declared canonical sources and contract-declared configuration.

No independently maintained prose may exist inside a full-projection target.

### 5.3 Split projection

A split projection separates deterministic current state from historical or explanatory material that is not canonical state.

The projected component and the historical component MUST have distinct target identities or distinct registered regions with explicit ownership.

The historical component MUST NOT be read as a semantic renderer input unless an accepted authority contract makes it canonical state.

### 5.4 Managed-head projection

A managed-head projection owns one leading registered region while preserving a following historical region.

It is an exceptional form and MUST define:

- exact projected-region boundaries;
- exact historical-region boundaries;
- projected-region lifecycle ownership;
- historical-region write ownership;
- append and edit policy;
- conflict behavior;
- consumer read assumptions;
- rollback behavior;
- cross-ref serialization requirements.

Managed-head projection MUST NOT permit automatic prose merge during drift recovery.

### 5.5 Hybrid document

A hybrid document contains at least one projected region and at least one manually maintained region.

Every region MUST have exactly one write owner. Region ownership MUST be non-overlapping and collectively sufficient to explain all target bytes.

A hybrid document is invalid when:

- region boundaries overlap;
- a byte range has no declared owner;
- multiple owners may write the same region;
- projected and manual normalization rules conflict;
- a consumer cannot determine which region carries current authoritative representation.

## 6. Authority model

### 6.1 Canonical sources

Projected semantic output MUST derive only from declared canonical sources.

Evidence, review artifacts, mutation plans and historical prose MUST NOT become canonical sources through convenience, repetition or migration pressure.

### 6.2 Contract-declared configuration

Contract-declared configuration MAY influence representation but MUST NOT silently own domain facts.

Configuration that changes output MUST be versioned and included in reproducibility and fingerprint contracts.

### 6.3 Projection target authority

A projection target is an authoritative representation only within the bounded authority delegated by its validated projection contract.

It MUST NOT become an independent canonical source for the facts it renders.

### 6.4 Historical regions

A historical region may have evidentiary or human value but is not canonical state by default.

Its permitted writer and mutation policy MUST be explicit. DPA-700 owns migration and rollback consequences for historical regions.

## 7. Write ownership

Each complete target and each registered region MUST have exactly one write owner.

Permitted write-owner classes are:

- existing document lifecycle for projected targets;
- governed manual editing for manual regions;
- a later explicitly accepted owner defined by a normative DPA contract.

Renderers MUST NOT be write owners.

Workflow orchestration MUST NOT be a semantic write owner; it authorizes and serializes lifecycle activity.

Evidence producers MUST NOT be target write owners merely because they record mutation activity.

## 8. Target semantics

A target-semantics contract MUST declare:

- replacement mode: full target or one registered region;
- byte encoding;
- line-ending policy;
- normalization policy;
- terminal-newline policy;
- region boundary preservation or replacement behavior;
- whether empty output is valid;
- behavior for missing or malformed boundaries;
- prohibited append behavior;
- fingerprint input domain.

Append semantics for projected output are prohibited unless a later accepted specification defines a bounded use that preserves deterministic reproduction and does not merge historical prose.

## 9. Consumer trust boundary

Generated bytes exist in one of these trust states:

1. **computed** — renderer output exists in memory but has not passed lifecycle validation;
2. **planned** — a mutation plan exists, but no accepted repository state is claimed;
3. **written-unverified** — bytes have been written in a governed workspace but required post-write checks or gates are incomplete;
4. **accepted** — lifecycle validation, required reproducibility checks and governing gates have completed for the applicable scope.

Only `accepted` output MAY be represented as accepted repository state.

DPA-500 owns the complete gate mapping. DPA-300 owns lifecycle transitions and prohibited bypasses.

## 10. Compatibility

Documents without projection contracts MUST preserve their existing behavior.

Optional projection metadata MUST NOT change validation or mutation behavior for unrelated manual documents.

Unknown document forms, unknown target semantics and ambiguous region ownership MUST fail loudly. Silent fallback from malformed projected behavior to manual mutation is prohibited.

## 11. Document-form selection

DP1 MUST select a document form only after recording:

- canonical authority for every rendered fact;
- all readers and their read order;
- all writers and mutation paths;
- complete target reconstruction capability;
- historical-region status;
- region-boundary compatibility;
- rollback source and recoverability;
- consumer trust and gate assumptions;
- concurrency requirements.

The selection order is:

1. full projection when complete reconstruction is proven;
2. split projection when current state is reconstructable but historical material is not canonical;
3. managed-head projection only as a justified exception;
4. no migration when authority, ownership, compatibility or rollback cannot be established.

A candidate-document listing is not a verified form selection.

## 12. Invalid document-model states

A document model MUST be rejected when any of these conditions holds:

- canonical authority is ambiguous;
- target identity is ambiguous;
- region boundaries overlap or cannot be resolved;
- write ownership is missing or duplicated;
- renderer output depends on undeclared semantic input;
- evidence or historical prose is used as runtime authority without an accepted authority decision;
- consumer trust is asserted before required validation;
- rollback depends on an unavailable or newly invented history source;
- migration would require automatic historical-prose merging;
- the model requires a parallel registry, lifecycle, freshness, evidence, Workspace or gate system.

## 13. Delegated specification obligations

### DPA-300

DPA-300 MUST define registry validation, lifecycle state transitions, region-write planning, atomicity, direct-write detection and crash-recovery obligations.

### DPA-400

DPA-400 MUST define renderer input resolution, purity, deterministic output, configuration handling and failure behavior.

### DPA-500

DPA-500 MUST define drift findings, trust-state gate transitions, source/target/contract drift and the rule that time alone cannot hard-fail.

### DPA-600

DPA-600 MUST define cross-branch and cross-PR serialization for shared targets and registered regions.

### DPA-700

DPA-700 MUST define migration, historical-region policy, rollback recoverability and reversal of every document form.

### DPA-800

DPA-800 MUST bind DP1–DP5 implementation work to the document-form decisions and validation evidence required here.

## 14. Traceability anchors

DPA-200 is primarily constrained by:

- `DPA-INV-001` canonical state owns no rendering logic;
- `DPA-INV-004` lifecycle validates, plans, locks and writes;
- `DPA-INV-008` one renderer computes one target;
- `DPA-INV-010` evidence is not runtime authority;
- `DPA-INV-011` runtime contracts remain in the existing system;
- `DPA-INV-012` no parallel subsystem;
- `DPA-INV-014` no automatic historical-prose merge;
- `DPA-INV-017` repository-specific claims require exact evidence.

Relevant accepted decisions include DPA-ADR-001, DPA-ADR-002, DPA-ADR-003, DPA-ADR-007, DPA-ADR-009, DPA-ADR-010, DPA-ADR-011 and DPA-ADR-012.

## 15. Open validation obligations

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- actual registry support for region-level targets;
- actual marker or boundary conventions;
- actual candidate-document readers and writers;
- actual lifecycle ownership and direct-write paths;
- actual canonical sources for each candidate target;
- actual atomic-write behavior;
- actual consumer gate placement;
- actual rollback inputs available from Git history or existing authority.

These obligations constrain DP1 and later implementation. They do not authorize implementation claims in the lab.

## 16. Draft exit criteria

DPA-200 may become `review-ready` only when:

- every document form has complete authority and ownership rules;
- target semantics and region invalidity are explicit;
- the consumer trust boundary is complete;
- delegated obligations do not conflict with stable DPA-000 or DPA-100;
- traceability includes tests, gates, evidence and rollback;
- no production document form is preselected without DP1 evidence;
- primary review and secondary verification inputs can be generated against one exact ref.