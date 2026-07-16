# DPA-400 — Renderer Contract

Status: draft
Status-date: 2026-07-16
Authority: normative DPA specification, subject to review and Probe evidence

## 1. Purpose

This specification defines the renderer contract for the Document Projection Architecture.

A renderer is a statically resolved, side-effect-free computation that reads only declared semantic inputs and contract-declared configuration and returns text or bytes for exactly one registered projection target.

This specification extends the existing documentation-management architecture. It does not create a plugin framework, a second registry, a second lifecycle, a command family, a state authority or a write path.

Concrete module names, callable signatures, renderer identifiers and implementation locations remain `NEEDS_MAIN_REPO_VALIDATION` until validated against an exact main-repository ref.

## 2. Normative dependencies

DPA-400 depends on:

- DPA-000 for the canonical invariants;
- DPA-100 for authority, source, configuration, determinism, fingerprint and failure vocabulary;
- DPA-200 for target identity, document forms, partition ownership and target semantics;
- DPA-300 for registry integration, lifecycle phase ordering, immutable plans, stale-plan guards, acceptance state and recovery;
- DPA-ADR-003, DPA-ADR-004, DPA-ADR-005, DPA-ADR-013, DPA-ADR-014, DPA-ADR-016 and DPA-ADR-017.

## 3. Scope

DPA-400 owns:

1. renderer identity and static resolution;
2. renderer callable and return contracts;
3. declared semantic inputs;
4. contract-declared configuration;
5. deterministic output requirements;
6. purity and side-effect prohibitions;
7. one-invocation/one-target behavior;
8. payload-only region output;
9. renderer failure classification at the architecture boundary;
10. renderer-version and fingerprint obligations;
11. renderer test and conformance obligations.

DPA-400 does not own:

- registry serialization;
- target or partition writes;
- mutation plans;
- locks or workflow serialization;
- acceptance-state persistence;
- lifecycle findings or severity mapping;
- gate outcomes;
- migration-form selection.

## 4. Renderer authority boundary

A renderer has projection authority only for the bytes it computes under one validated projection contract.

A renderer:

- MAY read declared canonical sources;
- MAY read contract-declared configuration;
- MUST return text or bytes only;
- MUST NOT write repository files, lifecycle state, registry state, evidence, logs used as runtime authority or acceptance state;
- MUST NOT acquire locks;
- MUST NOT invoke Git, shell commands, network calls, workflow commands or repository mutation APIs;
- MUST NOT assign trust states;
- MUST NOT decide whether output is accepted;
- MUST NOT repair malformed targets or partition boundaries;
- MUST NOT select a document form;
- MUST NOT treat prior projection output, evidence or historical prose as canonical input unless that input is independently declared canonical by another accepted authority contract.

The lifecycle remains the sole caller that may use renderer output for a governed mutation plan.

## 5. Renderer identity and static resolution

### 5.1 Renderer identifier

Every projection contract MUST declare one renderer identifier.

The identifier MUST be:

- stable within the contract version;
- declarative;
- reviewable in registry content;
- resolvable through a static mapping owned by reviewed main-repository code;
- included in contract and plan fingerprints.

A renderer identifier MUST NOT be:

- an import path supplied by registry data;
- a shell command;
- a URL;
- an expression;
- a dynamic module or package reference;
- a plugin-discovery entry point;
- a fallback chain.

### 5.2 Static mapping

Renderer resolution MUST use a closed, explicit mapping from renderer identifiers to reviewed implementations.

Unknown identifiers MUST fail loud before rendering and planning.

Duplicate identifiers, ambiguous aliases or environment-dependent resolution MUST fail loud.

The mapping MAY support reviewed aliases only when:

- every alias resolves to exactly one implementation;
- alias semantics are versioned;
- the canonical identity used in fingerprints is unambiguous;
- removal and deprecation follow governed compatibility rules.

The concrete mapping location and callable registration mechanism remain `NEEDS_MAIN_REPO_VALIDATION`.

## 6. Renderer callable contract

A conforming renderer receives an immutable invocation context containing, directly or through bounded value objects:

- the validated projection-contract identity and version;
- exactly one registered target identity;
- ordered declared source values or source snapshots;
- contract-declared configuration;
- target semantics required to shape the payload;
- renderer-version identity;
- representation-only context explicitly permitted by this specification.

A renderer MUST NOT receive mutable lifecycle, Workspace, registry, lock, Git client, filesystem writer, subprocess, network or gate objects.

The invocation context MUST be sufficient to compute output without ambient repository reads.

If a main-repository implementation permits a renderer to receive repository paths, those paths MUST refer only to declared sources already resolved and validated by the lifecycle. The renderer MUST NOT discover additional inputs by traversal, globbing or search.

## 7. Declared inputs

### 7.1 Semantic sources

Every semantic input that can change output facts MUST be declared by the projection contract.

The lifecycle MUST resolve and fingerprint declared sources before renderer invocation.

A renderer MUST reject or fail when a required source value is absent or structurally invalid. It MUST NOT substitute:

- prior target bytes;
- evidence records;
- historical prose;
- chat memory;
- environment defaults;
- current time;
- unversioned repository state.

### 7.2 Contract-declared configuration

Configuration MAY control representation such as headings, ordering, labels, templates, separators inside renderer-owned payload, optional sections or formatting policy.

Configuration MUST:

- be explicitly declared;
- be immutable for one invocation;
- have a defined schema and version;
- be included in the contract fingerprint when output-affecting;
- not silently own domain facts.

Unknown or malformed configuration MUST fail loud.

### 7.3 Incidental process context

Locale, timezone, working directory, process environment, host platform, hash randomization, filesystem enumeration order and current time MUST NOT affect semantic output unless explicitly declared and versioned as contract configuration.

Where representation legitimately depends on one of these values, the value MUST be captured explicitly and included in the fingerprint domain.

## 8. Output contract

### 8.1 Return type

A renderer MUST return exactly one of:

- Unicode text governed by an explicit encoding step in the lifecycle; or
- immutable bytes.

A renderer MUST NOT return:

- a path;
- a file handle;
- a stream with external side effects;
- a mutation callback;
- a command;
- a lifecycle finding as a substitute for output;
- multiple independently registered targets.

Structured internal values MAY be used inside the renderer implementation, but the renderer boundary exposed to the lifecycle MUST resolve to one text-or-bytes payload.

### 8.2 Complete target output

For a complete-target projection, renderer output represents all renderer-owned target bytes.

The renderer MUST NOT depend on existing target bytes to construct semantic output.

### 8.3 Registered-region output

For a registered-region projection, renderer output represents payload bytes only.

The renderer MUST NOT emit:

- partition markers;
- boundary separators;
- bytes owned by manual or historical regions;
- complete-parent reconstruction bytes outside its registered payload.

The lifecycle combines the payload with validated preserved bytes and the parent-entry `PartitionContract` under DPA-300.

### 8.4 Empty output

Empty output is valid only when target semantics explicitly permit it.

A renderer returning empty output where the contract prohibits it MUST cause validation failure before mutation.

## 9. Determinism and reproducibility

For identical:

- renderer implementation/version;
- projection contract;
- declared source values;
- contract-declared configuration;
- target-semantics version;

one renderer invocation MUST return byte-equivalent output after the contract-defined text encoding and normalization steps.

A renderer MUST NOT depend on:

- iteration order not fixed by contract;
- random values without a contract-declared fixed seed;
- wall-clock time;
- process IDs;
- temporary paths;
- network availability;
- mutable global state;
- filesystem metadata not declared as a source;
- prior invocation history.

Determinism tests MUST execute the same invocation multiple times in fresh process contexts where practical.

## 10. Purity and side-effect prohibition

A conforming renderer MUST be observationally pure at the architecture boundary.

During invocation it MUST NOT:

1. create, modify or delete files;
2. modify repository or process configuration;
3. mutate input objects;
4. alter global registries or caches whose state affects later semantic output;
5. emit evidence as runtime state;
6. invoke another renderer;
7. start a nested projection refresh;
8. acquire locks;
9. create commits, branches or pull requests;
10. perform network access;
11. invoke subprocesses or shell commands;
12. modify acceptance state or trust state.

Read-only internal memoization MAY be used only when cache identity covers the complete invocation fingerprint and cache loss cannot change output semantics. A cache MUST NOT become canonical state or evidence authority.

## 11. One invocation, one registered target

One renderer invocation MUST compute exactly one registered target identity.

A renderer MUST NOT:

- return a map of multiple targets;
- trigger another renderer;
- orchestrate dependent projections;
- update sibling regions;
- infer additional target identities from source content.

When multiple targets derive from the same canonical sources, each target requires its own registered contract, invocation, plan and lifecycle transition. Workflow orchestration MAY coordinate these refreshes, but the renderers remain independent.

## 12. Renderer version and fingerprints

Every renderer implementation used by a projection contract MUST expose a stable renderer-version identity.

The renderer version MUST change when an implementation change can alter output for identical declared inputs.

The renderer-version identity MUST be included in:

- the projection-contract fingerprint or its referenced version domain;
- immutable mutation plans;
- acceptance-state records;
- mutation evidence.

A source-code commit SHA MAY contribute to implementation evidence, but a raw current HEAD MUST NOT substitute for a stable renderer version when the contract requires reproducibility across refs.

The exact version representation remains `NEEDS_MAIN_REPO_VALIDATION`.

## 13. Validation before and after rendering

Before invocation, the lifecycle MUST validate:

- the renderer identifier;
- static mapping uniqueness;
- renderer-version availability;
- declared source completeness;
- configuration schema and version;
- target semantics;
- target identity;
- partition-contract identity for region targets.

After invocation and before plan capture, the lifecycle MUST validate:

- return type;
- encoding viability;
- empty-output policy;
- normalization rules;
- payload-only behavior for region targets;
- output fingerprint;
- size or bounded-resource policy where governed.

A renderer MUST NOT silently coerce invalid sources or invalid output into a valid-looking projection.

## 14. Failure contract

Renderer failures are explicit non-accepted outcomes.

A renderer invocation may fail because of:

- missing or invalid declared input;
- unknown renderer identity or version;
- invalid configuration;
- deterministic computation error;
- invalid output type;
- target-semantics violation;
- detected side effect;
- resource-bound violation.

On failure:

- no mutation plan authorizing a write may be produced;
- no target write may occur;
- the refresh attempt becomes `abandoned` through the lifecycle;
- the lifecycle emits the applicable abstract finding and bounded evidence;
- no fallback renderer may be selected automatically;
- prior accepted bytes and acceptance state remain unchanged unless DPA-500 defines an explicit independent invalidation rule.

DPA-500 owns finding identifiers, severity and gate consequences.

## 15. Resource bounds

Renderer execution SHOULD have explicit resource bounds appropriate to the target and implementation environment.

A resource policy MAY constrain:

- maximum input size;
- maximum output size;
- recursion depth;
- execution duration;
- memory use.

A resource limit MUST be deterministic, documented and applied as a validation or execution failure. Exceeding a limit MUST NOT produce truncated accepted output.

Concrete enforcement remains `NEEDS_MAIN_REPO_VALIDATION`.

## 16. Security and isolation

Registry data MUST NOT select arbitrary executable code.

Renderers MUST treat declared source text as data, not executable instructions.

Template or formatting facilities MUST NOT permit arbitrary code execution, imports, filesystem traversal or shell expansion.

Secrets, credentials and unrelated environment variables MUST NOT be exposed to renderers unless an accepted future contract explicitly establishes a bounded need. Such a future contract MUST preserve determinism and authority boundaries.

## 17. Conformance tests

A conforming implementation MUST include tests for:

1. known renderer identifier resolution;
2. unknown identifier rejection;
3. duplicate or ambiguous mapping rejection;
4. executable/dynamic registry reference rejection;
5. identical-input deterministic output;
6. fresh-process deterministic output where practical;
7. undeclared-input access rejection;
8. environment/time/randomness independence;
9. return-type enforcement;
10. renderer side-effect detection or prevention;
11. no file writes;
12. no lock acquisition;
13. no subprocess or network access;
14. no renderer chaining;
15. exactly one target per invocation;
16. payload-only region output;
17. partition-byte rejection;
18. empty-output policy;
19. malformed configuration rejection;
20. renderer-version drift invalidating an existing plan;
21. prior target bytes not used as semantic fallback;
22. evidence and acceptance state not used as inputs.

Tests MAY use fakes or capability-restricted contexts, but the production boundary MUST provide equivalent guarantees.

## 18. Relationship to existing command paths

Existing commands and workflows MAY request rendering only through the existing lifecycle.

They MUST NOT:

- call a renderer and write its result directly;
- bypass plan capture;
- pass ambient mutable repository objects into the renderer;
- assign acceptance based on renderer success alone.

If `CURRENT_HANDOFF.md` is later selected, the observed `admin-refresh-pr` path must route its renderer invocation through DPA-300. This statement does not select a document form and remains subject to Probe-time writer inventory and compatibility evidence.

## 19. Main-repository validation boundary

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- static renderer-map location and representation;
- callable signature and capability restriction mechanism;
- renderer-version representation;
- actual existing renderer candidates and reuse suitability;
- enforcement of filesystem, network and subprocess prohibition;
- deterministic resource-bound implementation;
- integration with the observed command and lifecycle surfaces;
- finding and gate mapping;
- exact tests and CI placement.

No claim in this document states that the current main repository already conforms.

## 20. Later-spec obligations

### DPA-500

DPA-500 MUST define findings and gates for:

- unknown or changed renderer identity;
- renderer output drift;
- nondeterministic output;
- invalid return type;
- side-effect or undeclared-input violations;
- renderer-version mismatch;
- evidence and acceptance-state requirements.

### DPA-600

DPA-600 MUST ensure renderer output is never integrated from a stale base, source, contract, renderer or target context across competing refs.

### DPA-700

DPA-700 MUST define rollback consequences when renderer behavior changes or a prior renderer version is no longer executable.

### DPA-800

DPA-800 MUST define:

- Probe recipes for renderer-map and purity compatibility;
- DP2 implementation steps;
- exact-ref renderer evidence;
- staged adoption and rollback;
- independent-context verification for high-risk renderer/lifecycle mutations only if later accepted governance requires it.

## 21. Invalid renderer states

The following are invalid:

1. unknown or ambiguous renderer identifier;
2. registry-selected executable import path;
3. renderer invocation before contract validation;
4. undeclared semantic input;
5. ambient repository discovery;
6. time-, random-, environment- or host-dependent output not declared by contract;
7. mutable global state affecting output;
8. renderer file, state, evidence or acceptance-state write;
9. lock acquisition;
10. subprocess or network access;
11. renderer chaining;
12. multi-target output;
13. partition bytes in region payload;
14. manual or historical bytes in renderer output;
15. invalid output type;
16. disallowed empty output;
17. silent fallback renderer;
18. renderer-version mismatch ignored by planning;
19. prior target or evidence used as semantic fallback;
20. renderer success represented as acceptance.

## 22. Review-ready criteria

DPA-400 may become `review-ready` when:

1. its authority boundary is consistent with DPA-000 through DPA-300;
2. identity, input, output, purity, determinism and failure contracts are complete;
3. every requirement is traceable to invariants, decisions, tests, later gates, evidence and rollback;
4. diagrams are synchronized with the normative text;
5. repository-specific implementation statements remain exact-ref fenced;
6. primary review, secondary verification, maintainer adjudication and required post-adjudication verification are complete.

DPA-400 MUST NOT become `stable` before relevant renderer compatibility and purity Probes have evidence at an exact main-repository validation ref.
