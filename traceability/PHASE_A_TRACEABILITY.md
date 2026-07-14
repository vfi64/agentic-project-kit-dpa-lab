# Phase A Traceability

Status: active
Status-date: 2026-07-14
Scope: architecture planning only; no implementation is claimed complete.

## Classification legend

- `NORMATIVE`: adopted requirement in the lab specification.
- `PLANNED`: future specification, DP slice, test, gate or evidence obligation.
- `VERIFIED`: exact main-repository evidence exists at the recorded ref.
- `NEEDS_MAIN_REPO_VALIDATION`: must be checked against fresh `origin/main` before implementation.

## Motivation-to-requirement matrix

| Motivation | Invariant / requirement | Decision | Specification | Planned implementation | Planned verification | Rollback obligation |
|---|---|---|---|---|---|---|
| A valid later section can coexist with stale leading content. | Projection freshness is derivational; consumers and target ownership must be explicit. | DPA-ADR-001, DPA-ADR-004 | DPA-000 §§2, 8–10; DPA-100 §§5, 7 | DP1 reader/writer/authority graph; DP2 first projection | Reproduce target from declared sources; consumer-order tests | Restore prior manual target and registry entry without losing history |
| Marker presence does not prove semantic currency. | Expected bytes must derive from declared sources and a static renderer. | DPA-ADR-003, DPA-ADR-005 | DPA-000 §§6–10; DPA-100 §§5–7 | DP1 proof renderer; DP2 lifecycle integration | Golden output, undeclared-input and unknown-renderer tests | Disable projection contract; preserve prior lifecycle behavior |
| Local locks do not serialize branches or PRs. | Local mutation locking and workflow serialization are separate responsibilities. | DPA-ADR-003, DPA-ADR-006 | DPA-000 §§6.4–6.5, 11; DPA-100 §§8–9 | DP1 evidence; DP2 local write guard; DP3/DP5 cross-PR rollout | Base/source/target/contract drift tests and merge-time revalidation | Block refresh, regenerate from fresh main, never merge historical prose automatically |
| A migration could accidentally invent a new authority source. | Evidence and historical prose are not runtime authority; no convenience history store. | DPA-ADR-001, DPA-ADR-002, DPA-ADR-007 | DPA-000 §§5, 8, 12; DPA-100 §§4–5 | DP1 authority discovery; DP4 conditional status migration | Authority graph review; negative tests for evidence-as-input | Revert to prior authoritative sources and manual document form |
| Registry extensibility could become arbitrary plugin execution. | Projection contracts are declarative; renderer identifiers resolve statically and fail loud. | DPA-ADR-005 | DPA-000 §§6.2–6.3, 13–14; DPA-100 §§5–6 | DP1 schema probe; DP2 static resolver | Schema compatibility, unknown identifier and dynamic-import prohibition tests | Remove optional projection block; retain backward-compatible manual path |
| Time-based checks may create false hard failures. | Wall-clock age alone cannot cause a hard fail. | DPA-ADR-008 | DPA-000 §§5, 10; DPA-100 §7.9 | DP5 staged gate adoption | Warn-mode and strict-mode policy tests | Return projection findings to warn/non-blocking mode |

## Invariant traceability

| ID | NORMATIVE invariant | Primary specification | Later specification owner | Planned DP slice | Planned evidence / tests |
|---|---|---|---|---|---|
| INV-01 | Canonical state does not own rendering logic. | DPA-000 §7.1 | DPA-200, DPA-400 | DP1–DP2 | Authority graph; renderer boundary tests |
| INV-02 | Renderers return text or bytes and never write. | DPA-000 §7.2–7.3 | DPA-400 | DP1–DP2 | Mutation-negative tests; pure-render tests |
| INV-03 | Existing lifecycle validates, plans, locks and writes. | DPA-000 §7.4 | DPA-300 | DP1–DP2 | Lifecycle integration evidence; dry-run/write tests |
| INV-04 | Workflow orchestration serializes across branches and PRs. | DPA-000 §7.5 | DPA-600 | DP1, DP3, DP5 | Competing-PR and stale-plan scenarios |
| INV-05 | Registry contracts do not name arbitrary imports. | DPA-000 §7.6–7.7 | DPA-300, DPA-400 | DP1–DP2 | Schema validation; static resolver tests |
| INV-06 | One renderer computes one target and triggers no renderer. | DPA-000 §7.8–7.9 | DPA-400 | DP1–DP2 | Call-graph and nested-render rejection tests |
| INV-07 | Evidence is not runtime authority. | DPA-000 §7.10 | DPA-200, DPA-300 | DP1–DP5 | Authority graph; evidence-input prohibition test |
| INV-08 | No parallel governance subsystem is introduced. | DPA-000 §7.11–7.12 | DPA-200–DPA-900 | DP1–DP5 | Architecture review and main-repo integration diff |
| INV-09 | Time alone does not hard-fail. | DPA-000 §7.13 | DPA-500 | DP5 | Temporal warning and non-blocking tests |
| INV-10 | Historical prose is not auto-merged on drift. | DPA-000 §7.14 | DPA-600, DPA-700 | DP3–DP4 | Drift conflict and rollback scenarios |
| INV-11 | Mutation defaults to dry-run. | DPA-000 §7.15 | DPA-300 | DP2 | CLI default and no-write tests |
| INV-12 | Production paths resolve through existing Workspace. | DPA-000 §7.16 | DPA-300 | DP1–DP2 | Fresh-main Workspace inspection and path tests |
| INV-13 | Repository-specific claims require exact evidence. | DPA-000 §7.17 | all | DP1 | Repo-fact records with exact refs and reproduction steps |

## Decision traceability

| Decision | Status | Normative effect | Affected specifications | Affected DP slices |
|---|---|---|---|---|
| DPA-ADR-001 | ACCEPTED | Extend existing document-management system only. | DPA-000–DPA-900 | DP1–DP5 |
| DPA-ADR-002 | ACCEPTED | Lab is planning authority, never production runtime authority. | all lab governance and specs | DP1–DP5 |
| DPA-ADR-003 | ACCEPTED | Renderer/lifecycle/workflow responsibility boundary. | DPA-000, DPA-100, DPA-300, DPA-400, DPA-600 | DP1–DP5 |
| DPA-ADR-004 | ACCEPTED | Freshness means reproducibility from declared authority, not age. | DPA-000, DPA-100, DPA-500 | DP1, DP2, DP5 |
| DPA-ADR-005 | ACCEPTED | Renderer resolution is static and fail-loud. | DPA-000, DPA-100, DPA-300, DPA-400 | DP1–DP2 |
| DPA-ADR-006 | ACCEPTED | Local locking and cross-ref serialization are distinct. | DPA-000, DPA-100, DPA-600 | DP1, DP3, DP5 |
| DPA-ADR-007 | ACCEPTED | No new canonical history source for migration convenience. | DPA-000, DPA-100, DPA-700 | DP1, DP4 |
| DPA-ADR-008 | ACCEPTED | Time alone cannot create a hard gate failure. | DPA-000, DPA-100, DPA-500 | DP5 |

## Main-repository evidence boundary

| Fact | Recorded status | Recorded ref | Reproduction source | Fresh validation owner |
|---|---|---|---|---|
| Existing integrated registry/lifecycle/freshness/workspace/gate stack | VERIFIED at recorded baseline | `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` and `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d` | `MAIN_REPOSITORY_CONTEXT.md` | DP1 |
| Optional projection block is schema-compatible | NEEDS_MAIN_REPO_VALIDATION | none | Run actual parser and validator | DP1 |
| Candidate handoff documents and their authority forms | NEEDS_MAIN_REPO_VALIDATION | none | Complete reader/writer/source graph | DP1 |
| Existing lifecycle findings can absorb projection drift | NEEDS_MAIN_REPO_VALIDATION | none | Inspect implementation and standard gates | DP1 |
| Existing workflows can enforce cross-PR stale-plan guards | NEEDS_MAIN_REPO_VALIDATION | none | Inspect refresh and pre-merge workflows | DP1 / DPA-600 |

## Phase A completion mapping

| Exit criterion | Evidence in branch | State |
|---|---|---|
| Terminology internally coherent | DPA-100 | REVIEW-READY, pending external review |
| No hidden parallel system implied | DPA-000 invariants; ADR-001; this matrix | SATISFIED FOR INTERNAL BASELINE |
| Main-repository claims classified | DPA-000 §16; DPA-100 §15; assumptions table | SATISFIED FOR INTERNAL BASELINE |
| Claude, ChatGPT and Gemini review prompts exist or are planned | Claude prompt to be committed; ChatGPT and Gemini prompts recorded as planned | PARTIAL |
| Accepted decisions recorded | `DECISIONS.md` | SATISFIED FOR INTERNAL BASELINE |

Phase A MUST NOT be marked stable until required model reviews are collected and adjudicated.