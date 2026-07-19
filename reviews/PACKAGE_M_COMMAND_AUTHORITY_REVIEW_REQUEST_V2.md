# Package M Command Authority Independent Review Request — V2

Status: active

Status-date: 2026-07-20

Review role: independent architecture verification

Review target repository: `vfi64/agentic-project-kit-dpa-lab`

Exact review ref: `d7d0bf5729d935579280f6acba96771ac8a54b44`

Immutable review branch: `review/package-m-command-authority-v2-20260720`

Working branch: `spec/dpa-600-concurrency`

Draft PR: `#5`

Supersedes for review execution: `reviews/PACKAGE_M_COMMAND_AUTHORITY_REVIEW_REQUEST.md`

## 1. Review objective

Verify whether Package M's command-mutation-authority proposal and bounded correction addendum safely extend the existing DPA authority model without creating a second command registry, lifecycle, writer authority, acceptance authority, state store, finding taxonomy, evidence service or gate system.

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
8. `integration/REMOTE_COMMAND_MUTATION_INVENTORY_20260719.md`;
9. `integration/REMOTE_HANDOFF_AND_TRANSFER_MUTATION_MAP_20260719.md`;
10. `integration/SEMANTIC_FACT_OVERLAP_MATRIX_20260719.md`;
11. `integration/GENERATED_ARTIFACT_OWNERSHIP_MATRIX_20260719.md`;
12. `integration/COMMAND_MUTATION_PROBE_COVERAGE_MAP_20260719.md`;
13. `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`;
14. `reviews/PACKAGE_M_INTERNAL_CONSISTENCY_AUDIT_20260720.md`;
15. `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`;
16. the existing Probe manuals and shared Probe execution/evidence contract;
17. `NEXT_CHAT_HANDOFF_PROMPT.md`.

Where the correction addendum conflicts with or narrows the original clause proposal, the addendum controls the review candidate.

## 3. Required review questions

Determine whether:

1. every proposed rule extends an existing authority rather than creating a parallel subsystem;
2. one semantic fact has exactly one canonical authority while permitting multiple derived projections;
3. write ownership remains distinct from command orchestration;
4. the lifecycle remains the sole writer and acceptance-state owner for projected targets;
5. the command mutation contract is safely bound to exactly one existing main-repository runtime authority selected after exact-ref validation;
6. independently editable duplicate command-contract declarations are prohibited;
7. command modes, aliases and secondary effects are classified with sufficient precision;
8. declared-versus-actual changed-path equality is testable and does not replace semantic verification;
9. synchronized projection sets preserve one renderer invocation per registered target;
10. aggregate completion is only a derived workflow-orchestration result and cannot become a trust state, acceptance-state record, canonical authority, target write owner or independent persistent state;
11. per-target acceptance and aggregate attempt outcome remain distinct;
12. partial synchronized-set success remains visible and recoverable without fabricated all-or-nothing semantics;
13. generator orchestration does not weaken renderer purity;
14. command-contract plan invalidation is correctly distinguished from target freshness;
15. proposed DPA-500 labels remain abstract subreason candidates and do not create concrete production finding codes;
16. proposal-local DMA identifiers do not create a second invariant namespace;
17. repository-specific mappings remain `NEEDS_MAIN_REPO_VALIDATION`;
18. the Probe impact is bounded and does not silently broaden an executed or frozen Probe identity;
19. DPA-600 remains frozen and DPA-700 remains unstarted;
20. any missing case, contradiction, false assurance claim or additional amendment surface exists.

## 4. Required explicit parallel-system assessment

For each of the following, classify the proposal as:

- `EXISTING_AUTHORITY_EXTENSION`;
- `PROPOSAL_LOCAL_VOCABULARY_ONLY`;
- `AMBIGUOUS_REQUIRES_CORRECTION`;
- `PARALLEL_SYSTEM_RISK`.

Subjects:

- command mutation contract;
- CMA primary classes;
- synchronized projection set;
- derived aggregate attempt result;
- aggregate recovery identity;
- changed-path verifier;
- proposal-local finding subreason labels;
- proposal-local DMA traceability identifiers.

Explain the controlling existing authority for every `EXISTING_AUTHORITY_EXTENSION` classification.

## 5. Finding taxonomy

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

## 6. Required verdict

Return exactly one verdict:

- `ACCEPT`;
- `ACCEPT_WITH_CHANGES`;
- `REJECT`.

Also state:

- whether any blocker exists;
- whether PMA-M01, PMA-M02, PMA-M03 and PMA-m01 are fully resolved;
- whether ADR-022 may proceed to Maintainer adjudication as a deferred proposal;
- whether the bounded DPA-200/300/400/500 amendment package is ready for adjudication but not yet normative application;
- whether additional remote inventory is required before adjudication;
- whether local exact-ref validation remains required before repository-specific acceptance;
- whether DPA-600 must remain frozen;
- review method and limitations;
- exact ref reviewed.

## 7. Prohibitions

- Do not edit the immutable review branch.
- Do not infer current main-repository implementation behavior from Lab planning.
- Do not claim Probe success, implementation, adoption or conformance.
- Do not accept a new command registry, acceptance store, finding system or lifecycle merely because it is called a contract or coordinator.
- Do not promote proposal-local labels to concrete production identifiers without exact-ref evidence.
- Do not release DPA-600 or begin DPA-700.
- Do not treat the internal audit as independent verification.
