# DP1 Discovery Record — DISC-006 Lifecycle Mutation Path

Status: active
Classification: VERIFIED
Inspection date: 2026-07-15
Fact family: DISC-006
Repository: `vfi64/agentic-project-kit`
Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

## Factual question

What planning, validation, mutation and evidence-writing paths exist in the documentation lifecycle at the validation ref?

## Inspected paths and symbols

- `src/agentic_project_kit/cli_commands/docs.py`
- `src/agentic_project_kit/doc_lifecycle.py`
  - `build_doc_lifecycle_report`
  - `build_doc_lifecycle_triage_payload`
  - `build_doc_lifecycle_plan_payload`
  - `build_doc_lifecycle_apply_payload`
  - `build_doc_lifecycle_evidence_report_payload`
  - `write_doc_lifecycle_json_report`
- `src/agentic_project_kit/documentation_registry.py`
- `src/agentic_project_kit/workspace.py`

## Observed result

1. The CLI exposes lifecycle subcommands `bootstrap`, `propose-delete`, `sweep`, `apply`, `report`, `plan` and `triage`.
2. `triage` is advisory and produces findings plus proposed actions with `execute=false`.
3. `plan` builds a deterministic dry-run plan from triage output and marks execution disabled.
4. `apply` requires an explicit `--execute` flag and one exact plan-step id.
5. At this ref, `build_doc_lifecycle_apply_payload()` only accepts `confirm-current` and `defer`; both return a no-op effect and `mutation: none`.
6. The apply implementation explicitly states that it never edits, moves, archives or deletes files in this slice.
7. `report` is dry-run by default and may write one bounded JSON evidence report only when `--execute` is supplied and the output path passes an allow-list check.
8. Evidence-report execution creates parent directories and writes formatted JSON; it reports `mutation: write-report`, while archive and delete remain disabled.
9. Lifecycle reporting reads registry entries, lifecycle headers, direction statuses and workspace hygiene configuration and emits structured findings.
10. Findings carry `code`, `path`, `message`, `severity`, optional document class and optional age.
11. The lifecycle uses `Workspace` to resolve the documentation registry and hygiene settings.
12. No lifecycle document-content writer, atomic target replacement or mutation-lock acquisition was observed in the inspected `doc_lifecycle.py` apply path at this ref.

## Limitations and unresolved questions

- `doc_lifecycle_sweep.py` and other commands may contain additional bounded mutations not fully inspected in this record.
- This record does not establish the complete repository-wide mutation-lock call graph.
- This record does not determine whether the current lifecycle is sufficient for DPA projection writes, trust-state transitions or direct-write detection.
- Atomic-write and crash-recovery behavior for future projection targets remain Probe and DPA-300 obligations.

## Related assumptions

- A-004 — existing lifecycle finding and mutation structures.
- A-005 — workflow and stale-plan enforcement, only insofar as lifecycle planning exposes bounded steps.

## Later Probe or Assessment obligation

After DPA-300 defines the lifecycle contract, test whether existing planning, locking, writing, evidence and finding mechanisms can implement the required projection semantics without a parallel lifecycle.

## No-generalization note

`VERIFIED` applies only to the inspected lifecycle surfaces and behavior at `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`. No sufficiency or compatibility judgment is made.
