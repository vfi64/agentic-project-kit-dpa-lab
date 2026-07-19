# Remote Command Mutation Inventory — 2026-07-19

Status: active

Status-date: 2026-07-19

Main-repository exact ref:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Lab working branch:

`spec/dpa-600-concurrency`

Classification: exact-ref remote inventory, incomplete pending full source and local installed-CLI confirmation

Governing plan:

`integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`

Proposed decision vocabulary:

`decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`

## 1. Purpose and evidence boundary

This inventory records document-like mutation command modes and internal writer surfaces observed directly at the exact main-repository ref above.

It is not a completeness claim, normative DPA amendment, Probe result, implementation authorization or main-repository conformance statement.

The GitHub remote inspection surface did not provide a complete indexed code search. Therefore entries are limited to files and call chains read directly. Missing command families remain explicit.

Local confirmation must later compare this inventory with:

- the installed CLI help tree;
- the complete source tree;
- direct writer-pattern search;
- disposable-repository before/after changed-path observations;
- Workspace profile resolution;
- composed-command call chains.

## 2. Provisional command-mode inventory

| ID | Public command mode | Internal writer or delegated surface | Primary provisional class | Canonical inputs observed | Declared or observed targets | Workspace resolution | Lock / lifecycle ownership | Post-write verification | Evidence status |
|---|---|---|---|---|---|---|---|---|---|
| CMI-001 | `agentic-kit handoff show` | `load_handoff_state()` | CMA-8 read-only-inspector | handoff state YAML | none | caller accepts direct path argument | none | not applicable | REMOTE_VERIFIED |
| CMI-002 | `agentic-kit handoff check` | `load_handoff_state()` plus `validate_handoff_state()` | CMA-8 read-only-inspector | handoff state YAML; documentation registry summary | none | handoff project-root inference plus registry Workspace loading | none | validation only | REMOTE_VERIFIED |
| CMI-003 | `agentic-kit handoff prompt` | `render_handoff_prompt()` and freshness guard | CMA-8 read-only-inspector | handoff state YAML | stdout only | direct handoff path argument | none | freshness assessment before output | REMOTE_VERIFIED |
| CMI-004 | `agentic-kit handoff refresh` without `--write` | `refresh_handoff_safe_state()` | CMA-8 read-only-inspector | current handoff YAML; current Git HEAD and subject | stdout only | direct handoff path argument | none | validates proposed state before output | REMOTE_VERIFIED |
| CMI-005 | `agentic-kit handoff refresh --write` | `save_handoff_state()` | CMA-3 state-transition-mutator | current handoff YAML; current Git HEAD and subject; preservation anchors | selected handoff-state YAML | direct path argument; default `.agentic/handoff_state.yaml` | no lifecycle or lock observed in inspected call chain | validates in-memory state before write; no reread comparison observed | REMOTE_VERIFIED for inspected path; local call-chain confirmation required |
| CMI-006 | `agentic-kit doc-registry register` | `register_documentation_registry_entry()` | CMA-1 canonical-source-mutator | explicit path, class and owner; current documentation registry | Workspace-resolved documentation registry | command passes project root; registry loader uses `Workspace.doc_registry_path()` | lifecycle ownership not observed at CLI boundary | result reports `written`; complete reread and changed-path verification not yet established | REMOTE_PARTIAL |
| CMI-007 | `agentic-kit doc-registry reconcile` | `build_doc_registry_reconcile_report()` | CMA-8 read-only-inspector | current registry, declared scope and decision projection | stdout only | project root passed to registry functions | execute mode is explicitly blocked | report result only | REMOTE_VERIFIED |
| CMI-008 | `agentic-kit doc-registry check-unregistered` | `build_unregistered_document_candidates_report()` | CMA-8 read-only-inspector | registry and documentation tree | stdout only | project root and Workspace registry resolution | none | report result only | REMOTE_VERIFIED |
| CMI-009 | `agentic-kit docs lifecycle bootstrap --dry-run` | `build_doc_lifecycle_bootstrap_payload(..., execute=False)` | CMA-8 read-only-inspector | lifecycle-scoped documents and headers | stdout only | root is resolved before delegation | delegated ownership requires further source inspection | payload status only | REMOTE_PARTIAL |
| CMI-010 | `agentic-kit docs lifecycle bootstrap --execute` | `build_doc_lifecycle_bootstrap_payload(..., execute=True)` | CMA-1 canonical-source-mutator, provisional | current document bytes and missing lifecycle headers | multiple documentation files | root is resolved before delegation | lifecycle helper owns operation; lock and exact writes not yet read | payload reports result; per-target reread unconfirmed | REMOTE_PARTIAL |
| CMI-011 | `agentic-kit docs lifecycle sweep --dry-run` | `build_doc_lifecycle_sweep_payload(..., execute=False)` | CMA-8 read-only-inspector | lifecycle findings, registry and requested selection | stdout only | root is resolved | no write in dry-run mode | payload status only | REMOTE_PARTIAL |
| CMI-012 | `agentic-kit docs lifecycle sweep --execute` | `build_doc_lifecycle_sweep_payload(..., execute=True)` | mixed; primary class requires per-action decomposition | lifecycle findings; selected finding IDs; optional dates | registry metadata and/or documentation headers depending on selected action | root is resolved | delegated lifecycle-sweep ownership; exact lock and writer coverage unknown | payload status; declared-versus-actual path equality unconfirmed | REMOTE_PARTIAL |
| CMI-013 | `agentic-kit docs lifecycle apply` without `--execute` | `build_doc_lifecycle_apply_payload(..., execute=False)` | CMA-8 read-only-inspector | lifecycle plan and selected step | stdout only | resolved root and scope | no mutation requested | payload status only | REMOTE_PARTIAL |
| CMI-014 | `agentic-kit docs lifecycle apply --execute` | `build_doc_lifecycle_apply_payload(..., execute=True)` | CMA-6 migration-or-archival-mutator or CMA-1, unresolved by plan step | lifecycle plan, selected step and target documents | one bounded lifecycle plan target per invocation | resolved root and scope | delegated lifecycle helper; exact writer, lock and rollback call chain pending | result payload only at CLI boundary | REMOTE_PARTIAL; frozen DPA-critical subject |
| CMI-015 | `agentic-kit docs lifecycle report` without `--execute` | `build_doc_lifecycle_evidence_report_payload(..., execute=False)` | CMA-8 read-only-inspector | lifecycle state and findings | stdout only | resolved root, explicit output path retained as plan input | no write requested | payload status only | REMOTE_PARTIAL |
| CMI-016 | `agentic-kit docs lifecycle report --execute` | `build_doc_lifecycle_evidence_report_payload(..., execute=True)` | CMA-4 evidence-report-writer | lifecycle state, findings and report configuration | default `docs/architecture/evidence/doc-lifecycle-report.json` or explicit output | root resolved; output path supplied separately | report writer, not lifecycle target authority | report payload result; reread/hash and containment pending | REMOTE_PARTIAL |
| CMI-017 | `agentic-kit docs lifecycle plan` | `build_doc_lifecycle_plan_payload()` | CMA-8 read-only-inspector | lifecycle state and target scope | stdout only | resolved root and scope | no write | payload status only | REMOTE_PARTIAL |
| CMI-018 | `agentic-kit docs lifecycle triage` | `build_doc_lifecycle_triage_payload()` | CMA-8 read-only-inspector | lifecycle findings and registry | stdout only | resolved root | no write | payload status only | REMOTE_PARTIAL |
| CMI-019 | `agentic-kit docs removed-source-audit` | `build_removed_source_audit()` | CMA-8 read-only-inspector | removed-source declarations, docs, registry and references | stdout only | root resolved; central target explicit | no write | structured audit result | REMOTE_VERIFIED at CLI boundary |
| CMI-020 | administrative transfer refresh mode, exact public command mapping pending | `_admin_refresh_paths()` plus downstream transfer orchestration | composed mutation requiring per-subcommand classification | handoff state, operational handoff state, status, current handoff, bootstrap prompts and successor package inputs | eleven fixed Workspace-resolved artifacts plus potentially package-directory artifacts | all fixed targets are obtained through Workspace methods | transfer orchestration uses Workspace mutation-lock imports; exact scoped call chain remains to be read | freshness checks cover package identities, required markers and permitted refresh-only changed paths; write verification still requires exact writer inspection | REMOTE_PARTIAL |

## 3. Confirmed internal writer surface

### IW-001 — Handoff state serialization

Observed function:

`handoff_state.save_handoff_state(data, path)`

Observed behavior:

- serializes YAML with stable key order disabled and Unicode enabled;
- restores required preservation anchors when absent from the serialized YAML;
- writes the resulting complete text directly to the selected path using `Path.write_text()`.

Provisional classification:

`CMA-3 state-transition-mutator`

Confirmed concerns:

- the function accepts a direct path rather than a Workspace object;
- no mutation lock is visible in the inspected direct caller `handoff refresh --write`;
- validation occurs before serialization, but post-write reread, hash verification and changed-path-scope verification were not observed;
- the same semantic handoff facts may also feed generated handoff and successor-package artifacts through other command paths.

Architecture disposition:

Suspected command-authority gap requiring complete call-chain and duplicate-writer evidence. No implementation change is authorized.

### IW-002 — Documentation registry mutation

Observed public path:

`agentic-kit doc-registry register`

Observed behavior:

- accepts exactly one reviewed path, class and owner tuple;
- delegates to `register_documentation_registry_entry()`;
- registry loading resolves through `Workspace.doc_registry_path()`;
- the command emits a `written` result field and fails when result status is not `PASS`.

Provisional classification:

`CMA-1 canonical-source-mutator`

Open evidence:

- exact serialization and atomicity;
- lock use;
- duplicate-entry and concurrent-writer behavior;
- post-write reread and schema validation;
- actual changed-path equality;
- all other registry writers and normalizers.

### IW-003 — Documentation lifecycle execution family

Observed public modes:

- `docs lifecycle bootstrap --execute`;
- `docs lifecycle sweep --execute`;
- `docs lifecycle apply --execute`;
- `docs lifecycle report --execute`.

Observed architectural fact:

These are not one mutation class. They include at least canonical document/header mutation, registry or lifecycle-metadata mutation, bounded plan application and evidence-report writing.

Required decomposition:

- one row per executable action selected by sweep;
- one row per apply plan-step kind;
- separate report-output writer;
- separate bootstrap header writer;
- exact lock, atomic-write, rollback and post-write verification ownership.

## 4. First semantic-fact overlap findings

| Overlap ID | Fact family | Observed representations or writers | Current classification | Required next evidence |
|---|---|---|---|---|
| OF-001 | current Git safe state and latest substantive state | `.agentic/handoff_state.yaml`; administrative evidence state; generated prompts and successor package | suspected one source with multiple projections, but duplicate mutation paths not yet excluded | inspect all callers of `refresh_handoff_safe_state()`, `save_handoff_state()` and operational refresh orchestration |
| OF-002 | next-chat bootstrap and successor instructions | `NEXT_CHAT_BOOTSTRAP.md`, `START_NEW_CHAT_PROMPT.md`, successor package prompt/context/execution/validation artifacts | composed generated-artifact family with shared semantic facts | identify canonical input record, every generator, output ordering and direct-edit policy |
| OF-003 | status and handoff current-state facts | status path, `CURRENT_HANDOFF.md`, handoff state and successor package | competing or composition-dependent writer suspected | inspect `_refresh_operational_handoff_docs()` and all status/handoff writers; compare source ownership |
| OF-004 | documentation lifecycle status | document headers, documentation registry metadata, lifecycle report JSON | legitimate layered representations possible, but authority split not yet established | inspect lifecycle bootstrap/sweep/apply implementations and report consumers |
| OF-005 | documentation registry membership | registry YAML, scope YAML, reconcile report and unregistered candidate report | one canonical source with multiple read-only projections observed | identify all registry writers and generated decision/reference artifacts |

## 5. Generated-artifact ownership findings

| Artifact family | Observed target set | Current owner hypothesis | Direct-edit policy | Current risk |
|---|---|---|---|---|
| Handoff state | `.agentic/handoff_state.yaml` | `handoff refresh --write` and transfer orchestration, exact exclusivity unproven | canonical state may be directly maintained only through governed state writer; policy not yet established | duplicate writer and missing post-write verification suspected |
| Operational handoff package | operational state, status, current handoff, bootstrap prompts, execution/source/context/prompt/validation package files | administrative transfer refresh orchestration | targets appear generated and should not be durable primary edit surfaces; exact contract pending | eleven fixed targets create high synchronization and partial-failure risk |
| Documentation registry | Workspace-resolved registry YAML | `doc-registry register` plus possible lifecycle sweep writers | direct manual maintenance policy requires exact contract inspection | multiple mutation modes may overlap |
| Lifecycle evidence report | default JSON report or explicit output | `docs lifecycle report --execute` | generated evidence; not canonical lifecycle state | explicit output may escape intended evidence location unless containment is enforced |
| Lifecycle headers and bounded document changes | registered or lifecycle-scoped documents | bootstrap, sweep and apply helpers | document class and action determine whether direct maintenance remains valid | mixed mutation classes hidden behind shared CLI group |

## 6. Immediate next remote inspection order

1. inspect all public transfer commands and aliases and map them to `transfer_repo_actions` functions;
2. inspect `_refresh_operational_handoff_docs()` and every writer it calls;
3. inspect operational handoff-state writer and status writer;
4. inspect lifecycle bootstrap, sweep, apply and report writer implementations;
5. inspect documentation-registry serialization and every caller;
6. inspect evidence, state, direction, work-order, scaffold, init, release and generated-reference command families;
7. inspect cleanup, archive, rename, replace, unlink and `rmtree` paths;
8. inspect composed PR/post-merge commands that invoke multiple document writers;
9. update this inventory with exact target paths, actual writer symbols, locks, verification, rollback and Probe coverage;
10. only after remote bounded completion prepare the semantic-fact overlap and generated-artifact ownership matrices as separate review artifacts.

## 7. Current conclusion

The remote evidence already confirms that document mutation is distributed across command families and that one administrative refresh operation treats at least eleven handoff, status and successor-package artifacts as one refresh set.

The evidence does not yet prove that these artifacts have conflicting semantic authority. It does prove that filename-level renderer and lifecycle contracts alone are insufficient for complete command-integration planning.

ADR-022 remains a deferred proposal. DPA-200 through DPA-500 remain unchanged. DPA-600 remains frozen and DPA-700 remains unstarted.
