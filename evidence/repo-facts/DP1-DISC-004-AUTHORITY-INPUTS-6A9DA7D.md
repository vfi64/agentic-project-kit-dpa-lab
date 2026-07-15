# DP1 DISC-004 — Authority Inputs

Status: VERIFIED

Repository: `vfi64/agentic-project-kit`

Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Inspection date: 2026-07-15

Fact family: `DISC-004`

Related assumptions: A-002, A-003

## Factual question

Which repository-backed inputs are currently read to produce or validate candidate handoff and bootstrap facts, and how are they treated by the observed code and contracts?

## Inspected paths and symbols

- `src/agentic_project_kit/chat_bootloader.py`
- `src/agentic_project_kit/cli_commands/handoff.py`
- `src/agentic_project_kit/handoff_prompt.py`
- `src/agentic_project_kit/operational_handoff_projection.py`
- `src/agentic_project_kit/post_merge_handoff_refresh.py`
- `src/agentic_project_kit/workspace.py`
- `.agentic/handoff_state.yaml` and `.agentic/operational_handoff_state.yaml` as named inputs
- `docs/reports/handoff-packages/latest/successor_context.yaml` as the preferred committed bootstrap context when present
- `docs/STATUS.md`, `docs/handoff/CURRENT_HANDOFF.md`, `docs/planning/PROJECT_DIRECTION.yaml` and governance documents as mandatory reader inputs

## Observed result

1. `.agentic/handoff_state.yaml` supplies repository, safe-state, release, active-rule, open-item, completed-work, failure-pattern, allowed-task and first-instruction data to `render_handoff_prompt`.
2. `.agentic/operational_handoff_state.yaml` supplies `current_head`, `last_substantive_work_state`, administrative context, freshness policy and next-safe-slice text to the operational handoff projection renderer.
3. The current Git HEAD and commit subject are read directly by refresh and freshness checks. They are compared with handoff-state-derived rendered content.
4. `docs/reports/handoff-packages/latest/successor_context.yaml` is preferred by `render_next_chat_bootstrap` when present; otherwise the package is rebuilt from live repository state.
5. `docs/STATUS.md`, `docs/handoff/CURRENT_HANDOFF.md`, `docs/planning/PROJECT_DIRECTION.yaml`, the documentation registry and governance contracts are mandatory boot inputs for successor-chat reconstruction. The bootloader treats them as sources that must be read, but the inspected existence checker does not resolve conflicts among them.
6. The documentation registry is read for registry metadata and summaries shown by handoff checks.
7. `CURRENT_HANDOFF.md` is an observed consumer-facing document and mandatory boot source. The inspected operational renderer derives only its marked current-state block from machine-readable state; historical prose outside that block is preserved rather than used as renderer input.
8. Review artifacts, evidence records and generated targets were not observed as semantic inputs to `render_handoff_prompt` or `render_current_operational_handoff_state` in the inspected modules.
9. Authority remains distributed in the observed current system: machine-readable handoff state owns several current operational facts, Git owns commit identity, the registry owns document classification metadata, PROJECT_DIRECTION owns planning items, and Markdown governance files own human-readable contracts.
10. No single code path inspected here establishes a complete conflict-resolution hierarchy across all mandatory boot inputs.

## Unresolved authority ambiguity

- The exact precedence applied by a human or LLM when `STATUS.md`, `CURRENT_HANDOFF.md`, successor package context and machine-readable handoff state disagree is not fully encoded in the inspected readers.
- The committed successor package is preferred for deterministic bootstrap rendering, while live state is used when the package context is absent; the compatibility and freshness implications belong to Probe.
- Historical prose in `CURRENT_HANDOFF.md` is preserved and read, but is not observed as canonical input to the operational current-state renderer.

## Limitations

- This is a bounded source inventory, not an exhaustive repository-wide authority proof.
- It does not promote any observed input to a new DPA canonical source.
- It does not decide whether the current authority distribution is sufficient or desirable.
- It does not select a migration form.

## Later Probe or Assessment obligations

- Define and test the required conflict-resolution order for a proposed DPA contract.
- Verify the exact fields needed to render each candidate current-state region.
- Determine whether committed successor context and live state can share one freshness contract without circular authority.
- Verify that evidence and historical prose remain excluded from semantic renderer inputs.

## No-generalization note

`VERIFIED` applies only to the facts, inspected paths and exact validation ref stated above. This record is evidence, not runtime authority or an architecture decision.
