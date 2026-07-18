# PROBE-002 Fixture Manifest

Status: draft

Status-date: 2026-07-18

Manual: `probes/PROBE-002-MANUAL.md`

Execution-state: not run

## 1. Fixture principles

- Fixtures describe semantic states and transitions before concrete main-repository serialization is selected.
- Each case has one stable fixture identifier and revision.
- Mutating fixtures MUST use an isolated disposable target and restoration source.
- Interruption fixtures MUST identify the exact interruption boundary and expected recoverable state.
- Negative fixtures differ from a valid parent by one declared mutation or interruption.
- Every materialized input, pre-state and expected restoration source requires a content hash.
- Actual file names, command paths, state schemas and lock paths remain `NEEDS_MAIN_REPO_VALIDATION`.

## 2. Baseline fixture families

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-BASELINE-CLEAN | Clean isolated lifecycle control | P002-C001 |
| F002-WORKSPACE-VALID | Workspace-resolved registry, target, state and evidence locations | P002-C002 |
| F002-TARGET-UNRESOLVED | Missing or ambiguous target/registry identity | P002-C003 |
| F002-OWNERSHIP-AMBIGUOUS | Conflicting or incomplete owner provenance | P002-C004, P002-C033 |
| F002-INPUT-UNDECLARED | Undeclared source or output-affecting configuration | P002-C005 |

## 3. Planning and drift fixtures

| Fixture ID | Parent | Mutation or state | Cases |
|---|---|---|---|
| F002-PLAN-DRY-RUN | F002-BASELINE-CLEAN | Create plan only | P002-C006 |
| F002-PLAN-DETERMINISTIC | F002-PLAN-DRY-RUN | Repeat identical planning inputs | P002-C007 |
| F002-EXECUTE-NO-PLAN | F002-BASELINE-CLEAN | Execute without exact plan identity | P002-C008 |
| F002-DRIFT-TARGET | F002-PLAN-DRY-RUN | Change target after Plan | P002-C009 |
| F002-DRIFT-SOURCE | F002-PLAN-DRY-RUN | Change one declared source | P002-C010 |
| F002-DRIFT-CONTRACT | F002-PLAN-DRY-RUN | Change one contract field | P002-C010 |
| F002-DRIFT-RENDERER | F002-PLAN-DRY-RUN | Change renderer identity/version evidence | P002-C011 |
| F002-DRIFT-PARTITION | F002-PLAN-DRY-RUN | Change partition fingerprint | P002-C011 |
| F002-DRIFT-OWNERSHIP | F002-PLAN-DRY-RUN | Change ownership fingerprint | P002-C011 |
| F002-DRIFT-ACCEPTANCE | F002-PLAN-DRY-RUN | Change acceptance-state context | P002-C011 |
| F002-TIME-ONLY | F002-PLAN-DRY-RUN | Change timestamp/evidence time only | P002-C012 |

## 4. Lock and revalidation fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-LOCK-COMPETITOR | Competing mutation attempts same governed scope | P002-C013 |
| F002-LOCK-REENTRANT | Same-process nested acquisition attempt | P002-C014 |
| F002-UNDER-LOCK-DRIFT | One mutation-relevant fingerprint changes before Revalidate | P002-C015 |
| F002-LOCK-UNAVAILABLE | Existing lock cannot be acquired | P002-C016 |
| F002-LOCK-STALE | Stale or interrupted lock owner evidence | P002-C017 |

## 5. Write and verification fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-WRITE-FULL | Complete-target atomic replacement | P002-C018 |
| F002-WRITE-REGION | Region payload with preserved and partition bytes | P002-C019, P002-C020 |
| F002-FAIL-PRE-WRITE | Inject failure before Write | P002-C021 |
| F002-FAIL-POST-WRITE | Inject failure after Write and before successful completion | P002-C022 |
| F002-OUT-OF-BAND-BYTES | Mutate lifecycle-owned bytes outside lifecycle | P002-C023 |

## 6. Acceptance fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-ACCEPT-SUCCESS | Verified output with required gates satisfied | P002-C024, P002-C025 |
| F002-ACCEPT-CONDITIONAL-BASE | Target requiring accepted-base persistence | P002-C026 |
| F002-ACCEPT-BASE-INDEPENDENT | Target not requiring accepted base | P002-C027 |
| F002-ACCEPT-RECORD-FAIL | Failure while persisting current acceptance result | P002-C028 |

## 7. Re-acceptance and layered acceptance fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-REACCEPT-GATESET-ONLY | Unchanged accepted bytes; gate set changed | P002-C029 |
| F002-REACCEPT-CONTEXT-DRIFT | One semantic or ownership fingerprint changed | P002-C030 |
| F002-LAYERED-REGION | Payload, preserved, partition and complete-target layers | P002-C031 |
| F002-PRESERVED-AUTHORIZED-EVOLUTION | Non-lifecycle owner changes preserved bytes within authority | P002-C032 |
| F002-PROVENANCE-AMBIGUOUS | Preserved-byte owner provenance unavailable | P002-C033 |

## 8. Interruption and recovery fixtures

| Fixture ID | Interruption boundary | Cases |
|---|---|---|
| F002-INTERRUPT-PRE-WRITE | After plan/revalidation, before Write | P002-C034 |
| F002-INTERRUPT-POST-WRITE | After Write, before Verify | P002-C035 |
| F002-INTERRUPT-POST-VERIFY | After Verify, before Record | P002-C036 |
| F002-INTERRUPT-RECORD | During Record | P002-C037 |
| F002-INTERRUPT-RELEASE | During or before Release completion | P002-C037 |
| F002-RECOVERY-UNRESOLVED | Recovery evidence cannot be dispositioned | P002-C038 |
| F002-RECOVERY-COMPLETE | Recover then force full revalidation | P002-C039 |

## 9. Findings and evidence fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-BOUNDED-DIAGNOSTIC | Trigger known rejection with bounded context | P002-C040 |
| F002-EVIDENCE-NONAUTHORITY | Attempt later action using evidence only | P002-C041 |
| F002-MANDATORY-STATE-UNKNOWN | Required lock/state/fingerprint unavailable | P002-C042 |
| F002-ADDITIONAL-PATH | Placeholder for newly discovered writer/reader/path | P002-C043 |

## 10. Required materialized metadata

Every executable fixture or state package MUST record:

- fixture ID and revision;
- governing case and normative anchors;
- exact main-repository and Lab refs;
- isolated workspace identity;
- target, registry, state, lock and evidence paths;
- pre-state hashes;
- declared mutation or interruption boundary;
- expected allowed and forbidden state changes;
- restoration source and hash;
- cleanup verification method;
- last normative synchronization ref.

## 11. Materialization gate

Executable fixtures MUST NOT be created until:

1. current lifecycle, writer, lock, acceptance-state and recovery paths are inventoried at an exact remote ref;
2. the same paths are locally confirmed;
3. an isolated disposable target and safe interruption method are demonstrated;
4. the actual state and plan representations are recorded without treating them as normative DPA forms;
5. cleanup restores all governed paths and is itself testable;
6. the manifest is updated with concrete paths, commands and hashes.

## 12. Completeness check

Before review:

- every P002-C001 through P002-C043 case maps to at least one fixture;
- every mutating fixture has pre-state, restoration and cleanup obligations;
- every interruption fixture has one exact boundary and expected trust state;
- target, source, contract, renderer, partition, ownership, gate-set and acceptance-state drift are distinct;
- gate-set-only re-acceptance prohibits renderer invocation and target mutation;
- layered region acceptance keeps payload, preserved, partition and complete-target evidence distinct;
- no fixture selects or changes production implementation;
- all concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.