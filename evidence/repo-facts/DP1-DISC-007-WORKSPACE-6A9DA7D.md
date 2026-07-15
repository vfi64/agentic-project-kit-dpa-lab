# DP1 Discovery Record — DISC-007 Workspace and Path APIs

Status: active
Classification: VERIFIED
Inspection date: 2026-07-15
Fact family: DISC-007
Repository: `vfi64/agentic-project-kit`
Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

## Factual question

What Workspace abstraction, path configuration and resolver methods exist for documentation, registries, evidence, temporary files and locking at the validation ref?

## Inspected paths and symbols

- `src/agentic_project_kit/workspace.py`
  - `KitConfig`
  - `LEGACY_DEFAULTS`
  - `NAMESPACE_DEFAULTS`
  - `PATH_OVERRIDE_ALIASES`
  - `Workspace`
- Consumers observed in:
  - `src/agentic_project_kit/documentation_registry.py`
  - `src/agentic_project_kit/doc_lifecycle.py`

## Observed result

1. `Workspace` is a frozen dataclass containing repository root, resolved `KitConfig`, profile/project metadata, module toggles, transfer visibility, lifecycle hygiene and gate overrides.
2. `KitConfig` declares paths for `docs`, temporary data, `.agentic`, `.agentic/tmp`, workspace manifest, workspace lock, transfer roots, reports, handoff state, planning, governance, reference, architecture, source root, documentation registry and rule registry.
3. `Workspace` provides central resolver methods including `docs_root`, `docs_file`, `tmp`, `agentic_root`, `agentic_tmp`, `workspace_lock_path`, `status_path`, `test_gates_path`, `documentation_coverage_path`, `doc_registry_path`, `rule_registry_path`, `rules_dir`, report directories and handoff-state paths.
4. `workspace_lock_path()` resolves to the configured `.agentic/tmp` root plus `workspace.lock`.
5. The default manifest path is `.agentic/config.yaml`.
6. Legacy defaults resolve the documentation registry to `docs/DOCUMENTATION_REGISTRY.yaml`; namespace defaults resolve it to `.agentic/registries/documentation.yaml`.
7. Namespace defaults also move status, handoff and report paths into `.agentic/state/...` while leaving project documentation under `docs`.
8. Path override aliases include `doc_registry_path`, `status_path`, `rule_registry_path`, handoff-state paths and handoff-package paths.
9. `documentation_registry.py` calls `load_workspace(project_root)` and reads the registry through `workspace.doc_registry_path()`.
10. `doc_lifecycle.py` uses `load_workspace()` for lifecycle hygiene configuration, although one internal registry-entry helper at this ref directly constructs `project_root / "docs" / "DOCUMENTATION_REGISTRY.yaml"`.
11. The inspected Workspace surface has no dedicated projection-target, projection-evidence or registered-region resolver at this ref.

## Limitations and unresolved questions

- This record is not a complete audit of every direct path literal in the repository.
- It does not determine whether DPA-specific resolver methods should be added or whether existing generic resolvers are sufficient.
- The direct legacy registry path inside `doc_lifecycle.py` is an observed fact, not a portability or conformance verdict.
- Manifest parsing and all consumers of each resolver were not exhaustively enumerated in this record.

## Related assumptions

- Workspace API obligation from DPA-100 and DPA-300 planning.
- A-001 and A-004 insofar as registry and lifecycle paths must resolve through the existing abstraction.

## Later Probe or Assessment obligation

After DPA-300 defines required path roles, verify that proposed registry, target, temporary-plan, evidence and lock paths can be resolved through the existing Workspace abstraction and identify any required bounded extension.

## No-generalization note

`VERIFIED` applies only to the inspected Workspace declarations and named consumers at `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`. This record does not approve a future path layout.
