# Next Chat Handoff Prompt

Copy the prompt below into a new ChatGPT session.

---

We are working in the repository `vfi64/agentic-project-kit-dpa-lab`.

Language and working style:

- Communicate with the Maintainer in German, concise, direct and evidence-based.
- Write normative specifications, ADRs, traceability and diagrams in English, following the repository style.
- Do not work from chat memory.
- The sources of truth are the current remote repository, exact refs, the Lab bootstrap hierarchy and recorded evidence.
- Do not claim test, gate, Probe, implementation or merge success without repository-backed evidence.
- Do not introduce production kit code, live `.agentic/` state, a second runtime authority or a parallel registry, lifecycle, evidence, Workspace, renderer, state or gate system into the Lab.

## Mandatory bootstrap

Before proposing or changing anything, inspect the current remote `main` ref and read these files completely in this exact order:

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
19. the current DPA-600 and DPA-700 files or stubs
20. all ADRs relevant to DPA-300 through DPA-700
21. relevant traceability and diagrams
22. `reviews/README.md`
23. relevant DPA-300, DPA-400 and DPA-500 reviews, adjudications and post-adjudication verifications
24. `integration/DP1_DISCOVERY_CONTRACT.md`
25. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
26. `integration/IMPORT_PLAN.md`
27. this file, `handoff/NEXT_CHAT_HANDOFF_PROMPT.md`

If an expected filename differs, locate the canonical corresponding file in the repository rather than guessing its content.

After the bootstrap, report exactly:

- repository and exact current `main` SHA;
- current Lab phase;
- status of DPA-000 through DPA-900;
- active masterplan and annex;
- current task;
- unresolved blocking decisions;
- main-repository facts used and their evidence classification;
- whether work may proceed.

## Authoritative current state

Treat the repository as authoritative and verify this summary rather than trusting it blindly:

- DPA-000 and DPA-100 are `stable`.
- DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`.
- DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence and adjudication.
- The recorded main-repository Discovery baseline is `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` and is historical evidence only.
- Every repository-specific finding must be revalidated against the current exact `origin/main` and locally confirmed before mutation.
- `MASTERPLAN.md` is the canonical execution plan.
- `MASTERPLAN_REMOTE_PREPARATION.md` is its governed annex for the remaining iPhone/remote preparation and staged independent verification strategy.
- No production code or Probe execution belongs in the Lab.

## Non-negotiable freeze

Do not propose or apply quick fixes before PROBE-002 execution, adjudication and subsequent architecture revalidation to:

- `transfer_repo_actions._refresh_operational_handoff_docs()`;
- writers of `docs/handoff/CURRENT_HANDOFF.md`;
- Doc Lifecycle Apply or governed content-writing behavior;
- mutation-plan execution semantics;
- acceptance-state schema or persistence;
- recovery completion semantics;
- re-acceptance;
- layered acceptance;
- projection-specific freshness or gate integration.

A writer inventory may be rebuilt read-only. Writers themselves remain frozen.

## Remote-preparation programme

The Lab may prepare, without execution claims:

1. DPA-600 — concurrency and workflow serialization;
2. DPA-700 — migration and rollback;
3. DPA-800 — DP1 through DP5 implementation contract;
4. DPA-900 — sustainable governance and review economics;
5. controlled import and PR plan;
6. PROBE-001, PROBE-002 and renderer Probe manuals;
7. CSC, namespace and external-habitability plan;
8. project-control surfaces.

Independent-review capacity is scarce. Use it only for closed, bounded packages:

- Package A: DPA-600 and DPA-700 plus synchronized ADRs, traceability, diagrams and internal audit;
- Package B: DPA-800, Probe manuals and controlled import/PR plan;
- Package C: DPA-900, CSC/habitability and final cross-DPA integration.

Do not ask the independent reviewer to co-author open drafts. Prepare complete packages first, then request evidence-backed verification against an exact Lab ref.

## Immediate assignment

Continue with Package A.

### Primary objective

Develop DPA-600 first, then DPA-700, as coherent architecture candidates suitable for later independent verification.

### DPA-600 required scope

At minimum cover:

- local Workspace locks and same-process reentrancy boundaries;
- base, source, target and contract drift;
- branch and pull-request concurrency;
- workflow serialization;
- stale-plan rejection;
- regeneration after drift;
- interaction with renderer-derived plans;
- interaction with acceptance state and recovery;
- fail-loud behavior;
- evidence and rollback obligations;
- prohibition of treating a local lock as cross-ref serialization.

### DPA-700 required scope

At minimum cover:

- full projection, split projection, managed-head hybrid and no-migration outcomes;
- candidate qualification and rejection;
- preservation of non-owned bytes;
- rollback before and after accepted writes;
- renderer-version change or disappearance;
- acceptance-state rollback;
- interrupted migration recovery;
- prohibition of automatic historical-prose merge;
- operator and evidence obligations.

### Required synchronization

For each coherent normative step, update as applicable:

- relevant ADRs or `DECISIONS.md`;
- traceability;
- diagrams;
- `specs/dpa/README.md`;
- `STATUS.md`;
- `ROADMAP.md`;
- assumptions and main-repository-validation markers.

Do not copy review prose directly into normative specifications. Review findings become normative only through Maintainer adjudication.

## Working method

1. Inspect the current DPA-600 and DPA-700 stubs and dependencies.
2. Identify unresolved decisions before writing normative text.
3. Create a bounded work branch from current `main`.
4. Draft DPA-600 in small coherent commits.
5. Run the Lab gates after each meaningful synchronization point.
6. Perform an internal consistency audit against DPA-000 through DPA-500.
7. Only after DPA-600 is coherent, proceed to DPA-700.
8. Prepare Package A with an exact immutable review ref and a concise independent-review prompt.
9. Do not merge a review-ready promotion until the required review, Maintainer adjudication and post-adjudication verification path has completed.

## Stop conditions

Stop and report instead of guessing when:

- a required main-repository fact lacks exact-ref evidence;
- DPA-600 or DPA-700 would contradict an earlier stable or review-ready contract;
- a proposal would introduce a parallel registry, lifecycle, Workspace, evidence, state, renderer, writer or gate system;
- a new runtime authority lacks an accepted decision;
- work crosses from remote preparation into Probe execution or production mutation;
- a Maintainer decision is required;
- the current repository state differs materially from the summary above.

## Required first response

Do not start drafting immediately. First complete the bootstrap and provide the required session-start report. Then state the proposed bounded first slice for DPA-600, including:

- files to inspect or change;
- decisions required;
- expected traceability and diagram effects;
- validation and gate plan;
- explicit exclusions.

Proceed without unnecessary follow-up questions when the repository contracts already resolve the issue. Ask the Maintainer only for decisions that cannot be derived from the current evidence and governance.

---
