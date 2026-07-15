# DP1 DISC-003b — CURRENT_HANDOFF command and writer follow-up

Status: active

Classification: VERIFIED

Inspection date: 2026-07-15

Fact family: DISC-003b

Repository: `vfi64/agentic-project-kit`

Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

## Factual question

Does the explicit pre-chat-switch command `agentic-kit transfer chat-switch-complete` write `docs/handoff/CURRENT_HANDOFF.md`, and which inspected command path writes that target at the validation ref?

## Inspected paths and symbols

- `src/agentic_project_kit/cli_commands/transfer_handoff_flow.py`
  - `_emit_successor_package`
  - `chat_switch_complete`
  - `prepare_successor_handoff`
- `src/agentic_project_kit/transfer_repo_actions.py`
  - `_admin_refresh_paths`
  - `_refresh_operational_handoff_docs`
  - `admin_refresh_pr`
  - `_admin_refresh_pr_unlocked`
- Workspace handoff and package path resolvers referenced by those functions.

## Observed result

1. `agentic-kit transfer chat-switch-complete` is an explicit user-invoked pre-chat-switch command.
2. It calls `write_successor_handoff_package(...)` through `_emit_successor_package`.
3. Its declared canonical-prompt update scope is `NEXT_CHAT_BOOTSTRAP.md`, `START_NEW_CHAT_PROMPT.md` and `CLOSEOUT_BEFORE_CHAT_SWITCH_PROMPT.md` plus the successor-package files.
4. The inspected `chat-switch-complete` code does not write `docs/handoff/CURRENT_HANDOFF.md`.
5. `prepare-successor-handoff` is a deprecated alias of `chat-switch-complete` and has the same relevant write scope.
6. `transfer_repo_actions._admin_refresh_paths()` includes `docs/handoff/CURRENT_HANDOFF.md` in the administrative refresh set.
7. `agentic-kit transfer admin-refresh-pr --after-pr <N>` invokes `_refresh_operational_handoff_docs()` under the existing workspace mutation lock and administrative branch/PR workflow.
8. `_refresh_operational_handoff_docs()` reads and writes `CURRENT_HANDOFF.md` directly. In the inspected implementation it removes only a narrowly matched prior refresh marker and appends a new operational refresh section.
9. The bounded inspection therefore confirms **an observed active writer path** for `CURRENT_HANDOFF.md`: `transfer admin-refresh-pr` → `_refresh_operational_handoff_docs()`.
10. The maintainer statement that the pre-chat-switch `chat-switch-complete` command itself generates `CURRENT_HANDOFF.md` is not supported at this validation ref.

## Classification of the correction statement

The earlier correction record's maintainer claim is **REJECTED at the inspected validation ref** for the specific proposition that `chat-switch-complete` writes `CURRENT_HANDOFF.md`.

The broader proposition that `CURRENT_HANDOFF.md` participates in governed handoff refresh activity remains VERIFIED through the observed `admin-refresh-pr` path.

## Limitations

- This inspection does not prove the global absence of every other shell, GUI, manual or future writer.
- It establishes the inspected command scopes and one active writer path only.
- It does not select a DPA document form or decide migration eligibility.
- It does not prove that the existing writer satisfies DPA-300.

## Related assumptions and artifacts

- A-002 must use `an observed admin-refresh writer path`, not `the active writer path`.
- The original DISC-003 writer graph must cite this follow-up.
- The correction record must be retained as historical evidence of a rejected assumption and point here.
- PROBE-002 must cover the observed `admin-refresh-pr` path and remain open to other writers discovered later.

## Later Probe obligation

After DPA-300 through DPA-700 provide reviewable contracts, PROBE-002 must test whether every then-known writer of a selected target is routed through the lifecycle. The observed `admin-refresh-pr` path is mandatory coverage; writer-set completeness must be revalidated against the Probe validation ref.

## No-generalization note

`VERIFIED` applies only to the inspected code, command scopes and exact validation ref above. This record is evidence, not runtime authority or a production-form decision.
