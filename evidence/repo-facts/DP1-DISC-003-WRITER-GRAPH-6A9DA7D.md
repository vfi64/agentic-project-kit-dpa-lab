# DP1 DISC-003 — Candidate Writer Graph

Status: VERIFIED

Repository: `vfi64/agentic-project-kit`

Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Inspection date: 2026-07-15

Fact family: `DISC-003`

Related assumptions: A-002, A-003, A-005

## Factual question

Which code and workflow paths write or regenerate the handoff and bootstrap candidate artifacts, and what ownership or boundary behavior is observable?

## Inspected paths and symbols

- `src/agentic_project_kit/chat_bootloader.py`
  - `write_next_chat_bootstrap`
  - `write_boot_report`
- `src/agentic_project_kit/cli_commands/handoff.py`
  - `refresh`
- `src/agentic_project_kit/cli_commands/transfer_handoff_flow.py`
  - `chat_switch_complete`
  - `prepare_successor_handoff`
  - `_emit_successor_package`
- `src/agentic_project_kit/successor_handoff_package.py`
  - `write_successor_handoff_package`
  - canonical prompt projection writers
- `src/agentic_project_kit/transfer_repo_actions.py`
  - `_refresh_operational_handoff_docs`
  - `admin_refresh_pr`
- `src/agentic_project_kit/handoff_prompt.py`
  - `render_handoff_prompt`
- `src/agentic_project_kit/operational_handoff_projection.py`
  - `load_operational_handoff_state`
  - `replace_generated_operational_handoff_block`
  - `render_current_operational_handoff_state`
- `src/agentic_project_kit/post_merge_handoff_refresh.py`
  - `evaluate_post_merge_handoff_refresh`
- `docs/handoff/CURRENT_HANDOFF.md`
- PRs #1249, #1253 and #1255, which introduced the operational state source, generated markers and bounded block replacement

## Observed result

1. `transfer chat-switch-complete` calls `write_successor_handoff_package` and writes the latest successor package plus the canonical prompt projections `NEXT_CHAT_BOOTSTRAP.md`, `START_NEW_CHAT_PROMPT.md` and `CLOSEOUT_BEFORE_CHAT_SWITCH_PROMPT.md`. It reads `CURRENT_HANDOFF.md` as a long-term source but does not write that file.
2. `prepare-successor-handoff` is a deprecated compatibility alias for the same package-generation path.
3. The mutating command path for `CURRENT_HANDOFF.md` is `transfer admin-refresh-pr`. It reaches `_refresh_operational_handoff_docs(after_pr)` while constructing an administrative post-merge handoff refresh.
4. `_refresh_operational_handoff_docs` updates `.agentic/handoff_state.yaml` and `.agentic/operational_handoff_state.yaml`, refreshes package projections, writes a post-PR successor prompt, and edits `STATUS.md`, `CURRENT_HANDOFF.md` and `START_NEW_CHAT_PROMPT.md`.
5. For `CURRENT_HANDOFF.md`, the function does not call `replace_generated_operational_handoff_block`. Instead it removes at most one prior section matching `Operational documentation refresh state after PR #...` and appends a new Markdown section at the end of the complete document.
6. The implemented regex only matches the current standardized refresh-section shape. Older historical sections with different headings or wording remain in place. This explains why accumulated historical content can remain at the start of `CURRENT_HANDOFF.md` even after a governed refresh.
7. `operational_handoff_projection.py` already provides a bounded generated-block renderer and a safe replacement primitive. The primitive requires exactly one ordered marker pair, requires replacement markers, and preserves bytes outside the marked block.
8. PR #1249 introduced `.agentic/operational_handoff_state.yaml` and the renderer. PR #1253 added explicit begin/end markers. PR #1255 added the bounded block replacement helper. At the validation ref, the administrative writer still uses the append/regex path rather than that bounded replacement helper for `CURRENT_HANDOFF.md`.
9. `write_next_chat_bootstrap` writes the complete generated `NEXT_CHAT_BOOTSTRAP.md` output through the Workspace handoff resolver. `handoff refresh --write` updates `.agentic/handoff_state.yaml`; without `--write` it is dry-run.
10. `render_handoff_prompt` and `render_current_operational_handoff_state` are renderers: they return text or line tuples. Repository writes occur in separate writer/orchestration functions.
11. No existing documentation-lifecycle API mediates the `CURRENT_HANDOFF.md` mutation in `_refresh_operational_handoff_docs`; the function writes the file directly with `Path.write_text`.

## Command adaptation obligation

The existing command cannot remain unchanged under the proposed DPA architecture.

The later DPA-300/DP1 Probe contract MUST evaluate and specify a migration of the `transfer admin-refresh-pr` / `_refresh_operational_handoff_docs` path so that:

- the operational current-state projection is rendered from declared canonical sources;
- the bounded generated region is replaced through the governed lifecycle writer rather than appended as ad-hoc prose;
- missing, duplicated or misordered boundaries fail loud;
- bytes outside the registered region retain an explicit owner and are preserved;
- the command does not accumulate a new historical refresh section on every invocation;
- package generation and `CURRENT_HANDOFF.md` refresh remain one governed, stale-plan-protected workflow;
- direct writes outside the lifecycle boundary become detectable;
- compatibility with existing manual or historical content is decided from DP1 evidence rather than assumed.

This obligation does not select managed-head, hybrid or another production form. It records that the current command path is an implementation surface that must be adapted if `CURRENT_HANDOFF.md` is selected for migration.

## Ownership observations

- `.agentic/operational_handoff_state.yaml` is the observed input consumed by the operational handoff projection renderer.
- `NEXT_CHAT_BOOTSTRAP.md` has a whole-file generated writer and byte-for-byte validation path.
- `CURRENT_HANDOFF.md` already contains a marked generated block and has a safe replacement primitive, but the active administrative refresh writer bypasses that primitive and appends a refresh section to the full document.
- The remaining historical and curated bytes have no complete machine-readable ownership policy in the inspected command path.

## Limitations

- This record does not prove the absence of additional shell, workflow, GUI or manual writers.
- The command was inspected statically at the exact validation ref; no mutating execution was performed.
- No statement is made yet about which DPA document form the target should use.
- No conformance or sufficiency judgement is made; those belong to DP1 Probe and Assessment after DPA-300.

## Later Probe or Assessment obligations

- Probe the proposed registry and lifecycle contract against this exact command surface.
- Verify whether the existing bounded replacement primitive can be retained behind the lifecycle boundary or must be refactored.
- Determine whether all writes to candidate targets can be routed through the existing lifecycle and Workspace APIs.
- Test missing/duplicate/misordered-marker failure, stale-plan rejection, direct-write detection and rollback.
- Establish the writer and mutation policy for all bytes outside the registered generated region.

## No-generalization note

`VERIFIED` applies only to the facts, inspected paths and exact validation ref stated above. This record is evidence, not runtime authority, a form selection or an implementation decision.
