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
- `src/agentic_project_kit/handoff_prompt.py`
  - `render_handoff_prompt`
- `src/agentic_project_kit/operational_handoff_projection.py`
  - `load_operational_handoff_state`
  - `replace_generated_operational_handoff_block`
  - `render_current_operational_handoff_state`
- `src/agentic_project_kit/post_merge_handoff_refresh.py`
  - `evaluate_post_merge_handoff_refresh`
- `docs/handoff/CURRENT_HANDOFF.md`
- recent administrative handoff refresh history evidenced by PR #1864 and the validation-ref commit

## Observed result

1. `write_next_chat_bootstrap` writes the complete generated `NEXT_CHAT_BOOTSTRAP.md` output through the Workspace handoff resolver. It creates parent directories and replaces the complete file contents.
2. `write_boot_report` similarly writes a complete generated boot report through the Workspace handoff resolver.
3. `handoff refresh --write` updates `.agentic/handoff_state.yaml` through `save_handoff_state`; without `--write` it is dry-run.
4. `render_handoff_prompt` is a pure text renderer over handoff-state data; the inspected function does not write files.
5. `operational_handoff_projection.py` defines a bounded generated block inside a larger document using explicit begin/end markers. It loads `.agentic/operational_handoff_state.yaml`, renders current and substantive commit facts, and can replace exactly one marked block while preserving bytes outside that block.
6. The block replacement rejects missing, duplicated or misordered markers and requires the replacement to include both markers.
7. `post_merge_handoff_refresh` reads handoff state, current Git head and commit subject, then reports whether an administrative refresh is required. The inspected module does not itself write `CURRENT_HANDOFF.md`.
8. At the validation ref, `CURRENT_HANDOFF.md` contains accumulated historical sections. The exact direct writer that appended every historical section was not located in the bounded code inspection. Recent PR history shows administrative handoff refresh commits changing handoff artifacts, but this record does not infer one universal writer implementation from commit history alone.
9. No lifecycle-mediated writer for projection targets or registered regions was observed in these handoff-specific writer paths.
10. No renderer was observed writing repository files directly; the rendering functions return strings or tuples, while separate writer functions perform file replacement.

## Ownership observations

- `.agentic/operational_handoff_state.yaml` is the observed source consumed by the operational handoff projection renderer.
- `NEXT_CHAT_BOOTSTRAP.md` has a whole-file generated writer and a byte-for-byte validation path.
- `CURRENT_HANDOFF.md` has an implemented bounded generated-block replacement primitive, but the full repository workflow that invokes it and owns all remaining historical bytes was not established by this bounded inspection.

## Limitations

- This record does not prove the absence of additional shell, workflow, GUI or manual writers.
- Commit and PR history identify administrative refresh activity but do not by themselves prove the internal write mechanism.
- No statement is made about whether the observed writer arrangement satisfies DPA-200.
- No production document form is selected.

## Later Probe or Assessment obligations

- Locate and execute the exact governed workflow that invokes the bounded operational handoff block replacement.
- Determine whether all writes to candidate targets can be routed through the existing lifecycle.
- Test direct-write detection and rollback behavior for any proposed target form.
- Establish the writer and mutation policy for bytes outside a managed generated block.

## No-generalization note

`VERIFIED` applies only to the facts, inspected paths and exact validation ref stated above. This record is evidence, not runtime authority or an ownership decision.
