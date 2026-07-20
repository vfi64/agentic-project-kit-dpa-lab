# Package M — Maintainer Adjudication

Status: complete

Status-date: 2026-07-20

## 1. Adjudication subject

This adjudication covers:

- `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`;
- `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`;
- `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`;
- `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_V2_20260720.md`;
- the supporting Package-M inventories, overlap and ownership matrices, and Probe-coverage map.

The immutable architecture-review candidate is:

- branch: `review/package-m-command-authority-v3-20260720`;
- exact ref: `3527a181fa602957ee2ff20b047fa50ce98f00e6`.

## 2. Evidence chain

The Maintainer considered:

1. the Package-M command and internal-mutator inventory;
2. the semantic-fact overlap matrix;
3. the generated-artifact ownership matrix;
4. the command-mutation Probe-coverage map;
5. the proposed clauses and both controlling correction addenda;
6. `reviews/PACKAGE_M_INTERNAL_CONSISTENCY_AUDIT_20260720.md`;
7. `reviews/PACKAGE_M_ADVERSARIAL_PRE_REVIEW_20260720.md`;
8. `reviews/PACKAGE_M_COMMAND_AUTHORITY_INDEPENDENT_REVIEW_20260720.md`;
9. `integration/PACKAGE_M_INDEPENDENT_REVIEW_DISPOSITION_20260720.md`;
10. `integration/PACKAGE_M_EVIDENCE_CLASSIFICATION_MAPPING_20260720.md`.

The independent review verdict is `ACCEPT_WITH_CHANGES` with:

- blockers: 0;
- majors: 0;
- minors: 1;
- editorials: 2.

All three new findings have an accepted bounded disposition. All seven earlier Package-M findings are independently confirmed resolved.

## 3. Maintainer decision

Decision: `ACCEPT_FOR_BOUNDED_NORMATIVE_DRAFTING`.

ADR-022 is accepted as the governing deferred architecture direction for preparing one synchronized bounded amendment package across DPA-200, DPA-300, DPA-400 and DPA-500.

This decision accepts the following architecture principles:

1. every independently invocable, independently schedulable or independently recoverable document-mutating command mode must be governed by one mutation contract;
2. subordinate internal helpers inherit the owning contract and must not broaden its authority;
3. one semantic fact has exactly one canonical authority;
4. multiple representations of that fact remain derived projections only;
5. command orchestration does not acquire lifecycle, renderer, writer, acceptance, trust-state, finding, gate, evidence or persistence authority;
6. the lifecycle remains the sole writer and target-scoped acceptance-state owner for registered projection targets;
7. a command mutation contract must extend exactly one existing main-repository runtime authority selected after exact-ref validation;
8. independently editable duplicate command-contract declarations are prohibited;
9. synchronized projection sets preserve one target identity, one renderer invocation and one lifecycle-owned result per member;
10. an aggregate attempt result is derived workflow output only and cannot become target acceptance, trust state, canonical authority, writer ownership or independent persistent state;
11. aggregate recovery uses existing workflow or lifecycle recovery structures only and cannot create a new recovery store or owner;
12. changed-path verification is a plan-bound conformance relation over authorized, required, conditional and temporary paths and does not replace semantic, ownership, acceptance or gate verification;
13. DPA-300 owns command-plan, mutation-attempt, changed-path, secondary-effect, alias, composed-step and recovery failure semantics;
14. DPA-500 owns only the resulting projection-freshness, trust-evaluation and gate consequences;
15. proposal-local CMA, DMA and finding-subreason labels do not create new runtime registries, invariant namespaces or finding systems;
16. all repository-specific mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

## 4. Effect of the decision

This adjudication authorizes:

- drafting one synchronized bounded amendment package for DPA-200, DPA-300, DPA-400 and DPA-500;
- assigning concrete section numbers and eliminating proposal placeholders such as `11.x` during that drafting;
- synchronizing traceability and diagrams with the drafted amendments;
- preparing an explicit, separately reviewed Probe-contract amendment proposal where command-integration coverage requires it;
- preparing local exact-ref validation instructions for the command-contract runtime home and changed-path behavior.

This adjudication does not itself amend any normative DPA specification.

ADR-022 remains a `DEFERRED PROPOSAL` until the bounded normative amendment package has been drafted, independently verified and accepted through the normal normative-change process.

## 5. Restrictions preserved

This adjudication does not authorize:

- main-repository mutation;
- implementation or adoption;
- creation of a new command registry, lifecycle, writer authority, acceptance store, trust-state taxonomy, finding system, gate runner, evidence service, state store or recovery store;
- promotion of proposal-local labels to production identifiers;
- claims of command-inventory completeness;
- claims of main-repository conformance;
- Probe execution or silent amendment of an existing Probe identity;
- promotion of DPA-400 or DPA-500 to `stable`;
- continuation or promotion of DPA-600;
- beginning DPA-700.

## 6. Required validation before normative application

Before repository-specific normative application or implementation planning:

1. re-read the current main-repository exact ref;
2. confirm local and remote HEAD equality and worktree cleanliness;
3. enumerate the installed CLI and complete source-level command and internal-writer inventory;
4. identify exactly one existing runtime authority capable of carrying the command mutation contract;
5. prove that no independently editable duplicate declaration exists;
6. observe approved commands in a disposable repository and compare actual path effects with the authorized, required, conditional and temporary path contract;
7. validate Workspace, lifecycle, lock, renderer, verification, finding, gate, recovery and evidence ownership;
8. adjudicate explicit Probe amendments before execution;
9. independently review the synchronized normative amendment package.

## 7. Sequencing decision

The next governed step is the synchronized drafting of the bounded DPA-200/300/400/500 amendment package.

The package must remain non-normative during drafting and must preserve the precedence already established by the two Package-M correction addenda.

DPA-600 remains frozen at `draft`. DPA-700 remains `planned` and unstarted.

## 8. Final disposition

- ADR-022 architecture direction: accepted for bounded normative drafting.
- ADR-022 normative effect: none yet.
- Package-M independent-review findings open: 0.
- Additional remote inventory required before drafting: no.
- Local exact-ref validation required before repository-specific acceptance: yes.
- New review-candidate ref required now: no.
- Independent review required after normative drafting: yes.
