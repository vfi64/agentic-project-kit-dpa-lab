# Package M Command Authority Independent Review Request — V3

Status: active

Status-date: 2026-07-20

Review role: independent architecture verification

Review target repository: `vfi64/agentic-project-kit-dpa-lab`

Exact review ref: `3527a181fa602957ee2ff20b047fa50ce98f00e6`

Immutable review branch: `review/package-m-command-authority-v3-20260720`

Working branch: `spec/dpa-600-concurrency`

Draft PR: `#5`

Supersedes for review execution: `reviews/PACKAGE_M_COMMAND_AUTHORITY_REVIEW_REQUEST_V2.md`

## 1. Review objective

Verify whether Package M's command-mutation-authority proposal and its two bounded correction addenda safely extend the existing DPA authority model without creating a second command registry, lifecycle, writer authority, acceptance authority, state store, finding taxonomy, evidence service or gate system.

This is a review of planning and proposed clauses. It is not executed Probe evidence, implementation validation, adoption or main-repository conformance.

## 2. Mandatory bootstrap

Read the repository bootstrap in the order defined by `LAB_BOOTSTRAP.md`, then read:

1. `STATUS.md`;
2. `MASTERPLAN.md`;
3. `MASTERPLAN_REMOTE_PREPARATION.md`;
4. DPA-200, DPA-300, DPA-400 and DPA-500;
5. ADRs relevant to authority, lifecycle ownership, renderer purity, acceptance and layered acceptance;
6. `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`;
7. `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`;
8. the Package M remote inventories, semantic-overlap matrix, generated-artifact ownership matrix and Probe-coverage map;
9. `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`;
10. `reviews/PACKAGE_M_INTERNAL_CONSISTENCY_AUDIT_20260720.md`;
11. `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`;
12. `reviews/PACKAGE_M_ADVERSARIAL_PRE_REVIEW_20260720.md`;
13. `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_V2_20260720.md`;
14. the existing Probe manuals and shared Probe execution/evidence contract;
15. `NEXT_CHAT_HANDOFF_PROMPT.md`.

Precedence for the review candidate is:

1. correction addendum V2;
2. first correction addendum;
3. original clause proposal.

A later document controls only where it explicitly replaces, narrows or clarifies earlier proposal text.

## 3. Required review questions

Determine whether:

1. every proposed rule extends an existing authority rather than creating a parallel subsystem;
2. one semantic fact has exactly one canonical authority while permitting multiple derived projections;
3. write ownership remains distinct from command orchestration;
4. the lifecycle remains the sole writer and acceptance-state owner for projected targets;
5. the command mutation contract is safely bound to exactly one existing main-repository runtime authority selected after exact-ref validation;
6. independently editable duplicate command-contract declarations are prohibited;
7. contract identity attaches only to externally invocable or independently authority-bearing/recoverable mutation boundaries, while subordinate helpers inherit and cannot broaden the owning contract;
8. command modes, aliases and secondary effects are classified with sufficient precision;
9. changed-path conformance correctly distinguishes maximum authorized scope, required changes, conditional outcomes and temporary-path obligations;
10. changed-path conformance remains testable and does not replace semantic, ownership or acceptance verification;
11. synchronized projection sets preserve one renderer invocation per registered target;
12. aggregate completion is only a derived workflow-orchestration result and cannot become a trust state, acceptance-state record, canonical authority, target write owner or independent persistent state;
13. per-target acceptance and aggregate attempt outcome remain distinct;
14. partial synchronized-set success remains visible and recoverable without fabricated all-or-nothing semantics;
15. generator orchestration does not weaken renderer purity;
16. command-contract plan invalidation is correctly distinguished from target freshness;
17. DPA-300 owns command-plan, mutation-attempt, verification and recovery failure semantics;
18. DPA-500 is limited to registered-projection freshness and gate consequences and does not become a general command-failure system;
19. proposed labels remain abstract subreason candidates and do not create concrete production finding codes;
20. proposal-local DMA identifiers do not create a second invariant namespace;
21. repository-specific mappings remain `NEEDS_MAIN_REPO_VALIDATION`;
22. the Probe impact is bounded and does not silently broaden an executed or frozen Probe identity;
23. DPA-600 remains frozen and DPA-700 remains unstarted;
24. any missing case, contradiction, false assurance claim or additional amendment surface exists.

## 4. Required explicit parallel-system assessment

For each subject classify the proposal as:

- `EXISTING_AUTHORITY_EXTENSION`;
- `PROPOSAL_LOCAL_VOCABULARY_ONLY`;
- `AMBIGUOUS_REQUIRES_CORRECTION`;
- `PARALLEL_SYSTEM_RISK`.

Subjects:

- command mutation contract;
- authority-bearing command boundary;
- inherited subordinate helper;
- CMA primary classes;
- synchronized projection set;
- derived aggregate attempt result;
- aggregate recovery identity;
- changed-path conformance verifier;
- DPA-300 command failure semantics;
- DPA-500 projection consequences;
- proposal-local finding subreason labels;
- proposal-local DMA traceability identifiers.

Explain the controlling existing authority for every `EXISTING_AUTHORITY_EXTENSION` classification.

## 5. Prior-finding verification

Explicitly determine whether all of the following are fully resolved:

- `PMA-M01`;
- `PMA-M02`;
- `PMA-M03`;
- `PMA-m01`;
- `PMA2-M01`;
- `PMA2-M02`;
- `PMA2-m01`.

A prior finding is not resolved merely because a later document claims resolution. Verify the resulting combined contract.

## 6. Finding taxonomy

Classify each finding as:

- `BLOCKER` — Package M cannot proceed to Maintainer adjudication;
- `MAJOR` — material authority, safety, acceptance, evidence or scope defect;
- `MINOR` — bounded completeness or synchronization defect;
- `EDITORIAL` — wording or navigation issue without contract effect.

For every finding provide:

- stable finding ID;
- exact file and section;
- governing normative anchor;
- observed defect;
- consequence;
- smallest safe correction;
- whether refreeze or rereview is required.

## 7. Required verdict

Return exactly one verdict:

- `ACCEPT`;
- `ACCEPT_WITH_CHANGES`;
- `REJECT`.

Also state:

- whether any blocker exists;
- whether all seven prior findings are fully resolved;
- whether ADR-022 may proceed to Maintainer adjudication as a deferred proposal;
- whether the bounded DPA-200/300/400/500 amendment package is ready for adjudication but not yet normative application;
- whether additional remote inventory is required before adjudication;
- whether local exact-ref validation remains required before repository-specific acceptance;
- whether DPA-600 must remain frozen;
- review method and limitations;
- exact ref reviewed.

## 8. Prohibitions

- Do not edit the immutable review branch.
- Do not infer current main-repository implementation behavior from Lab planning.
- Do not claim Probe success, implementation, adoption or conformance.
- Do not accept a new command registry, acceptance store, finding system or lifecycle merely because it is called a contract, verifier or coordinator.
- Do not require independent command contracts for subordinate helpers that cannot independently broaden or exercise mutation authority.
- Do not treat maximum authorized changed-path scope as proof that every authorized path must change.
- Do not promote DPA-300 command failures into DPA-500 target staleness without a target-contract basis.
- Do not promote proposal-local labels to concrete production identifiers without exact-ref evidence.
- Do not release DPA-600 or begin DPA-700.
- Do not treat either internal review as independent verification.
