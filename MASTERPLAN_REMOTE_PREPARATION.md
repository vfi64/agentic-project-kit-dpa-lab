# DPA Masterplan Annex — Remote Preparation and Staged Independent Verification

Status: active

Status-date: 2026-07-18

Parent-plan: `MASTERPLAN.md`

Superseded-by: n/a

## 1. Authority and purpose

This document is a governed execution annex to `MASTERPLAN.md`. It defines how Probe preparation, portability planning, later downstream architecture work, import planning and habitability planning MAY be advanced remotely during the no-Mac period.

This annex does not replace `MASTERPLAN.md`, `LAB_EXECUTION_CONTRACT.md`, `ROADMAP.md`, normative DPA specifications, accepted ADRs or exact-ref evidence. If this annex conflicts with the sequencing or mutation freezes in `MASTERPLAN.md`, the Masterplan prevails.

The governing division of labor is:

- this Lab and the current ChatGPT workstream: drafting, consolidation, traceability, Probe design, test matrices, import planning, slice planning and review-package preparation;
- an independent reviewer such as Claude: bounded verification of closed artifacts against exact Lab refs;
- the Mac/main-repository phase: exact-ref Probe execution, local revalidation, implementation, tests, gates, evidence and governed mutation.

No remote preparation may be represented as executed Probe evidence, implementation evidence, main-repository conformance or operational safety.

## 2. Governing sequencing rule

Probe preparation and Probe-independent portability planning precede substantive downstream specification of DPA-600 through DPA-900.

DPA-600 through DPA-900 MAY receive bounded exploratory drafts before Probe execution only when all of the following hold:

- the draft remains `draft`;
- it contains no repository-specific `VERIFIED` claim;
- concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`;
- it does not displace preparation of Probe manuals, fixtures, evidence contracts or adjudication rules;
- it does not select a production implementation;
- it does not weaken the mutation freeze in `MASTERPLAN.md`.

A bounded exploratory draft MUST be frozen when its next material decisions depend on unexecuted Probe evidence.

## 3. Remote preparation sequence

The binding preparation sequence is:

1. shared Probe execution and evidence contract;
2. PROBE-001 manual and fixtures;
3. PROBE-002 manual and fixtures;
4. DPA-400 renderer Probe manual and fixtures;
5. current-ref revalidation and exact Probe-ref freeze procedures;
6. CSC and namespace-profile checklist;
7. Probe-independent portability slice specifications;
8. bounded DPA-600 and DPA-700 drafts, constrained by available evidence;
9. controlled import and pull-request plan;
10. DPA-800 and DPA-900 only to the extent not dependent on unexecuted Probe evidence;
11. final project-control synchronization.

The sequence MAY be adjusted only when an earlier artifact is blocked by a documented dependency. It MUST NOT be adjusted merely to use available drafting capacity or to bypass required review, exact-ref validation or Probe preparation.

## 4. Active package — Remote Probe Preparation

The active work package is **Package P — Remote Probe Preparation**.

### P1. Shared Probe contract

Prepare:

- common terminology and identifiers;
- exact-ref requirements;
- fixture identity and revision rules;
- setup and environment recording;
- expected-result encoding;
- PASS, FAIL, PARTIAL and BLOCKED criteria;
- bounded evidence schema;
- observation, interpretation and adjudication separation;
- cleanup, rollback and repeatability rules;
- command placeholders that may remain provisional until local confirmation.

### P2. PROBE-001

Prepare:

- `ProjectionContract` and `PartitionContract` fixtures;
- manual-registry compatibility controls;
- invalid schema, unknown version, unknown field and missing field cases;
- target identity and registered-region cases;
- expected parser and validator results;
- evidence and cleanup contracts.

Preparation does not establish parser compatibility.

### P3. PROBE-002

Prepare:

- immutable plan and acceptance-state fixtures;
- Workspace, local-lock and same-process reentrancy cases;
- stale-plan and guard mismatch cases;
- Write, Verify, Record and Release ordering;
- interruption and recovery cases;
- conditional accepted-base persistence;
- base-independent post-acceptance evaluation;
- gate-set re-acceptance without renderer invocation or target mutation;
- layered acceptance for registered-region projections;
- ownership, out-of-band mutation and ambiguous-owner cases;
- expected findings, trust-state and gate decisions;
- evidence ordering, cleanup and rollback.

Preparation does not establish lifecycle, persistence, recovery or acceptance conformance.

### P4. DPA-400 renderer Probes

Prepare:

- static renderer-map resolution;
- unknown renderer and interface incompatibility;
- semantic-version and implementation-evidence changes;
- immutable lifecycle-resolved inputs;
- deterministic repeat execution;
- output-type and target-scope validation;
- prohibited filesystem, network, subprocess, lock, workflow, state and evidence writes;
- nested-renderer prohibition;
- deterministic semantic resource bounds;
- non-semantic operational abort;
- bounded failure diagnostics.

### P5. Exact-ref and adjudication procedure

Prepare:

- current remote-main identification;
- historical-finding revalidation matrix;
- local confirmation requirements;
- exact Probe-ref freeze and ref-move rules;
- evidence directory and manifest expectations;
- discrepancy classification;
- Maintainer adjudication record;
- architecture-amendment and Probe-rerun obligations.

## 5. Frozen DPA-600 draft

PR #5 and branch `spec/dpa-600-concurrency` contain a bounded initial DPA-600 draft.

That draft is frozen while Package P is active:

- DPA-600 remains `draft`;
- no `review-ready` promotion is permitted;
- no material expansion into concrete main-repository locking, workflow, branch-protection, merge-queue, recovery or rollback mechanics is permitted;
- DPA-700 MUST NOT begin;
- existing DPA-600 artifacts MAY receive only sequencing, status, evidence-boundary or defect-correction edits required to preserve consistency.

After Package P is complete, DPA-600 may resume only within the remaining evidence-independent surface. Material Probe-dependent decisions wait for applicable Probe evidence and adjudication.

## 6. Probe-independent portability planning

During the remote phase, portability work is specification only.

Every proposed portability slice MUST record:

- affected file and symbol;
- historical baseline and current remote revalidation result;
- Workspace or resolver authority;
- smallest bounded change;
- focused legacy-profile and namespace-profile negative tests;
- expected no-change areas;
- impact on Probe fixtures and validation refs;
- reason the slice does not alter registry schema, lifecycle semantics, writer semantics, acceptance state or gate authority.

Implementation remains Mac/main-repository work.

## 7. Later downstream architecture work

After Package P and portability planning:

- DPA-600 and DPA-700 MAY continue as bounded drafts;
- DPA-800 MAY prepare DP entry, exit, evidence and stop criteria without claiming implementation readiness;
- DPA-900 MAY prepare governance and review-economics rules without reducing assurance;
- controlled import and PR planning MAY proceed without selecting a second runtime authority.

No downstream document may outrank exact-ref evidence or silently pre-adjudicate Probe results.

## 8. Independent verification packages

Independent-review capacity MUST be spent on closed, bounded packages.

### Package P review

The reviewer verifies:

- executable clarity of the shared Probe contract and manuals;
- separation of preparation, execution, observation, interpretation and adjudication;
- exact-ref and evidence obligations;
- negative-path coverage;
- cleanup, rollback and repeatability;
- whether Probe cases test the actual normative claims;
- absence of implementation or conformance claims.

### Later DPA-600/700 review

A later package MAY contain DPA-600 and DPA-700 only after the sequencing gate permits resumed work. Promotion beyond `draft` requires an explicit Maintainer decision and must not precede applicable Probe evidence where the candidate depends on it.

### Final integration review

DPA-800, DPA-900, import planning, CSC/habitability and final cross-DPA consistency are reviewed only after their upstream dependencies are closed.

## 9. Review and merge controls

Every verification request MUST identify the exact Lab ref, closed file list, normative boundaries, evidence boundaries and explicit verdict requested.

For governed normative batches whose assurance depends on commit sequence:

- squash merge MUST NOT be used;
- merge-commit or another method preserving the governed commit sequence MUST be selected;
- the selected merge method MUST be recorded before merge;
- source commit SHAs and review refs MUST be preserved in durable evidence, not only in a deletable branch.

The historical branch `spec/dpa-500-freshness-gates` SHOULD be retained until its governed commit sequence is durably recorded outside the branch.

## 10. Boundary with the Mac phase

The following remain Mac/main-repository work:

- local confirmation of remote revalidation;
- exact Probe-ref freezing;
- execution of PROBE-001, PROBE-002 and renderer Probes;
- focused, negative, recovery and integration tests;
- production-code mutation;
- execution of portability slices;
- gate and CI evidence;
- DP2 implementation;
- external-repository adoption and habitability evidence.

Remote work may prepare these operations completely but MUST NOT claim their execution.

## 11. Immediate next work order

The current and next sessions MUST:

1. treat Package P as the active package;
2. keep PR #5 as a frozen Draft PR;
3. complete the shared Probe contract;
4. prepare PROBE-001, PROBE-002 and renderer Probe manuals and fixtures;
5. prepare exact-ref freeze, evidence and adjudication procedures;
6. synchronize STATUS, ROADMAP and handoff surfaces;
7. run the Lab gates;
8. avoid DPA-700 and material DPA-600 expansion;
9. avoid main-repository mutation or Probe-execution claims.

## 12. Completion condition

This annex is complete when all remote-preparation areas have a governed disposition, Package P is closed and reviewable, later downstream architecture work is evidence-bounded, merge controls are recorded, and the remaining Mac work is reduced to exact-ref validation, execution, adjudication and implementation rather than unresolved Probe design.