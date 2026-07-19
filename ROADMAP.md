# Roadmap

Status: active

Status-date: 2026-07-19

## Specification sequence

1. DPA-000 — Vision and principles — stable
2. DPA-100 — Foundations and terminology — stable, synchronized through ADR-019
3. DPA-200 — Document model — review-ready
4. DPA-300 — Registry and lifecycle integration — review-ready, restructure lineage ratified and ADR-021 amendment verified
5. DPA-400 — Renderer contract — review-ready after independent post-adjudication verification
6. DPA-500 — Freshness and gates — review-ready after independent post-adjudication verification
7. DPA-600 — Concurrency and workflow serialization — bounded draft frozen in PR #5
8. DPA-700 — Migration and rollback — planned, not started
9. DPA-800 — DP1–DP5 implementation specification — planned
10. DPA-900 — Future evolution — planned
11. reversible Lab adoption with `agentic-project-kit`
12. controlled import into `vfi64/agentic-project-kit`

The normative DPA-number sequence is unchanged. It does not determine the immediate execution order.

`MASTERPLAN.md` owns the canonical execution sequence. `MASTERPLAN_REMOTE_PREPARATION.md` defines the corrected remote order and cannot override the Masterplan. `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md` is a binding Package-M planning addendum and cannot by itself amend normative DPA contracts.

## Immediate execution order

The active sequence remains Probe-first, with an added command-authority preparation track required to exclude the motivating handoff and status drift failure class:

1. Package P shared Probe contract, three Probe packages, freeze/evidence/adjudication procedures, CSC checklist and portability planning — complete and finally closed;
2. fresh current-main remote read and exact-ref remote surface inventory — complete for the 2026-07-19 observation;
3. remote command-to-document discovery, mutation-class inventory, semantic-fact overlap matrix and generated-artifact ownership map — active and safe on iPhone;
4. proposed ADR-022 and bounded DPA-200/300/400/500 amendment package — prepare and independently review, but do not yet make normative;
5. provisional mapping of command-authority coverage into PROBE-001, PROBE-002 and renderer Probe cases;
6. local ref/environment/isolation baseline — after Mac access;
7. complete local reader/writer/command/lifecycle/lock/renderer/state/gate/recovery/evidence inventories;
8. disposable-repository observation of approved document-producing commands, including declared-versus-actual output scope;
9. semantic-to-concrete fixture reconciliation and bounded materialization — after inventory gates;
10. exact Probe-ref and fixture freeze — after materialization exits;
11. PROBE-001, PROBE-002 and renderer Probe execution — only after freeze;
12. evidence capture and Maintainer adjudication;
13. adjudication of ADR-022 and synchronized bounded DPA amendments where supported;
14. DPA-300 through DPA-500 revalidation and independent verification of normative amendments;
15. evidence-bounded continuation of DPA-600;
16. DPA-700 through DPA-900, controlled import and implementation after upstream release decisions.

DPA-600 through DPA-900 MUST NOT displace the active reality-contact and command-authority sequence. DPA-600 remains frozen and DPA-700 remains unstarted.

## Current package

**Package P — Remote Probe Preparation** is finally closed.

The active work package is now:

**Package M — Exact-Ref Materialization Preparation and Document Mutation Authority Integration**

Governing artifacts:

- `evidence/repo-facts/MAIN_REPO_CURRENT_REF_20260719.md`;
- `integration/MAIN_REPO_REMOTE_SURFACE_INVENTORY_20260719.md`;
- `integration/LOCAL_FIXTURE_MATERIALIZATION_PLAN.md`;
- `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`;
- `decisions/DPA-ADR-022-DOCUMENT-MUTATION-AUTHORITY.md`;
- existing Package-P Probe contracts and procedures.

Package M is planning and inventory first. It authorizes no Probe execution and no main-repository implementation change.

ADR-022 remains a `DEFERRED PROPOSAL`. Its mutation classes and amendment requirements are planning hypotheses until exact-ref inventory, independent review and Maintainer adjudication are complete.

## Evidence-first DP1 sequencing

Completed:

- DPA-200 adjudication and review-ready promotion;
- DP1 read-only Discovery at `6a9da7d…`;
- DISC-001 through DISC-010 and DISC-003b;
- assumptions, main-repository context and Probe backlog synchronization;
- DPA-300 review, verification, adjudication, correction and review-ready promotion;
- DPA-300 restructure-equivalence verification and Maintainer ratification;
- DPA-400 normative contract, traceability, diagram, review, amendment, verification and promotion;
- DPA-500 normative contract, traceability, diagram, review, ADR-021 amendment, verification and promotion;
- merge of the DPA-500 slice through PR #3 at `1f3e5a64f4be5a974bf979f066d9434505a1d74c`;
- durable read-only Lab gates for the reviewed architecture slices;
- bounded initial DPA-600 draft, traceability and diagram in Draft PR #5;
- complete Package-P preparation, independent review, correction, limited rereview and final closure;
- fresh 2026-07-19 remote read of main-repository `main` at `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`;
- bounded exact-ref remote surface inventory;
- governed local fixture-materialization plan;
- binding document-mutation-authority and command-integration planning addendum;
- non-normative ADR-022 proposal.

Pending under `MASTERPLAN.md` and the Package-M planning addendum:

1. complete remote command and internal-mutator inventory;
2. semantic-fact overlap and generated-artifact ownership matrices;
3. provisional command mutation classification and Probe coverage map;
4. bounded proposed DPA-200/300/400/500 clauses, traceability and diagrams;
5. independent review and Maintainer adjudication of the proposal package;
6. local equality, cleanliness, environment and isolation baseline;
7. complete local exact-ref surface inventories;
8. disposable-repository command observations and output-scope verification;
9. concrete fixture materialization with immutable revisions and hashes;
10. exact Probe-ref freeze;
11. Probe execution and evidence adjudication;
12. bounded DPA-300 through DPA-500 revalidation and amendments where required;
13. independent verification of normative amendments to review-ready specifications;
14. evidence-bounded continuation of DPA-600 through DPA-900;
15. DP2 implementation through existing registry, lifecycle, Workspace, findings, gate and evidence authorities;
16. migration or deprecation of non-conforming direct document writers;
17. external-repository habitability validation;
18. sustainable-governance and review-economics closeout.

Remote inspection currently confirms concrete Workspace, registry, lifecycle-reporting, lock, evidence and CLI surfaces. It does not yet confirm a complete DPA renderer, acceptance state, re-acceptance, recovery, staged-enforcement or command-to-document mutation-authority implementation. Missing surfaces must be recorded as absent or blocked, not invented.

Early Discovery, remote source inspection, command classification, fixture preparation and exploratory drafting do not constitute adoption, implementation, migration or Probe success.

## Probe and specification relationship

PROBE-001 tests the real registry parser and validator against the DPA-300/ADR-017 `ProjectionContract` and `PartitionContract` serialization proposal.

PROBE-002 tests lifecycle, immutable planning, Workspace, locks, Write, Verify, acceptance-state, recovery, conditional base persistence, gate-set re-acceptance and layered acceptance against an exact main-repository ref.

The DPA-400 renderer Probe package tests renderer mapping, interface compatibility, version behavior, deterministic execution, immutable inputs, output scope and prohibited capabilities.

The Package-M command-integration track must additionally map command mutation authority, canonical inputs, generated-artifact ownership, duplicate semantic writers, composed-command order, declared-versus-actual changed paths and post-write verification into the appropriate Probe and evidence contracts. Any case amendment must be explicit, synchronized and reviewed.

DPA-400 and DPA-500 remain `review-ready`. Repository-dependent claims MUST remain `NEEDS_MAIN_REPO_VALIDATION`, and neither specification may become `stable` before relevant Probe evidence is available and adjudicated.

DPA-600 remains `draft`. Its concrete concurrency and workflow mappings require exact-ref validation and applicable Probe evidence before promotion can be considered.

## Merge discipline

Governed batches whose assurance depends on commit sequence MUST NOT be squash-merged. Their source commit SHAs, review refs and selected merge method MUST be recorded durably. The DPA-500 governed branch should be retained until its sequence is preserved outside the branch.