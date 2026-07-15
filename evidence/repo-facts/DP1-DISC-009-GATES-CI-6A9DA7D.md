# DP1 Discovery Record — DISC-009 Gates and CI

Status: active
Classification: VERIFIED
Inspection date: 2026-07-15
Fact family: DISC-009
Repository: `vfi64/agentic-project-kit`
Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

## Factual question

Which documentation/lifecycle gate mappings and CI execution surfaces exist at the validation ref?

## Inspected paths and symbols

- `src/agentic_project_kit/doc_lifecycle.py`
  - report `ok` mapping
  - strict blocker selection
  - triage and plan result mapping
- `src/agentic_project_kit/cli_commands/docs.py`
- `src/agentic_project_kit/transfer_repo_actions.py`
  - post-merge and successor-package freshness checks
- `.github/workflows/ci.yml`
- documented standard gate and protected-diff workflows referenced by the transfer and handoff contracts

## Observed result

1. Documentation-lifecycle findings use structured severities; `FAIL` and `BLOCK` make the general report non-OK.
2. Strict lifecycle enforcement is staged through a bounded code allow-list rather than treating every warning as a hard failure.
3. Triage and plan return explicit `PASS` or `BLOCK` result statuses and expose warning/failure counts.
4. Time-budget age alone is observed as a warning signal in the inspected lifecycle path, not as an unconditional hard failure.
5. Post-merge handoff checks produce named states and next actions, including successor-package refresh requirements.
6. Successor-package validation requires a PASS validation report, a supported execution-contract kind, required rule identifiers and acceptable generated-head freshness.
7. Protected handoff/governance changes are routed through protected-diff planning according to the generated execution contract and transfer workflow.
8. The repository CI workflow runs on pushes and pull requests to `main` and on manual dispatch.
9. CI uses Python 3.13 and runs three top-level stages: Ruff, the complete pytest suite, and CLI smoke checks.
10. The CI YAML does not enumerate individual documentation lifecycle commands as separate workflow steps; their enforcement is therefore represented through tests, invoked wrappers or other workflows not separately listed in this file.
11. No projection-specific required check, strict projection mode or source/target/contract drift gate exists in the inspected CI recipe.

## Limitations and unresolved questions

- GitHub branch-protection and required-check configuration was not available as repository content and is not inferred.
- This record does not prove that every locally documented standard gate is a GitHub required check.
- It does not determine the future severity-to-gate mapping for DPA findings.
- Additional workflows may exist outside the inspected primary CI file.

## Related assumptions

- A-004 — lifecycle finding and gate structures.
- A-005 — workflow and integration enforcement.

## Later Probe or Assessment obligation

After DPA-500 defines staged projection enforcement, verify the exact CLI-to-CI wiring, required-check behavior and warning/failure mapping for projection freshness and drift.

## No-generalization note

`VERIFIED` applies only to the inspected gate mappings and CI recipe at the exact validation ref. This record is evidence, not a future gate-policy decision.
