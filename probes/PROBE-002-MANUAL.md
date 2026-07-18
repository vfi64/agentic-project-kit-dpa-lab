# PROBE-002 Manual — Lifecycle, Planning, Acceptance and Recovery

Status: draft

Status-date: 2026-07-18

Consumes: `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`

Fixture manifest: `probes/PROBE-002-FIXTURE-MANIFEST.md`

Governing architecture: DPA-300 §§7–17, DPA-500, ADR-016 and ADR-021

Execution-state: not run

## 1. Purpose

PROBE-002 measures the exact-ref main-repository lifecycle, planning, locking, writing, verification, acceptance, recovery, freshness, gate and re-acceptance capabilities relevant to the DPA.

It distinguishes:

- currently observed lifecycle capability;
- missing implementation;
- incompatible implementation;
- architecture behavior not yet implemented;
- unavailable or unsafe measurement;
- defective fixtures or expectations.

Preparation does not establish lifecycle conformance.

## 2. Hard boundary

This Probe is a measurement package, not an implementation request. Before execution it MUST NOT cause quick fixes to:

- handoff writers;
- lifecycle Apply behavior;
- mutation-plan execution semantics;
- acceptance-state persistence;
- recovery completion;
- gate-set re-acceptance;
- layered acceptance;
- projection freshness or gate integration.

Historical Discovery evidence may shape cases but does not establish current behavior.

## 3. Required execution preconditions

Before execution:

1. identify current remote `origin/main` and confirm the same exact local ref;
2. record clean worktree and environment identity;
3. inventory lifecycle entry points, target writers, lock paths, acceptance-state readers/writers, recovery paths, findings, gates and evidence emitters;
4. select an isolated disposable target and fixture workspace;
5. freeze exact main-repository, Lab manual and fixture refs;
6. record pre-state hashes for target, registry, acceptance state, lock/state paths and protected planning paths;
7. confirm interruption and recovery cases can be executed without risking production state;
8. define cleanup and rollback commands;
9. stop if a safe isolated path cannot be demonstrated.

## 4. Lifecycle sequence under test

Where supported, observations must be mapped to the ordered DPA-300 lifecycle:

1. Recover
2. Resolve
3. Inspect
4. Validate
5. Render
6. Plan
7. Preflight
8. Lock
9. Revalidate
10. Write
11. Verify
12. Record
13. Release

A current implementation need not already expose these names. The Probe records actual phases and maps them without inventing equivalence.

## 5. Case families

### P002-A — Resolution and validation

- P002-C001: clean isolated baseline and current manual lifecycle control.
- P002-C002: Workspace-resolved target and state paths.
- P002-C003: unresolved target or registry identity fails before render/write.
- P002-C004: ambiguous ownership fails before mutation.
- P002-C005: undeclared source or configuration fails before planning where support is claimed.

### P002-B — Immutable planning and drift

- P002-C006: dry-run plan creation does not mutate target or acceptance state.
- P002-C007: plan has deterministic identity and binds target, base, contract, renderer, sources, configuration, partition, ownership, acceptance-state context and expected output.
- P002-C008: execute action without exact matching plan is rejected.
- P002-C009: target drift after Plan and before Lock rejects the plan.
- P002-C010: source drift after Plan rejects the plan.
- P002-C011: contract drift after Plan rejects the plan.
- P002-C012: output-affecting configuration drift maps deterministically to contract drift and rejects the stale plan.
- P002-C013: renderer identifier, interface-version or semantic-version drift rejects the stale plan.
- P002-C014: partition, ownership or acceptance-state drift after Plan rejects the plan.
- P002-C015: implementation-evidence-only renderer change does not automatically become semantic drift.
- P002-C016: time-only change does not by itself create a hard stale-plan failure or activate strict enforcement.

### P002-C — Locking and under-lock revalidation

- P002-C017: current Workspace mutation lock excludes a competing mutation where applicable.
- P002-C018: same-process reentrancy behavior is observed and bounded.
- P002-C019: under-lock revalidation repeats every mutation-relevant comparison without a second render.
- P002-C020: failed lock acquisition leaves target and acceptance state unchanged.
- P002-C021: release occurs exactly once for the acquired instance and stale-lock recovery is explicit.

### P002-D — Write and Verify

- P002-C022: write reconstructs and atomically replaces the complete target through lifecycle ownership.
- P002-C023: region write preserves non-owned bytes and partition bytes.
- P002-C024: post-Write Verify checks payload, preserved region, partition, ownership, target semantics and complete-target fingerprints.
- P002-C025: failure before Write leaves target unchanged.
- P002-C026: failure after Write leaves bytes non-accepted and creates explicit recovery obligation.
- P002-C027: out-of-band lifecycle-byte mutation is detected rather than normalized silently.

### P002-E — Acceptance state and freshness inputs

- P002-C028: accepted state is written only after successful Verify and required gate `pass`.
- P002-C029: acceptance record binds exactly one target and all applicable contract, renderer, source, configuration, payload, complete-target, partition, preserved-region, ownership, target-semantics and gate-set identities.
- P002-C030: conditional accepted-base persistence occurs only for contract-declared base dependence.
- P002-C031: base-independent post-acceptance evaluation does not invent a missing base dependency.
- P002-C032: failed acceptance update preserves the prior accepted record or leaves an explicit recoverable non-accepted state.
- P002-C033: missing acceptance state yields `indeterminate` or `invalid` plus gate `failure`, never `fresh`.
- P002-C034: malformed, unknown-version or internally inconsistent acceptance state fails closed and is not repaired from target bytes or evidence.
- P002-C035: target-scope mismatch in acceptance state fails closed.
- P002-C036: missing mandatory evaluation input or machinery yields explicit `indeterminate` or `invalid` classification and gate `failure`.

### P002-F — Re-acceptance and layered acceptance

- P002-C037: gate-set-only re-acceptance of unchanged already-accepted bytes does not invoke renderer or mutate target.
- P002-C038: re-acceptance is rejected when target, source, configuration, contract, renderer, partition, ownership, target semantics, required base or acceptance-state context changed.
- P002-C039: gate `warning` or `failure` during re-acceptance leaves target bytes and prior acceptance record unchanged.
- P002-C040: successful re-acceptance updates only lifecycle-owned acceptance state and bounded evidence.
- P002-C041: registered-region projection uses layered acceptance while keeping payload, preserved-region, partition, ownership and complete-target guards distinct.
- P002-C042: authorized non-lifecycle-owner evolution of preserved bytes is not projection target drift and does not require regeneration or re-acceptance.
- P002-C043: ambiguous owner provenance prevents acceptance and fails closed.

### P002-G — Interruption and recovery

- P002-C044: interruption before Write leaves target unchanged and supports bounded retry.
- P002-C045: interruption after Write but before Verify creates recoverable `written-unverified` state.
- P002-C046: interruption after Verify but before Record does not imply acceptance without the authoritative record.
- P002-C047: interruption during Record or Release is detected and dispositioned before a new refresh.
- P002-C048: unresolved recovery blocks new mutation and integration conclusions.
- P002-C049: recovery may complete only when exact written bytes and all required identities match the governed plan and current contract, followed by full revalidation.
- P002-C050: recovery does not reconstruct acceptance state from target bytes alone.

### P002-H — Findings, evidence, gates and staged enforcement

- P002-C051: every independent rejection dimension remains separately visible in structured bounded findings.
- P002-C052: evidence does not authorize later mutation or substitute for acceptance state.
- P002-C053: evidence recording failure after Write or re-acceptance is an explicit lifecycle failure and does not fabricate success.
- P002-C054: read-only audit produces findings and gate decision without target or acceptance-state mutation.
- P002-C055: `pass`, `warning` and `failure` gate decisions remain distinct from freshness classification, drift class, consumer trust state and enforcement stage.
- P002-C056: observe, warn, block-new and strict enforcement stages preserve mandatory mutation and acceptance safety.
- P002-C057: unknown findings affecting mutation safety, contract interpretation, target identity, ownership or acceptance fail closed.
- P002-C058: additional writer, reader, lock, state, gate, evidence or recovery path is recorded without silent scope expansion.

## 6. Observation model

For each case record:

- actual entry point and symbols;
- ordered observed phases;
- pre-state and post-state hashes;
- plan identity and captured fingerprints;
- lock acquisition, owner, scope and release disposition;
- target mutation result;
- verification result;
- freshness classification;
- drift class and finding subreason;
- gate decision and enforcement stage;
- prior and resulting consumer trust state;
- acceptance-state delta;
- recovery-state delta;
- findings and bounded evidence;
- cleanup and rollback outcome;
- exact refs and fixture hashes.

Observation, interpretation and Maintainer adjudication remain separate records.

## 7. Outcome rules

- `NOT_RUN`: no local execution.
- `BLOCKED`: safe isolation, exact ref, required entry point, interruption harness or evidence path cannot be established.
- `FAIL`: unauthorized write, stale-plan execution, missing under-lock comparison, false acceptance, silent recovery completion, target loss, unexplained state mutation, prohibited evidence authority, collapsed independent failure dimensions or weakened mandatory safety occurs.
- `PARTIAL`: only a bounded subset can be measured or current implementation lacks required mechanisms without contradicting measured safety behavior.
- `PASS`: every mandatory case executes with complete evidence and observed behavior satisfies the tested DPA requirements.

A Probe-level `PASS` does not by itself promote a specification or authorize implementation.

## 8. Cleanup and rollback

Every mutating case requires:

- isolated disposable target;
- exact pre-state capture;
- declared restoration source;
- post-cleanup hash comparison;
- lock and temporary-state cleanup;
- preservation of evidence only in the declared evidence location.

Any unexplained residual target, registry, state, lock or planning-path change blocks reuse of the worktree.

## 9. Adjudication

Every discrepancy must be assigned exactly one primary class:

1. implementation conforms;
2. required implementation is missing;
3. implementation exists but differs;
4. DPA assumption is falsified or incomplete;
5. fixture or harness is defective;
6. another writer/reader/lock/state/gate/evidence/recovery path was discovered;
7. evidence is insufficient or blocked.

The record must identify whether architecture, implementation, fixture, evidence or rerun obligations change.

## 10. Review readiness

This manual is reviewable only when:

- every P002-C001 through P002-C058 case maps to a fixture;
- DPA-300, DPA-500, ADR-016 and ADR-021 anchors are synchronized;
- interruption cases are explicitly bounded and safe;
- freshness classification, drift class, trust state, gate decision and enforcement stage remain distinct;
- concrete main-repository mappings remain provisional;
- no implementation or execution claim is present;
- Lab gates pass.