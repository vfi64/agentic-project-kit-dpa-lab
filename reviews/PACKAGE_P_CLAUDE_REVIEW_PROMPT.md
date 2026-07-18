# Claude Review Prompt — Package P

Copy the complete prompt below into a fresh Claude review chat.

---

We are developing the Document Projection Architecture (DPA) in the private architecture Lab `vfi64/agentic-project-kit-dpa-lab`.

You are acting as an **independent technical verifier** for **Package P — Remote Probe Preparation**.

## Review target

Review only this exact immutable Lab ref:

`18d0fd08b27d97aef1b06b5a75079527290ca8e4`

Immutable review branch:

`review/package-p-20260718`

Draft PR for context only:

`#5`

Do not review a later working-branch state. Do not edit the immutable review branch. If the checked-out or remotely inspected ref differs from the exact SHA above, stop and report `REVIEW_REF_MISMATCH`.

The Lab gate for the exact review ref completed successfully:

- workflow: `DPA lab gates`
- run: `29660679403`
- conclusion: `success`

Treat that result only as Lab validation evidence. It is not Probe execution evidence and does not establish main-repository conformance.

## Language and working method

- Write the final review in English.
- Work only from the exact remote repository ref and its documented contracts.
- Do not use chat memory as authority.
- Do not infer current main-repository behavior from Lab proposals or historical Discovery evidence.
- Do not modify files, create commits, update branches or propose quick production fixes.
- Separate observation, interpretation and recommendation.
- Quote only bounded excerpts and always identify the exact file and section.

## Mandatory bootstrap

Before any substantive review, read the repository bootstrap completely and in the order required by `LAB_BOOTSTRAP.md`.

At minimum, ensure that the following have been read in their required context:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `MASTERPLAN.md`
9. `MASTERPLAN_REMOTE_PREPARATION.md`
10. `DECISIONS.md`
11. `ASSUMPTIONS.md`
12. `specs/dpa/README.md`
13. `specs/dpa/DPA-000-VISION.md`
14. `specs/dpa/DPA-100-FOUNDATIONS.md`
15. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
16. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
17. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
18. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`
19. `specs/dpa/DPA-600-CONCURRENCY.md`
20. all accepted ADRs relevant to partition contracts, lifecycle planning, acceptance, recovery, renderer identity and inputs, freshness, promotion and evidence boundaries
21. relevant traceability and diagrams
22. `probes/README.md`
23. `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`
24. `probes/PROBE-001-MANUAL.md`
25. `probes/PROBE-001-FIXTURE-MANIFEST.md`
26. `probes/PROBE-001-INTERNAL-CONTRACT-AUDIT.md`
27. `probes/PROBE-002-MANUAL.md`
28. `probes/PROBE-002-FIXTURE-MANIFEST.md`
29. `probes/PROBE-002-INTERNAL-CONTRACT-AUDIT.md`
30. `probes/DPA-400-RENDERER-PROBE-MANUAL.md`
31. `probes/DPA-400-RENDERER-FIXTURE-MANIFEST.md`
32. `probes/DPA-400-RENDERER-INTERNAL-CONTRACT-AUDIT.md`
33. `probes/EXACT_REF_FREEZE_PROCEDURE.md`
34. `probes/EVIDENCE_CAPTURE_PROCEDURE.md`
35. `probes/PROBE_ADJUDICATION_PROCEDURE.md`
36. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
37. `integration/PORTABILITY_SLICE_PLAN.md`
38. `reviews/PACKAGE_P_INTERNAL_CONSISTENCY_AUDIT.md`
39. `reviews/PACKAGE_P_REVIEW_REQUEST.md`
40. `NEXT_CHAT_HANDOFF_PROMPT.md`

Do not begin the technical assessment before this bootstrap is complete.

## Authority order

Apply this authority order:

1. current exact-ref main-repository evidence, where actually available;
2. normative DPA specifications and accepted ADRs;
3. Probe-specific manuals;
4. shared Probe execution and evidence contract;
5. freeze, evidence-capture and adjudication procedures;
6. planning, status and handoff documents;
7. internal audits as non-independent review evidence only.

Historical Discovery observations at `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` remain historical exact-ref evidence. They must not be represented as proof of current implementation capability unless the package itself provides valid current-ref evidence.

## Review objective

Determine whether Package P is internally coherent, normatively aligned, sufficiently complete and safely bounded for Maintainer adjudication before any local executable-fixture materialization or any reconsideration of DPA-600 continuation.

No Probe has run. No executable fixture has been materialized. No current main-repository conformance is claimed.

## Required review questions

Answer all of the following:

1. Is Probe preparation cleanly separated from Probe execution?
2. Is the outcome vocabulary closed and consistently used across all manuals and procedures?
3. Are observation, case result, interpretation and Maintainer adjudication kept distinct?
4. Are exact refs, fixture revisions, hashes, changed-path evidence, cleanup, rollback, repeatability and rerun rules sufficient and mutually consistent?
5. Does PROBE-001 fully represent the DPA-300 and ADR-017 obligations for registry, parent-entry `PartitionContract`, ownership and validation without inventing current serialization?
6. Does PROBE-002 adequately cover lifecycle ordering, immutable planning, stale-plan rejection, locking, under-lock revalidation, Write–Verify–Record–Release, acceptance state, layered acceptance, gate-set re-acceptance, interruption, recovery, evidence failure and staged enforcement?
7. Does the DPA-400 renderer Probe adequately cover closed static resolution, immutable declared inputs, source-as-data behavior, configuration, deterministic output, one-target scope, payload-only region output, purity, prohibited capabilities, secret isolation, version distinctions, semantic bounds, operational aborts and lifecycle-only invocation?
8. Does any artifact accidentally create or imply a second registry, lifecycle, writer, state store, evidence authority, lock authority, gate authority or acceptance authority?
9. Are all repository-specific parser, writer, state, renderer, command, lock, evidence and path mappings correctly fenced as `NEEDS_MAIN_REPO_VALIDATION`?
10. Can the portability slice plan alter a Probe subject, writer behavior, lifecycle semantics, acceptance state, gate authority or a frozen DPA-critical surface without detection?
11. Does the CSC and namespace-profile checklist extend existing main-repository authority rather than defining a parallel operational system?
12. Are the DPA-600 freeze and DPA-700 prohibition consistent across `STATUS.md`, plans, Probe documents, PR framing and handoff?
13. Is Package P complete enough to proceed to Maintainer adjudication?
14. After successful adjudication, is it complete enough to begin local executable-fixture materialization planning, while still prohibiting Probe execution until exact-ref and safety preconditions are met?
15. Is there any missing mandatory case, contradictory expectation, ambiguous state transition, false assurance claim, unverifiable status statement or hidden implementation selection?
16. Do the internal audit verdicts accurately describe only internal synchronization, without being treated as independent verification?
17. Do the freeze, evidence and adjudication procedures form one coherent crash-safe and non-authoritative evidence chain?
18. Are refreeze and rereview obligations sufficiently explicit when manuals, fixtures, normative expectations, mappings or implementation refs change?

## Finding taxonomy

Classify every finding as exactly one of:

- `BLOCKER` — Package P cannot proceed to Maintainer adjudication or local materialization planning.
- `MAJOR` — material normative, safety, authority, evidence or scope defect.
- `MINOR` — bounded completeness, consistency or synchronization defect.
- `EDITORIAL` — wording or navigation defect without contract effect.

Use stable finding IDs:

- `PPR-B01`, `PPR-B02`, ... for blockers;
- `PPR-M01`, `PPR-M02`, ... for majors;
- `PPR-m01`, `PPR-m02`, ... for minors;
- `PPR-e01`, `PPR-e02`, ... for editorials.

For every finding provide:

- finding ID;
- severity;
- exact file and section;
- governing normative anchor;
- observed defect;
- concrete consequence;
- smallest safe correction;
- affected artifacts;
- whether a new Lab ref is required;
- whether independent rereview is required;
- whether any Probe case, freeze or future execution would be invalidated.

Do not combine unrelated defects into one finding merely to shorten the report.

## Required verdict

Return exactly one package verdict:

- `ACCEPT`
- `ACCEPT_WITH_CHANGES`
- `REJECT`

The verdict must be based on the exact reviewed ref only.

## Mandatory final report structure

Use exactly this top-level structure:

1. `Review identity`
2. `Bootstrap confirmation`
3. `Executive verdict`
4. `Blockers`
5. `Major findings`
6. `Minor findings`
7. `Editorial findings`
8. `Cross-artifact consistency assessment`
9. `Probe-specific assessment`
   - `PROBE-001`
   - `PROBE-002`
   - `DPA-400 renderer Probe`
10. `Freeze, evidence and adjudication assessment`
11. `CSC, namespace and portability assessment`
12. `Authority and false-assurance assessment`
13. `Required corrections and sequencing`
14. `Refreeze and rereview obligations`
15. `Maintainer adjudication readiness`
16. `Local materialization-planning readiness`
17. `DPA-600 and DPA-700 disposition`
18. `Review method and limitations`
19. `Final machine-readable summary`

The final machine-readable summary must use this exact form:

```yaml
reviewed_repository: vfi64/agentic-project-kit-dpa-lab
reviewed_ref: 18d0fd08b27d97aef1b06b5a75079527290ca8e4
reviewed_branch: review/package-p-20260718
verdict: ACCEPT | ACCEPT_WITH_CHANGES | REJECT
blocker_count: <integer>
major_count: <integer>
minor_count: <integer>
editorial_count: <integer>
package_p_may_proceed_to_maintainer_adjudication: true | false
local_fixture_materialization_planning_may_begin_after_adjudication: true | false
dpa_600_must_remain_frozen: true
dpa_700_must_remain_unstarted: true
new_lab_ref_required: true | false
independent_rereview_required: true | false
probe_execution_claimed: false
main_repository_conformance_claimed: false
limitations:
  - <bounded limitation>
```

## Prohibitions

- Do not edit or move `review/package-p-20260718`.
- Do not review the later working branch as the package target.
- Do not infer main-repository implementation capability from architecture documents.
- Do not claim Probe execution, successful fixtures, adoption or conformance.
- Do not select concrete production parser, writer, lock, renderer, state, evidence or workflow mechanisms where exact-ref evidence is absent.
- Do not release DPA-600.
- Do not begin or recommend beginning DPA-700.
- Do not convert internal audit verdicts into independent verification.
- Do not implement corrections. Report findings only.

Begin by confirming the exact reviewed ref and completion of the mandatory bootstrap. Then perform the review without intermediate implementation work.
