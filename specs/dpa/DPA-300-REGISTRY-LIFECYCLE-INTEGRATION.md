# DPA-300 — Registry and Lifecycle Integration

Status: draft

Status-date: 2026-07-15

Authority: normative DPA specification, subject to post-adjudication verification

## 1. Purpose

This specification defines how document projection and partition contracts integrate with the existing documentation registry and document lifecycle of `vfi64/agentic-project-kit`.

DPA-300 does not create a second registry, lifecycle, evidence service, Workspace abstraction, command family, state authority or gate architecture. It defines the contract by which the existing mechanisms are extended after implementation validation.

Concrete main-repository module names, serialized fields, paths and command mappings remain `NEEDS_MAIN_REPO_VALIDATION` until the corresponding DP1 Probe is executed against an exact validation ref.

## 2. Normative dependencies

DPA-300 depends on:

- DPA-000 for architectural invariants;
- DPA-100 for authority, lifecycle-state, trust-state, drift and fingerprint vocabulary;
- DPA-200 for document forms, registered targets, regions, partition ownership and target semantics;
- DPA-ADR-001 through DPA-ADR-017;
- DP1 Discovery records DISC-001 through DISC-010 and DISC-003b at validation ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`.

Discovery evidence informs this contract but is not normative authority.

## 3. Scope

DPA-300 owns:

1. projection-contract and partition-contract representation in the existing registry;
2. static contract loading and fail-loud validation;
3. lifecycle refresh planning;
4. immutable plan identity and stale-plan invalidation;
5. local mutation-lock requirements;
6. lifecycle-owned target and partition writes;
7. interrupted-refresh detection and recovery;
8. post-write verification;
9. acceptance-state persistence and direct-write classification;
10. bounded evidence emission;
11. integration obligations for existing candidate-document writers.

DPA-300 does not own renderer implementation details, gate severity policy, cross-ref serialization, migration selection or concrete implementation sequencing. Those belong respectively to DPA-400, DPA-500, DPA-600, DPA-700 and DPA-800.

## 4. Integration principle

The existing documentation registry MUST remain the sole registry authority for projection and partition contracts.

The existing document lifecycle MUST remain the sole writer of registered projection targets, lifecycle-owned partition bytes and projection lifecycle state.

Workflow orchestration MAY request, schedule or serialize a refresh, but MUST NOT write projection targets or assign trust states directly.

Renderers MUST NOT write files, acquire locks, update registry or lifecycle state, emit acceptance decisions or invoke another renderer.

## 5. Registry contracts

### 5.1 Optional projection extension

A projection contract MUST be an optional extension of an existing registered-document entry.

Manual documents without a projection contract MUST remain valid and retain existing behavior.

Unknown, malformed or partially declared projection metadata MUST fail loud and MUST NOT silently downgrade to manual behavior.

The exact serialized field names remain `NEEDS_MAIN_REPO_VALIDATION` until PROBE-001. The semantic object is `ProjectionContract`.

### 5.2 ProjectionContract required fields

A `ProjectionContract` MUST declare:

- contract schema version;
- target identity;
- primary document form;
- renderer identifier;
- ordered declared canonical sources;
- contract-declared representation configuration, if any;
- complete DPA-200 target semantics;
- lifecycle policy identifier;
- freshness policy identifier;
- fingerprint algorithm and input-domain version;
- evidence policy identifier;
- compatibility or migration version.

A region projection MUST additionally declare:

- parent document identity;
- region identity;
- parent partition-contract identity;
- region payload target semantics.

A projected region MUST NOT independently configure partition-byte ownership, boundary representation, malformed-boundary behavior or a non-lifecycle write owner.

### 5.3 Parent PartitionContract

A parent registered-document entry containing registered regions MUST declare exactly one `PartitionContract`.

The `PartitionContract` MUST declare:

- partition schema version and identity;
- parent document identity;
- complete ordered region identities;
- one owner class for every region;
- projected, manual and historical region classification;
- adjacency and ordering constraints;
- boundary representation for every boundary or one document-wide rule;
- separator ownership where separators exist;
- encoding and normalization rules affecting partition bytes;
- missing, duplicate, overlapping, reordered and malformed-boundary behavior;
- partition fingerprint algorithm and input-domain version.

The partition contract MUST explain ownership of every target byte.

### 5.4 Static and declarative form

Projection and partition metadata MUST be declarative. They MUST NOT contain executable import paths, arbitrary plugin references, shell fragments, dynamic expressions, unreviewed semantic globs or runtime fallback commands.

Renderer identifiers MUST resolve through the static reviewed mapping defined by DPA-400.

### 5.5 Contract identity

Every effective projection and partition contract MUST have a deterministic fingerprint covering every field that can change source selection, renderer resolution, semantic output, target representation, partitioning, ownership, validation, write behavior or interpretation by evidence and gates.

A covered registry change MUST invalidate every previously captured mutation plan and accepted-state comparison that depends on the changed contract.

## 6. Contract loading and validation

The lifecycle MUST load contracts only through the existing registry loader and validator path. Validation MUST complete before renderer invocation or mutation planning and MUST be side-effect free.

Validation MUST reject at least:

- missing required fields;
- unknown contract or partition schema versions;
- unknown fingerprint algorithms or input-domain versions;
- unknown renderer identifiers;
- ambiguous or duplicate target identity;
- region targets without exactly one valid parent partition contract;
- dangling or inconsistent partition references;
- regions absent from the parent's ordered region list;
- overlapping regions or unexplained bytes;
- multiple owners for one byte range;
- independently configurable projected-region boundary ownership;
- undeclared canonical sources;
- evidence, lifecycle state, generated output or historical prose used as canonical input without separate accepted authority;
- incomplete target semantics;
- unsupported form combinations;
- renderer-write permission;
- silent fallback to manual behavior.

## 7. Lifecycle operation model

A projection refresh MUST follow this ordered lifecycle:

1. **Recover** — detect and dispose of an interrupted prior refresh for the same target.
2. **Resolve** — load Workspace, registry entry, effective contracts, acceptance state and target identity.
3. **Inspect** — read declared sources, target bytes, partition bytes and relevant repository state.
4. **Validate** — validate registry, authority, form, partition and renderer prerequisites.
5. **Render** — invoke exactly one renderer once for exactly one registered target payload.
6. **Plan** — capture an immutable mutation plan without writing.
7. **Preflight** — recheck all guards before lock acquisition.
8. **Lock** — acquire the existing Workspace mutation lock.
9. **Revalidate** — recompute every plan guard under the lock without a second render when captured semantic inputs remain identical.
10. **Write** — perform one lifecycle-owned atomic complete-target replacement.
11. **Verify** — reread and verify exact planned bytes, partition and fingerprints.
12. **Record** — persist lifecycle state and emit bounded evidence and findings.
13. **Release** — release the local lock.

A failure before Write MUST leave target bytes unchanged.

A successful Write immediately places the refresh output in `written-unverified`.

Verification or state/evidence failure after Write MUST emit explicit findings and MUST NOT produce `accepted`.

## 8. Mutation plan contract

### 8.1 Required fields

A mutation plan MUST include:

- plan schema version and deterministic plan identity;
- exact repository base SHA;
- registry-entry identity;
- projection-contract fingerprint;
- partition-contract fingerprint where applicable;
- renderer identifier and renderer-version fingerprint;
- ordered source identities and source fingerprints;
- target identity;
- observed pre-mutation complete-target fingerprint;
- expected complete-target fingerprint;
- planned payload fingerprint;
- planned complete target bytes or exact payload plus deterministic reconstruction inputs;
- preserved-region fingerprint for hybrid targets;
- target semantics version;
- write mode;
- required lock scope;
- creator command context;
- creation timestamp as evidence only;
- explicit dry-run status.

For region targets, payload, preserved-region, partition and expected complete-target fingerprints are all mandatory and distinct.

Time MUST NOT determine plan validity by itself.

### 8.2 Dry-run and execution binding

Planning MUST default to dry-run.

Mutation requires an explicit execution signal and exact plan identity or an equivalent deterministic recomputation guard. A generic `--execute` without plan binding is insufficient.

### 8.3 Plan identity

The plan identity MUST cover every semantic and mutation precondition. It MUST change on base, contract, partition, renderer, source, target, ownership, target-semantics or output change.

## 9. Stale-plan invalidation

A plan MUST be rejected before Write when any captured guard differs from current state.

The lifecycle MUST classify the mismatches using the DPA-100 drift vocabulary: base, source, target, contract, renderer, partition and ownership drift. Multiple classes MAY be reported together.

The lifecycle MUST NOT merge current target changes into generated output or reconstruct historical/manual bytes from a stale target. Regeneration from declared canonical sources is the only generated-content recovery path.

## 10. Lock, nested mutation and atomic write

### 10.1 Local lock

Every projection mutation MUST acquire the existing Workspace mutation lock. It protects only the local workspace and MUST NOT be represented as branch or PR serialization.

A projection refresh MUST NOT initiate another projection refresh or acquire the lock for a second projection mutation while holding it.

Existing same-process reentrancy MAY be used only by outer orchestration wrapping exactly one projection refresh with deterministic release.

### 10.2 Sole writer

The lifecycle MUST be the sole writer of:

- full projection targets;
- projected regions through complete-parent replacement;
- partition bytes;
- acceptance-state records;
- generated target metadata governed by the contract.

Renderers, workflow coordinators, evidence writers, manual editors and migration helpers MUST NOT write those bytes or state directly.

### 10.3 Atomicity

The write MUST atomically replace the complete target file or provide an equivalent crash-safe replacement proven by Probe evidence.

In-place partial region writes are prohibited. The target MUST expose either complete prior bytes or complete planned replacement bytes.

Renderer payload MUST exclude lifecycle-owned partition bytes.

### 10.4 Preserved bytes

For hybrid targets, bytes outside the projected region MUST be copied from the validated pre-mutation target without semantic interpretation. Their fingerprint MUST be in the plan and revalidated under lock.

The lifecycle MUST fail rather than guess when boundaries cannot be resolved exactly.

## 11. Post-write verification

After Write and before any acceptance transition, the lifecycle MUST:

- reread the complete target;
- verify the expected complete-target fingerprint;
- verify the projected payload fingerprint;
- verify partition fingerprint and ordered boundaries;
- verify byte identity of preserved regions;
- verify encoding, normalization and terminal newline semantics;
- verify contract, renderer and source guards still match the plan;
- emit a deterministic verification result.

Verification success retains `written-unverified` until DPA-500 accepts the complete required gate set. Verification failure transitions the refresh instance to `abandoned` and emits a finding. The lifecycle MUST NOT assign `accepted`.

## 12. Acceptance state and direct-write detection

### 12.1 Persisted acceptance-state record

For every accepted target or region, the lifecycle MUST persist one Workspace-resolved acceptance-state record under `.agentic/` lifecycle state after validated implementation.

The record is lifecycle state, not evidence, registry authority, canonical source state or renderer input.

It MUST include:

- target and region identity;
- accepted plan identity;
- projection- and partition-contract fingerprints;
- renderer identity and version fingerprint;
- ordered accepted source fingerprints;
- accepted base or precondition identity;
- accepted payload and complete-target fingerprints;
- partition and preserved-region fingerprints where applicable;
- acceptance event identity and evidence-only timestamp.

The exact path and serialized schema remain `NEEDS_MAIN_REPO_VALIDATION` for PROBE-002.

### 12.2 Drift classification

Later inspection MUST compare current state independently with the acceptance-state record:

- changed declared sources produce source drift;
- target bytes differing from accepted complete-target bytes produce target drift;
- changed partition contract or partition bytes produce partition drift;
- changed contract, renderer, base or ownership produce their corresponding class;
- simultaneous differences produce simultaneous findings.

Recomputation MAY be a secondary integrity check but MUST NOT replace persisted comparison or use evidence as runtime state.

Out-of-band changes MUST produce findings and MUST NOT be silently normalized.

Detection MAY occur at refresh, preflight, audit or gate time; an OS watcher is not required.

## 13. Interrupted-refresh recovery

Before a new plan or mutation for a target, the lifecycle MUST detect an interrupted prior instance, including:

- a stale lock associated with a prior refresh;
- a persisted plan without matching completed verification/state sequence;
- target bytes matching a planned-but-unverified output;
- lifecycle state indicating Write occurred without completed Record and Release.

The detecting lifecycle operation MUST transition the interrupted instance to `abandoned`, emit a finding and record stale-lock takeover and recovery disposition before proceeding.

Written bytes MAY be re-verified against the recovered plan only when the exact plan is available and every captured base, source, target, contract, renderer, partition, ownership and output guard still matches.

If any guard differs or the plan cannot be recovered exactly, the generated content MUST be regenerated. Interrupted bytes MUST NOT be silently accepted, merged with historical prose or treated as authority.

Orphaned plan/state cleanup MUST preserve enough bounded evidence to explain the disposition but MUST NOT create a new history store.

## 14. Evidence emission

Lifecycle evidence MUST be bounded, reproducible and non-authoritative.

A mutation evidence record MUST include:

- repository and base SHA;
- registry, contract and plan identities;
- renderer identity;
- source, target, output and partition fingerprints;
- lock and recovery result;
- Write and Verify result;
- lifecycle-state update result;
- produced findings;
- command context and limitations.

Additional context MAY be recorded.

Evidence MUST NOT become a renderer input, canonical source or acceptance-state substitute.

Evidence-writing failure after verified Write MUST remain `written-unverified`, emit a finding and block DPA-500 acceptance.

## 15. Existing command integration

Every existing command that writes a candidate target MUST be routed through this lifecycle if that target becomes a registered projection target.

Discovery verified **an observed writer path** at validation ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`:

`agentic-kit transfer admin-refresh-pr`

→ `transfer_repo_actions._refresh_operational_handoff_docs()`

DISC-003b verified that the inspected `transfer chat-switch-complete` path does not write `CURRENT_HANDOFF.md` at that ref. Global writer-set completeness remains a Probe-time revalidation obligation.

If `CURRENT_HANDOFF.md` is later selected as a projection target, every then-known writer MUST be adapted rather than supplemented by a parallel DPA-only command.

The adapted behavior MUST update declared canonical state before rendering, use registry and lifecycle contracts, execute a plan-bound atomic replacement, preserve validated outside-region bytes, retain branch/PR orchestration, fail loud on malformed partition state and emit verification, lifecycle state and evidence.

DPA-300 constrains governed write behavior, not permanent CLI naming. User-facing commands MAY evolve through the main repository's command-deprecation governance.

This clause does not select a production document form.

## 16. Trust-state integration

DPA-300 owns transitions among `computed`, `plan-captured`, `written-unverified` and `abandoned`. DPA-500 alone owns transition to `accepted`.

- successful renderer completion MAY produce `computed`;
- successful immutable plan capture MAY produce `plan-captured`;
- successful atomic Write MUST produce `written-unverified`;
- failed validation, invalid plan, failed verification, rejected mutation or detected interrupted instance MUST produce `abandoned` for that instance;
- no renderer, wrapper or workflow coordinator may assign `accepted`.

A new refresh instance starts at `computed` without rewriting the historical fact that prior bytes were accepted for their former scope.

## 17. Failure behavior

The lifecycle MUST fail loud and preserve pre-Write target bytes when registry validation, source resolution, renderer resolution, target identity, partition resolution, plan validity, lock acquisition, preserved-byte validation, output semantics or atomic replacement fails.

After Write, failure MUST follow §§11–14 and cannot be represented as complete success.

Warnings never authorize mutation. Mutation requires an explicit valid plan-bound execution path regardless of warning severity.

No temporal signal may cause a hard failure solely because time elapsed.

## 18. Compatibility requirements

Implementation MUST preserve manual registry entries and workflows, existing registry/parser authority, Workspace path resolution, local lock semantics, governed command behavior and existing branch/PR orchestration unless a later accepted specification changes the relevant contract.

Compatibility MUST be demonstrated by Probe evidence, not inferred from this specification.

## 19. Repository-validation obligations

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- serialized projection and partition shapes;
- parser unknown-field behavior;
- exact lifecycle integration points;
- acceptance-state path and schema;
- interrupted-instance detection mechanics;
- atomic replacement implementation;
- complete writer inventory at the Probe ref;
- finding identifiers and required-check mapping;
- region representability;
- production-form eligibility of any candidate.

## 20. Planned DP1 Probes

DPA-300 requires:

- PROBE-001 — registry projection/partition schema compatibility;
- PROBE-002 — lifecycle state, recovery and governed bounded replacement for every then-known `CURRENT_HANDOFF.md` writer, limited to available specification ownership;
- PROBE-003 — lifecycle finding compatibility with DPA-500;
- PROBE-005 — lock and orchestration compatibility with DPA-600.

A Probe MAY falsify an implementation mapping without invalidating the architecture. Falsified mappings return the specification or implementation plan to adjudication.

## 21. Conformance requirements

A conforming implementation MUST demonstrate:

1. backward-compatible manual registry loading;
2. fail-loud projection and partition validation;
3. deterministic plan identity;
4. dry-run by default and exact plan binding;
5. stale-plan rejection for every guard;
6. Workspace-resolved lifecycle state and paths;
7. existing local lock use without nested projection mutation;
8. sole lifecycle ownership;
9. atomic complete-file replacement;
10. exact preservation of non-projected bytes;
11. correct `written-unverified` timing;
12. post-write verification;
13. persisted acceptance state and correct multi-class drift detection;
14. interrupted-refresh recovery;
15. non-authoritative evidence;
16. no direct transition to `accepted`;
17. integration of existing writers without a parallel subsystem.

## 22. Exit criteria

DPA-300 may advance to `review-ready` only when:

- this contract, DPA-100 and DPA-200 are internally consistent;
- every requirement is traceable to invariants, decisions, evidence, tests, Probes and rollback consequences;
- registry, lifecycle, command, execution/trust and recovery diagrams are synchronized;
- Discovery completion claims reflect DISC-003b;
- all repository-specific claims remain exact-ref bounded;
- no production form or implementation success is claimed;
- independent post-adjudication verification passes.

DPA-300 may advance to `stable` only after qualifying review, maintainer adjudication, required corrections and any later stability review required by governance.
