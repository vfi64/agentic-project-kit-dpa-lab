# DPA-500 — Freshness and Gates

Status: draft
Status-date: 2026-07-17
Authority: normative DPA specification, subject to primary review, technical verification, Maintainer adjudication and applicable Probe evidence

## 1. Purpose

This specification defines freshness evaluation, findings, trust-state consequences and gate behavior for registered document projections.

DPA-500 extends the existing main-repository documentation registry, lifecycle, findings and gate architecture. It does not create a second freshness engine, a second finding taxonomy, a second gate runner, a second evidence store or a new runtime authority.

Repository-specific finding identifiers, severity mappings, command names, workflow integration points and strict-adoption switches remain `NEEDS_MAIN_REPO_VALIDATION` until validated against an exact main-repository ref.

## 2. Normative dependencies

DPA-500 depends on:

- DPA-000 for canonical invariants;
- DPA-100 for authority, classification, trust-state, finding, freshness, fingerprint and gate vocabulary;
- DPA-200 for target identity, document form, partition ownership and target semantics;
- DPA-300 for registry contracts, lifecycle ordering, immutable plans, acceptance state, recovery and evidence boundaries;
- DPA-400 for renderer identity, immutable inputs, semantic versions, deterministic output, purity and failure behavior;
- DPA-ADR-013, DPA-ADR-014, DPA-ADR-016, DPA-ADR-017, DPA-ADR-019 and DPA-ADR-020.

## 3. Scope

DPA-500 owns:

1. projection freshness dimensions;
2. freshness evaluation inputs;
3. structured drift classes;
4. abstract finding semantics;
5. trust-state consequences;
6. gate outcome semantics;
7. strictness and staged enforcement rules;
8. handling of missing, stale, tampered or unverifiable acceptance state;
9. handling of renderer, source, contract, target and evidence drift;
10. recovery-facing gate behavior;
11. freshness and gate test obligations.

DPA-500 does not own:

- registry serialization;
- target rendering or writing;
- lifecycle lock acquisition;
- workflow serialization across refs;
- concrete finding codes or severities before main-repository validation;
- command UX;
- migration-form selection;
- production implementation.

## 4. Authority boundary

Freshness evaluation is lifecycle-owned and gate-integrated.

A renderer MUST NOT:

- assign freshness;
- emit authoritative findings;
- select severity;
- assign trust state;
- decide gate pass or failure;
- repair stale state;
- accept its own output.

Evidence MAY explain a decision but MUST NOT become the authority that decides freshness or acceptance.

The existing main-repository gate architecture remains the sole production gate authority. DPA-500 defines the projection-specific contract that the existing architecture must later implement.

## 5. Freshness model

Freshness is multidimensional. A projection is fresh only when every applicable declared dimension is current and verifiable for the evaluated target identity.

The mandatory dimensions are:

1. **contract freshness** — the registered projection and partition contracts match the accepted contract identity and fingerprint;
2. **source freshness** — every declared canonical source matches the accepted ordered source fingerprints;
3. **configuration freshness** — output-affecting configuration matches the accepted configuration fingerprint;
4. **renderer freshness** — renderer identifier and semantic version match the accepted identities, and interface compatibility remains valid;
5. **target freshness** — current target or renderer-owned region bytes match the accepted output fingerprint;
6. **target-semantics freshness** — encoding, normalization, line-ending, partition and target-semantics versions match the accepted state;
7. **gate-set freshness** — the acceptance state records the gate-set identity required by the current contract;
8. **acceptance-state freshness** — the acceptance record is present, valid, correctly scoped and internally coherent;
9. **base-context freshness** — any base, repository or workflow identity required by the accepted plan remains current for the operation being authorized.

Time alone MUST NOT make a projection stale unless time is an explicitly declared semantic source or an accepted policy requires bounded revalidation for reasons independent of output equivalence.

## 6. Evaluation inputs

A freshness evaluation MUST use only lifecycle-resolved and Workspace-resolved inputs.

At minimum it evaluates:

- registered target identity;
- projection-contract identity and fingerprint;
- partition-contract identity and fingerprint when applicable;
- current declared-source fingerprints;
- current configuration fingerprint;
- renderer identifier;
- renderer interface version;
- renderer semantic version;
- current target, payload, preserved-region, partition and complete-target fingerprints as applicable;
- target-semantics version;
- acceptance-state record;
- current required gate-set identity;
- base or ref context where the requested operation requires it.

Missing mandatory input MUST produce an explicit non-fresh result. It MUST NOT be interpreted as fresh, unknown-but-pass or an invitation to infer prior state.

## 7. Acceptance state

Acceptance state is lifecycle state, not evidence.

A valid acceptance-state record MUST be scoped to exactly one registered target identity and MUST contain sufficient identities and fingerprints to reproduce the freshness comparison required by DPA-300 through DPA-500.

The record MUST include, directly or through a versioned schema:

- target identity;
- projection-contract identity and fingerprint;
- partition-contract identity and fingerprint when applicable;
- renderer identifier and semantic version;
- renderer interface version used for compatibility validation;
- ordered source fingerprints;
- configuration fingerprint;
- accepted output fingerprint or applicable payload and complete-target fingerprints;
- target-semantics version;
- gate-set identity;
- accepted lifecycle outcome;
- acceptance timestamp as evidence metadata only, not semantic freshness authority;
- schema version.

An acceptance-state record is invalid when it is missing required fields, uses an unknown schema version, names another target, cannot be parsed, contradicts the target contract or contains internally inconsistent fingerprints.

Invalid acceptance state MUST NOT be repaired silently from current target bytes or evidence.

## 8. Trust states

DPA-500 applies the consumer trust-state vocabulary owned by DPA-100.

For projection-gate purposes:

- `accepted` means the current target has passed all required checks against the current immutable plan and the acceptance state has been recorded successfully;
- `written-unverified` means bytes may have been written but complete verification and acceptance did not finish;
- `stale` means at least one current freshness dimension differs from the accepted state without evidence of malformed or hostile state;
- `invalid` means the target, contract, state or boundary cannot be safely interpreted under the registered contract;
- `unknown` means required current information is unavailable and no stronger valid state can be established;
- `abandoned` describes an attempt outcome and MUST NOT be misrepresented as target acceptance.

Trust-state assignment MUST be deterministic for the same evaluated tree and state inputs.

A lower-trust state MUST NOT be promoted to `accepted` by suppression, evidence presence, elapsed time, successful rendering alone or a previously green workflow run.

## 9. Drift classes

The lifecycle MUST distinguish at least the following drift classes:

1. `contract_drift`;
2. `partition_contract_drift`;
3. `source_drift`;
4. `configuration_drift`;
5. `renderer_identifier_drift`;
6. `renderer_interface_drift`;
7. `renderer_semantic_drift`;
8. `target_drift`;
9. `preserved_region_drift`;
10. `partition_boundary_drift`;
11. `target_semantics_drift`;
12. `gate_set_drift`;
13. `acceptance_state_missing`;
14. `acceptance_state_invalid`;
15. `acceptance_state_tamper_or_scope_mismatch`;
16. `base_or_ref_drift`;
17. `nondeterministic_renderer_output`;
18. `renderer_side_effect_or_capability_violation`;
19. `renderer_operational_abort`;
20. `renderer_failure_diagnostic`;
21. `write_verification_failure`;
22. `evidence_recording_failure`.

Concrete identifiers and mapping to existing main-repository findings remain `NEEDS_MAIN_REPO_VALIDATION`.

Independent dimensions MUST remain independently visible. A single generic `stale` message MUST NOT erase which comparisons failed.

## 10. Finding contract

Each projection freshness finding MUST be structured and bounded.

It MUST include:

- abstract drift class;
- target identity;
- lifecycle phase;
- expected identity or fingerprint when safe and useful;
- observed identity or fingerprint when safe and useful;
- whether mutation occurred;
- current trust state;
- applicable contract or gate-set identity;
- remediation category;
- evidence reference when bounded evidence exists.

Findings MUST NOT include secrets, unbounded file content or fabricated expected values.

Multiple independent failures MUST remain separately reportable even when one gate outcome blocks the operation.

Severity and user-facing wording are implementation mappings owned by the existing main-repository finding system and remain subject to exact-ref validation.

## 11. Gate outcomes

Projection gates produce one of these abstract outcomes:

- `pass` — every required check for the requested operation passed;
- `warn` — only explicitly non-blocking findings exist under the active staged policy;
- `block` — the requested operation MUST NOT proceed or integrate;
- `error` — the gate could not evaluate reliably because required machinery or inputs failed.

`error` MUST fail closed for mutation, acceptance, integration and strict validation.

A `warn` outcome MUST NOT authorize a target to become `accepted` when a mandatory acceptance check failed.

Gate outcome and target trust state are related but distinct. A read-only audit may complete with `block` while preserving the prior target bytes and prior recorded state.

## 12. Mandatory blocking conditions

The following MUST block mutation acceptance and integration regardless of staged rollout mode:

- malformed or ambiguous target or partition contract;
- missing required declared source;
- unknown renderer identifier;
- renderer interface incompatibility;
- renderer semantic-version mismatch against an immutable execution plan;
- stale plan after lock or preflight revalidation;
- partition-boundary invalidity;
- target identity mismatch;
- renderer nondeterminism detected during required verification;
- renderer side effect or prohibited capability use;
- operational abort represented as successful output;
- truncated or invalid output;
- post-Write verification failure;
- acceptance-state write failure after target Write;
- evidence or state represented as canonical source without an accepted authority contract.

A staged policy MAY control whether pre-existing noncompliance blocks unrelated read-only commands, but it MUST NOT weaken the safety conditions for new mutation or acceptance.

## 13. Staged enforcement

Adoption MUST be staged through the existing gate and lifecycle architecture.

At minimum the stages are:

1. **observe** — emit structured findings and evidence without changing mutation behavior not already protected by existing safety rules;
2. **warn** — surface projection-specific noncompliance prominently while preserving bounded compatibility;
3. **block-new** — block creation or acceptance of new nonconforming projection states while allowing explicitly governed legacy states to remain readable;
4. **strict** — block every in-scope nonconforming operation under the active gate policy.

Stage transitions MUST be explicit, reviewable, reversible and controlled by existing configuration or direction authority. They MUST NOT be activated by elapsed time alone.

Unknown findings MUST fail closed when they affect mutation safety, contract interpretation, target identity or acceptance. Treatment of unrelated unknown findings remains a main-repository policy decision.

No lab statement activates production strict mode.

## 14. Freshness checks by operation

### 14.1 Read-only audit

A read-only audit MUST evaluate all available dimensions and return structured findings without mutation.

### 14.2 Dry-run plan

Dry-run MUST resolve the current contract, sources, renderer identities, target state and required gates and MUST produce a plan that is fingerprint-bound to those inputs.

Dry-run success does not authorize later execution after drift.

### 14.3 Mutation execution

Before Write, execution MUST revalidate every plan-bound identity and fingerprint under the lifecycle lock. Any drift MUST abandon the attempt before Write.

### 14.4 Post-Write verification

After Write, the lifecycle MUST verify target bytes, partition preservation, target semantics, renderer output equivalence where required and every mandatory gate.

Only complete success permits acceptance-state recording and transition to `accepted`.

### 14.5 Integration or protected workflow

Integration MUST reject evidence or output produced from a stale base, source, target, contract, renderer, gate-set or acceptance-state context. DPA-600 owns cross-ref serialization mechanics.

## 15. Renderer-related findings

DPA-400 failure classes map into DPA-500 as follows:

- unknown or changed renderer identifier: block before rendering;
- incompatible interface version: block before rendering;
- changed semantic version: stale accepted state and invalidate stale plans;
- changed implementation evidence without semantic change: evidence update only, unless Probe or policy identifies an unversioned semantic change;
- nondeterministic output: `invalid` for acceptance and mandatory block;
- side effect or capability violation: `invalid`, attempt `abandoned`, mandatory block;
- deterministic semantic-bound violation: renderer failure, attempt `abandoned`, no acceptance;
- operational safety abort: attempt `abandoned`, structured finding, no semantic output and no acceptance;
- bounded failure diagnostic: lifecycle-translated finding only, never acceptance authority.

A raw repository commit change MUST NOT by itself create renderer semantic drift when the declared renderer semantic version and behavior contract remain unchanged; implementation evidence remains evidence-only.

## 16. Target and partition handling

For complete-target projections, target freshness compares the complete target fingerprint.

For registered-region projections, freshness MUST independently evaluate:

- renderer-owned payload fingerprint;
- preserved-region fingerprint;
- partition-contract fingerprint;
- partition-boundary validity;
- complete-target fingerprint where required for plan and acceptance integrity.

Manual or historical regions MUST NOT be regenerated merely to clear projection staleness.

Preserved-region drift MUST invalidate a stale execution plan but MUST NOT automatically classify the renderer-owned payload itself as semantically stale.

## 17. Recovery and interrupted operations

A target left `written-unverified` after interruption MUST NOT be treated as accepted.

Recovery MUST inspect:

- current target bytes;
- acceptance state;
- interrupted attempt state;
- plan identity where available;
- applicable contract and gate-set identities.

Recovery MAY verify and complete recording only when the exact written bytes and all required identities can be proven to match the governed plan and current contract. Otherwise it MUST preserve evidence, report findings and require regeneration or Maintainer-governed remediation.

Recovery MUST NOT reconstruct acceptance state from target bytes alone.

## 18. Evidence behavior

Gate evidence is non-authoritative and bounded.

Evidence SHOULD record:

- exact evaluated ref or tree identity;
- target identity;
- contract, renderer and gate-set identities;
- evaluated dimensions;
- findings and abstract outcomes;
- mutation and verification phases reached;
- prior and resulting trust states;
- limitations and unavailable checks.

Evidence failure after Write is a lifecycle failure. It MUST NOT erase the more important distinction between verified target bytes and recorded acceptance state, and it MUST NOT fabricate a successful evidence record.

Exact evidence ordering relative to acceptance-state persistence remains `NEEDS_MAIN_REPO_VALIDATION` and MUST preserve crash-safe semantics.

## 19. Main-repository validation boundary

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- concrete mapping to existing finding identifiers and severities;
- current gate-set representation and configuration authority;
- exact acceptance-state schema and Workspace path;
- current strict-adoption switches and defaults;
- command-specific gate integration;
- unknown-finding behavior outside mutation safety;
- evidence/state persistence ordering;
- CI job and required-check placement;
- compatibility behavior for existing registered non-projection documents;
- performance bounds for repository-wide freshness evaluation.

No claim in this document states that the current main repository already conforms.

## 20. Conformance tests

A conforming implementation MUST test:

1. fresh accepted complete-target projection;
2. fresh accepted registered-region projection;
3. missing acceptance state;
4. malformed acceptance state;
5. target-scope mismatch in acceptance state;
6. contract drift;
7. source drift;
8. configuration drift;
9. renderer identifier drift;
10. renderer interface incompatibility;
11. renderer semantic-version drift;
12. implementation-evidence-only change without semantic drift;
13. target-byte drift;
14. preserved-region drift;
15. partition-boundary drift;
16. target-semantics drift;
17. gate-set drift;
18. stale plan before lock;
19. stale plan after lock revalidation;
20. nondeterministic renderer output;
21. renderer side-effect detection;
22. semantic resource-bound failure;
23. operational abort without accepted output;
24. bounded failure diagnostic translation;
25. post-Write verification failure;
26. acceptance-state recording failure;
27. evidence recording failure;
28. interrupted `written-unverified` recovery;
29. observe, warn, block-new and strict stages;
30. no time-only staleness;
31. unknown mandatory input failing closed;
32. read-only audit producing findings without mutation.

Tests MUST prove that a successful renderer invocation alone cannot produce `accepted`.

## 21. Invalid states

The following are invalid:

1. freshness inferred from target existence alone;
2. missing acceptance state treated as fresh;
3. evidence treated as acceptance state;
4. target bytes used to reconstruct authority silently;
5. independent drift dimensions collapsed into an unstructured result;
6. stale plan executed after any bound input changed;
7. warning policy allowing mandatory acceptance failure to pass;
8. operational abort represented as renderer success;
9. nondeterministic output accepted;
10. side-effecting renderer accepted;
11. interface incompatibility ignored;
12. semantic-version drift ignored;
13. implementation commit SHA used as automatic semantic version;
14. partition drift repaired by renderer output;
15. manual or historical bytes regenerated to clear projection drift;
16. `written-unverified` represented as accepted;
17. acceptance-state recording failure hidden;
18. unknown mandatory input interpreted as pass;
19. strict mode activated by time alone;
20. a lab gate represented as main-repository runtime conformance.

## 22. Review-ready criteria

DPA-500 may become `review-ready` when:

1. freshness dimensions and drift classes are complete and consistent with DPA-300 and DPA-400;
2. finding, trust-state and gate semantics are unambiguous;
3. staged enforcement preserves fail-closed mutation safety;
4. acceptance-state and recovery behavior are complete;
5. every requirement is traced to invariants, tests, later implementation, evidence and rollback;
6. diagrams are synchronized;
7. repository-specific mappings remain exact-ref fenced;
8. primary review, technical verification, Maintainer adjudication and required post-adjudication verification are complete.

DPA-500 MUST NOT become `stable` before applicable freshness, finding, gate, recovery and strict-adoption Probes have evidence at an exact main-repository validation ref.
