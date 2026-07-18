# PROBE-002 Manual — Lifecycle, Planning, Acceptance and Recovery

Status: draft

Status-date: 2026-07-18

Consumes: `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`

Fixture manifest: `probes/PROBE-002-FIXTURE-MANIFEST.md`

Governing architecture: DPA-300 §§7–17, DPA-500, ADR-016 and ADR-021

Execution-state: not run

## 1. Purpose

PROBE-002 measures the exact-ref main-repository lifecycle, planning, locking, writing, verification, acceptance, recovery and re-acceptance capabilities relevant to the DPA.

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
3. inventory lifecycle entry points, target writers, lock paths, acceptance-state readers/writers, recovery paths, findings and evidence emitters;
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

### P002-B — Immutable planning

- P002-C006: dry-run plan creation does not mutate target or acceptance state.
- P002-C007: plan has deterministic identity and binds target, base, contract, renderer, sources, configuration and expected output.
- P002-C008: execute action without exact matching plan is rejected.
- P002-C009: target drift after Plan and before Lock rejects the plan.
- P002-C010: source or contract drift after Plan rejects the plan.
- P002-C011: renderer, partition, ownership or acceptance-state drift after Plan rejects the plan.
- P002-C012: time-only change does not by itself create a hard stale-plan failure.

### P002-C — Locking and under-lock revalidation

- P002-C013: current Workspace mutation lock excludes a competing mutation where applicable.
- P002-C014: same-process reentrancy behavior is observed and bounded.
- P002-C015: under-lock revalidation repeats every mutation-relevant comparison without a second render.
- P002-C016: failed lock acquisition leaves target and acceptance state unchanged.
- P002-C017: release occurs exactly once for the acquired instance and stale lock recovery is explicit.

### P002-D — Write and Verify

- P002-C018: write reconstructs and atomically replaces the complete target through lifecycle ownership.
- P002-C019: region write preserves non-owned bytes and partition bytes.
- P002-C020: post-Write Verify checks payload, preserved region, partition and complete-target fingerprints.
- P002-C021: failure before Write leaves target unchanged.
- P002-C022: failure after Write leaves bytes non-accepted and creates explicit recovery obligation.
- P002-C023: out-of-band lifecycle-byte mutation is detected rather than normalized silently.

### P002-E — Acceptance state

- P002-C024: accepted state is written only after successful Verify and required gates.
- P002-C025: acceptance record binds target, relevant fingerprints, gate set and exact context.
- P002-C026: conditional accepted-base persistence is recorded only when required by the governed target form.
- P002-C027: base-independent post-acceptance evaluation does not invent a missing base dependency.
- P002-C028: failed acceptance update preserves the prior accepted record and marks current bytes non-accepted.

### P002-F — Re-acceptance and layered acceptance

- P002-C029: gate-set-only re-acceptance of unchanged already-accepted bytes does not invoke renderer or mutate target.
- P002-C030: re-acceptance is rejected when target, source, contract, renderer, partition or ownership context changed.
- P002-C031: registered-region projection uses layered acceptance for payload, preserved region, partition and complete target.
- P002-C032: authorized non-lifecycle-owner evolution of preserved bytes is distinguished from lifecycle-owned drift.
- P002-C033: ambiguous owner provenance prevents acceptance.

### P002-G — Interruption and recovery

- P002-C034: interruption before Write leaves target unchanged and supports bounded retry.
- P002-C035: interruption after Write but before Verify creates recoverable non-accepted state.
- P002-C036: interruption after Verify but before Record does not imply acceptance without the authoritative record.
- P002-C037: interruption during Record or Release is detected and dispositioned before a new refresh.
- P002-C038: unresolved recovery blocks new mutation and integration conclusions.
- P002-C039: recovery completion is followed by full revalidation before continuation.

### P002-H — Findings, evidence and negative paths

- P002-C040: every rejection has bounded finding/evidence without unrelated repository leakage.
- P002-C041: evidence does not authorize later mutation or substitute for acceptance state.
- P002-C042: unknown or unavailable mandatory state fails loud.
- P002-C043: additional writer, reader, lock, state or recovery path is recorded without silent scope expansion.

## 6. Observation model

For each case record:

- actual entry point and symbols;
- ordered observed phases;
- pre-state and post-state hashes;
- plan identity and captured fingerprints;
- lock acquisition, owner, scope and release disposition;
- target mutation result;
- verification result;
- acceptance-state delta;
- recovery-state delta;
- findings and bounded evidence;
- cleanup and rollback outcome;
- exact refs and fixture hashes.

Observation, interpretation and Maintainer adjudication remain separate records.

## 7. Outcome rules

- `NOT_RUN`: no local execution.
- `BLOCKED`: safe isolation, exact ref, required entry point, interruption harness or evidence path cannot be established.
- `FAIL`: unauthorized write, stale-plan execution, missing under-lock comparison, false acceptance, silent recovery completion, target loss, unexplained state mutation or prohibited evidence authority occurs.
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
6. another writer/reader/lock/state/recovery path was discovered;
7. evidence is insufficient or blocked.

The record must identify whether architecture, implementation, fixture, evidence or rerun obligations change.

## 10. Review readiness

This manual is reviewable only when:

- every P002-C001 through P002-C043 case maps to a fixture;
- DPA-300, DPA-500, ADR-016 and ADR-021 anchors are synchronized;
- interruption cases are explicitly bounded and safe;
- concrete main-repository mappings remain provisional;
- no implementation or execution claim is present;
- Lab gates pass.