# Package M Command Mutation Authority Independent Review Request

Status: active

Status-date: 2026-07-20

Review role: independent architecture verification

Review target repository: `vfi64/agentic-project-kit-dpa-lab`

Exact review ref: `eab8b3aefb04f0c557f41f0c06d4b7ec00eb261c`

Immutable review branch: `review/package-m-command-authority-20260720`

Working branch: `spec/dpa-600-concurrency`

Draft PR: `#5`

## 1. Review objective

Verify whether the Package M command-mutation-authority proposal closes the identified writer-authority gap without creating a parallel command registry, lifecycle, writer service, state store, evidence service or gate system.

The review concerns planning and proposed clauses only.

No Probe has run. No main-repository command has been locally executed for this package. No normative DPA file has been amended. ADR-022 remains a `DEFERRED PROPOSAL`.

## 2. Mandatory bootstrap

Read the repository bootstrap in the order defined by `LAB_BOOTSTRAP.md`, then read:

1. `STATUS.md`;
2. `MASTERPLAN.md`;
3. `MASTERPLAN_REMOTE_PREPARATION.md`;
4. DPA-200, DPA-300, DPA-400 and DPA-500;
5. DPA-600 only to verify that its freeze remains intact;
6. `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`;
7. `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`;
8. `integration/REMOTE_COMMAND_MUTATION_INVENTORY_20260719.md`;
9. `integration/REMOTE_HANDOFF_AND_TRANSFER_MUTATION_MAP_20260719.md`;
10. `integration/SEMANTIC_FACT_OVERLAP_MATRIX_20260719.md`;
11. `integration/GENERATED_ARTIFACT_OWNERSHIP_MATRIX_20260719.md`;
12. `integration/COMMAND_MUTATION_PROBE_COVERAGE_MAP_20260719.md`;
13. `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`;
14. PROBE-001 and PROBE-002 manuals and the shared Probe execution/evidence contract;
15. `NEXT_CHAT_HANDOFF_PROMPT.md`.

Review only the immutable exact ref and identify it in the result.

## 3. Required review questions

Determine whether:

1. the motivating failure class is correctly identified as a command/writer-authority gap rather than merely a renderer defect;
2. the proposed command mutation contract extends existing authorities rather than becoming a second runtime command registry;
3. the eight provisional CMA classes are necessary, mutually understandable and non-authoritative until ADR acceptance;
4. command mode, alias and secondary-effect distinctions are sufficient and testable;
5. semantic-fact authority remains singular and distinct from target write ownership;
6. the generated-surface edit rule is appropriately strict without inventing unsupported emergency-repair semantics;
7. declared-versus-actual changed-path equality is feasible and correctly separated from semantic verification;
8. the synchronized projection-set concept preserves one renderer invocation per registered target and one lifecycle result per target;
9. aggregate source-snapshot identity and partial-completion recovery are placed in DPA-300 rather than improperly assigned to renderer authority;
10. generator determinism is correctly distinguished from renderer determinism;
11. DPA-500 freshness and findings remain distinct from trust state, gate decision and enforcement stage;
12. the proposed amendment ownership across DPA-200, DPA-300, DPA-400 and DPA-500 is correct;
13. the proposed traceability identifiers avoid creating a second invariant namespace;
14. repository-specific claims remain fenced as `NEEDS_MAIN_REPO_VALIDATION` or `REMOTE_PARTIAL`;
15. the six Probe amendment candidates are adequate, excessive or incomplete;
16. the proposal silently broadens any existing Probe PASS condition;
17. DPA-600 remains frozen and DPA-700 remains unstarted;
18. any clause introduces an accidental new authority, circular authority, untestable obligation or contradiction with existing normative text;
19. any required clause, negative case, recovery case or migration precondition is missing;
20. the proposal is ready for Maintainer adjudication as a bounded amendment candidate.

## 4. Special focus: parallel-system risk

The reviewer MUST explicitly test whether any of the following would become a parallel system:

- the command mutation contract;
- the CMA classification;
- synchronized projection-set orchestration;
- aggregate completion state;
- changed-path verification;
- proposal-local DMA identifiers.

For each item, state one of:

- valid extension of an existing authority;
- acceptable planning vocabulary but not yet a runtime construct;
- ambiguous and requiring correction;
- prohibited parallel authority.

## 5. Special focus: authority graph

For handoff and successor-package generation, verify the proposed distinction among:

- canonical source authorities;
- generated projection targets;
- generator orchestration;
- per-target lifecycle ownership;
- aggregate completion;
- evidence and reports;
- compatibility aliases.

Identify any edge that would permit one target, report, prompt or evidence artifact to become an independent semantic authority.

## 6. Finding taxonomy

Classify each finding as:

- `BLOCKER` — the proposal cannot proceed to Maintainer adjudication;
- `MAJOR` — material authority, lifecycle, safety, testability or scope defect;
- `MINOR` — bounded completeness or synchronization defect;
- `EDITORIAL` — wording or navigation issue without contract effect.

For every finding provide:

- stable finding ID;
- exact file and section;
- governing normative anchor;
- observed defect;
- consequence;
- smallest safe correction;
- whether the clause proposal or inventory must be refrozen;
- whether another independent review is required.

Do not collapse distinct authority, lifecycle, renderer, freshness, gate, evidence or migration defects into one finding.

## 7. Required verdict

Return exactly one package verdict:

- `ACCEPT`;
- `ACCEPT_WITH_CHANGES`;
- `REJECT`.

Also state:

- whether any blocker exists;
- whether ADR-022 may proceed to Maintainer adjudication;
- whether the proposed clauses may become the basis of a synchronized normative amendment after adjudication;
- whether additional remote inventory is required before adjudication;
- whether local exact-ref validation is still mandatory before repository-specific acceptance or implementation;
- whether Probe amendment design may proceed;
- whether DPA-600 must remain frozen;
- review method and limitations;
- exact ref reviewed.

## 8. Required output structure

1. Executive verdict.
2. Review method and exact ref.
3. Authority-model assessment.
4. Parallel-system-risk assessment table.
5. Findings ordered by severity.
6. Missing coverage or negative cases.
7. Required corrections.
8. Maintainer-adjudication recommendation.
9. Explicit boundary statement that no Probe or main-repository conformance was established.

## 9. Prohibitions

- Do not edit the immutable review branch.
- Do not infer local or executable behavior from remote source inspection.
- Do not claim command-inventory completeness beyond the inspected exact refs.
- Do not accept ADR-022 on behalf of the Maintainer.
- Do not amend normative DPA files.
- Do not redefine existing Probe cases after execution; no Probe has run in this package.
- Do not create a new command registry, lifecycle, writer service, state store, evidence service or gate system.
- Do not release DPA-600 or begin DPA-700.
- Do not treat the clause proposal as current runtime behavior.
