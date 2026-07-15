# DPA-300 — Registry and Lifecycle Integration

Status: draft

Status-date: 2026-07-15

Authority: normative DPA specification, subject to review and adjudication

## 1. Purpose

This specification defines how document projection contracts integrate with the existing documentation registry and document lifecycle of `vfi64/agentic-project-kit`.

DPA-300 does not create a second registry, lifecycle, evidence service, workspace abstraction, command family or gate architecture. It defines the contract by which the existing mechanisms are extended after implementation validation.

All concrete main-repository module names, field names and command mappings remain `NEEDS_MAIN_REPO_VALIDATION` until a DP1 Probe is executed against an exact validation ref.

## 2. Normative dependencies

DPA-300 depends on:

- DPA-000 for architectural invariants;
- DPA-100 for authority, terminology, freshness and trust-state vocabulary;
- DPA-200 for document forms, registered targets, registered regions, partition ownership and target semantics;
- DPA-ADR-001 through DPA-ADR-015;
- DP1 Discovery records DISC-001 through DISC-010 at validation ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`.

Discovery evidence informs this contract but is not normative authority.

## 3. Scope

DPA-300 owns:

1. projection-contract representation in the existing documentation registry;
2. registry validation and static contract loading;
3. lifecycle planning for projection refreshes;
4. mutation-plan identity and stale-plan invalidation;
5. local mutation-lock requirements;
6. lifecycle-owned target and partition writes;
7. post-write verification;
8. direct-write detection boundaries;
9. evidence emission after validation and mutation;
10. integration obligations for existing commands that mutate candidate documents.

DPA-300 does not own:

- renderer implementation and purity details, owned by DPA-400;
- finding severity and gate policy, owned by DPA-500;
- cross-branch and cross-PR serialization, owned by DPA-600;
- migration selection and rollback policy, owned by DPA-700;
- concrete implementation sequencing, owned by DPA-800.

## 4. Integration principle

The existing documentation registry MUST remain the sole registry authority for projection contracts.

The existing document lifecycle MUST remain the sole writer of registered projection targets and lifecycle-owned partition bytes.

Workflow orchestration MAY request, schedule or serialize a refresh, but MUST NOT write projection targets directly.

Renderers MUST NOT write files, acquire locks, update registry state, emit acceptance decisions or invoke other renderers.

## 5. Registry projection contract

### 5.1 Optional extension

A projection contract MUST be represented as an optional extension of an existing registered-document entry.

Manual documents without a projection contract MUST remain valid and retain their existing behavior.

Unknown, malformed or partially declared projection metadata MUST fail loud. It MUST NOT silently downgrade a registered projection to manual-document behavior.

The exact serialized field name remains `NEEDS_MAIN_REPO_VALIDATION` until PROBE-001. The semantic object is named `ProjectionContract` in this specification.

### 5.2 Required fields

A `ProjectionContract` MUST declare:

- contract schema version;
- target identity;
- primary document form;
- renderer identifier;
- ordered declared canonical sources;
- contract-declared representation configuration, if any;
- target semantics;
- lifecycle policy identifier;
- freshness policy identifier;
- fingerprint algorithm and input-domain version;
- evidence policy identifier;
- compatibility or migration version.

A region target MUST additionally declare:

- parent document identity;
- region identity;
- partition-contract identity;
- boundary representation;
- region write owner;
- malformed-boundary behavior.

### 5.3 Static and declarative form

Projection metadata MUST be declarative.

It MUST NOT contain:

- executable import paths;
- arbitrary plugin references;
- shell fragments;
- dynamic expressions;
- unreviewed file globs as semantic sources;
- runtime fallback commands.

Renderer identifiers MUST resolve through the static reviewed mapping defined by DPA-400.

### 5.4 Contract identity

Every effective projection contract MUST have a deterministic contract fingerprint.

The contract fingerprint MUST cover every registry field that can change:

- source selection;
- renderer resolution;
- semantic output;
- target byte representation;
- ownership;
- validation;
- write behavior;
- evidence or gate interpretation.

A registry edit that changes any covered input MUST invalidate every previously captured mutation plan.

## 6. Contract loading and validation

The lifecycle MUST load a projection contract only through the existing registry loader and validator path.

Validation MUST complete before renderer invocation or mutation planning.

Validation MUST reject at least:

- missing required fields;
- unknown contract schema versions;
- unknown renderer identifiers;
- ambiguous target identity;
- duplicate target identity;
- overlapping registered regions;
- unowned target bytes;
- multiple write owners for one byte range;
- region targets without one partition contract;
- undeclared canonical sources;
- evidence or generated output declared as canonical input without separate canonical authority;
- target semantics missing any DPA-200 required element;
- unsupported document-form combinations;
- a lifecycle policy that permits renderer writes;
- silent fallback to manual behavior.

Registry validation MUST be side-effect free.

## 7. Lifecycle operation model

A projection refresh MUST follow this ordered lifecycle:

1. **Resolve** — load Workspace, registry entry, effective projection contract and target identity.
2. **Inspect** — read declared sources, target bytes, partition metadata and relevant repository state.
3. **Validate** — validate registry, authority, target form, boundaries and renderer resolution prerequisites.
4. **Render** — obtain text or bytes from exactly one renderer invocation for exactly one registered target.
5. **Plan** — construct an immutable mutation plan without writing the target.
6. **Preflight** — recheck all plan preconditions before lock acquisition.
7. **Lock** — acquire the existing workspace mutation lock for the bounded local mutation.
8. **Revalidate** — recompute plan guards under the lock.
9. **Write** — perform one lifecycle-owned atomic target mutation.
10. **Verify** — reread the target and verify exact planned bytes, boundaries and fingerprints.
11. **Record** — emit bounded evidence and findings.
12. **Release** — release the local mutation lock.

A failure before `Write` MUST leave the target unchanged.

A failure after `Write` MUST produce an explicit incomplete-mutation or post-write-verification finding and MUST NOT mark the output `accepted`.

## 8. Mutation plan contract

### 8.1 Required plan fields

A mutation plan MUST include:

- plan schema version;
- exact repository base SHA;
- registry-entry identity;
- contract fingerprint;
- renderer identifier and renderer-version fingerprint;
- ordered source identities and source fingerprints;
- target identity;
- observed pre-mutation target fingerprint;
- partition fingerprint for region targets;
- planned output fingerprint;
- planned complete target bytes or exact bounded replacement payload;
- target semantics version;
- write mode;
- required lock scope;
- creation timestamp as evidence only;
- plan creator identity or command context;
- explicit dry-run status.

Time MUST NOT determine plan validity by itself.

### 8.2 Dry-run default

Planning MUST default to dry-run.

A mutation command MUST require an explicit execution signal and an exact plan identity or equivalent deterministic recomputation guard.

A generic `--execute` flag without plan binding is insufficient for projection mutation.

### 8.3 Plan identity

The plan identity MUST be a deterministic fingerprint over all semantic and mutation preconditions.

The plan identity MUST change when any of the following changes:

- base SHA;
- contract;
- renderer identity or version;
- declared source content;
- target content;
- partition metadata;
- target semantics;
- planned output.

## 9. Stale-plan invalidation

A plan MUST be rejected before write when any captured guard differs from current state.

At minimum, rejection MUST occur for:

- base drift;
- source drift;
- target drift;
- contract drift;
- renderer drift;
- partition drift;
- ownership drift.

The lifecycle MUST NOT automatically merge current target changes into generated output.

Historical or manual bytes MUST NOT be reconstructed from a stale target during plan recovery.

Regeneration from declared authoritative sources is the only permitted generated-content recovery path.

## 10. Lock and write contract

### 10.1 Local lock

Every projection mutation MUST acquire the existing workspace mutation lock.

The lock protects local workspace mutation only. It MUST NOT be represented as cross-branch or cross-PR serialization.

Nested lifecycle calls MAY rely on the existing same-process reentrancy behavior only where the complete call graph has one top-level mutation owner and deterministic release behavior.

### 10.2 Sole writer

The lifecycle MUST be the sole writer of:

- full projection targets;
- projected regions;
- lifecycle-owned partition bytes;
- generated target metadata stored with the target.

A renderer, workflow coordinator, evidence writer, manual editor or migration helper MUST NOT write those bytes directly.

### 10.3 Atomicity

The write operation MUST be atomic at the target-file boundary or MUST provide an equivalent crash-safe replacement contract proven by Probe evidence.

For a region target, the lifecycle MUST construct and atomically replace the complete parent document. In-place partial writes are prohibited.

The rendered payload MUST NOT include lifecycle-owned boundary bytes unless a later accepted contract explicitly changes DPA-ADR-013.

### 10.4 Pre-write preservation

For hybrid documents, bytes outside the governed projected region MUST be copied from the validated pre-mutation target without semantic interpretation.

Their fingerprint MUST be captured in the plan and revalidated under lock.

The lifecycle MUST fail rather than guess when boundaries cannot be resolved exactly.

## 11. Post-write verification

After write and before any acceptance transition, the lifecycle MUST:

- reread the complete target;
- verify the complete target fingerprint;
- verify the projected region payload;
- verify exactly one ordered boundary pair for each registered region;
- verify byte identity of preserved regions;
- verify terminal newline and normalization semantics;
- verify that the effective contract and source fingerprints still match the plan;
- emit a deterministic verification result.

A successful write moves bytes only to `written-unverified` until the complete required DPA-500 gate set accepts them.

The lifecycle MUST NOT directly assign `accepted`.

## 12. Direct-write detection

The system MUST be able to distinguish lifecycle-owned writes from out-of-band target changes.

The minimum contract is:

1. the lifecycle records the accepted contract, source, target and output fingerprints;
2. later inspection recomputes the expected projection;
3. a target mismatch not explained by a currently valid lifecycle plan is target drift;
4. boundary mutation outside a valid lifecycle plan is partition drift;
5. out-of-band changes MUST produce findings and MUST NOT be silently normalized.

DPA-300 does not require an operating-system file watcher. Detection MAY occur at command preflight, audit, gate or refresh time.

Evidence of a previous lifecycle write MUST NOT itself authorize a later write.

## 13. Evidence emission

Lifecycle evidence MUST be bounded, reproducible and non-authoritative.

A mutation evidence record SHOULD include:

- repository and base SHA;
- registry identity and contract fingerprint;
- plan identity;
- renderer identity;
- source fingerprints;
- target pre- and post-fingerprints;
- partition fingerprints;
- lock acquisition and release result;
- write result;
- post-write verification result;
- produced findings;
- command context;
- limitations.

Evidence MUST NOT become a semantic renderer input or canonical source.

Evidence-writing failure after a successful verified target write MUST be reported explicitly. It MUST NOT be concealed as a complete lifecycle success.

## 14. Existing command integration

Existing commands that write candidate documents MUST be routed through the lifecycle contract when their target becomes a registered projection target.

At the recorded validation ref, Discovery identified:

`agentic-kit transfer admin-refresh-pr`

through the observed implementation path:

`transfer_repo_actions._refresh_operational_handoff_docs()`

This is a `VERIFIED` observation only at validation ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`.

If `CURRENT_HANDOFF.md` is later selected as a projection target, the existing command MUST be adapted rather than replaced by a parallel DPA-only refresh command.

The adapted path MUST:

- update declared canonical state before rendering;
- call the existing registry and lifecycle integration;
- use a lifecycle mutation plan;
- replace the governed region rather than append another current-state block;
- preserve validated bytes outside the region;
- retain existing branch/PR orchestration and handoff-package behavior;
- fail loud on malformed boundaries;
- emit post-write verification and evidence.

This requirement does not select a production document form. Form eligibility remains a later DP1 Assessment decision.

## 15. Trust-state integration

DPA-300 owns lifecycle transitions among:

- `computed`;
- `plan-captured`;
- `written-unverified`;
- `abandoned`.

DPA-500 owns the gate transition to `accepted`.

Required transition rules:

- successful renderer completion MAY produce `computed`;
- successful immutable plan capture MAY produce `plan-captured`;
- successful atomic write and byte verification MAY produce `written-unverified`;
- failed validation, invalidated plan or rejected mutation MUST produce `abandoned` for that refresh instance;
- no renderer, command wrapper or workflow coordinator may assign `accepted`.

Drift of previously accepted bytes starts a new refresh instance; it does not rewrite historical trust-state evidence.

## 16. Failure behavior

The lifecycle MUST fail loud and preserve the target when:

- registry validation fails;
- renderer resolution fails;
- a canonical source is missing;
- target identity is ambiguous;
- boundaries are missing, duplicated, overlapping or reordered;
- the plan is stale;
- the workspace lock cannot be acquired;
- preserved bytes changed after planning;
- output violates target semantics;
- atomic replacement cannot be established;
- post-write verification fails.

A warning-only lifecycle signal MUST NOT authorize mutation.

No temporal signal may cause a hard failure solely because time elapsed.

## 17. Compatibility requirements

Implementation MUST preserve:

- validity and behavior of registry entries without projection contracts;
- existing manual-document workflows;
- existing registry ownership and parser authority;
- existing Workspace path resolution;
- existing local mutation-lock semantics;
- existing command entry points where they remain user-facing contracts;
- existing branch and PR orchestration unless a later accepted DPA-600 decision replaces it.

Compatibility MUST be demonstrated by DP1 Probe evidence. It MUST NOT be inferred from this specification.

## 18. Repository-validation obligations

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- the serialized registry extension shape;
- unknown-field compatibility behavior of the actual parser;
- exact lifecycle class and command integration points;
- atomic-write implementation;
- complete direct-write detection path;
- projection finding identifiers;
- required-check mapping;
- whether region targets are representable in the existing registry;
- whether `CURRENT_HANDOFF.md` is eligible for any projection form.

## 19. Planned DP1 Probes

DPA-300 requires:

- PROBE-001 — registry projection-schema compatibility;
- PROBE-002 — `CURRENT_HANDOFF.md` governed bounded replacement, limited to DPA-300-owned aspects until DPA-400 through DPA-700 exist;
- PROBE-003 — lifecycle finding compatibility, jointly with DPA-500;
- PROBE-005 — local lock and orchestration compatibility, jointly with DPA-600.

A Probe MAY falsify an implementation mapping without invalidating the architecture. A falsified mapping MUST return the specification or implementation plan to adjudication.

## 20. Conformance requirements

A conforming DPA-300 implementation MUST demonstrate:

1. backward-compatible registry loading for manual documents;
2. fail-loud projection-contract validation;
3. deterministic plan identity;
4. dry-run by default;
5. stale-plan rejection for every captured guard;
6. existing workspace-lock use;
7. sole lifecycle ownership of target and partition writes;
8. atomic complete-file replacement;
9. exact preservation of non-projected bytes;
10. post-write byte verification;
11. direct-write drift detection;
12. non-authoritative evidence emission;
13. no direct transition to `accepted`;
14. integration of existing mutating command paths rather than creation of a parallel subsystem.

## 21. Exit criteria

DPA-300 may advance to `review-ready` only when:

- this contract is complete and internally consistent;
- every requirement is traceable to invariants, evidence, tests, Probe obligations and rollback consequences;
- registry, lifecycle and command-flow diagrams are synchronized;
- an internal pre-review audit reports no known contradiction with stable DPA-000, DPA-100 or review-ready DPA-200;
- all repository-specific claims remain exact-ref bounded;
- no production form or implementation success is claimed;
- a qualifying primary architecture review prompt is bound to one immutable commit.

DPA-300 may advance to `stable` only after qualifying review, maintainer adjudication, required corrections and post-adjudication verification.