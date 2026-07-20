# Local Fixture Materialization Plan

Status: active

Status-date: 2026-07-19

Governing package: Package P — Remote Probe Preparation

Current remote main-repository ref observed on 2026-07-19:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Related evidence and inventories:

- `evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`
- `integration/MAIN_REPO_REMOTE_SURFACE_INVENTORY_20260719.md`
- `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
- `probes/EXACT_REF_FREEZE_PROCEDURE.md`
- `probes/EVIDENCE_CAPTURE_PROCEDURE.md`
- `probes/PROBE_ADJUDICATION_PROCEDURE.md`

## 1. Purpose

This plan governs the transition from semantic Probe fixtures to executable local fixtures on the Mac.

It is a materialization-planning contract, not a Probe runbook and not an implementation authorization.

The local phase must map each semantic fixture to current exact-ref main-repository representations without weakening the DPA contract, inventing missing production mechanisms, mutating production state or obscuring implementation absence.

## 2. Entry state

Package P is closed after:

- independent review;
- Maintainer adjudication;
- bounded corrections;
- limited PPR-M03 rereview;
- editorial closure;
- successful Lab gates.

No executable fixture has been materialized and no Probe has run.

DPA-600 remains frozen. DPA-700 remains unstarted.

## 3. Hard entry gates

No fixture materialization may begin until all of the following are recorded in one local baseline report:

1. current remote `origin/main` SHA;
2. local HEAD SHA;
3. exact equality or an explicit discrepancy stop;
4. clean worktree, except one declared in-progress evidence log if the main-repository workflow permits it;
5. Python and tool environment identity;
6. current package version;
7. current Workspace profile and manifest state;
8. selected disposable fixture root;
9. selected isolated evidence root;
10. pre-state hashes for every protected path class;
11. confirmation that no production registry, handoff, state, planning or target path is writable through the chosen harness;
12. rollback and cleanup commands tested on a disposable sentinel fixture.

Failure of any gate yields `MATERIALIZATION_BLOCKED`. It does not authorize a workaround.

## 4. Required local baseline record

Create one record with this minimum schema:

```text
baseline_id:
recorded_at_utc:
main_repository:
remote_main_ref:
local_head_ref:
refs_equal:
worktree_status:
python_version:
agentic_kit_version:
venv_identity:
workspace_profile:
workspace_manifest_path:
workspace_manifest_hash:
doc_registry_path:
doc_registry_hash:
workspace_lock_path:
disposable_fixture_root:
evidence_root:
protected_path_hash_manifest:
cleanup_sentinel_result:
operator:
limitations:
decision:
```

The baseline record is evidence, not acceptance state.

## 5. Local inventory pass

Before creating fixture bytes, perform a read-only inventory in this order.

### 5.1 Workspace and profiles

Record:

- `load_workspace()` caller behavior;
- implicit-legacy behavior;
- manifest-bearing namespace behavior;
- all path overrides relevant to registry, temporary, report, state, handoff, transfer and lock paths;
- unknown profile, unknown path alias and root-escape behavior;
- path equality under the legacy profile;
- expected path differences under the namespace profile.

Output:

`workspace_surface_inventory.json`

### 5.2 Registry readers, parser, validator and normalization

Find every exact-ref path and symbol that:

- reads the documentation registry;
- parses YAML;
- validates registry root, version, entry fields or class rules;
- normalizes or rewrites registry data;
- registers new entries;
- consumes registry entries for lifecycle, command, GUI, handoff or other behavior.

For each symbol record:

```text
path:
symbol:
role: reader | parser | validator | normalizer | writer | consumer
workspace_resolved: yes | no | partial
input_representation:
output_representation:
unknown_field_behavior:
unknown_version_behavior:
side_effects:
called_by:
tests:
probe_cases_affected:
```

Output:

`registry_surface_inventory.json`

Stop condition:

If not all relevant readers can be bounded, PROBE-001 may continue only as `PARTIAL` planning with explicit missing paths. No full-coverage claim is allowed.

### 5.3 Lifecycle, writers and target ownership

Build a complete read-only writer inventory for:

- documentation registry;
- lifecycle-scoped documents;
- handoff documents;
- generated documentation;
- state and acceptance-like records;
- evidence and reports;
- Git/GitHub mutation paths.

For each writer record:

```text
path:
symbol:
entry_points:
targets:
workspace_resolved:
lock_used:
atomic_write_method:
verification_after_write:
state_written:
recovery_marker:
cleanup_behavior:
probe_subject:
frozen_surface:
```

Output:

`writer_and_lifecycle_inventory.json`

No writer may be modified during this pass.

### 5.4 Locking

Inventory:

- `acquire_workspace_lock`;
- `workspace_mutation_lock`;
- all direct and delegated call sites;
- same-process reentrancy;
- competing-process behavior;
- stale-lock takeover;
- release and residual-state behavior;
- lock-path resolution under both profiles;
- lock coverage audit behavior and known exclusions.

Output:

`lock_surface_inventory.json`

### 5.5 Renderer candidates

Search all source and tests for:

- renderer identifiers;
- static mapping tables;
- Markdown or template rendering helpers;
- callable interfaces returning text or bytes;
- direct file writers that combine rendering and mutation;
- source/configuration input handling;
- subprocess, network, filesystem, environment and global-state access.

Classify each candidate:

- `pure-renderer-candidate`;
- `render-and-write-combined`;
- `report-renderer-only`;
- `template-helper`;
- `not-a-renderer`;
- `implementation-absent`.

Output:

`renderer_surface_inventory.json`

If no bounded static callable exists, record `implementation-absent`. Do not invent one for the Probe.

### 5.6 State, acceptance, gates and recovery

Inventory every candidate schema and writer for:

- lifecycle status;
- handoff state;
- operational state;
- command state;
- evidence state;
- acceptance-like fingerprints;
- gate results and gate-set identity;
- trust state;
- recovery and interruption markers.

Classify each candidate against the DPA requirements. Similar names do not establish semantic equivalence.

Outputs:

- `state_and_acceptance_inventory.json`
- `gate_and_freshness_inventory.json`
- `recovery_surface_inventory.json`

If authoritative acceptance or recovery state is absent, record absence explicitly.

## 6. Isolation architecture

All executable fixtures must live outside production authority paths.

Preferred structure:

```text
<disposable-root>/
  workspace-legacy/
  workspace-namespace/
  fixtures/
    probe-001/
    probe-002/
    renderer/
  evidence/
  restoration/
  manifests/
```

Required properties:

- disposable root is created for one materialization identity;
- production repository files are read-only inputs or copied fixtures, never test targets;
- fixture workspaces have independent `.agentic/`, registry, state, report, lock and target paths;
- no symlink may escape the disposable root;
- all resolved paths are checked for containment before loading or writing;
- cleanup deletes only the declared disposable root after evidence preservation;
- a failed containment check is `BLOCKED`.

## 7. Materialization identity

Every fixture set receives an immutable materialization identity:

```text
materialization_id:
probe_id:
semantic_manifest_ref:
semantic_fixture_set_revision:
main_repository_ref:
local_environment_identity:
workspace_profile:
serialization_mapping_revision:
fixture_root:
fixture_file_manifest_hash:
expected_result_manifest_hash:
created_at_utc:
created_by:
limitations:
```

A change to any identity field requires a new materialization identity.

## 8. PROBE-001 materialization sequence

### 8.1 Control first

Materialize only the current valid manual-entry control initially.

Required evidence:

- exact local registry version and schema;
- one valid current entry shape;
- parser and validator entry points;
- isolated loading mechanism;
- no production registry delta;
- deterministic repeated load/validate result.

The control must pass before DPA metadata fixtures are materialized.

### 8.2 Serialization reconciliation

Build a mapping table from every semantic `ProjectionContract` and `PartitionContract` field to one of:

- current exact serialized field;
- supported extension location;
- unsupported but representable candidate;
- impossible under current schema;
- ambiguous;
- reader-path dependent;
- requires architecture amendment;
- requires implementation.

No unresolved field may receive an invented default.

### 8.3 Fixture construction

Construct fixtures in dependency order:

1. manual control;
2. minimal full-target candidate;
3. minimal parent PartitionContract candidate;
4. minimal region reference candidate;
5. one-mutation negative fixtures;
6. relational negative fixtures;
7. unknown renderer/policy/version cases;
8. executable/dynamic content rejection cases.

Every fixture must record:

- source semantic fixture ID;
- exact bytes and hash;
- parent fixture hash;
- single mutation;
- expected parser result;
- expected validator result;
- expected normalized representation or explicit unavailability;
- cleanup result.

### 8.4 PROBE-001 materialization exit

Materialization may be marked `READY_TO_FREEZE` only when:

- every P001-C001 through P001-C027 case maps to concrete fixture bytes or an explicit non-materializable classification;
- every concrete fixture maps back to a declared case;
- all parser/validator paths are recorded or the limitation is bounded;
- production paths remain unchanged;
- repeated control execution is stable;
- the fixture-set hash manifest is complete.

## 9. PROBE-002 materialization sequence

PROBE-002 must not be forced into executable form where implementation surfaces are absent.

### 9.1 Capability map

For each P002 case, assign exactly one materialization class:

- `EXECUTABLE_CURRENT_SURFACE`;
- `EXECUTABLE_OBSERVATION_ONLY`;
- `IMPLEMENTATION_ABSENT`;
- `UNSAFE_TO_EXECUTE`;
- `SURFACE_AMBIGUOUS`;
- `HARNESS_REQUIRED`;
- `BLOCKED_BY_INVENTORY`.

### 9.2 First executable families

The safest initial candidates are read-only or disposable:

- Workspace path resolution;
- dry-run/report behavior;
- lock acquisition, competition, reentrancy and cleanup in a disposable workspace;
- evidence non-authority checks;
- read-only lifecycle findings;
- unknown-path discovery reporting.

### 9.3 Mutating and interruption families

Write, Verify, Record, Release, interruption and recovery fixtures remain blocked until:

- one disposable target writer is identified;
- complete target ownership is known;
- atomicity and restoration are demonstrated;
- post-write verification can be observed;
- interruption injection cannot affect production state;
- recovery state can be recorded without inventing authority.

### 9.4 Acceptance and re-acceptance families

If no authoritative acceptance-state mechanism exists, cases P002-C028 through P002-C043 and P002-C059 must be materialized as implementation-absence observation plans, not fake state files.

A semantic fixture may describe the required state, but no serialized acceptance record may be invented and then attributed to the current implementation.

### 9.5 Staged-enforcement families

Current lifecycle hygiene modes and DPA staged enforcement must remain distinct.

P002-C056 and P002-C060 may be executable only after exact gate/enforcement ownership is established. Otherwise they remain implementation-absence or blocked cases.

### 9.6 PROBE-002 materialization exit

Materialization may be marked `READY_TO_FREEZE` only when:

- all 60 cases have one explicit materialization class;
- every executable case has a fixture, expected result, isolation proof and cleanup method;
- every absent/blocked case has exact evidence and no fabricated mechanism;
- writer, lock, state, gate, recovery and evidence inventories are complete enough for the claimed scope;
- changed-path and protected-path manifests are empty after cleanup.

## 10. Renderer Probe materialization sequence

### 10.1 Boundary decision

Identify one exact callable boundary or record implementation absence.

A callable qualifies only if:

- renderer identity is statically resolvable;
- inputs can be supplied immutably;
- output can be observed before target mutation;
- side effects can be monitored;
- failure can be captured without conferring authority.

### 10.2 Harness design

Where a callable exists, the harness must observe:

- filesystem writes;
- network attempts;
- subprocess attempts;
- lock acquisition;
- registry/state/evidence mutation;
- Git/GitHub mutation;
- environment and secret reads where safely observable;
- repeated same-process and fresh-process output;
- return type and output hash;
- bounded failure envelope.

### 10.3 No-boundary outcome

If rendering is inseparably combined with writing or no static renderer mapping exists, record:

- exact files and symbols;
- observed coupling;
- cases blocked or classed as implementation absence;
- no renderer PASS claim.

### 10.4 Renderer materialization exit

Materialization may be marked `READY_TO_FREEZE` only when all 55 cases map bidirectionally to executable fixtures or explicit absence/blocked classifications and the capability-observation harness is safe and repeatable.

## 11. Evidence and cleanup rehearsal

Before freeze, execute a materialization-only rehearsal that:

- creates disposable fixture roots;
- writes fixture bytes;
- computes hashes;
- loads controls where permitted;
- performs no Probe-level aggregation;
- preserves materialization logs;
- cleans all disposable state;
- confirms protected-path hashes unchanged.

This rehearsal is not Probe execution. Case outcomes must remain `NOT_RUN` until the exact Probe freeze and formal execution identity exist.

## 12. Freeze handoff

When all three packages satisfy their materialization exits:

1. generate exact fixture manifests;
2. generate content-hash manifests;
3. record local environment and Workspace identities;
4. record complete inventory revisions;
5. choose one exact main-repository Probe ref or justify divergent refs;
6. run the exact-ref freeze procedure;
7. create immutable Lab and main-repository evidence refs as required;
8. only then authorize Probe execution.

## 13. Stop conditions

Stop immediately on:

- remote/local ref mismatch;
- dirty protected paths;
- unbounded writer or reader discovery;
- production-path resolution from a fixture workspace;
- symlink or root escape;
- fixture loading that mutates production state;
- unknown cleanup behavior;
- inability to distinguish evidence from state or acceptance authority;
- need to invent a renderer, acceptance state, recovery state or gate mechanism;
- DPA-600/DPA-700 scope expansion;
- any architecture contradiction requiring Maintainer adjudication.

## 14. Completion definition

This plan is complete when the repository contains a locally confirmed exact-ref materialization package that:

- preserves all semantic fixture identities;
- maps current implementation surfaces honestly;
- marks absence and blocked behavior explicitly;
- contains no invented production contract;
- proves isolation and cleanup;
- is ready for exact-ref freeze;
- still claims no Probe execution or DPA conformance.
