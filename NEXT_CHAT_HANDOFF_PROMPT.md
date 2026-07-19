# Next Chat Handoff Prompt

We are developing the Document Projection Architecture in the private architecture Lab `vfi64/agentic-project-kit-dpa-lab`.

Work only from the current remote repositories and documented contracts. Do not work from chat memory.

## Mandatory bootstrap

Read fully and in this order:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `MASTERPLAN.md`
9. `MASTERPLAN_REMOTE_PREPARATION.md`
10. `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`
11. `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`
12. `DECISIONS.md`
13. `ASSUMPTIONS.md`
14. `specs/dpa/README.md`
15. `specs/dpa/DPA-000-VISION.md`
16. `specs/dpa/DPA-100-FOUNDATIONS.md`
17. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
18. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
19. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
20. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`
21. `specs/dpa/DPA-600-CONCURRENCY.md`
22. relevant accepted ADRs, especially ADR-016, ADR-017, ADR-019, ADR-020 and ADR-021
23. relevant traceability and diagrams
24. `probes/README.md`
25. `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`
26. `probes/PROBE-001-MANUAL.md`
27. `probes/PROBE-001-FIXTURE-MANIFEST.md`
28. `probes/PROBE-002-MANUAL.md`
29. `probes/PROBE-002-FIXTURE-MANIFEST.md`
30. `probes/DPA-400-RENDERER-PROBE-MANUAL.md`
31. `probes/DPA-400-RENDERER-FIXTURE-MANIFEST.md`
32. `probes/EXACT_REF_FREEZE_PROCEDURE.md`
33. `probes/EVIDENCE_CAPTURE_PROCEDURE.md`
34. `probes/PROBE_ADJUDICATION_PROCEDURE.md`
35. `reviews/claude/CLAUDE_PACKAGE_P_REVIEW.md`
36. `reviews/adjudication/PACKAGE_P_REVIEW_ADJUDICATION.md`
37. `reviews/claude/CLAUDE_PACKAGE_P_PPR_M03_REREVIEW.md`
38. `reviews/adjudication/PACKAGE_P_FINAL_CLOSURE.md`
39. `evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`
40. `integration/MAIN_REPO_REMOTE_SURFACE_INVENTORY_20260719.md`
41. `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`
42. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
43. `integration/PORTABILITY_SLICE_PLAN.md`
44. this handoff prompt

Do not begin substantive work before completing the bootstrap.

## Authority and evidence

- Current exact-ref main-repository evidence outranks Lab proposals.
- Normative DPA contracts and accepted ADRs outrank planning documents.
- `MASTERPLAN.md` is the canonical execution plan.
- `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md` is a binding Package-M planning addendum but is not itself a normative DPA specification.
- ADR-022 is a `DEFERRED PROPOSAL`, not an accepted decision.
- The current remote main-repository ref was freshly read on 2026-07-19 as `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`.
- That equality with the historical Discovery baseline does not remove the requirement for a fresh read immediately before local work.
- Local equality, cleanliness, environment identity and executable behavior remain unconfirmed.
- No repository-specific claim is `VERIFIED` without current exact-ref inspection and required local confirmation.

## Current Lab state

- DPA-000 and DPA-100: `stable`.
- DPA-200 through DPA-500: `review-ready`.
- DPA-400 and DPA-500 remain blocked from `stable` pending applicable Probe evidence and adjudication.
- Branch `spec/dpa-600-concurrency` and Draft PR #5 contain a bounded initial DPA-600 draft.
- DPA-600 remains `draft` and frozen.
- DPA-700 is `planned` and has not started.
- The Lab contains no production kit code and has not been adopted by the main repository.

## Package P state

Package P — Remote Probe Preparation is finally closed.

Completed:

- primary independent verdict `ACCEPT_WITH_CHANGES`;
- 0 blockers, 3 majors, 4 minors and 3 editorials adjudicated and corrected;
- limited PPR-M03 rereview completed;
- its sole editorial numbering finding corrected;
- final Maintainer closure recorded;
- no further Package-P independent rereview required.

No executable fixture has been materialized. No Probe has run. No implementation or main-repository conformance is claimed.

## Active Package M

The active work is **Package M — Exact-Ref Materialization Preparation and Document Mutation Authority Integration**.

Remote planning already completed:

1. fresh current-main record;
2. exact-ref remote source inventory;
3. governed local fixture-materialization plan;
4. binding document-mutation-authority and command-integration plan;
5. non-normative ADR-022 proposal;
6. status and roadmap synchronization.

Remote inspection confirms concrete current surfaces for Workspace/path resolution, documentation-registry loading and validation, lifecycle reporting, Workspace mutation locking, operational evidence tooling and CLI routing.

Remote inspection does not yet establish a complete DPA renderer, ProjectionContract/PartitionContract serialization, DPA lifecycle mutation sequence, authoritative acceptance state, re-acceptance, layered acceptance, recovery, staged enforcement or complete command-to-document mutation-authority implementation. Those must remain absent, partial or blocked until exact-ref evidence exists. Do not invent them.

## Identified architecture gap

The DPA already separates registry, renderer, lifecycle, workflow, evidence, freshness and gates. It does not yet completely classify every Agentic Kit command and internal entry point that creates, updates, moves, archives or deletes document-like artifacts.

The motivating handoff and status drift failure class remains possible unless the architecture defines:

- one canonical authority per semantic fact;
- command mutation classes;
- canonical inputs and generated targets;
- declared and actual changed-path scope;
- direct-edit rules for generated artifacts;
- composed-command ordering;
- Workspace, lock, lifecycle and workflow ownership;
- post-write verification;
- migration or deprecation of non-conforming direct writers.

This is a confirmed planning-level architecture gap and a repository-specific mapping question. It is not yet an accepted normative amendment.

## Current immediate task while only iPhone access exists

Work read-only against the current main repository and planning-only in the Lab:

1. inventory every public command mode, alias and internal entry point that may create, rewrite, append, replace, move, archive or delete document-like files;
2. inspect command call chains rather than classifying by names alone;
3. record canonical inputs, target paths, discovered writes, Workspace resolution, mutation lock, lifecycle ownership, workflow serialization, evidence and cleanup behavior;
4. classify each mode provisionally under CMA-1 through CMA-8 from ADR-022;
5. build the semantic-fact overlap matrix for handoff, status, planning, registry, command-reference, lifecycle, transfer and evidence families;
6. build the generated-artifact ownership matrix and direct-edit policy;
7. identify duplicate, ambiguous or composition-dependent writers;
8. map command-authority requirements to existing Probe cases and identify explicit bounded additions;
9. prepare exact proposed clauses for DPA-200, DPA-300, DPA-400 and DPA-500 plus traceability and diagram changes;
10. prepare a bounded independent-review package for ADR-022 and the amendment proposal;
11. continue the provisional materializability classification of all Probe cases;
12. refine the later local execution contract.

Do not claim global command completeness until local installed-CLI and source confirmation.

## Later immediate task on the Mac

In the real `vfi64/agentic-project-kit` checkout:

1. reread `origin/main` and record the exact SHA;
2. record local HEAD and require equality;
3. record `git status --short` and require the permitted clean baseline;
4. record Python, virtual environment, package version and Workspace profile/manifest identity;
5. enumerate the installed CLI and compare it with the remote inventory;
6. create a disposable fixture root and isolated evidence root;
7. prove path containment, sentinel cleanup and unchanged protected-path hashes;
8. execute only approved read-only inventory and disposable-repository observation stages;
9. produce complete Workspace, registry, reader, writer, command, lifecycle, lock, renderer, state/acceptance, gate/freshness, recovery and evidence inventories;
10. compare declared versus actual changed paths for document-producing commands;
11. classify every Probe case by materialization class;
12. stop before fixture bytes if any entry gate, isolation proof or inventory boundary fails;
13. do not execute any Probe before exact freeze;
14. do not mutate frozen DPA-critical production paths.

## Generated-document discipline

Before changing any document-like file, determine whether it is:

- canonical manually maintained source;
- lifecycle-governed projection;
- generated reference;
- state artifact;
- evidence or report;
- temporary artifact;
- historical archive.

If an Agentic Kit command generates or updates it, identify the canonical input and responsible command before proposing a direct edit. A direct output patch must not be represented as the durable fix unless the architecture explicitly permits direct maintenance.

## Required distinction

The following are different states and MUST NOT be collapsed:

- semantic fixture prepared;
- concrete fixture materialized;
- fixture set frozen;
- Probe case executed;
- evidence captured;
- result interpreted;
- Maintainer adjudication completed;
- architecture revalidated;
- implementation authorized.

The current state is remote planning and command inventory active; local baseline and executable inventories pending.

## DPA-600 and main-repository mutation freeze

Until applicable Probe execution, adjudication and architecture revalidation:

- do not materially expand or promote DPA-600;
- do not begin DPA-700;
- do not select concrete lock, workflow, branch-protection, merge-queue, recovery or rollback mechanisms;
- do not implement quick fixes to handoff writers, status writers, Doc Lifecycle Apply, writer semantics, immutable-plan execution, acceptance state, recovery, re-acceptance, layered acceptance, freshness or gate integration;
- do not represent portability candidates as verified without exact source inspection;
- do not materialize fake implementation state to make a Probe executable;
- do not introduce a second command registry, lifecycle, writer authority, state store, evidence service or gate system.

## Proactive architecture-gap obligation

Surface material specialist concerns even when the Maintainer did not know to ask. Classify each as:

- confirmed architecture gap;
- suspected gap requiring evidence;
- implementation defect under an adequate contract;
- editorial inconsistency;
- out-of-scope improvement.

Do not silently continue when the current plan would leave the motivating failure class possible.

## Merge discipline

Governed batches whose assurance depends on commit sequence MUST NOT be squash-merged. Preserve source commit SHAs, review refs and the selected merge method durably.

Do not claim Probe execution, implementation, adoption or main-repository conformance.