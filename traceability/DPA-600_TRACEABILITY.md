# DPA-600 Traceability

Status: draft
Status-date: 2026-07-18
Normative-owner: `specs/dpa/DPA-600-CONCURRENCY.md`

This file is derived traceability. It does not own or redefine normative meaning.

| ID | DPA-600 anchor | Canonical invariants | Decisions | Earlier contract dependency | Planned validation | Gate / integration consequence | Evidence obligation | Rollback obligation | Main-repository status |
|---|---|---|---|---|---|---|---|---|---|
| C600-001 | §4 concurrency domains | DPA-INV-002, DPA-INV-004, DPA-INV-005, DPA-INV-012 | ADR-003, ADR-006 | DPA-300 §§4,7,10; DPA-400 §§3–4 | Authority-boundary negative tests | Reject renderer/workflow target writes | Domain and caller identity | Leave target and lifecycle state unchanged | NEEDS_MAIN_REPO_VALIDATION |
| C600-002 | §5 local Workspace lock | DPA-INV-004, DPA-INV-015, DPA-INV-016 | ADR-006, ADR-016 | DPA-300 §§7,10,13 | Cross-process exclusion; acquisition/release failure | Failure before Write | Lock scope, owner, acquisition and release | No target or acceptance-state mutation before Write | NEEDS_MAIN_REPO_VALIDATION |
| C600-003 | §6 same-process reentrancy | DPA-INV-004, DPA-INV-005, DPA-INV-012 | ADR-006, ADR-016 | DPA-300 §10.1 and §13 | Same-instance reentrancy; cross-target rejection; balanced release | Fail closed on ambiguous identity or release count | Process, refresh, target and release identities | Interrupted-instance disposition before retry | NEEDS_MAIN_REPO_VALIDATION |
| C600-004 | §7 guard domains | DPA-INV-004, DPA-INV-005, DPA-INV-017 | ADR-004, ADR-006, ADR-019, ADR-021 | DPA-100 §7.5; DPA-300 §§8–9,12; DPA-500 §§5,10 | Independent and simultaneous guard mismatch tests | Mutation and integration failure for mandatory mismatch | Expected and observed identity/fingerprint per guard | Regenerate from current authoritative inputs | NEEDS_MAIN_REPO_VALIDATION |
| C600-005 | §8 plan lifecycle across refs | DPA-INV-004, DPA-INV-005, DPA-INV-015 | ADR-003, ADR-006 | DPA-300 §§8–11; DPA-500 §15 | Pre-lock, under-lock and integration-time stale-plan tests | Reject stale or unverifiable plans | Plan identity, validation ref and all revalidation results | Protected ref unchanged; new plan required | NEEDS_MAIN_REPO_VALIDATION |
| C600-006 | §9 branch concurrency | DPA-INV-005, DPA-INV-012, DPA-INV-014 | ADR-006, ADR-007 | DPA-200 §§5,11,13; DPA-300 §9 | Competing branches with source, target and ownership changes | Require revalidation or regeneration | Branch refs and changed guard domains | No textual merge of generated or historical bytes | NEEDS_MAIN_REPO_VALIDATION |
| C600-007 | §10 pull-request concurrency | DPA-INV-005, DPA-INV-012 | ADR-006 | DPA-000 §11; DPA-500 §15.5 | Competing PR ordering and obsolete green-result tests | Block integration after guard-context change | PR, base, head and integration-ref identities | Protected ref unchanged on rejection | NEEDS_MAIN_REPO_VALIDATION |
| C600-008 | §11 stale-plan rejection | DPA-INV-004, DPA-INV-005, DPA-INV-013, DPA-INV-015 | ADR-004, ADR-006, ADR-008 | DPA-300 §9; DPA-500 §§13,15 | Unknown guard, missing context and time-only tests | Mandatory failure; time alone non-blocking | Exact stale or unavailable guard set | Preserve current target; regenerate | NEEDS_MAIN_REPO_VALIDATION |
| C600-009 | §12 regeneration after drift | DPA-INV-002, DPA-INV-004, DPA-INV-014 | ADR-003, ADR-006, ADR-007 | DPA-300 §§7–9; DPA-400 §§6–13 | New exact-ref plan; no payload/prose merge | Only regenerated current plan may proceed | Link rejected and regenerated attempts | Preserve non-owned bytes; no authority reconstruction | NEEDS_MAIN_REPO_VALIDATION |
| C600-010 | §13 renderer-derived plans | DPA-INV-002, DPA-INV-003, DPA-INV-007, DPA-INV-008 | ADR-003, ADR-005, ADR-019 | DPA-400 §§5–13 | Renderer identity/version and immutable-input drift tests | Invalidate affected plan | Renderer identity, semantic version and implementation evidence | Regenerate; adjudicate unversioned semantic change | NEEDS_MAIN_REPO_VALIDATION |
| C600-011 | §14 acceptance and re-acceptance | DPA-INV-004, DPA-INV-005, DPA-INV-010 | ADR-016, ADR-021 | DPA-300 §§12–16; DPA-500 §§8–9,15.6 | Cross-ref accepted-state and gate-set-only re-acceptance tests | Workflow may sequence but not assign acceptance | Accepted scope, gate-set and ref comparisons | Prior accepted record preserved on failed re-acceptance | NEEDS_MAIN_REPO_VALIDATION |
| C600-012 | §15 recovery interaction | DPA-INV-004, DPA-INV-005, DPA-INV-010 | ADR-016, ADR-021 | DPA-300 §13; DPA-500 §18 | Interrupted Write/Record/Release and integration blocking | Unresolved recovery is non-integrable | Recovery disposition and post-recovery revalidation | Lifecycle recovery before workflow continuation | NEEDS_MAIN_REPO_VALIDATION |
| C600-013 | §16 fail-loud behavior | DPA-INV-004, DPA-INV-005, DPA-INV-012, DPA-INV-014 | ADR-006, ADR-007 | DPA-300 §17; DPA-500 §§12–13 | Negative tests for every mandatory uncertainty class | Failure for mutation, acceptance and integration | Structured bounded failure context | No silent fallback or merge | NEEDS_MAIN_REPO_VALIDATION |
| C600-014 | §17 evidence | DPA-INV-010, DPA-INV-017 | ADR-002, ADR-011 | DPA-300 §14; DPA-500 §19 | Evidence completeness and non-authority tests | Missing evidence cannot fabricate serialization success | Exact ref, guards, lock, workflow and disposition | Evidence does not replace rollback source | NEEDS_MAIN_REPO_VALIDATION |
| C600-015 | §18 rollback | DPA-INV-010, DPA-INV-014 | ADR-007, ADR-016 | DPA-300 §§11,13; DPA-500 §18 | Pre-Write, post-Write and incorrect-integration rollback cases | Keep protected ref unchanged or mark output non-accepted | Exact rollback ref, plan and guard identities | Governed repository rollback plus lifecycle recovery | NEEDS_MAIN_REPO_VALIDATION |

## Package A dependencies

- DPA-700 MUST consume C600-009, C600-012 and C600-015 without redefining concurrency ownership.
- DPA-800 MUST map the planned validation cases to DP1 Probe, DP2 implementation and DP3/DP5 integration work.
- PROBE-002 MUST test the local-lock, stale-plan, recovery, acceptance-state and re-acceptance rows.
- Later integration Probes MUST test branch and pull-request serialization against an exact main-repository ref.

## Classification note

Discovery evidence at `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` recorded local reentrancy and workflow guards for the inspected scope. Those observations are `VERIFIED` only for that exact historical ref. Current behavior, suitability and DPA-600 conformance remain `NEEDS_MAIN_REPO_VALIDATION`.
