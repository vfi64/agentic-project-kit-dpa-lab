# Phase A Traceability Baseline

Status: active
Status-date: 2026-07-14

This artifact records planning traceability. It does not claim completed implementation in `vfi64/agentic-project-kit`.

| Motivation / goal | Normative anchors | Decision | Planned DP slice | Required validation | Planned tests / gates | Evidence / rollback |
|---|---|---|---|---|---|---|
| `DPA-GOAL-001` deterministic registered projections | DPA-000 §§3, 6.2, 11; DPA-100 §§4, 6 | DPA-ADR-003 | DP1, DP2 | Fresh reader/writer/source graph and renderer proof | Determinism, idempotence, unknown-renderer failure | Exact ref, source hashes, target hash; disable contract and restore target |
| `DPA-GOAL-002` reuse existing document management | DPA-000 §§1, 5, 6.1, 6.3 | DPA-ADR-001 | DP1–DP5 | Registry, lifecycle, freshness, Workspace and gate inspection | Existing audit and standard-gate integration | Import only approved contracts; remove optional projection metadata on rollback |
| `DPA-GOAL-003` explicit authority boundaries | DPA-000 §§3, 6.1; DPA-100 §3 | DPA-ADR-002 | DP1, DP4 | Identify actual canonical authority for each candidate | Authority and missing-source negative tests | Exact-ref authority record; no migration where authority is unresolved |
| `DPA-GOAL-004` pure renderers and lifecycle-owned writes | DPA-000 §§6.2–6.3; DPA-100 §§4.3–4.5 | DPA-ADR-003 | DP1, DP2 | Verify lifecycle mutation boundary and static resolver integration | Renderer purity, dry-run, mutation-lock coverage | Reproducible output and protected diff; rollback renderer registration |
| `DPA-GOAL-005` freshness and fail-loud drift detection | DPA-000 §6.4; DPA-100 §6 | pending detailed DPA-500 decision | DP2, DP5 | Inspect lifecycle finding model and gate semantics | Source/target/contract drift and unverifiable-state tests | Finding evidence; staged warn/block rollback |
| `DPA-GOAL-006` branch and PR serialization | DPA-000 §6.5; DPA-100 §7 | pending DPA-600 decision | DP1, DP3 | Inspect current refresh workflows and remote guards | Stale-base, competing-PR and regeneration tests | Base SHA and hashes; block/regenerate, never prose merge |
| `DPA-GOAL-007` evidence-driven reversible migration | DPA-000 §§6.6, 9; DPA-100 §5 | pending DPA-700 decision | DP1–DP4 | Classify each candidate as full, split, managed-head or no migration | Migration and rollback fixtures | Pre-migration target snapshot and explicit reversal plan |
| `DPA-GOAL-008` implementation-ready DP1–DP5 | DPA-000 §§4, 11; LAB_EXECUTION_CONTRACT §16 | later DPA-800 decisions | DP1–DP5 | Fresh main validation checklist complete | Focused tests, docs audit, lifecycle audit, standard gates | Per-slice exact-ref evidence and rollback record |

## Classification

- Normative architecture: DPA-000 and DPA-100.
- Planned implementation: DP1–DP5 entries above.
- Verified implementation: none asserted by this artifact.
- Main-repository facts: remain `NEEDS_MAIN_REPO_VALIDATION` except the recorded baseline in `MAIN_REPOSITORY_CONTEXT.md`.

## Maintenance rule

Every accepted architecture change MUST update this table when it changes a goal, invariant, decision, DP slice, validation requirement, test/gate expectation, evidence requirement or rollback path.
