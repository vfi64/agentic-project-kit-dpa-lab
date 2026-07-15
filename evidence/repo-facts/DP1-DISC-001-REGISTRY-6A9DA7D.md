# DP1 Discovery Record — DISC-001 Registry Representation

Status: active
Classification: VERIFIED
Inspection date: 2026-07-15
Fact family: DISC-001
Repository: `vfi64/agentic-project-kit`
Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

## Factual question

What documentation-registry representation, loaders, validators, commands and identity fields exist at the validation ref?

## Inspected paths and symbols

- `docs/DOCUMENTATION_REGISTRY.yaml`
- `src/agentic_project_kit/documentation_registry.py`
  - `load_documentation_registry`
  - `load_documentation_registry_scope`
  - `build_documentation_registry_summary`
  - `find_unregistered_document_candidates`
- `src/agentic_project_kit/cli_commands/doc_registry.py`
  - `doc-registry register`
  - `doc-registry reconcile`
  - `doc-registry check-unregistered`
- `src/agentic_project_kit/workspace.py`
  - `KitConfig.documentation_registry_file`
  - `Workspace.doc_registry_path`

## Observed result

1. The registry is YAML, version `1`, and is resolved through `Workspace.doc_registry_path()`.
2. The root contains `status`, `schema`, `class_rules` and `documents`.
3. Required document fields are `path`, `class` and `owner`.
4. The registry-declared optional document fields at this ref are only `review_after` and `deferred_until`.
5. Registered identity is a repository-relative document `path`; no region identifier or region-boundary representation was observed in the inspected schema and loader paths.
6. `load_documentation_registry()` parses YAML and requires the root to be a mapping.
7. `doc-registry register` is an explicit mutating command for one reviewed path/class/owner entry.
8. `doc-registry reconcile` is dry-run only at this ref; `--execute` returns `BLOCK`.
9. `doc-registry check-unregistered` inventories unregistered `.md`, `.yaml` and `.yml` files under `docs`, with configured exclusions and optional strict declared-scope handling.
10. The registry status explicitly says `broad_migration_allowed: false` and describes the schema as an experimental minimal baseline.

## Limitations and unresolved questions

- This record does not determine whether an optional DPA `projection` structure would be accepted by all actual validation paths.
- This record does not prove that unknown nested fields are rejected or preserved in every code path.
- No region-level registry identity was observed; absence from the inspected paths is not yet a proof that no other repository mechanism represents regions.
- Parser/validator compatibility with a proposed DPA-300 schema remains a DP1 Probe obligation.

## Related assumptions

- A-001 — optional projection-block compatibility.
- Region-level target representation obligation from DPA-200.

## Later Probe or Assessment obligation

Construct a bounded sample registry extension after DPA-300 defines the proposed contract, then run the actual parser, validators and relevant tests at an exact Probe validation ref.

## No-generalization note

`VERIFIED` applies only to the listed files, symbols and observed behavior at `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`. This record makes no architecture decision and does not select a production representation.
