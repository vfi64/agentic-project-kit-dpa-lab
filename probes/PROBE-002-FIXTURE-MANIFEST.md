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

## 2. Resolution and validation

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-BASELINE-CLEAN | Clean isolated lifecycle control | P002-C001 |
| F002-WORKSPACE-VALID | Workspace-resolved registry, target, state and evidence locations | P002-C002 |
| F002-TARGET-UNRESOLVED | Missing or ambiguous target/registry identity | P002-C003 |
| F002-OWNERSHIP-AMBIGUOUS | Conflicting or incomplete owner provenance | P002-C004, P002-C043 |
| F002-INPUT-UNDECLARED | Undeclared source or output-affecting configuration | P002-C005 |

## 3. Planning and drift

| Fixture ID | Parent | Mutation or state | Cases |
|---|---|---|---|
| F002-PLAN-DRY-RUN | F002-BASELINE-CLEAN | Create plan only | P002-C006 |
| F002-PLAN-DETERMINISTIC | F002-PLAN-DRY-RUN | Repeat identical planning inputs | P002-C007 |
| F002-EXECUTE-NO-PLAN | F002-BASELINE-CLEAN | Execute without exact plan identity | P002-C008 |
| F002-DRIFT-TARGET | F002-PLAN-DRY-RUN | Change target after Plan | P002-C009 |
| F002-DRIFT-SOURCE | F002-PLAN-DRY-RUN | Change one declared source | P002-C010 |
| F002-DRIFT-CONTRACT | F002-PLAN-DRY-RUN | Change one contract field | P002-C011 |
| F002-DRIFT-CONFIG | F002-PLAN-DRY-RUN | Change output-affecting configuration | P002-C012 |
| F002-DRIFT-RENDERER-ID | F002-PLAN-DRY-RUN | Change renderer identifier | P002-C013 |
| F002-DRIFT-RENDERER-INTERFACE | F002-PLAN-DRY-RUN | Change interface version | P002-C013 |
| F002-DRIFT-RENDERER-SEMANTIC | F002-PLAN-DRY-RUN | Change semantic version | P002-C013 |
| F002-DRIFT-PARTITION | F002-PLAN-DRY-RUN | Change partition fingerprint | P002-C014 |
| F002-DRIFT-OWNERSHIP | F002-PLAN-DRY-RUN | Change ownership fingerprint | P002-C014 |
| F002-DRIFT-ACCEPTANCE | F002-PLAN-DRY-RUN | Change acceptance-state context | P002-C014 |
| F002-RENDERER-EVIDENCE-ONLY | F002-PLAN-DRY-RUN | Change implementation evidence without semantic version | P002-C015 |
| F002-TIME-ONLY | F002-PLAN-DRY-RUN | Change timestamp/evidence time only | P002-C016 |

## 4. Lock, write and verify

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-LOCK-COMPETITOR | Competing mutation attempts in same scope | P002-C017 |
| F002-LOCK-REENTRANT | Same-process nested acquisition | P002-C018 |
| F002-UNDER-LOCK-DRIFT | One bound fingerprint changes before Revalidate | P002-C019 |
| F002-LOCK-UNAVAILABLE | Existing lock cannot be acquired | P002-C020 |
| F002-LOCK-STALE | Stale or interrupted lock owner evidence | P002-C021 |
| F002-WRITE-FULL | Complete-target atomic replacement | P002-C022 |
| F002-WRITE-REGION | Region payload with preserved and partition bytes | P002-C023, P002-C024 |
| F002-FAIL-PRE-WRITE | Inject failure before Write | P002-C025 |
| F002-FAIL-POST-WRITE | Inject failure after Write | P002-C026 |
| F002-OUT-OF-BAND-BYTES | Mutate lifecycle-owned bytes outside lifecycle | P002-C027 |

## 5. Acceptance and freshness

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-ACCEPT-SUCCESS | Verified output with required gates satisfied | P002-C028, P002-C029 |
| F002-ACCEPT-CONDITIONAL-BASE | Contract-declared base dependence | P002-C030 |
| F002-ACCEPT-BASE-INDEPENDENT | No accepted base dependency | P002-C031 |
| F002-ACCEPT-RECORD-FAIL | Acceptance persistence failure | P002-C032 |
| F002-ACCEPT-MISSING | Acceptance state absent | P002-C033 |
| F002-ACCEPT-MALFORMED | Unknown schema, parse failure or inconsistent fingerprints | P002-C034 |
| F002-ACCEPT-SCOPE-MISMATCH | Acceptance state names another target | P002-C035 |
| F002-EVALUATION-UNAVAILABLE | Mandatory input or machinery unavailable | P002-C036 |

## 6. Re-acceptance and layered acceptance

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-REACCEPT-GATESET-PASS | Unchanged accepted bytes; new gate set passes | P002-C037, P002-C040 |
| F002-REACCEPT-CONTEXT-DRIFT | One non-gate semantic dimension changed | P002-C038 |
| F002-REACCEPT-WARNING | New gate set returns warning | P002-C039 |
| F002-REACCEPT-FAILURE | New gate set returns failure | P002-C039 |
| F002-LAYERED-REGION | Distinct payload, preserved, partition, ownership and complete-target guards | P002-C041 |
| F002-PRESERVED-AUTHORIZED-EVOLUTION | Declared non-lifecycle owner changes preserved bytes | P002-C042 |
| F002-PROVENANCE-AMBIGUOUS | Responsible owner cannot be proven | P002-C043 |

## 7. Interruption and recovery

| Fixture ID | Interruption boundary | Cases |
|---|---|---|
| F002-INTERRUPT-PRE-WRITE | Before Write | P002-C044 |
| F002-INTERRUPT-POST-WRITE | After Write, before Verify | P002-C045 |
| F002-INTERRUPT-POST-VERIFY | After Verify, before Record | P002-C046 |
| F002-INTERRUPT-RECORD | During Record | P002-C047 |
| F002-INTERRUPT-RELEASE | During Release | P002-C047 |
| F002-RECOVERY-UNRESOLVED | Required identity cannot be proven | P002-C048 |
| F002-RECOVERY-EXACT-MATCH | Written bytes and all identities match plan and contract | P002-C049 |
| F002-RECOVERY-BYTES-ONLY | Target bytes exist but authoritative state is absent | P002-C050 |

## 8. Findings, evidence and enforcement

| Fixture ID | Purpose | Cases |
|---|---|---|
| F002-MULTI-DIMENSION-FAILURE | Trigger two independent failures | P002-C051 |
| F002-EVIDENCE-NONAUTHORITY | Attempt later action using evidence only | P002-C052 |
| F002-EVIDENCE-FAIL-POST-WRITE | Evidence persistence fails after Write | P002-C053 |
| F002-EVIDENCE-FAIL-REACCEPT | Evidence persistence fails during re-acceptance | P002-C053 |
| F002-AUDIT-READ-ONLY | Evaluate accepted target without mutation | P002-C054 |
| F002-VOCABULARY-SEPARATION | Exercise classification, drift, trust, gate and stage fields | P002-C055 |
| F002-STAGE-OBSERVE | Observe policy | P002-C056 |
| F002-STAGE-WARN | Warn policy | P002-C056 |
| F002-STAGE-BLOCK-NEW | Block-new policy | P002-C056 |
| F002-STAGE-STRICT | Strict policy | P002-C056 |
| F002-UNKNOWN-SAFETY-FINDING | Unknown finding affects safety or authority | P002-C057 |
| F002-ADDITIONAL-PATH | Newly discovered writer/reader/gate/evidence path | P002-C058 |

## 9. Required materialized metadata

Every executable fixture or state package MUST record fixture ID and revision, governing case and normative anchors, exact main-repository and Lab refs, isolated workspace identity, governed paths, pre-state hashes, declared mutation or interruption boundary, expected allowed and forbidden changes, restoration source and hash, cleanup verification method and last normative synchronization ref.

## 10. Materialization gate

Executable fixtures MUST NOT be created until current lifecycle, writer, lock, acceptance-state, gate, evidence and recovery paths are inventoried at an exact remote ref and locally confirmed; safe isolation and interruption are demonstrated; actual state and plan representations are recorded without treating them as normative forms; and cleanup is testable.

## 11. Completeness check

Before review:

- every P002-C001 through P002-C058 case maps to at least one fixture;
- every mutating fixture has restoration and cleanup obligations;
- every interruption fixture has one exact boundary and expected trust state;
- target, source, configuration, contract, renderer, partition, ownership, gate-set and acceptance-state conditions remain distinct;
- re-acceptance prohibits renderer invocation and target mutation;
- layered acceptance keeps all guard layers distinct;
- freshness classification, drift class, trust state, gate decision and enforcement stage remain separate;
- no fixture selects or changes production implementation;
- all concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.