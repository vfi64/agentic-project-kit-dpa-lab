# DP1 DISC-002 — Candidate Reader Graph

Status: VERIFIED

Repository: `vfi64/agentic-project-kit`

Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Inspection date: 2026-07-15

Fact family: `DISC-002`

Related assumptions: A-002, A-003

## Factual question

Which repository-backed readers consume the handoff and bootstrap candidate documents, in what order, and with what observed scope?

## Inspected paths and symbols

- `src/agentic_project_kit/chat_bootloader.py`
  - `MANDATORY_BOOT_SOURCES`
  - `check_boot_sources`
  - `render_bootloader`
  - `render_next_chat_bootstrap`
  - `validate_generated_bootstrap`
- `src/agentic_project_kit/cli_commands/handoff.py`
  - `show`
  - `check`
  - `prompt`
  - `post_merge_refresh_status`
- `src/agentic_project_kit/handoff_prompt.py`
  - `MANDATORY_SUCCESSOR_CHAT_SOURCES`
  - `render_handoff_prompt`
- `docs/handoff/CURRENT_HANDOFF.md`
- `docs/handoff/NEXT_CHAT_BOOTSTRAP.md` and `docs/handoff/START_NEW_CHAT_PROMPT.md` as named mandatory sources

## Observed result

1. The chat bootloader declares an ordered tuple of mandatory repository sources. The sequence includes machine-readable state first, followed by `docs/STATUS.md`, `docs/handoff/CURRENT_HANDOFF.md`, successor-chat prompts, governance contracts, the documentation registry and `docs/planning/PROJECT_DIRECTION.yaml`.
2. `docs/handoff/CURRENT_HANDOFF.md` is consumed as a complete mandatory boot source; no bounded-region reader or section selector was observed in the inspected bootloader path.
3. The bootloader checks source existence and tells the successor chat to read the sources before repository changes. Its file-existence check does not itself parse semantic sections of `CURRENT_HANDOFF.md`.
4. `render_next_chat_bootstrap` prefers `docs/reports/handoff-packages/latest/successor_context.yaml` when present and otherwise builds a successor handoff package from repository state.
5. `validate_generated_bootstrap` compares the complete committed `NEXT_CHAT_BOOTSTRAP.md` bytes with the expected generated output.
6. `handoff prompt` reads `.agentic/handoff_state.yaml`, validates it, renders the complete handoff prompt and optionally prepends a freshness guard.
7. `MANDATORY_SUCCESSOR_CHAT_SOURCES` extends the boot sources with `docs/TEST_GATES.md` and relevant source/tests.
8. At the validation ref, `CURRENT_HANDOFF.md` begins with historical administrative sections including Post-PR1245 and older states; the observed reader contract still requires reading the document as a whole from the top.
9. Human and LLM consumers are explicitly named by the bootstrap workflow. CLI readers are evidenced by `handoff` and `boot` commands. No GUI-specific reader of `CURRENT_HANDOFF.md` was established in this bounded inspection.

## Read-order observation

The explicit boot source order places `.agentic/` context and handoff state before Markdown status and handoff documents. Within `CURRENT_HANDOFF.md`, no machine-enforced section priority or current-region boundary was observed; ordinary readers encounter the first bytes first.

## Limitations

- This record is bounded to the inspected bootloader and handoff modules at the validation ref.
- Repository-wide dynamic references, external scripts, user habits and GUI code were not exhaustively proven absent.
- The record does not decide which document form should be selected.
- It does not judge whether the existing reader order is acceptable under DPA-200.

## Later Probe or Assessment obligations

- Verify whether all production consumers can honor a registered current region or generated target.
- Test whether any proposed migration preserves required boot ordering and byte expectations.
- Enumerate any GUI or external consumers not visible in this bounded source inspection.

## No-generalization note

`VERIFIED` applies only to the facts, inspected paths and exact validation ref stated above. This record is evidence, not runtime authority or a migration decision.
