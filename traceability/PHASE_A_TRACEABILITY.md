# Phase A Traceability

Status: active
Status-date: 2026-07-15
Scope: architecture planning and adjudication only; no main-repository implementation is claimed complete.

## Vocabulary dimensions

- Classification: `NORMATIVE`, `VERIFIED`, `VERIFIED_AT_RECORDED_BASELINE`, `ASSUMPTION`, `PROPOSAL`, `REJECTED`, `NEEDS_MAIN_REPO_VALIDATION`.
- Document status: `planned`, `draft`, `review-ready`, `stable`, `adopted`, `active`.
- Progress: `pending`, `partial`, `complete`, `blocked`, `not-required`.
- Access outcome: `accessible`, `access-blocked`.

## Motivation-to-requirement matrix

| Motivation | Canonical invariant / requirement | Decision | Specification owner | Planned implementation | Planned verification | Rollback obligation | Review origin |
|---|---|---|---|---|---|---|---|
| Stale leading content can coexist with a valid later section. | DPA-INV-001, DPA-INV-004, DPA-INV-017; explicit target and consumer trust boundary. | ADR-001, ADR-004 | DPA-200, DPA-300, DPA-500 | DP1 graph; DP2 first projection | Reproduction and consumer-order tests | Restore prior manual target and registry entry | Original baseline; TVA-m03 |
| Marker presence does not prove semantic currency. | DPA-INV-003, DPA-INV-006, DPA-INV-007. | ADR-003, ADR-005 | DPA-300, DPA-400, DPA-500 | DP1 renderer proof; DP2 integration | Golden output, undeclared-input and unknown-renderer tests | Disable projection contract | Original baseline |
| Local locks do not serialize branches or PRs. | DPA-INV-004, DPA-INV-005. | ADR-003, ADR-006 | DPA-600 | DP1 evidence; DP3/DP5 rollout | Base/source/target/contract drift tests | Block and regenerate from validation ref | Original baseline; Claude |
| Migration may invent a new authority source. | DPA-INV-010, DPA-INV-011, DPA-INV-014. | ADR-001, ADR-002, ADR-007 | DPA-200, DPA-700 | DP1 authority discovery; DP4 migration | Authority graph; evidence-as-input negative tests | Revert to prior authoritative sources and manual form | Original baseline |
| Registry metadata could become arbitrary plugin execution. | DPA-INV-006, DPA-INV-007. | ADR-005 | DPA-300, DPA-400 | DP1 schema probe; DP2 resolver | Schema and dynamic-import prohibition tests | Remove optional projection block | Original baseline |
| Time-based checks may create false hard failures. | DPA-INV-013. | ADR-008 | DPA-500 | DP5 staged gate adoption | Warn/block policy tests | Return findings to non-blocking mode | Original baseline |
| Mutation execution may be implicit. | DPA-INV-015. | ADR-003 | DPA-300 | DP2 lifecycle integration | Dry-run default and no-write tests | Retain manual target | Claude traceability gap |
| Manual documents must remain usable. | Compatibility requirement; DPA-INV-012. | ADR-001, ADR-005 | DPA-200, DPA-300 | DP1 compatibility; DP2 projection | Manual-document regression tests | Remove optional contract and restore target | Claude traceability gap |
| Rendered bytes may be consumed before validation. | Consumer trust boundary; DPA-INV-004. | ADR-003; later DPA-500 decision | DPA-200, DPA-500 | DP2–DP5 | Pre-validation and failed-gate tests | Discard unvalidated output | Claude; TVA-m03 |
| Rollback can depend on unavailable history. | DPA-INV-014 and reversibility requirement. | ADR-007 | DPA-700 | DP2–DP4 | Rollback from tracked pre-migration state | No rollout without recoverable inputs | Claude |

## Canonical invariant traceability

| Canonical ID | Condensed invariant | Decision links | Later specification owner | Planned DP slices | Planned evidence / tests |
|---|---|---|---|---|---|
| DPA-INV-001 | Canonical state owns no rendering logic. | ADR-002, ADR-003 | DPA-200, DPA-400 | DP1–DP2 | Authority graph; renderer-boundary tests |
| DPA-INV-002 | Renderers own no write logic. | ADR-003 | DPA-400 | DP1–DP2 | Mutation-negative tests |
| DPA-INV-003 | Renderers return text or bytes only. | ADR-003 | DPA-400 | DP1–DP2 | Pure-render and type-boundary tests |
| DPA-INV-004 | Lifecycle validates, plans, locks and writes. | ADR-003 | DPA-300 | DP1–DP2 | Lifecycle integration; dry-run/write tests |
| DPA-INV-005 | Workflow orchestration serializes across refs. | ADR-006 | DPA-600 | DP1, DP3, DP5 | Competing-PR and stale-plan scenarios |
| DPA-INV-006 | Registry contracts are declarative, not plugins. | ADR-005 | DPA-300, DPA-400 | DP1–DP2 | Schema validation; dynamic-import prohibition |
| DPA-INV-007 | Renderer resolution is static and reviewed. | ADR-005 | DPA-400 | DP1–DP2 | Unknown-ID and static-map tests |
| DPA-INV-008 | One invocation computes one target. | ADR-003, ADR-005 | DPA-400 | DP1–DP2 | Single-target tests |
| DPA-INV-009 | Renderers do not trigger renderers. | ADR-003 | DPA-400 | DP1–DP2 | Call-graph rejection tests |
| DPA-INV-010 | Evidence is not runtime authority. | ADR-002, ADR-007, ADR-011 | DPA-200, DPA-300 | DP1–DP5 | Evidence-input prohibition tests |
| DPA-INV-011 | Runtime projection contracts live only in the main repository's existing system. | ADR-001 | DPA-300 | DP1–DP5 | Integration map at validation ref |
| DPA-INV-012 | No parallel registry/lifecycle/freshness/evidence/Workspace/gate subsystem. | ADR-001 | DPA-200–DPA-900 | DP1–DP5 | Architecture review and implementation diff |
| DPA-INV-013 | Time alone does not hard-fail. | ADR-008 | DPA-500 | DP5 | Temporal warning and non-blocking tests |
| DPA-INV-014 | Historical prose is not auto-merged. | ADR-007 | DPA-600, DPA-700 | DP2–DP4 conditional on DP1 form | Drift conflict and rollback tests |
| DPA-INV-015 | Mutation defaults to dry-run. | ADR-003 | DPA-300 | DP2 | CLI default and no-write tests |
| DPA-INV-016 | Production paths resolve through Workspace. | ADR-001 | DPA-300 | DP1–DP2 | Workspace API and path tests |
| DPA-INV-017 | Repository-specific behavior requires exact validation-ref evidence. | ADR-009, ADR-011 | all | DP1 | Repo-fact records and reproduction steps |

## Review finding disposition

| Finding | Source verdict | Adjudicated disposition | Decision / owner | Progress |
|---|---|---|---|---|
| F-M01 | Claude ACCEPT; TVA VERIFIED | ACCEPTED | ADR-009; DPA-100 | complete |
| F-M02 | Claude ACCEPT; TVA VERIFIED | ACCEPTED | ADR-010; DPA-000 | complete |
| F-M03 | Claude ACCEPT; TVA VERIFIED with severity clarification | ACCEPTED as governance/evidence defect, not architecture defect | ADR-011 | complete |
| F-m01 | VERIFIED | ACCEPTED | LEC §9 owns phase exits | complete |
| F-m02 | VERIFIED | ACCEPTED editorially | DPA-100 authority wording; governance cleanup | partial |
| F-m03 | VERIFIED | ACCEPTED | this one-to-one table | complete |
| F-m04 | VERIFIED | ACCEPTED | DPA-100 validation ref | complete |
| F-m05 | VERIFIED | ACCEPTED | DPA-100 document status | complete |
| F-m06 | PARTIALLY VERIFIED | ACCEPTED as explicit alias/containment clarification | DPA-100 | complete |
| F-m07 | VERIFIED | ACCEPTED | diagram alignment remains | pending |
| TVA-M01 | Additional | ACCEPTED | ADR-012 | complete |
| TVA-m01 | Additional | ACCEPTED | consolidated review must distinguish baseline and later planning refs | pending |
| TVA-m02 | Additional | ACCEPTED | DPA-100 access outcome vocabulary | complete |
| TVA-m03 | Additional | ACCEPTED | DPA-200/DPA-500 consumer trust boundary | planned |

## Decision traceability

| Decision | Status | Effect | Review origin |
|---|---|---|---|
| ADR-001–ADR-008 | ACCEPTED | Foundation architecture | Original Phase A baseline |
| ADR-009 | ACCEPTED | Separates classification, document status, progress and access outcome | Claude F-M01; TVA |
| ADR-010 | ACCEPTED | DPA-000 owns stable invariant IDs | Claude F-M02; TVA |
| ADR-011 | ACCEPTED | Minimal static evidence bar for recorded baselines | Claude F-M03; TVA |
| ADR-012 | ACCEPTED | Role-based review governance | TVA-M01; Gemini access experience |

## Main-repository evidence boundary

| Fact | Classification | Recorded ref | Evidence record | Validation owner |
|---|---|---|---|---|
| Administrative handoff baseline after PR #1863 | VERIFIED_AT_RECORDED_BASELINE | `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` | `evidence/repo-facts/BASELINE-6A9DA7D-HANDOFF-REFRESH.md` | DP1 revalidation |
| Substantive post-L5 lifecycle-evidence baseline | VERIFIED_AT_RECORDED_BASELINE | `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d` | `evidence/repo-facts/BASELINE-5D4EA12-POST-L5-LIFECYCLE.md` | DP1 revalidation |
| Optional projection block compatibility | NEEDS_MAIN_REPO_VALIDATION | none | actual parser/validator evidence required | DP1 |
| Candidate authority and reader/writer graphs | NEEDS_MAIN_REPO_VALIDATION | none | exact source graph required | DP1 |
| Lifecycle/gate absorption of projection findings | NEEDS_MAIN_REPO_VALIDATION | none | implementation and gate mapping required | DP1 |
| Cross-PR stale-plan mechanism | NEEDS_MAIN_REPO_VALIDATION | none | workflow inspection required | DP1 / DPA-600 |

## Phase A exit tracking

The normative owner is LAB_EXECUTION_CONTRACT §9.

| Exit criterion | Evidence | Progress |
|---|---|---|
| DPA-000 and DPA-100 review-ready | current branch | complete |
| Terminology and invariant references coherent | ADR-009/010; DPA-000; DPA-100; this artifact | complete |
| No hidden parallel subsystem or runtime authority | Claude review; TVA | complete |
| Repository claims correctly classified | ADR-009/011; evidence records | complete |
| Initial one-to-one traceability | this artifact | complete |
| Primary architecture review | Claude review | complete |
| Secondary technical verification | ChatGPT TVA | complete |
| Maintainer adjudication | ADR-009 through ADR-012 accepted | complete |
| Accepted normative changes synchronized | core normative files updated | partial |
| No unresolved Phase A blocker hidden in prose | final consolidated review and cleanup required | pending |

Phase A remains `review-ready`, not `stable`, until the consolidated adjudication record, remaining governance/diagram cleanup and final consistency check are complete.
