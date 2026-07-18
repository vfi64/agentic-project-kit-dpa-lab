# Shared Probe Execution and Evidence Contract

Status: draft

Status-date: 2026-07-18

Normative-scope: Probe preparation and later exact-ref Probe execution

Runtime-authority: none

## 1. Purpose

This contract defines the common structure for PROBE-001, PROBE-002 and the DPA-400 renderer Probe package.

It governs:

- preparation artifacts;
- exact-ref execution preconditions;
- fixture identity;
- expected-result representation;
- bounded evidence;
- outcome classification;
- cleanup and rollback;
- repeatability;
- separation of observation, interpretation and Maintainer adjudication.

This contract does not execute a Probe, select an implementation or establish main-repository conformance.

## 2. Authority order

For every Probe:

1. current exact-ref main-repository evidence;
2. applicable normative DPA specification and accepted ADRs;
3. the Probe-specific manual;
4. this shared contract;
5. planning and handoff documents.

A Probe manual MUST NOT weaken a normative DPA requirement. A planning document MUST NOT override observed exact-ref behavior.

## 3. Required identities

Every prepared and executed Probe MUST identify:

- `probe_id`;
- `probe_revision`;
- `case_id`;
- Lab repository and Lab artifact ref;
- main repository;
- exact main-repository validation ref;
- fixture set identifier and revision;
- operator or automation identity;
- execution environment identity;
- start and completion timestamps;
- command or action sequence revision.

A missing or ambiguous required identity makes the affected case `BLOCKED` unless the Probe-specific manual defines a narrower non-semantic field.

## 4. Preparation versus execution

### 4.1 Preparation

Preparation MAY define:

- fixtures;
- command placeholders;
- expected results;
- evidence paths;
- cleanup and rollback actions;
- negative cases;
- known limitations;
- adjudication mappings.

Preparation MUST be labelled as preparation and MUST NOT claim observed runtime behavior.

### 4.2 Execution

Execution begins only after:

- the current remote `origin/main` ref is recorded;
- the local checkout is synchronized and clean or any exception is explicitly recorded;
- the exact Probe ref is frozen;
- fixtures and manuals have immutable revisions;
- required tools and permissions are available;
- cleanup and rollback prerequisites are satisfied.

Execution against a moving, unknown or unrecorded ref is prohibited.

## 5. Case structure

Every Probe case MUST contain:

- `case_id` and title;
- purpose;
- governing DPA and ADR anchors;
- preconditions;
- fixture inputs;
- ordered actions;
- expected observations;
- prohibited observations;
- evidence to capture;
- cleanup and rollback;
- outcome rule;
- known limitations;
- adjudication mapping.

Negative cases MUST identify the exact failure boundary and the state that MUST remain unchanged.

## 6. Expected-result encoding

Expected results MUST distinguish:

- required success;
- required rejection;
- allowed implementation variation;
- informational observation;
- unavailable or deferred measurement.

An expected result MUST NOT encode a preferred implementation mechanism when the normative contract constrains only behavior.

## 7. Outcome vocabulary

Each case receives exactly one execution outcome:

- `PASS` — all mandatory expected observations occurred, no prohibited observation occurred and required evidence is complete;
- `FAIL` — at least one mandatory expected observation did not occur or a prohibited observation occurred;
- `PARTIAL` — the case executed and produced valid but incomplete evidence that supports only a bounded conclusion;
- `BLOCKED` — the case could not validly execute because a precondition, identity, tool, permission, environment or safety requirement was unavailable;
- `NOT_RUN` — the case was intentionally not executed and no runtime conclusion is permitted.

`PARTIAL` is an execution outcome, not a normative DPA document status.

A Probe-level conclusion MUST be derived from case outcomes using rules declared in its manual. A Probe MUST NOT report `PASS` when any mandatory case is `FAIL` or `BLOCKED`.

## 8. Observation, interpretation and adjudication

Evidence records MUST keep three layers separate.

### 8.1 Observation

Observation records what occurred:

- command or action;
- return code or API result;
- bounded output;
- created, changed or unchanged paths;
- hashes, refs and state transitions;
- timestamps and environment facts.

Observation MUST NOT contain an architecture decision disguised as fact.

### 8.2 Interpretation

Interpretation maps observations to one primary discrepancy class:

1. implementation conforms to the tested requirement;
2. required implementation is missing;
3. implementation exists but differs from the DPA proposal;
4. a DPA assumption is falsified or incomplete;
5. the Probe, fixture or expected result is defective;
6. an additional reader, writer, parser, resolver, state, lock or workflow path was discovered;
7. evidence is insufficient or execution is blocked.

Interpretation MUST cite the observations and governing anchors.

### 8.3 Maintainer adjudication

Adjudication decides whether to:

- confirm the architecture;
- amend the architecture;
- change implementation planning;
- repair the Probe or fixture;
- collect more evidence;
- rerun affected cases;
- defer with an explicit blocker.

Probe evidence MUST NOT silently modify normative architecture.

## 9. Evidence schema

Each execution MUST produce a bounded evidence set containing at least:

- `execution_manifest`;
- `case_results`;
- `command_or_action_log`;
- `environment_record`;
- `fixture_manifest`;
- `changed_path_manifest`;
- `cleanup_record`;
- `interpretation_report`;
- `adjudication_record` when adjudication has occurred.

The execution manifest MUST include exact refs and hashes for every governed input.

Large raw logs MAY be stored separately, but the bounded evidence set MUST include their paths, hashes, size and retention status.

Evidence is evidentiary authority only. It MUST NOT become runtime state, acceptance state, a lock, a registry or workflow-serialization authority.

## 10. Ordering and integrity

Evidence capture MUST preserve the order:

1. precondition record;
2. exact-ref and fixture identity;
3. pre-state snapshot;
4. action or command;
5. immediate result;
6. post-state snapshot;
7. cleanup or rollback;
8. cleanup verification;
9. interpretation;
10. adjudication.

A later summary MUST NOT overwrite earlier observations. Corrections MUST be additive and identify the superseded interpretation.

## 11. Mutation and safety boundaries

A Probe case that mutates a test worktree or fixture state MUST declare:

- allowed mutation scope;
- forbidden paths and authorities;
- pre-state hash or equivalent identity;
- expected intermediate state;
- cleanup or rollback action;
- post-cleanup verification.

No Probe preparation or execution may mutate protected production state without the explicit governed Mac/main-repository work order.

The pre-PROBE-002 mutation freeze remains binding for quick fixes. Probe execution MAY exercise frozen paths only as explicitly designed measurement subjects against the frozen exact ref.

## 12. Cleanup and rollback

Every mutating case MUST define cleanup that is:

- deterministic;
- bounded;
- independently verifiable;
- safe after partial execution;
- explicit about artifacts intentionally retained as evidence.

Cleanup success does not erase the execution record.

A failed cleanup makes the case at least `PARTIAL` and normally `FAIL` or `BLOCKED` according to the manual. The affected worktree MUST NOT be reused until disposition is recorded.

## 13. Repeatability

Each manual MUST identify:

- deterministic inputs;
- environment-sensitive inputs;
- required ordering constraints;
- whether cases are isolated or sequential;
- rerun rules;
- expected stable and variable outputs;
- second-run or second-operator requirements.

A repeat run MUST use a new execution identity and MUST link to, not overwrite, the earlier evidence.

## 14. Ref movement

If `origin/main`, a fixture, a Probe manual, a normative expectation or a tested portability slice changes after ref freeze:

- the affected Probe ref or artifact revision MUST be re-frozen;
- impacted cases MUST be identified;
- prior evidence remains historical;
- affected cases MUST be rerun unless a documented equivalence argument is independently verified and accepted.

Elapsed time alone does not invalidate evidence; changed governed identity does.

## 15. Review readiness for a Probe package

A prepared Probe package is reviewable only when:

- all mandatory cases have identifiers and governing anchors;
- fixtures are complete or explicitly marked provisional;
- expected and prohibited observations are explicit;
- outcome aggregation is defined;
- evidence, cleanup, rollback and repeatability are defined;
- unresolved main-repository mappings are classified `NEEDS_MAIN_REPO_VALIDATION`;
- no execution or conformance claim is made;
- Lab gates and an internal synchronization audit pass.

Review readiness of a Probe package is not Probe success.

## 16. Immediate consumers

The next artifacts MUST consume this contract without redefining its outcome vocabulary or evidence layers:

- `probes/PROBE-001-MANUAL.md`;
- `probes/PROBE-002-MANUAL.md`;
- `probes/DPA-400-RENDERER-PROBE-MANUAL.md`;
- their fixture manifests and case matrices;
- the exact-ref freeze and adjudication procedure.