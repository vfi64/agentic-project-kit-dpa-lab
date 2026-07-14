# Phase A Traceability

Status: active
Status-date: 2026-07-14
Scope: architecture planning only; no implementation is claimed complete.

## Classification note

The classification/status model is under adjudication through proposed DPA-ADR-009. Until that decision is accepted, this artifact avoids upgrading any recorded-baseline fact and treats review-derived work as planning only.

## Motivation-to-requirement matrix

| Motivation | Invariant / requirement | Decision | Specification | Planned implementation | Planned verification | Rollback obligation | Review origin |
|---|---|---|---|---|---|---|---|
| A valid later section can coexist with stale leading content. | Projection freshness is derivational; consumers and target ownership must be explicit. | DPA-ADR-001, DPA-ADR-004 | DPA-000 §§2, 8–10; DPA-100 §§5, 7 | DP1 reader/writer/authority graph; DP2 first projection | Reproduce target from declared sources; consumer-order tests | Restore prior manual target and registry entry without losing history | Original Phase A baseline |
| Marker presence does not prove semantic currency. | Expected bytes must derive from declared sources and a static renderer. | DPA-ADR-003, DPA-ADR-005 | DPA-000 §§6–10; DPA-100 §§5–7 | DP1 proof renderer; DP2 lifecycle integration | Golden output, undeclared-input and unknown-renderer tests | Disable projection contract; preserve prior lifecycle behavior | Original Phase A baseline |
| Local locks do not serialize branches or PRs. | Local mutation locking and workflow serialization are separate responsibilities. | DPA-ADR-003, DPA-ADR-006 | DPA-000 §§6.4–6.5, 11; DPA-100 §§8–9 | DP1 evidence; DP2 local write guard; DP3/DP5 cross-PR rollout | Base/source/target/contract drift tests and merge-time revalidation | Block refresh, regenerate from a validation ref, never merge historical prose automatically | Original Phase A baseline; Claude §9/§11 |
| A migration could accidentally invent a new authority source. | Evidence and historical prose are not runtime authority; no convenience history store. | DPA-ADR-001, DPA-ADR-002, DPA-ADR-007 | DPA-000 §§5, 8, 12; DPA-100 §§4–5 | DP1 authority discovery; DP4 conditional status migration | Authority graph review; negative tests for evidence-as-input | Revert to prior authoritative sources and manual document form | Original Phase A baseline |
| Registry extensibility could become arbitrary plugin execution. | Projection contracts are declarative; renderer identifiers resolve statically and fail loud. | DPA-ADR-005 | DPA-000 §§6.2–6.3, 13–14; DPA-100 §§5–6 | DP1 schema probe; DP2 static resolver | Schema compatibility, unknown identifier and dynamic-import prohibition tests | Remove optional projection block; retain backward-compatible manual path | Original Phase A baseline |
| Time-based checks may create false hard failures. | Wall-clock age alone cannot cause a hard fail. | DPA-ADR-008 | DPA-000 §§5, 10; DPA-100 §7.9 | DP5 staged gate adoption | Warn-mode and strict-mode policy tests | Return projection findings to warn/non-blocking mode | Original Phase A baseline |
| Mutation commands can damage documents when execution is implicit. | Mutation-capable operations default to dry-run and require governed authorization to write. | DPA-ADR-003 | DPA-000 lifecycle boundary; DPA-100 mutation terms | DP2 lifecycle integration | CLI default, no-write and explicit-execution tests | Retain manual target and disable projection mutation | Claude §9 traceability gap |
| Existing manual documents must remain usable during staged adoption. | Optional projection metadata and fail-loud projection handling must preserve the manual path for non-projected documents. | DPA-ADR-001, DPA-ADR-005 | DPA-200, DPA-300 | DP1 compatibility proof; DP2 first projection | Registry compatibility and manual-document regression tests | Remove optional projection contract and restore prior target | Claude §9 traceability gap |
| Rendered bytes may be consumed before validation or merge gates run. | Unvalidated output must not be represented as accepted repository state; consumer assumptions and gate placement must be explicit. | pending DPA-500 decision | DPA-200, DPA-500 | DP2–DP5 | branch-local consumption, failed-validation and pre-merge gate tests | Discard unvalidated output and restore tracked target | Claude §11 failure-mode audit |
| Rollback can fail if it depends on a newly invented or unavailable history source. | Rollback inputs must be recoverable from Git history or another already-authoritative source. | DPA-ADR-007; pending DPA-700 decision | DPA-700 | DP2–DP4 | rollback fixture from tracked pre-migration state | No rollout where recoverability cannot be proven | Claude §9/§11 |

## Review-finding traceability

| Finding | Severity | Planning owner | Proposed decision | Later spec owner | Planned DP slices | Tests / evidence | State |
|---|---|---|---|---|---|---|---|
| F-M01 | MAJOR | consolidated adjudication | ADR-009 | DPA-100 and governance | DP1–DP5 classification use | vocabulary consistency and transition audit | MAINTAINER_DECISION |
| F-M02 | MAJOR | consolidated adjudication | ADR-010 | DPA-000 / LEC ownership | DP1–DP5 | one-to-one invariant reference audit | MAINTAINER_DECISION |
| F-M03 | MAJOR | evidence planning | ADR-011 or ADR-009 scope | DPA-800 entry evidence | DP1 | exact-ref minimal repo-fact records | MAINTAINER_DECISION |
| F-m01 | MINOR | phase governance | no new ADR required unless ownership is disputed | LEC §9 | n/a | single-owner exit-criteria audit | AWAITING_REVIEWS |
| F-m02 | MINOR | terminology cleanup | editorial | governance docs | n/a | prohibited-term search | AWAITING_REVIEWS |
| F-m03 | MINOR | traceability regeneration | ADR-010 dependency | traceability | all | Decision column and one invariant per row | BLOCKED BY F-M02 |
| F-m04 | MINOR | terminology | adjudication batch | DPA-100 | DP1 | exact validation-ref use audit | AWAITING_REVIEWS |
| F-m05 | MINOR | document-status semantics | ADR-009 dependency | DPA-100 / LEC §14 | n/a | status vocabulary audit | BLOCKED BY F-M01 |
| F-m06 | MINOR | source terminology | adjudication batch | DPA-100 / DPA-400 | DP1–DP2 | undeclared/evidence input negative tests | AWAITING_REVIEWS |
| F-m07 | MINOR | diagram maintenance | editorial | diagrams/architecture.mmd | n/a | diagram-to-model comparison | AWAITING_REVIEWS |

## Provisional invariant traceability

This table remains provisional until ADR-010 identifies the canonical invariant owner and stable IDs. The current grouped IDs MUST NOT be treated as the final invariant register.

| Provisional ID | Invariant group | Current primary reference | Decision links | Later specification owner | Planned DP slice | Planned evidence / tests |
|---|---|---|---|---|---|---|
| INV-P01 | Canonical state does not own rendering logic. | DPA-000 §7.1 | ADR-002, ADR-003 | DPA-200, DPA-400 | DP1–DP2 | Authority graph; renderer boundary tests |
| INV-P02 | Renderers return text or bytes and never write. | DPA-000 §7.2–7.3 | ADR-003 | DPA-400 | DP1–DP2 | Mutation-negative tests; pure-render tests |
| INV-P03 | Existing lifecycle validates, plans, locks and writes. | DPA-000 §7.4 | ADR-003 | DPA-300 | DP1–DP2 | Lifecycle integration evidence; dry-run/write tests |
| INV-P04 | Workflow orchestration serializes across branches and PRs. | DPA-000 §7.5 | ADR-006 | DPA-600 | DP1, DP3, DP5 | Competing-PR and stale-plan scenarios |
| INV-P05 | Registry contracts do not name arbitrary imports. | DPA-000 §7.6–7.7 | ADR-005 | DPA-300, DPA-400 | DP1–DP2 | Schema validation; static resolver tests |
| INV-P06 | One renderer computes one target and triggers no renderer. | DPA-000 §7.8–7.9 | ADR-003, ADR-005 | DPA-400 | DP1–DP2 | Call-graph and nested-render rejection tests |
| INV-P07 | Evidence is not runtime authority. | DPA-000 §7.10 | ADR-002, ADR-007 | DPA-200, DPA-300 | DP1–DP5 | Authority graph; evidence-input prohibition test |
| INV-P08 | Runtime projection contracts remain in the existing system; no parallel subsystem. | DPA-000 §7.11–7.12 | ADR-001 | DPA-200–DPA-900 | DP1–DP5 | Architecture review and main-repo integration diff |
| INV-P09 | Time alone does not hard-fail. | DPA-000 §7.13 | ADR-008 | DPA-500 | DP5 | Temporal warning and non-blocking tests |
| INV-P10 | Historical prose is not auto-merged on drift. | DPA-000 §7.14 | ADR-007 | DPA-600, DPA-700 | DP2–DP4 conditional on DP1 form | Drift conflict and rollback scenarios |
| INV-P11 | Mutation defaults to dry-run. | DPA-000 §7.15 | ADR-003 | DPA-300 | DP2 | CLI default and no-write tests |
| INV-P12 | Production paths resolve through existing Workspace. | DPA-000 §7.16 | ADR-001 | DPA-300 | DP1–DP2 | Validation-ref Workspace inspection and path tests |
| INV-P13 | Repository-specific claims require exact evidence. | DPA-000 §7.17 | proposed ADR-009/011 | all | DP1 | Repo-fact records with exact refs and reproduction steps |

## Decision traceability

| Decision | Status | Normative or planned effect | Affected specifications | Affected DP slices | Review origin |
|---|---|---|---|---|---|
| DPA-ADR-001 | ACCEPTED | Extend existing document-management system only. | DPA-000–DPA-900 | DP1–DP5 | Original baseline |
| DPA-ADR-002 | ACCEPTED | Lab is planning authority, never production runtime authority. | all lab governance and specs | DP1–DP5 | Original baseline |
| DPA-ADR-003 | ACCEPTED | Renderer/lifecycle/workflow responsibility boundary. | DPA-000, DPA-100, DPA-300, DPA-400, DPA-600 | DP1–DP5 | Original baseline |
| DPA-ADR-004 | ACCEPTED | Freshness means reproducibility from declared authority, not age. | DPA-000, DPA-100, DPA-500 | DP1, DP2, DP5 | Original baseline |
| DPA-ADR-005 | ACCEPTED | Renderer resolution is static and fail-loud. | DPA-000, DPA-100, DPA-300, DPA-400 | DP1–DP2 | Original baseline |
| DPA-ADR-006 | ACCEPTED | Local locking and cross-ref serialization are distinct. | DPA-000, DPA-100, DPA-600 | DP1, DP3, DP5 | Original baseline |
| DPA-ADR-007 | ACCEPTED | No new canonical history source for migration convenience. | DPA-000, DPA-100, DPA-700 | DP1, DP4 | Original baseline |
| DPA-ADR-008 | ACCEPTED | Time alone cannot create a hard gate failure. | DPA-000, DPA-100, DPA-500 | DP5 | Original baseline |
| DPA-ADR-009 | PROPOSAL | Close and separate classification, document-status and progress vocabularies. | governance, DPA-000, DPA-100, traceability | DP1–DP5 | Claude F-M01 |
| DPA-ADR-010 | PROPOSAL | Establish one canonical invariant register with stable IDs. | DPA-000, LEC, all later specs | DP1–DP5 | Claude F-M02 |
| DPA-ADR-011 | PROPOSAL | Set a minimal non-circular evidence bar for recorded baseline facts. | context, evidence records, DPA-800 | DP1 | Claude F-M03 |

## Main-repository evidence boundary

| Fact | Current treatment | Recorded ref | Required non-circular record | Fresh validation owner |
|---|---|---|---|---|
| Existing integrated registry/lifecycle/freshness/workspace/gate stack | Classification pending ADR-009/011; recorded baseline only | `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` and `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d` | Minimal records under `evidence/repo-facts/` if ADR-011 accepts that bar | DP1 |
| Optional projection block is schema-compatible | NEEDS_MAIN_REPO_VALIDATION | none | Run actual parser and validator | DP1 |
| Candidate handoff documents and their authority forms | NEEDS_MAIN_REPO_VALIDATION | none | Complete reader/writer/source graph | DP1 |
| Existing lifecycle findings can absorb projection drift | NEEDS_MAIN_REPO_VALIDATION | none | Inspect implementation and standard gates | DP1 |
| Existing workflows can enforce cross-PR stale-plan guards | NEEDS_MAIN_REPO_VALIDATION | none | Inspect refresh and pre-merge workflows | DP1 / DPA-600 |

## Phase A completion mapping

The normative owner of Phase A exit criteria is itself under minor-finding adjudication (F-m01). This table is a tracking view only.

| Exit criterion | Evidence in branch | Current assessment |
|---|---|---|
| DPA-000 and DPA-100 review-ready | reviewed baseline `1a73ec435a09d0367cb7e9f123241d9f61550b0f` | SATISFIED WITH CHANGES |
| Terminology internally coherent | DPA-100 plus backlog F-M01/F-m04/F-m05/F-m06 | CHANGES REQUIRED |
| No hidden parallel system implied | Claude review executive and boundary audits | SATISFIED |
| Main-repository claims classified | strong discipline, but recorded-baseline family pending ADR-009/011 | CHANGES REQUIRED |
| Initial traceability exists | this artifact | SATISFIED WITH CHANGES |
| Claude review input exists | `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md` | SATISFIED |
| ChatGPT review input exists | not yet committed against common baseline | NOT SATISFIED |
| Gemini review input exists | not yet committed against common baseline | NOT SATISFIED |
| Required findings adjudicated | backlog and proposed ADRs only | NOT SATISFIED |

Phase A MUST NOT be marked stable until the required reviews are collected, consolidated and adjudicated, accepted normative changes are applied, and traceability is regenerated against the accepted status model and invariant register.
