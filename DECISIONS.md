# Decisions

Status: active
Status-date: 2026-07-14

## DPA-ADR-001 — Extend the existing document-management system

Status: ACCEPTED

### Context

The main repository already has integrated registry, lifecycle, freshness, evidence, Workspace and gate mechanisms at the recorded baseline.

### Decision

DPA SHALL extend those mechanisms and SHALL NOT create a parallel projection-management system.

### Alternatives considered

- independent projection registry and lifecycle;
- lab-owned runtime projection authority;
- renderer-managed writes.

### Rationale

A parallel system would duplicate authority, create incompatible findings and gates, and violate the lab execution contract.

### Consequences

Every production schema, module and gate integration point remains subject to fresh main-repository validation. Optional DPA metadata must be backwards-compatible.

### Validation status

Architecture decision: `NORMATIVE`. Concrete integration: `NEEDS_MAIN_REPO_VALIDATION`.

### Affected specifications and slices

DPA-000 through DPA-900; DP1–DP5.

## DPA-ADR-002 — Lab is non-authoritative

Status: ACCEPTED

### Context

The lab is temporary and must not become a runtime dependency or competing source of truth.

### Decision

The lab SHALL contain proposals, reviews, decisions and normative design. Runtime authority SHALL remain exclusively in the main repository after validated adoption.

### Alternatives considered

- retain the lab as permanent runtime architecture authority;
- import the lab wholesale;
- treat model reviews as accepted runtime contracts.

### Rationale

Permanent split authority would make implementation and rollback ambiguous.

### Consequences

The lab is imported selectively and later archived. Reviews remain non-normative until adjudicated.

### Validation status

`NORMATIVE` for lab governance.

### Affected specifications and slices

All DPA specifications; integration and import planning.

## DPA-ADR-003 — Renderer responsibility boundary

Status: ACCEPTED

### Context

Projection computation, filesystem mutation and cross-PR coordination have different safety and authority requirements.

### Decision

Renderers SHALL read declared inputs and return text or bytes only. The existing document lifecycle SHALL validate, plan, locally lock and write. Workflow orchestration SHALL serialize across branches and pull requests.

### Alternatives considered

- renderer-owned writes;
- renderer-triggered renderer chains;
- lifecycle-owned cross-PR semantics without workflow orchestration;
- arbitrary renderer imports declared in registry data.

### Rationale

The accepted boundary keeps renderers deterministic and testable, preserves the existing mutation authority, and prevents local locks from being misrepresented as repository-wide serialization.

### Consequences

Renderer resolution must be static and fail-loud. One renderer computes one target. DP1 must verify the real lifecycle and workflow integration points.

### Validation status

Boundary: `NORMATIVE`. Main-repository integration points: `NEEDS_MAIN_REPO_VALIDATION`.

### Affected specifications and slices

DPA-000, DPA-100, DPA-300, DPA-400, DPA-600 and DP1–DP3.

## DPA-ADR-004 — Source-relative freshness

Status: ACCEPTED

### Context

Wall-clock age can be useful as an advisory signal but does not prove projection correctness.

### Decision

Projection freshness SHALL be defined by reproducibility from declared source state and projection-contract inputs. Time passage alone SHALL NOT cause a hard failure.

### Alternatives considered

- age-only blocking thresholds;
- marker-presence as sufficient freshness proof;
- a separate DPA freshness audit.

### Rationale

Source-relative freshness detects relevant drift while reusing the existing lifecycle finding and gate architecture.

### Consequences

DPA-500 must define source, target, contract and unverifiable-state findings and integrate them into existing gates.

### Validation status

Semantics: `NORMATIVE`. Existing finding-model compatibility: `NEEDS_MAIN_REPO_VALIDATION`.

### Affected specifications and slices

DPA-000, DPA-100, DPA-500 and DP2/DP5.

## DPA-ADR-005 — Evidence-driven document-form hierarchy

Status: ACCEPTED

### Context

Candidate documents may combine reconstructable current state with historical prose that is not canonical.

### Decision

DP1 SHALL prefer full projection only when complete content is reconstructable, otherwise split current projection from historical evidence, and use managed head plus append history only as a justified exception. No migration SHALL occur where authority or rollback is unresolved.

### Alternatives considered

- create a new canonical history database;
- automatically merge historical prose;
- preselect a document form in the lab without reader/writer evidence.

### Rationale

The hierarchy avoids inventing authority and keeps migration reversible.

### Consequences

Each candidate requires a fresh reader/writer/source graph, explicit classification and rollback plan.

### Validation status

Hierarchy: `NORMATIVE`. Candidate classifications: `NEEDS_MAIN_REPO_VALIDATION`.

### Affected specifications and slices

DPA-000, DPA-700, DPA-800 and DP1–DP4.
