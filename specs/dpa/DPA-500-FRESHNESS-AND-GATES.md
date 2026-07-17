# DPA-500 — Freshness and Gates

Status: draft
Status-date: 2026-07-17
Authority: normative DPA specification, subject to primary review, technical verification, Maintainer adjudication and applicable Probe evidence

## 1. Purpose

This specification defines freshness evaluation, structured findings, consumer-trust consequences and gate behavior for registered document projections.

DPA-500 extends the existing main-repository documentation registry, lifecycle, findings and gate architecture. It does not create a second freshness engine, a second finding taxonomy, a second gate runner, a second evidence store or a new runtime authority.

Repository-specific finding identifiers, severity mappings, command names, workflow integration points and strict-adoption switches remain `NEEDS_MAIN_REPO_VALIDATION` until validated against an exact main-repository ref.

## 2. Normative dependencies

DPA-500 depends on:

- DPA-000 for canonical invariants;
- DPA-100 for authority, classification, consumer trust-state, drift, freshness, fingerprint and gate vocabulary;
- DPA-200 for target identity, document form, partition ownership and target semantics;
- DPA-300 for registry contracts, lifecycle ordering, immutable plans, acceptance state, recovery and evidence boundaries;
- DPA-400 for renderer identity, immutable inputs, semantic versions, deterministic output, purity and failure behavior;
- DPA-ADR-013, DPA-ADR-014, DPA-ADR-016, DPA-ADR-017, DPA-ADR-019 and DPA-ADR-020.

## 3. Scope

DPA-500 owns:

1. projection freshness dimensions and classification;
2. freshness evaluation inputs;
3. projection-specific finding subreasons mapped to the DPA-100 drift vocabulary;
4. abstract finding semantics;
5. consumer trust-state consequences;
6. gate-decision semantics within the existing DPA-100 gate vocabulary;
7. strictness and staged enforcement rules;
8. handling of missing, stale, tampered or unverifiable acceptance state;
9. handling of renderer, source, contract, target and evidence failures;
10. recovery-facing gate behavior;
11. freshness and gate test obligations.

DPA-500 does not own:

- foundational vocabulary owned by DPA-100;
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

- assign freshness classification;
- emit authoritative findings;
- select severity;
- assign consumer trust state;
- decide gate pass, warning or failure;
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

## 6. Freshness classification

Freshness classification is distinct from consumer trust state, lifecycle attempt outcome, finding severity, gate decision and enforcement stage.

The projection-specific freshness classifications are:

- `fresh` — every applicable mandatory dimension matches and is verifiable;
- `stale` — one or more comparable current dimensions differ from the accepted state;
- `invalid` — the contract, target, partition, acceptance state or comparison boundary cannot be safely interpreted;
- `indeterminate` — mandatory current information or evaluation machinery is unavailable and neither `fresh`, `stale` nor `invalid` can be established safely.

These classifications do not extend the closed DPA-100 consumer trust-state vocabulary.

The same evaluated tree, lifecycle state and declared inputs MUST produce the same freshness classification and finding set.

## 7. Evaluation inputs

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

Missing mandatory input MUST classify the evaluation as `indeterminate` or `invalid` according to the failure type and MUST produce an explicit finding. It MUST NOT be interpreted as fresh or as permission to infer prior state.

## 8. Acceptance state

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

## 9. Consumer trust-state consequences

DPA-500 applies, and does not extend, the consumer trust-state vocabulary owned by DPA-100:

- `computed` remains bytes produced without an immutable mutation plan;
- `plan-captured` remains bytes owned by an immutable lifecycle plan and its guards;
- `written-unverified` remains written bytes whose required verification, evidence and gates are incomplete;
- `accepted` remains bytes accepted by the complete required gate set with acceptance state recorded;
- `abandoned` remains a refresh instance that ended through rejection, failure, invalidation or interruption and cannot later become accepted.

A freshness classification of `stale`, `invalid` or `indeterminate` does not itself create a new trust state. It produces findings and gate consequences while preserving the currently recorded trust state unless the lifecycle contract requires a transition for the active attempt.

Only complete post-Write verification, required gate `pass`, successful acceptance-state persistence and lifecycle completion may produce `accepted`.

No state may be promoted to `accepted` by suppression, evidence presence, elapsed time, successful rendering alone or a previously green workflow run.

## 10. Drift vocabulary and finding subreasons

DPA-500 MUST use the closed DPA-100 drift classes:

1. `base drift`;
2. `source drift`;
3. `target drift`;
4. `contract drift`;
5. `renderer drift`;
6. `partition drift`;
7. `ownership drift`.

Projection-specific findings MAY refine those classes with stable subreasons, including:

- projection-contract change or partition-contract change under `contract drift` or `partition drift` as applicable;
- declared-source fingerprint or output-affecting configuration change under `source drift` or `contract drift` according to the accepted contract model;
- renderer identifier, interface-version or semantic-version change under `renderer drift`;
- complete-target, payload or preserved-region byte mismatch under `target drift`;
- partition-contract, partition-byte or boundary mismatch under `partition drift`;
- declared byte-owner mapping change under `ownership drift`;
- repository base or required ref mismatch under `base drift`.

The following are finding causes or lifecycle failures, not new drift classes:

- missing, malformed, tampered or scope-mismatched acceptance state;
- gate-set mismatch;
- renderer nondeterminism;
- renderer side effect or prohibited capability use;
- renderer operational abort;
- bounded renderer failure diagnostic;
- post-Write verification failure;
- acceptance-state persistence failure;
- evidence recording failure;
- unavailable mandatory evaluation machinery.

Concrete identifiers and mapping to existing main-repository findings remain `NEEDS_MAIN_REPO_VALIDATION`.

Independent dimensions and subreasons MUST remain independently visible. A single generic stale message MUST NOT erase which comparisons or evaluations failed.

## 11. Finding contract

Each projection freshness finding MUST be structured and bounded.

It MUST include:

- DPA-100 drift class when the finding represents drift, otherwise an explicit non-drift category;
- projection-specific subreason;
- target identity;
- lifecycle phase;
- freshness classification;
- expected identity or fingerprint when safe and useful;
- observed identity or fingerprint when safe and useful;
- whether mutation occurred;
- current consumer trust state;
- applicable contract or gate-set identity;
- remediation category;
- evidence reference when bounded evidence exists.

Findings MUST NOT include secrets, unbounded file content or fabricated expected values.

Multiple independent failures MUST remain separately reportable even when one gate decision blocks the operation.

Severity and user-facing wording are implementation mappings owned by the existing main-repository finding system and remain subject to exact-ref validation.

## 12. Gate decisions

DPA-500 uses the DPA-100 gate vocabulary:

- `pass` — every required check for the requested operation passed;
- `warning` — only explicitly non-blocking findings exist under the active staged policy;
- `failure` — the requested operation MUST NOT proceed, integrate or become accepted.

Evaluation machinery failure or unavailable mandatory input MUST yield a `failure` decision for mutation, acceptance, integration and strict validation. The finding MUST preserve whether the underlying freshness classification was `indeterminate` or `invalid`.

A `warning` decision MUST NOT authorize a target to become `accepted` when any mandatory acceptance check failed.

Gate decision, freshness classification and consumer trust state are related but distinct. A read-only audit may return `failure` while preserving prior target bytes and recorded lifecycle state.

## 13. Mandatory failure conditions

The following MUST produce gate `failure` for mutation, acceptance and integration regardless of staged rollout mode:

- malformed or ambiguous target or partition contract;
- missing required declared source;
- unknown renderer identifier;
- renderer interface incompatibility;
- renderer semantic-version mismatch against an immutable execution plan;
- stale plan after lock or preflight revalidation;
- partition invalidity;
- target identity mismatch;
- renderer nondeterminism detected during required verification;
- renderer side effect or prohibited capability use;
- operational abort represented as successful output;
- truncated or invalid output;
- post-Write verification failure;
- acceptance-state write failure after target Write;
- evidence or lifecycle state represented as canonical source without an accepted authority contract;
- unavailable mandatory evaluation machinery.

A staged policy MAY control whether pre-existing noncompliance blocks unrelated read-only commands, but it MUST NOT weaken the safety conditions for new mutation or acceptance.

## 14. Staged enforcement

Adoption MUST be staged through the existing gate and lifecycle architecture.

At minimum the enforcement stages are:

1. **observe** — emit structured findings and evidence without changing mutation behavior not already protected by existing safety rules;
2. **warn** — surface projection-specific noncompliance prominently while preserving bounded compatibility;
3. **block-new** — prevent creation or acceptance of new nonconforming projection states while allowing explicitly governed legacy states to remain readable;
4. **strict** — fail every in-scope nonconforming operation under the active gate policy.

The stage name `warn` is an enforcement-stage token and MUST NOT be used as a gate-decision token; the gate decision remains `warning`.

Stage transitions MUST be explicit, reviewable, reversible and controlled by existing configuration or Direction authority. They MUST NOT be activated by elapsed time alone.

Unknown findings MUST fail closed when they affect mutation safety, contract interpretation, target identity or acceptance. Treatment of unrelated unknown findings remains a main-repository policy decision.

No lab statement activates production strict mode.

## 15. Freshness checks by operation

### 15.1 Read-only audit

A read-only audit MUST evaluate all available dimensions and return structured findings without mutation.

### 15.2 Dry-run plan

Dry-run MUST resolve the current contract, sources, renderer identities, target state and required gates and MUST produce a plan that is fingerprint-bound to those inputs.

Dry-run success does not authorize later execution after drift.

### 15.3 Mutation execution

Before Write, execution MUST revalidate every plan-bound identity and fingerprint under the lifecycle lock. Any mismatch or mandatory evaluation failure MUST abandon the attempt before Write.

### 15.4 Post-Write verification

After Write, the lifecycle MUST verify target bytes, partition preservation, target semantics, renderer output equivalence where required and every mandatory gate.

Only complete success permits acceptance-state recording and transition to `accepted`.

### 15.5 Integration or protected workflow

Integration MUST reject evidence or output produced from a mismatched or unverifiable base, source, target, contract, renderer, gate-set or acceptance-state context. DPA-600 owns cross-ref serialization mechanics.

## 16. Renderer-related findings

DPA-400 failure classes map into DPA-500 as follows:

- unknown or changed renderer identifier: `renderer drift` where comparable, otherwise a non-drift contract-resolution failure; gate `failure` before rendering;
- incompatible interface version: `renderer drift`; gate `failure` before rendering;
- changed semantic version: `renderer drift`, freshness `stale`, stale plans invalidated;
- changed implementation evidence without semantic change: evidence update only, unless Probe or policy identifies an unversioned semantic change;
- nondeterministic output: freshness `invalid`, attempt `abandoned`, gate `failure`;
- side effect or capability violation: freshness `invalid`, attempt `abandoned`, gate `failure`;
- deterministic semantic-bound violation: renderer failure, attempt `abandoned`, no acceptance;
- operational safety abort: attempt `abandoned`, structured non-drift finding, no semantic output and no acceptance;
- bounded failure diagnostic: lifecycle-translated finding only, never acceptance authority.

A raw repository commit change MUST NOT by itself create renderer semantic drift when the declared renderer semantic version and behavior contract remain unchanged; implementation evidence remains evidence-only.

## 17. Target and partition handling

For complete-target projections, target freshness compares the complete target fingerprint.

For registered-region projections, freshness MUST independently evaluate:

- renderer-owned payload fingerprint;
- preserved-region fingerprint;
- partition-contract fingerprint;
- partition-boundary validity;
- complete-target fingerprint where required for plan and acceptance integrity.

Manual or historical regions MUST NOT be regenerated merely to clear projection staleness.

Preserved-region target drift MUST invalidate a stale execution plan but MUST NOT automatically classify the renderer-owned payload itself as semantically stale.

## 18. Recovery and interrupted operations

A target left `written-unverified` after interruption MUST NOT be treated as accepted.

Recovery MUST inspect:

- current target bytes;
- acceptance state;
- interrupted attempt state;
- plan identity where available;
- applicable contract and gate-set identities.

Recovery MAY verify and complete recording only when the exact written bytes and all required identities can be proven to match the governed plan and current contract. Otherwise it MUST preserve evidence, report findings and require regeneration or Maintainer-governed remediation.

Recovery MUST NOT reconstruct acceptance state from target bytes alone.

## 19. Evidence behavior

Gate evidence is non-authoritative and bounded.

Evidence SHOULD record:

- exact evaluated ref or tree identity;
- target identity;
- contract, renderer and gate-set identities;
- evaluated dimensions;
- freshness classification;
- DPA-100 drift classes and finding subreasons;
- gate decision and enforcement stage;
- mutation and verification phases reached;
- prior and resulting consumer trust states;
- limitations and unavailable checks.

Evidence failure after Write is a lifecycle failure. It MUST NOT erase the distinction between verified target bytes and recorded acceptance state, and it MUST NOT fabricate a successful evidence record.

Exact evidence ordering relative to acceptance-state persistence remains `NEEDS_MAIN_REPO_VALIDATION` and MUST preserve crash-safe semantics.

## 20. Main-repository validation boundary

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

## 21. Conformance tests

A conforming implementation MUST test:

1. fresh accepted complete-target projection;
2. fresh accepted registered-region projection;
3. missing acceptance state producing `indeterminate` or `invalid` and gate `failure`;
4. malformed acceptance state;
5. target-scope mismatch in acceptance state;
6. contract drift;
7. source drift;
8. configuration-related contract or source drift according to its declared ownership;
9. renderer identifier drift;
10. renderer interface incompatibility;
11. renderer semantic-version drift;
12. implementation-evidence-only change without semantic drift;
13. target-byte drift;
14. preserved-region target drift;
15. partition drift;
16. target-semantics-related contract or partition drift;
17. gate-set mismatch as a non-drift finding cause;
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
29. observe, warn, block-new and strict enforcement stages;
30. pass, warning and failure gate decisions;
31. no time-only staleness;
32. unavailable mandatory input failing closed;
33. read-only audit producing findings without mutation;
34. separation of freshness classification, drift class, trust state, gate decision and enforcement stage.

Tests MUST prove that a successful renderer invocation alone cannot produce `accepted`.

## 22. Invalid states

The following are invalid:

1. freshness inferred from target existence alone;
2. missing acceptance state treated as fresh;
3. evidence treated as acceptance state;
4. target bytes used to reconstruct authority silently;
5. independent drift dimensions collapsed into an unstructured result;
6. finding causes represented as new DPA-100 drift classes;
7. freshness classifications represented as consumer trust states;
8. enforcement stages represented as gate decisions;
9. stale plan executed after any bound input changed;
10. warning policy allowing mandatory acceptance failure to pass;
11. operational abort represented as renderer success;
12. nondeterministic output accepted;
13. side-effecting renderer accepted;
14. interface incompatibility ignored;
15. semantic-version drift ignored;
16. implementation commit SHA used as automatic semantic version;
17. partition drift repaired by renderer output;
18. manual or historical bytes regenerated to clear projection drift;
19. `written-unverified` represented as accepted;
20. acceptance-state recording failure hidden;
21. unavailable mandatory input interpreted as pass;
22. strict mode activated by time alone;
23. a lab gate represented as main-repository runtime conformance.

## 23. Review-ready criteria

DPA-500 may become `review-ready` when:

1. freshness dimensions and classifications are complete and consistent with DPA-100 through DPA-400;
2. DPA-100 drift classes and DPA-500 finding subreasons are cleanly separated;
3. finding, consumer trust-state and gate semantics are unambiguous;
4. staged enforcement preserves fail-closed mutation safety;
5. acceptance-state and recovery behavior are complete;
6. every requirement is traced to invariants, tests, later implementation, evidence and rollback;
7. diagrams are synchronized;
8. repository-specific mappings remain exact-ref fenced;
9. primary review, technical verification, Maintainer adjudication and required post-adjudication verification are complete.

DPA-500 MUST NOT become `stable` before applicable freshness, finding, gate, recovery and strict-adoption Probes have evidence at an exact main-repository validation ref.
