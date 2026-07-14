# DPA-000 — Vision and Architectural Principles

Status: review-ready
Status-date: 2026-07-14
Superseded-by: n/a

## 1. Purpose

This specification defines the vision, scope, architectural boundaries and governing principles of the Document Projection Architecture (DPA).

The DPA extends the existing document-management architecture of `vfi64/agentic-project-kit`. It does not establish a second registry, lifecycle, freshness, evidence, workspace, workflow or gate system.

Repository-specific implementation statements in this document are classified as `NEEDS_MAIN_REPO_VALIDATION` unless they cite an exact main-repository ref and reproducible evidence.

## 2. Problem statement

Repository documents may combine current operational state, generated content, manually maintained prose and historical evidence. A mutation may update one valid region while leaving an earlier region stale. Readers, bootstraps and automation may then consume a syntactically valid but semantically obsolete view.

Marker presence, file existence and wall-clock age alone do not prove that the consumed document represents its declared canonical sources. Local mutation locks also do not serialize competing branches or pull requests.

The DPA addresses this class of problem by making selected registered documents deterministic projections of declared canonical repository-backed state while preserving existing authority and lifecycle boundaries.

## 3. Vision

A registered projection target is a reproducible document view whose content can be computed from explicitly declared canonical sources by a statically resolved renderer, validated and written only through the existing document lifecycle, and protected against local and cross-workflow drift.

The DPA SHALL make projection behavior inspectable, reviewable, fail-loud and reversible. It SHALL preserve the main repository as the only runtime authority.

## 4. Goals

The DPA MUST:

1. extend the existing documentation registry and lifecycle rather than bypass them;
2. define explicit authority relationships among canonical state, projections, evidence and historical prose;
3. ensure renderers are pure with respect to repository mutation;
4. make projection contracts statically resolvable and reviewable;
5. detect source, target and workflow drift without inventing a parallel audit;
6. distinguish local mutation locking from branch and pull-request serialization;
7. support dry-run planning before mutation;
8. preserve backwards compatibility for documents without projection contracts;
9. provide migration and rollback paths that do not create a new canonical history source;
10. provide traceability from motivation through requirements, decisions, DP1–DP5, tests, gates, evidence and rollback.

## 5. Non-goals

The DPA MUST NOT:

1. become a general plugin framework;
2. permit arbitrary executable imports from registry data;
3. move render logic into canonical state;
4. permit renderers to write files, acquire locks, invoke workflows or trigger other renderers;
5. create a second documentation registry, lifecycle, freshness checker, evidence system, workspace resolver or gate suite;
6. treat evidence artifacts as runtime authority;
7. create a new canonical history database or log solely to simplify migration;
8. automatically merge append-only historical prose during drift recovery;
9. make elapsed wall-clock time alone a hard failure;
10. claim production implementation, test success or gate success from lab artifacts.

## 6. Architectural actors

### 6.1 Canonical state

Canonical state owns domain facts and authoritative repository-backed state. It MUST NOT own renderer selection, formatting or target-write behavior.

### 6.2 Documentation registry

The existing documentation registry owns the declarative projection contract after validated adoption in the main repository. It describes approved identifiers, sources, target semantics and lifecycle policy. It MUST NOT contain arbitrary executable imports.

### 6.3 Renderer

A renderer reads only its declared inputs and computes exactly one registered target as text or bytes. It MUST be deterministic for identical declared inputs and relevant versioned configuration. It MUST NOT write, lock, mutate, invoke another renderer or invent domain state.

### 6.4 Document lifecycle

The existing document lifecycle validates contracts, resolves declared inputs, plans changes, acquires the existing mutation lock, writes targets and emits lifecycle findings and evidence. It MUST remain the only component that writes projection targets.

### 6.5 Workflow orchestration

Workflow orchestration serializes branch- and pull-request-level refresh activity, verifies base and source assumptions against fresh repository state, and prevents stale plans from being committed. It MUST NOT define document semantics.

### 6.6 Evidence

Evidence records what was inspected, planned, rendered, validated or written. Evidence MAY support audit and review, but it MUST NOT become runtime authority or a canonical source unless an independent accepted architecture decision explicitly establishes such authority.

### 6.7 Consumer

A consumer reads a registered target. Consumers SHOULD NOT need to understand renderer internals, but their read order and assumptions MUST be included in migration analysis where stale-leading-content risk exists.

## 7. Binding architectural invariants

1. Canonical state MUST NOT own rendering logic.
2. Renderers MUST NOT own write logic.
3. Renderers MUST return text or bytes only.
4. The document lifecycle MUST validate, plan, lock and write projection targets.
5. Workflow orchestration MUST serialize refresh activity across branches and pull requests.
6. The registry MUST describe reviewed contracts, not arbitrary plugins.
7. Renderer identifiers MUST resolve through static, reviewed code.
8. One renderer invocation MUST compute exactly one registered target.
9. A renderer MUST NOT trigger another renderer.
10. Evidence MUST NOT be runtime authority.
11. Runtime projection contracts MUST live only in the main repository's existing registry and lifecycle system.
12. The DPA MUST NOT introduce a parallel registry, lifecycle, freshness, evidence, workspace or gate subsystem.
13. Time-based findings MUST NOT become hard failures solely because time elapsed.
14. Historical prose MUST NOT be automatically merged during drift recovery.
15. Mutation commands MUST default to dry-run.
16. Production paths MUST resolve through the main repository's existing Workspace abstraction after validated implementation.
17. Repository-specific field names, module names and current behaviors MUST remain `NEEDS_MAIN_REPO_VALIDATION` until verified against an exact fresh ref.

## 8. Authority model

The DPA distinguishes:

- **runtime authority**: the main repository's accepted canonical state and existing governed contracts;
- **projection authority**: authority delegated by a validated registry contract to derive a target from declared canonical sources;
- **planning authority**: accepted lab specifications and decisions for architecture work only;
- **evidentiary value**: records supporting reproduction, review or audit without runtime authority;
- **historical value**: prose or records retained for human history but not automatically canonical.

A projection is authoritative only as a view of its declared canonical sources. It never becomes an independent source of the facts it renders unless a separate accepted contract explicitly says otherwise.

## 9. Projection lifecycle vision

A conforming projection refresh SHALL conceptually perform these stages:

1. resolve the registered target and its declared contract;
2. resolve canonical sources through the existing Workspace abstraction;
3. validate contract compatibility and renderer identity;
4. capture base, source and target fingerprints;
5. render in memory without mutation;
6. compare expected and actual target content;
7. emit a dry-run plan and lifecycle findings;
8. acquire the existing mutation lock for an approved write;
9. revalidate stale-plan guards;
10. write atomically through the existing lifecycle;
11. emit evidence without promoting evidence to authority;
12. verify reproducibility against the required repository state.

Exact commands, schemas and module boundaries are `NEEDS_MAIN_REPO_VALIDATION` until DP1 inspects a fresh main repository.

## 10. Freshness and failure principles

Projection freshness is derivational, not merely chronological. A target is fresh when it is reproducible from the declared sources, renderer identity and relevant versioned configuration under the governing contract.

The DPA MUST fail loudly for unknown renderer identifiers, invalid contracts, missing required sources, non-deterministic output, stale mutation plans and prohibited authority relationships.

The DPA MUST NOT hard-fail solely because a timestamp threshold elapsed. Time MAY produce warning or review signals when integrated with the existing lifecycle policy.

## 11. Concurrency principles

Local mutation locking protects a workspace mutation boundary. It does not prevent two branches or pull requests from independently producing conflicting valid-looking outputs.

A production workflow MUST therefore capture and verify at least:

- base commit identity;
- declared source fingerprints;
- target-region or full-target fingerprint;
- renderer and contract identity;
- reproducibility against fresh `origin/main` before final integration.

On drift, the workflow MUST block and regenerate from fresh authoritative state. It MUST NOT auto-merge historical prose.

## 12. Migration principles

DP1 MUST discover the real reader, writer and authority graph before selecting a migration form.

The preferred decision order is:

1. full projection when complete target content is reconstructable from existing canonical sources;
2. split current projection and historical evidence when history is not canonical;
3. managed head plus append history only as a justified exception with complete workflow serialization.

Migration MUST be reversible, must preserve non-projected documents, and must not establish a new canonical history source merely for convenience.

## 13. Compatibility principles

Documents without a projection contract MUST retain their existing lifecycle behavior.

Optional registry extensions MUST be backwards compatible or fail with a bounded, explicit validation error. Unknown renderer identifiers and malformed projection contracts MUST fail loud. Silent fallback to ad hoc behavior is prohibited.

## 14. Security and safety principles

Registry data MUST NOT enable arbitrary code loading. Renderer resolution MUST use a static reviewed mapping. Declared sources MUST remain within validated workspace boundaries. Dry-run MUST precede mutation, and stale-plan validation MUST occur after lock acquisition and before write.

## 15. Specification relationship

- DPA-100 defines terminology, authority classes and requirement language.
- DPA-200 defines document and projection forms.
- DPA-300 defines registry and lifecycle integration.
- DPA-400 defines the renderer contract.
- DPA-500 defines freshness and gate behavior.
- DPA-600 defines concurrency and workflow serialization.
- DPA-700 defines migration and rollback.
- DPA-800 defines DP1–DP5 implementation work.
- DPA-900 bounds future evolution.

Later specifications MUST conform to this document and the lab execution contract.

## 16. Repository evidence classification

### VERIFIED at recorded baseline

At main-repository refs `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` and `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`, the lab context records an existing integrated document-management stack and completed post-L5 lifecycle evidence. The reproduction source is `MAIN_REPOSITORY_CONTEXT.md`; fresh implementation work MUST revalidate these facts.

### NEEDS_MAIN_REPO_VALIDATION

Exact registry fields, module names, renderer integration points, lifecycle finding types, source authority, reader/writer graphs, workflow checks and candidate migration targets require DP1 inspection against a fresh `origin/main`.

## 17. Success criteria

The DPA architecture succeeds when:

1. DPA-000 through DPA-900 form a coherent reviewed specification series;
2. no contract introduces a parallel governance or runtime subsystem;
3. DP1–DP5 are implementation-ready but not falsely marked implemented;
4. every repository-specific dependency is verified or explicitly classified;
5. traceability covers requirements, decisions, tests, gates, evidence and rollback;
6. validated contracts can be imported selectively into the main repository;
7. runtime authority remains exclusively in the main repository after adoption.

## 18. Open validation obligations

The following remain intentionally unresolved in Phase A:

- exact registry schema extension;
- exact lifecycle and finding integration points;
- actual canonical sources for candidate documents;
- actual reader/writer graph;
- exact cross-PR serialization mechanism;
- final migration form for any production document.

These are not Phase A blockers. They are bounded inputs to later specifications and DP1.