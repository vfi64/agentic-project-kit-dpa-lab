# Main-Repository Remote Surface Inventory — 2026-07-19

Status: active

Status-date: 2026-07-19

Main-repository ref:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Purpose: provide a bounded, exact-ref, read-only mapping from Package-P Probe subjects to currently observed main-repository files and symbols before local materialization planning.

This inventory is provisional until locally confirmed. It records observed source surfaces, not DPA conformance and not a complete global writer/reader inventory.

## 1. Evidence classes

- `REMOTE_VERIFIED`: file and relevant symbols were read at the exact ref.
- `REMOTE_PARTIAL`: a relevant surface was observed, but ownership or completeness is not established.
- `VERIFICATION_BLOCKED`: no sufficiently grounded exact-ref mapping was established remotely.
- `NOT_IMPLEMENTATION_EVIDENCE`: the observed surface is infrastructure or an audit/reporting layer, not proof of the DPA behavior under test.

## 2. Workspace and path authority

Classification: `REMOTE_VERIFIED`

File:

`src/agentic_project_kit/workspace.py`

Observed authorities:

- `KitConfig` defines legacy and namespace-resolved path configuration.
- `Workspace` resolves documentation, registry, state, report, transfer, handoff, temporary and lock paths.
- `Workspace.doc_registry_path()` resolves the documentation registry.
- `Workspace.workspace_lock_path()` resolves the configured Workspace lock path.
- namespace defaults place the documentation registry at `.agentic/registries/documentation.yaml` and state/report surfaces below `.agentic/state/...`.
- manifest-bearing and implicit-legacy profiles are represented distinctly.

Materialization consequence:

- all fixture workspace, registry, state, report and lock paths MUST be resolved through `load_workspace()` and `Workspace` during local planning;
- no fixture may hard-code a legacy path as authoritative;
- both implicit-legacy and manifest-bearing namespace profiles require positive and negative path checks.

Limitations:

- local manifest behavior and actual profile selection remain to be executed;
- the remote read does not prove every consumer uses Workspace correctly.

## 3. Documentation registry parser and validator surface

Classification: `REMOTE_VERIFIED` for the current registry reader/validator entry points; `REMOTE_PARTIAL` for global reader completeness.

Files:

- `src/agentic_project_kit/documentation_registry.py`
- `src/agentic_project_kit/cli_commands/doc_registry.py`

Observed symbols and behavior:

- `load_documentation_registry(project_root)` loads YAML from `workspace.doc_registry_path()` and requires a mapping root.
- `documentation_registry_findings_for_data(...)` validates registry version, class rules and document entries.
- `check_documentation_registry(...)` provides a read-only validation entry point.
- `register_documentation_registry_entry(...)` is an explicit reviewed mutator for one path/class/owner entry.
- `build_doc_registry_reconcile_report(...)` is explicitly dry-run and produces structured findings.
- CLI commands expose `doc-registry register`, `doc-registry reconcile`, and `doc-registry check-unregistered`.
- the currently observed document-entry schema requires `path`, `class`, and `owner`; optional fields include `review_after` and `deferred_until`.
- current registry version handling is version `1`.

Materialization consequence for PROBE-001:

- the first executable fixture layer should exercise the existing YAML loader and validation functions directly in an isolated workspace copy;
- the current schema has no remotely verified `ProjectionContract` or `PartitionContract` representation;
- serialized DPA metadata MUST NOT be invented before local inspection of the exact registry file, tests, all registry readers, and unknown-field behavior;
- the current manual-entry control must use an exact valid version-1 entry copied or minimally reproduced from the local exact-ref registry.

Frozen mutation boundary:

- `register_documentation_registry_entry(...)` MUST NOT be used against the production registry during Probe materialization;
- any loading harness must point to disposable fixture state only.

Completeness limitation:

- remote inspection did not establish every registry consumer or normalization path;
- global reader completeness remains `NEEDS_MAIN_REPO_VALIDATION`.

## 4. Documentation lifecycle reporting surface

Classification: `REMOTE_VERIFIED` as a read-only report/findings surface; `NOT_IMPLEMENTATION_EVIDENCE` for DPA lifecycle mutation.

File:

`src/agentic_project_kit/doc_lifecycle.py`

Observed symbols and behavior:

- `build_doc_lifecycle_report(...)` reads registered and lifecycle-scoped documents and returns structured documents, findings, deferred entries and registry summary.
- `DocLifecycleReport.ok` fails on `FAIL` or `BLOCK` findings.
- `build_doc_lifecycle_strict_findings(...)` selects configured strict blockers.
- current lifecycle status vocabulary includes `idea-note`, `proposed`, `active`, `accepted`, `implemented`, `rejected`, `superseded`, and `archived`.
- report generation is read-only; JSON report writing is a reporting side effect, not a governed target writer.

Materialization consequence for PROBE-002:

- this surface can support read-only observation of current lifecycle findings and registry/header consistency;
- it does not by itself implement DPA Render–Plan–Preflight–Lock–Revalidate–Write–Verify–Record–Release;
- it does not establish DPA acceptance-state persistence, re-acceptance, layered acceptance, recovery completion or projection freshness.

Therefore:

- PROBE-002 fixture planning must distinguish existing report/findings behavior from absent or unverified DPA mutation behavior;
- no report function may be treated as acceptance authority.

## 5. Workspace mutation lock

Classification: `REMOTE_VERIFIED` for the lock implementation; `REMOTE_PARTIAL` for complete call-site coverage.

Files:

- `src/agentic_project_kit/workspace_lock.py`
- `src/agentic_project_kit/mutation_lock_audit.py`
- `src/agentic_project_kit/cli_commands/mutation_lock_audit.py`

Observed symbols and behavior:

- `acquire_workspace_lock(root, command)` uses exclusive lock-file creation.
- lock payload records process ID, command, and acquisition time.
- same-process reentrancy is implemented through `_REENTRANT_LOCK_DEPTHS`.
- a live foreign holder raises `WorkspaceLockBusy`.
- a stale holder may be removed after process-liveness evaluation.
- outer acquisition removes the lock file on release.
- `workspace_mutation_lock(...)` is the semantic alias for mutation locking.
- `audit_mutation_lock_coverage(...)` scans source for mutation patterns and lock markers.
- the current audit hard-blocking scope is concentrated on named core Git/GitHub runtime mutators, while report/filesystem writers generally remain review-visible but non-blocking.

Materialization consequence for PROBE-002:

- isolated lock fixtures can be planned around the observed lock path and public context manager;
- reentrancy, competing live process, failed acquisition, stale-lock takeover and release behavior are concrete candidate harness surfaces;
- DPA target-write locking and complete lifecycle lock coverage are not proven by the existence of this lock;
- local inventory must identify every actual lifecycle/target writer before any conclusion about DPA lock coverage.

Safety boundary:

- stale-lock tests require a disposable workspace and must never manipulate the production Workspace lock;
- process-liveness and cleanup behavior must be observed without leaving residual lock state.

## 6. Evidence tooling

Classification: `REMOTE_VERIFIED` as operational evidence tooling; `NOT_IMPLEMENTATION_EVIDENCE` for DPA acceptance authority.

File:

`src/agentic_project_kit/cli_commands/evidence.py`

Observed command surfaces:

- `evidence guard`
- `evidence inspect`
- `evidence classify-log`
- `evidence finalize-log`
- `evidence commit-paths`
- `evidence scope-check`
- `evidence clean-check`
- `evidence clean`

Observed properties:

- explicit distinction between log validation, inspection, classification, finalization, explicit-path commit, change-scope checks and cleanup;
- evidence commands can themselves mutate evidence or Git state when explicitly requested;
- cleanup preserves untracked documentation reports for human review rather than deleting them indiscriminately.

Materialization consequence:

- Probe evidence must be written only to a declared isolated evidence location;
- existing evidence tools may be reused only after local confirmation that their mutation and cleanup behavior matches the Probe evidence contract;
- evidence output must never be used as registry, lifecycle, gate or acceptance authority.

## 7. CLI command topology

Classification: `REMOTE_VERIFIED` for top-level command routing.

File:

`src/agentic_project_kit/cli.py`

Observed relevant command groups:

- `doc-registry`
- `docs`
- `evidence`
- `state`
- `workspace`
- `workflow`
- `workflow-guard`
- `handoff`
- `transfer`
- `governance`
- `audit-mutation-lock-coverage`
- `standard-gates-audit-suite`

Materialization consequence:

- local inventory must identify which commands are read-only, report-writing, repository-mutating, target-writing, state-writing or delegating wrappers;
- command names alone do not establish lifecycle phase ownership.

## 8. Renderer surface

Classification: `VERIFICATION_BLOCKED`

Remote evidence established no sufficiently grounded static renderer map, callable renderer interface, semantic-version mapping, renderer invocation boundary or renderer-specific fixture loader at the exact ref.

Required local work:

- search all source and tests for renderer identifiers, mapping tables, template/render functions and direct target writers;
- distinguish general Markdown/report rendering helpers from a DPA-compatible pure renderer boundary;
- record every candidate file, symbol, caller, inputs, outputs and side effects;
- do not materialize renderer fixtures until one exact callable boundary or an explicit implementation absence is established.

## 9. Acceptance state, re-acceptance and layered acceptance

Classification: `VERIFICATION_BLOCKED`

Remote evidence did not establish an authoritative DPA acceptance-state schema or persistence path.

The presence of lifecycle status words, reports, evidence logs or handoff state MUST NOT be interpreted as DPA acceptance state.

Required local work:

- inventory all state readers/writers and schemas;
- search for accepted fingerprints, gate-set identity, target identity, source/configuration/renderer/partition/ownership bindings and trust state;
- classify each candidate as operational state, handoff state, lifecycle report, evidence, or potential acceptance state;
- record explicit absence when no candidate satisfies the DPA contract.

No acceptance fixture may be serialized before this classification.

## 10. Recovery and interruption surface

Classification: `VERIFICATION_BLOCKED`

Remote evidence did not establish a complete DPA recovery state machine or authoritative written-unverified / verified-unrecorded representation.

Required local work:

- inventory interruption markers, temporary files, transaction state, lock recovery, writer recovery, handoff recovery and cleanup paths;
- distinguish stale Workspace-lock takeover from target-write recovery;
- identify whether current writers are atomic and how post-write verification failure is represented;
- if absent, record implementation absence rather than creating a fixture around an invented mechanism.

## 11. Gate and freshness surface

Classification: `REMOTE_PARTIAL`

The Workspace manifest supports configured extra/skip gate lists, CLI exposes standard gate and workflow-guard surfaces, and lifecycle reports can produce findings. These observations do not establish DPA gate-set identity, gate-set freshness, re-acceptance or staged enforcement.

Required local work:

- inventory gate construction, execution, result schemas, gate-set identity and enforcement modes;
- distinguish command/test gates from DPA projection gates;
- identify current `off`/`warn`/`strict` lifecycle hygiene behavior separately from DPA `observe`/`warn`/`block-new`/`strict` staged enforcement.

## 12. Current disposition matrix

| Probe area | Remote status | Materialization decision |
|---|---|---|
| Workspace/path resolution | REMOTE_VERIFIED | plan concrete profile and path fixtures |
| Registry YAML loading | REMOTE_VERIFIED | plan isolated manual controls |
| Projection/Partition serialization | VERIFICATION_BLOCKED | do not serialize yet |
| Registry unknown-field/version behavior | REMOTE_PARTIAL | inspect exact tests and all readers locally |
| Lifecycle read-only reporting | REMOTE_VERIFIED | usable as observation only |
| DPA lifecycle mutation sequence | VERIFICATION_BLOCKED | do not invent harness |
| Workspace mutation lock | REMOTE_VERIFIED | plan disposable lock fixtures |
| Complete target-writer lock coverage | REMOTE_PARTIAL | rebuild local writer/call-site inventory |
| Operational evidence tooling | REMOTE_VERIFIED | evaluate for bounded reuse |
| Static renderer mapping/callable | VERIFICATION_BLOCKED | local exact-ref search required |
| Acceptance state | VERIFICATION_BLOCKED | local exact-ref inventory required |
| Re-acceptance/layered acceptance | VERIFICATION_BLOCKED | no serialization or execution |
| Recovery state machine | VERIFICATION_BLOCKED | local exact-ref inventory required |
| DPA gate-set freshness/enforcement | REMOTE_PARTIAL | local mapping required |

## 13. Freeze boundary

This inventory authorizes planning only.

It does not authorize:

- executable fixture creation in the main repository;
- production registry mutation;
- target writes;
- handoff-writer changes;
- lifecycle Apply changes;
- acceptance-state or recovery implementation;
- Probe execution;
- DPA-600 continuation;
- DPA-700 work;
- claims of implementation or conformance.
