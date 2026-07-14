# DPA-100 — Foundations and Terminology

Status: review-ready
Status-date: 2026-07-14
Superseded-by: n/a
Depends-on: DPA-000

## 1. Purpose

This specification defines the foundational vocabulary, authority model, status semantics and conformance language used by the Document Projection Architecture.

Terms in later DPA specifications MUST use the meanings defined here unless a later specification explicitly narrows them without contradiction.

## 2. Normative language

The keywords `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and `MAY` are normative. Repository facts still require exact-ref evidence.

## 3. Authority model

### 3.1 Runtime authority

A **runtime authority** is a main-repository source whose value is consumed as authoritative during normal operation. A projection target MUST NOT become runtime authority merely because it is generated, registered or widely read.

### 3.2 Canonical state

**Canonical state** is repository-backed state that owns the facts from which a projection is computed. It MUST be independently authoritative before projection and MUST NOT own rendering logic.

### 3.3 Canonical source

A **canonical source** is one declared authoritative input to a projection. A projection target MUST NOT be its own canonical source.

### 3.4 Projection target

A **projection target** is the registered file or bounded region produced from declared canonical sources. It is a representation, not automatically canonical state.

### 3.5 Evidence

**Evidence** is reproducible information used for validation, review or audit. It MAY include exact refs, hashes, commands, graphs and test reports. It MUST NOT become runtime authority without an independent existing contract.

### 3.6 Lab authority

The lab is authoritative only for its accepted architecture decisions and normative planning contracts. It is not authoritative for current `agentic-project-kit` runtime state.

## 4. Core architecture terms

### 4.1 Document projection

A **document projection** is a deterministic representation computed from declared canonical sources and explicit configuration.

### 4.2 Projection contract

A **projection contract** is the bounded declarative registry contract that identifies the target, renderer identifier, declared sources, output form, freshness inputs, compatibility mode and required validation metadata. The exact production schema remains `NEEDS_MAIN_REPO_VALIDATION`.

### 4.3 Renderer

A **renderer** is statically resolved reviewed code that reads declared inputs and returns text or bytes for exactly one target. It MUST NOT write, lock, mutate canonical state, invoke Git or trigger another renderer.

### 4.4 Renderer identifier

A **renderer identifier** is a stable registry-facing name resolved by static reviewed code. It MUST NOT be an arbitrary import path, shell command or evaluated expression. Unknown identifiers MUST fail loudly.

### 4.5 Document lifecycle

The **document lifecycle** is the existing main-repository mechanism responsible for contract validation, change planning, local mutation locking and writes. DPA extends it; DPA does not define a parallel lifecycle.

### 4.6 Workflow orchestration

**Workflow orchestration** coordinates operations across branches, pull requests and authoritative remote state. It owns serialization and drift guards, not document semantics.

### 4.7 Workspace

The **Workspace** is the main repository's existing path and repository-context abstraction. Production DPA paths MUST resolve through it. Its exact API remains `NEEDS_MAIN_REPO_VALIDATION`.

## 5. Document forms

### 5.1 Full projection

A **full projection** is a target whose complete content is reproducible from declared canonical sources.

### 5.2 Split projection

A **split projection** separates deterministic current state from historical or explanatory material that is not canonical. Historical material MUST NOT be silently promoted to canonical state.

### 5.3 Managed region

A **managed region** is a bounded part of a document controlled by the lifecycle under a projection contract. Boundaries, readers and writers MUST be unambiguous.

### 5.4 Managed head plus append history

A **managed head plus append history** document contains a lifecycle-controlled current region followed by separately governed append-only prose. This form is exceptional and requires complete workflow serialization, reader clarity and rollback.

### 5.5 Historical prose

**Historical prose** is narrative about prior states that is not necessarily reconstructable from current canonical state. It MUST NOT be automatically merged during drift recovery.

## 6. Freshness and drift

### 6.1 Freshness

**Freshness** means that a target is reproducible from its declared source state and projection contract. Freshness is source-relative, not age-relative.

### 6.2 Source drift

**Source drift** occurs when declared canonical inputs differ from those used to produce or validate the target.

### 6.3 Target drift

**Target drift** occurs when target bytes or a managed-region hash differ from deterministic renderer output for the declared source state.

### 6.4 Contract drift

**Contract drift** occurs when renderer identity, source declarations, output mode or other contract inputs change.

### 6.5 Structural invalidity

**Structural invalidity** occurs when a contract or target violates required schema, boundaries, encoding or static resolution rules.

### 6.6 Unverifiable state

An **unverifiable state** exists when required sources, hashes, authority information or renderer resolution are unavailable or ambiguous. It MUST fail loudly where correctness depends on verification.

### 6.7 Time-based staleness

**Time-based staleness** is an age signal derived from wall-clock time. It MAY produce advisory findings but MUST NOT alone cause a hard failure.

## 7. Mutation and concurrency

### 7.1 Dry-run

A **dry-run** computes findings and a proposed change plan without mutation. Mutation-capable DPA operations MUST default to dry-run unless an existing governed workflow explicitly authorizes execution.

### 7.2 Mutation lock

A **mutation lock** is the existing local mechanism that serializes filesystem mutations within its scope. It does not serialize branches, clones or pull requests.

### 7.3 Base SHA

A **base SHA** is the exact authoritative commit against which sources and target state were read for a planned refresh.

### 7.4 Source hash

A **source hash** is a reproducible digest of one declared source or its normalized authoritative representation.

### 7.5 Target hash

A **target hash** is a reproducible digest of the full target or explicitly managed region.

### 7.6 Workflow serialization

**Workflow serialization** is repository-level coordination that prevents competing branch or pull-request operations from silently publishing incompatible projections.

### 7.7 Regeneration

**Regeneration** is recomputation from fresh authoritative state after drift invalidates a prior plan. It MUST replace stale planned output and MUST NOT auto-merge historical prose.

## 8. Status classifications

- `VERIFIED`: exact ref, inspected source or command, reproducible method and bounded conclusion are recorded.
- `ASSUMPTION`: a working belief not yet validated against the relevant authority.
- `NORMATIVE`: an accepted lab architecture requirement; it does not prove implementation.
- `PROPOSAL`: a candidate design awaiting adjudication.
- `REJECTED`: an explicitly declined alternative with rationale.
- `NEEDS_MAIN_REPO_VALIDATION`: a repository-specific claim or dependency requiring fresh main-repository inspection.

## 9. Completion terms

- **Draft**: structure exists and unresolved issues are visible.
- **Review-ready**: terminology is coherent, alternatives are visible, traceability has started and repository assumptions are classified.
- **Stable**: required reviews are adjudicated, decisions and traceability are complete for scope, and no known contradiction remains.
- **Adopted**: validated against fresh main-repository evidence and accepted through governed main-repository changes.

## 10. Implementation-status terms

- **Planned implementation**: specified work not yet proven in the main repository.
- **Verified implementation**: main-repository behavior supported by exact-ref code, test and gate evidence.
- **Future extension**: explicitly outside the current implementation baseline.

## 11. Conformance

A later DPA specification conforms to DPA-100 only when it:

- uses authority terms consistently;
- does not treat projections or evidence as implicit canonical state;
- distinguishes local locking from workflow serialization;
- classifies repository-specific claims;
- distinguishes normative design from verified implementation;
- preserves static renderer resolution and existing-lifecycle ownership;
- does not introduce a parallel governance subsystem.

## 12. Open validation boundaries

The following remain `NEEDS_MAIN_REPO_VALIDATION` before production implementation:

- exact registry schema and extension compatibility;
- exact lifecycle findings and enforcement wiring;
- current Workspace APIs;
- candidate-document reader/writer/source graphs;
- refresh workflow concurrency controls;
- exact gate and check integration points.
