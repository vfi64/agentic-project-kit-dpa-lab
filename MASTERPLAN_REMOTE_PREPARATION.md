# DPA Masterplan Annex — Remote Preparation and Staged Independent Verification

Status: active

Status-date: 2026-07-18

Parent-plan: `MASTERPLAN.md`

Superseded-by: n/a

## 1. Authority and purpose

This document is a governed execution annex to `MASTERPLAN.md`. It defines how the remaining architecture, Probe, implementation-planning, import-planning and habitability work MAY be prepared remotely during the no-Mac period and how independent verification capacity is to be used efficiently before main-repository implementation.

This annex does not replace `MASTERPLAN.md`, `LAB_EXECUTION_CONTRACT.md`, `ROADMAP.md`, normative DPA specifications, accepted ADRs or exact-ref evidence. Where they conflict, current exact-ref evidence and normative contracts prevail.

The governing division of labor is:

- this Lab and the current ChatGPT workstream: drafting, consolidation, traceability, Probe design, test matrices, import planning, slice planning and review-package preparation;
- independent reviewer such as Claude: bounded verification of closed artifacts against exact Lab refs, without alternative architecture development unless a blocker requires it;
- Mac/main-repository phase: exact-ref Probe execution, local revalidation, implementation, tests, gates, evidence and governed mutation.

No remote preparation may be represented as executed Probe evidence, implementation evidence, main-repository conformance or operational safety.

## 2. Work that may be prepared remotely

The following eight work areas MAY be advanced from the iPhone/remote environment.

### 2.1 DPA-600 — Concurrency and workflow serialization

Prepare:

- local Workspace-lock semantics;
- same-process reentrancy boundaries;
- base, source, target and contract drift;
- branch and pull-request concurrency;
- workflow serialization;
- stale-plan rejection;
- regeneration after drift;
- interaction with renderer-derived plans;
- interaction with acceptance state and recovery;
- fail-loud behavior;
- traceability, decisions and diagrams.

Remote completion means a coherent review candidate only. It does not prove that the main repository implements the contract.

### 2.2 DPA-700 — Migration and rollback

Prepare:

- full-projection, split-projection, managed-head-hybrid and no-migration outcomes;
- candidate selection constraints;
- preservation of non-owned bytes;
- rollback before and after accepted writes;
- renderer-version change and disappearance;
- acceptance-state rollback;
- recovery from interrupted migration;
- prohibition of automatic historical-prose merge;
- rollback evidence and operator obligations;
- traceability, decisions and diagrams.

### 2.3 DPA-800 — DP1 through DP5 implementation contract

Prepare:

- DP1 Discovery, Probe and Assessment entry and exit criteria;
- DP2 first production projection;
- DP3 controlled rollout;
- DP4 status-authority discovery and conditional migration;
- DP5 staged strict lifecycle-gate adoption;
- dependencies among DP slices;
- exact-ref requirements;
- evidence and rollback per slice;
- stop conditions;
- Maintainer decisions;
- distinction between planning, validation, implementation and adoption.

DP2 implementation remains blocked by the governing conditions in `MASTERPLAN.md`.

### 2.4 DPA-900 — sustainable governance and review economics

Prepare:

- risk classes;
- triggers for the full review path;
- bounded fast paths for non-normative metadata and proven editorial-only changes;
- diff-scoped equivalence verification;
- independent-context verification triggers;
- escalation when equivalence is unproven;
- machine-checkable synchronization controls;
- review-cost and defect-rate measures;
- Maintainer override and fallback rules;
- prohibition of assurance reduction merely to save review cost.

### 2.5 Controlled import and pull-request plan

Prepare:

- artifact-to-destination mapping;
- ADR and specification import order;
- main-repository PR slice boundaries;
- dependencies and stop gates;
- required tests and audit suites;
- rollback per slice;
- status and handoff updates;
- which Lab artifacts remain historical rather than imported;
- prevention of a second runtime authority.

### 2.6 Probe manuals

Prepare complete execution manuals for:

- PROBE-001;
- PROBE-002;
- DPA-400 renderer Probes.

Each manual MUST include:

- exact purpose and governing requirements;
- fixture identifiers;
- setup preconditions;
- command sequence placeholders;
- expected results;
- PASS, FAIL, PARTIAL and BLOCKED rules;
- negative cases;
- evidence schema;
- cleanup and rollback;
- repeatability requirements;
- known limitations;
- adjudication mapping.

The command sequence may remain provisional until the current main-repository ref and local environment are confirmed.

### 2.7 CSC, namespace and external-habitability plan

Prepare:

- namespace-profile validation;
- Workspace-path checks;
- registry and boot-source behavior;
- lifecycle and report behavior;
- transfer and handoff;
- state and lock paths;
- GUI readiness;
- removed-source audit;
- protected planning paths;
- silent legacy fallback detection;
- external-repository adoption sequence;
- repeatability and second-operator evidence.

### 2.8 Project control surfaces

Prepare and maintain:

- phase and slice status table;
- dependency matrix;
- DPA/Probe/DP/PR traceability matrix;
- risk register;
- decision queue;
- verification queue;
- exact-ref evidence ledger pointers;
- blocked-work register;
- parked editorial register;
- next-action field.

These control surfaces are planning aids and MUST NOT become a parallel runtime state or evidence system.

## 3. Remote preparation sequence

The preferred preparation sequence is:

1. DPA-600;
2. DPA-700;
3. shared DPA-500/600/700 traceability and diagrams;
4. DPA-800;
5. Probe manuals;
6. controlled import and PR plan;
7. DPA-900;
8. CSC, namespace and habitability plan;
9. final project-control synchronization.

The sequence MAY be adjusted when an earlier unresolved contract blocks later work. It MUST NOT be adjusted merely to bypass a required review or exact-ref validation dependency.

## 4. Staged independent verification strategy

Independent-review capacity is scarce and MUST be spent on closed, bounded packages rather than open-ended co-authoring.

### Package A — DPA-600 and DPA-700

The package SHOULD contain:

- exact Lab ref;
- DPA-600 and DPA-700 candidates;
- related ADRs;
- synchronized traceability;
- diagrams;
- internal audit;
- explicit unresolved main-repository validation needs.

The reviewer verifies:

- consistency with DPA-300 through DPA-500;
- completeness of concurrency layers;
- preservation and rollback completeness;
- absence of new runtime authority or parallel systems;
- correctness of repository-fact classifications;
- readiness for Maintainer adjudication and possible review-ready promotion.

### Package B — DPA-800, Probe manuals and import plan

The reviewer verifies:

- executable clarity of DP1 through DP5;
- strict separation of Discovery, Probe, Assessment and implementation;
- entry and exit criteria;
- exact-ref and evidence obligations;
- absence of premature production-form selection;
- whether Probe cases test the actual normative claims;
- whether import and PR slices preserve existing authorities;
- whether rollback and stop conditions are complete.

### Package C — DPA-900, CSC/habitability and final integration

The reviewer verifies:

- review-cost reduction without reduced assurance;
- correct classification of full-path versus bounded-path changes;
- escalation rules;
- consistency with the established DPA-300 through DPA-500 review practice;
- external habitability criteria;
- final cross-DPA consistency and closeout readiness.

## 5. Reviewer prompt contract

Every independent verification request MUST:

- identify repository and exact ref;
- require the Lab bootstrap and authority order;
- list the exact files in scope;
- state the normative and evidence boundaries;
- forbid reliance on chat memory;
- ask for verification rather than alternative architecture generation;
- require exact anchors for every finding;
- classify findings as blocker, major, minor or editorial;
- distinguish architecture defects from `NEEDS_MAIN_REPO_VALIDATION`;
- require an explicit overall verdict;
- state whether Maintainer adjudication, bounded amendment, rerun or no change is recommended.

Preferred instruction:

> Verify the closed artifact set against the existing normative contracts and exact Lab ref. Do not redesign the architecture unless a demonstrated blocker makes the current contract unsound. Report only evidence-backed blocker, major, minor and editorial findings with exact anchors, consequences and proposed dispositions.

## 6. Review economy rules

To conserve independent-review capacity:

- do not submit incomplete drafts;
- do not ask the reviewer to repeat repository summaries already recorded in canonical files;
- do not submit each small edit separately;
- consolidate coherent artifacts and synchronize derived files before review;
- perform an internal consistency audit first;
- provide a closed file list and exact ref;
- separate architecture review from later main-repository implementation verification;
- reuse prior accepted findings only through exact references, not by copying review prose into normative text;
- send follow-up verification only after Maintainer adjudication and bounded amendments are complete.

## 7. Mandatory governance path after review

For every normative candidate or bounded amendment:

1. preserve the reviewed exact ref;
2. record independent findings under `reviews/`;
3. perform Maintainer adjudication;
4. update accepted decisions;
5. amend normative and derived artifacts together;
6. preserve the post-adjudication exact ref;
7. run independent post-adjudication verification when required by the governing DPA status and risk class;
8. disposition all findings;
9. perform status-only promotion only after the verification gate passes.

No review finding becomes normative without adjudication.

## 8. Boundary with the Mac phase

The following remain Mac/main-repository work:

- local confirmation of remote revalidation;
- exact Probe-ref freezing;
- execution of PROBE-001, PROBE-002 and renderer Probes;
- actual focused, negative, recovery and integration tests;
- mutation of production code;
- execution of portability slices;
- gate and CI evidence;
- DP2 implementation;
- external-repository adoption execution;
- habitability evidence.

Remote work may prepare these operations completely but MUST NOT claim their execution.

## 9. Immediate next work order

The next new chat SHOULD:

1. bootstrap from the current Lab `main` ref;
2. confirm `MASTERPLAN.md` and this annex as active planning authorities;
3. inspect the current DPA-600 and DPA-700 stubs and their dependencies;
4. create a bounded work branch for DPA-600 and DPA-700 architecture development;
5. draft DPA-600 first;
6. synchronize ADRs, traceability, diagrams, STATUS and ROADMAP as required;
7. run the Lab gates;
8. prepare Package A for later independent verification;
9. avoid any main-repository mutation or Probe-execution claim.

## 10. Completion condition

This annex is complete when all eight remote-preparation areas have a governed disposition, all three independent-verification packages have been processed or explicitly deferred by Maintainer decision, and the remaining Mac work is reduced to exact-ref validation, evidence-backed amendment and implementation rather than unresolved architecture design.