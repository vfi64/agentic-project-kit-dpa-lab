# DP1 Discovery Record — DISC-005 Lifecycle Findings

Status: active
Classification: VERIFIED
Inspection date: 2026-07-15
Fact family: DISC-005
Repository: `vfi64/agentic-project-kit`
Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

## Factual question

Which structured documentation-lifecycle findings, severities, producers and result mappings exist at the validation ref?

## Inspected paths and symbols

- `src/agentic_project_kit/doc_lifecycle.py`
  - `DocLifecycleFinding`
  - `DocLifecycleReport.ok`
  - `STRICT_BLOCKING_CODES`
  - `build_doc_lifecycle_report`
  - `build_doc_lifecycle_strict_findings`
  - `build_doc_lifecycle_triage_payload`
  - `build_doc_lifecycle_plan_payload`
- `src/agentic_project_kit/doc_lifecycle_signals.py`
- documentation-registry reconciliation inputs consumed by the lifecycle report

## Observed result

1. A lifecycle finding is a structured value with `code`, `path`, `message`, `severity`, optional document class and optional age in days.
2. The general report treats severities `FAIL` and `BLOCK` as non-OK; other severities do not make `DocLifecycleReport.ok` false.
3. Observed finding codes include `HEADER_REGISTRY_MISMATCH`, `SUPERSEDED_TARGET_MISSING`, `STALE_BY_BUDGET`, `REVIEW_DUE_RELEASE`, `REVIEW_DUE_DIRECTION` and `SOURCE_OF_CLOSED_ITEM_STILL_ACTIVE`, plus header/status findings emitted by the document audit path.
4. Time-budget findings such as `STALE_BY_BUDGET` are emitted as `WARN` in the inspected path.
5. Header/registry mismatch and missing supersession targets are also emitted as `WARN` by the general report.
6. `STRICT_BLOCKING_CODES` identifies a bounded subset for strict lifecycle enforcement. Strict findings are returned separately rather than changing every warning globally.
7. The triage payload normalizes lifecycle findings into `WARN` or `FAIL`, counts both, emits proposed actions, and returns `BLOCK` only when failures are present.
8. The plan payload remains dry-run and assigns safety classes `no-op-confirmation`, `advisory` or `human-decision-required`; a blocking triage produces a blocking plan only when human-decision-required steps are present.
9. Finding consumers observed in this path are rendered lifecycle reports, strict lifecycle blockers, triage, plan and downstream CLI/gate invocation. This record does not assert the complete repository-wide consumer graph.
10. No projection-specific source-, target-, base- or contract-drift finding identifiers exist in the inspected lifecycle vocabulary.

## Limitations and unresolved questions

- This record does not enumerate every finding code outside the documentation lifecycle.
- It does not determine whether existing fields or severity mapping are sufficient for DPA projection drift.
- Required-check names and all CI consumers are covered separately by DISC-009.
- No production finding identifier is proposed here.

## Related assumptions

- A-004 — existing lifecycle finding structures.

## Later Probe or Assessment obligation

After DPA-300 and DPA-500 define projection findings and gate consequences, test whether the existing structured finding model can be extended without parallel reporting or incompatible severity semantics.

## No-generalization note

`VERIFIED` applies only to the inspected finding structures, codes and mappings at the exact validation ref. This record is evidence, not a sufficiency judgment or normative finding contract.
