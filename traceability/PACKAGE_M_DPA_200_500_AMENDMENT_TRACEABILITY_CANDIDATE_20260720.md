# Package M DPA-200–DPA-500 Amendment Traceability Candidate

Status: review-candidate

Status-date: 2026-07-20

Authority: non-normative synchronized traceability candidate for the Package M amendment draft

Normative-source-candidate:

- `integration/PACKAGE_M_SYNCHRONIZED_DPA_200_500_AMENDMENT_DRAFT_20260720.md`

## 1. Boundary

This file maps the proposal-local DMA requirement groups to existing DPA authority, expected conformance evidence, Probe impact, gate consequence, recovery obligation and later normative traceability homes.

It does not create accepted requirement identifiers, amend existing DPA traceability, alter Probe identities or claim implementation conformance.

## 2. Candidate mapping

| ID | Requirement | Candidate owner | Existing authority preserved | Conformance evidence | Probe / test consequence | Gate consequence | Recovery / rollback consequence |
|---|---|---|---|---|---|---|---|
| `DMA-001` | one semantic fact has one canonical authority | DPA-200 | canonical-source and projection-authority model | authority graph; semantic-fact overlap matrix; duplicate-writer disposition | exact-ref writer inventory; conflict and ambiguity tests | unknown or duplicate authority blocks mutation and acceptance | choose one authority, compose under one operation, or deprecate/block a writer |
| `DMA-002` | generated surfaces are not normal edit sources | DPA-200 | canonical-source and historical/evidence non-authority rules | generated-artifact ownership map; direct-edit policy | direct-edit regression; emergency-repair non-acceptance test | direct repair cannot become accepted state | correct canonical source and regenerate/re-accept; preserve repair evidence |
| `DMA-003` | write ownership is distinct from command orchestration | DPA-200 / DPA-300 | lifecycle sole-writer boundary; workflow non-writer boundary | command-to-document authority map; lifecycle invocation evidence | direct-writer detection; wrapper cannot write lifecycle bytes | unauthorized lifecycle-byte write fails closed | dispose out-of-band bytes and rerun through lifecycle |
| `DMA-004` | each authority-bearing mode or independently recoverable step has one command mutation contract; subordinate helpers inherit | DPA-300 | existing command authority selected after exact-ref validation | contract-home decision; static delegation graph; helper non-bypass evidence | authority-bearing mode Probe coverage; focused helper delegation tests | unknown contract or helper broadening blocks mutation | restore owning contract boundary; independently classify only real authority-bearing steps |
| `DMA-005` | aliases are equivalent or independently classified | DPA-300 | existing command compatibility/deprecation authority | alias mapping and behavior comparison | alias equivalence and divergence cases | divergent undeclared alias fails closed | route to canonical contract, independently classify, block or remove alias |
| `DMA-006` | immutable plan binds command authority, target set, path predicates and orchestration order | DPA-300 | immutable mutation-plan authority | plan identity fields and invalidation evidence | plan invalidation for command, mode, targets, predicates, ordering and secondary effects | stale or mismatched command plan blocks Write | create a new plan from current authoritative inputs |
| `DMA-007` | actual changes conform to plan-bound authorized, required, conditional and temporary path outcomes | DPA-300 | lifecycle preflight, verification and changed-path audit surfaces | pre/post path inventory; predicate evaluation; cleanup evidence | unauthorized path, missing required path, valid no-op, residual temporary path | any violated conformance condition fails mutation | restore/disposition unauthorized or residual paths and replan |
| `DMA-008` | every secondary writer effect is declared and verified | DPA-300 | existing lifecycle/state/evidence/report ownership | secondary-effect inventory and per-effect verification | undeclared, failed and conditional secondary-effect cases | undeclared or failed effect blocks command completion | preserve partial outcomes; disposition each effect before new mutation |
| `DMA-009` | synchronized sets retain per-target lifecycle acceptance and only a derived aggregate result | DPA-300 | one-renderer/one-target; lifecycle target-scoped acceptance; workflow orchestration | source-snapshot identity; per-target results; bounded aggregate recovery record | mixed snapshot, partial completion, reuse-after-revalidation and cleanup cases | false aggregate success or mixed snapshot fails closed | lifecycle recovery per target; orchestration tracks unresolved members without aggregate acceptance state |
| `DMA-010` | renderer remains pure under generator orchestration | DPA-400 | renderer purity and lifecycle-only caller boundary | renderer invocation boundary and capability-negative evidence | generator/renderer separation; no writes, state, orchestration or aggregate decision in renderer | renderer capability violation abandons attempt | decompose or bound combined implementation; no target mutation from renderer |
| `DMA-011` | generator determinism is distinct from renderer determinism | DPA-400 | declared-input and deterministic-output contracts | command contract, source snapshot, target contracts and ordered orchestration evidence | same aggregate inputs produce same per-target and aggregate result; variable evidence normalization | unverifiable or mixed deterministic context blocks acceptance | new current plan and source snapshot; do not infer aggregate determinism from member renderers |
| `DMA-012` | command-aware projection freshness and gate consequences remain distinct from mutation-attempt failures | DPA-500 | freshness dimensions, trust-state separation, existing findings and gates | accepted contract declaring command semantics; active-operation findings | command-semantic contract drift, mixed snapshot, partial set, direct generated edit, stale reference | unsafe active operation gets gate failure without automatically staling independently fresh accepted bytes | preserve prior accepted state where still valid; remediate active command failure and re-evaluate |

## 3. Required synchronization targets

A later normative amendment must update, in one governed review unit:

- `traceability/DPA-200_TRACEABILITY.md` for `DMA-001` through `DMA-003`;
- `traceability/DPA-300_TRACEABILITY.md` for `DMA-003` through `DMA-009`;
- `traceability/DPA-400_TRACEABILITY.md` for `DMA-010` and `DMA-011`;
- `traceability/DPA-500_TRACEABILITY.md` for `DMA-012` and gate consequences inherited from DPA-300 failures;
- the corresponding architecture diagrams;
- the Probe coverage disposition, without silently changing an immutable Probe identity.

## 4. Review checks

Independent review must confirm:

1. no row establishes a second registry, command registry, lifecycle, state store, finding service, evidence authority or acceptance authority;
2. helper inheritance cannot become a bypass;
3. DPA-300 failure semantics and DPA-500 freshness/gate semantics remain separate;
4. synchronized-set aggregate state remains derived and non-authoritative;
5. changed-path conformance supports exact, conditional and cleanup-sensitive commands without broad authorization;
6. all repository-specific implementation mappings remain `NEEDS_MAIN_REPO_VALIDATION`.
