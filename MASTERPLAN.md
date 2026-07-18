# DPA Execution Masterplan

Status: active

Status-date: 2026-07-18

Superseded-by: n/a

## 1. Purpose

This document is the canonical execution plan for the remaining DPA laboratory, exact-ref Probe, main-repository implementation and external-repository habitability work.

It complements, but does not replace:

- `LAB_BOOTSTRAP.md`, which governs session entry and authority order;
- `LAB_EXECUTION_CONTRACT.md`, which governs how work is performed;
- `ROADMAP.md`, which owns the DPA-000 through DPA-900 specification sequence;
- normative DPA specifications and accepted ADRs;
- exact-ref evidence from `vfi64/agentic-project-kit`.

When this plan conflicts with current exact-ref main-repository evidence or a normative DPA contract, the evidence and normative contract prevail. Chat memory is never authoritative.

## 2. Current baseline

### Lab state

- DPA-000 and DPA-100 are `stable`.
- DPA-200, DPA-300, DPA-400 and DPA-500 are `review-ready`.
- DPA-300 through DPA-500 completed their established architecture review, Maintainer adjudication and independent verification paths.
- DPA-400 and DPA-500 remain blocked from `stable` until applicable exact-ref Probe evidence is available and adjudicated.
- The lab contains no production kit code and has not been adopted by the kit.

### Main-repository evidence state

The last recorded DP1 Discovery baseline is:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Every repository-specific observation from that baseline is historical evidence only. Before mutation, it MUST be revalidated against the then-current exact `origin/main` ref and locally confirmed against the actual checkout.

## 3. Governing distinction

The remaining work has two fundamentally different streams.

### 3.1 Probe-independent portability work

Confirmed path-resolution and namespace-portability defects MAY be planned in parallel after current-ref revalidation and MAY be implemented during the Mac/Codex phase when focused tests and namespace negative tests are available.

Typical candidates include:

- direct documentation-registry literals;
- Workspace bypasses;
- pure resolver substitutions;
- confirmed namespace-profile path defects;
- equivalent portability defects that do not alter DPA Probe subjects.

### 3.2 DPA-critical writer and lifecycle work

Writer, lifecycle, acceptance-state, re-acceptance, layered-acceptance and projection-gate changes MUST remain blocked until PROBE-002 has executed and the resulting evidence has been adjudicated.

These paths are Probe subjects and future DP2 implementation surfaces. Premature fixes could change the measurement baseline, prejudge the architecture or invalidate Probe evidence.

## 4. Non-negotiable controls

Before any main-repository mutation:

1. determine the current remote `origin/main` SHA;
2. revalidate the relevant historical finding against that exact ref;
3. record the result and source location;
4. locally synchronize and confirm the same state on the Mac;
5. run the required focused and negative tests;
6. preserve an exact implementation or Probe ref in evidence.

No historical observation may be represented as a current defect without this two-stage revalidation.

No Probe preparation may be represented as Probe execution.

No Lab gate or review result may be represented as main-repository runtime conformance.

## 5. Phase A — remaining iPhone and remote preparation

Phase A is planning and read-only verification work. It does not include local implementation or executed main-repository tests.

Two parallel tracks are allowed.

### Track A — architecture and Probe preparation

#### A1. Determine the current remote main ref

Read-only against GitHub:

- identify the current `vfi64/agentic-project-kit` `origin/main` SHA;
- compare it with historical validation ref `6a9da7d…`;
- inspect every previously evidenced code-level finding;
- record a revalidation matrix using the following outcomes:
  - still present;
  - changed but still relevant;
  - already fixed;
  - no longer found;
  - additional related path discovered;
  - verification blocked.

Remote revalidation is provisional until locally confirmed before mutation.

#### A2. Prepare PROBE-001 completely

PROBE-001 preparation MUST include:

- a proposed `ProjectionContract` fixture;
- a proposed `PartitionContract` fixture;
- manual-registry compatibility controls;
- invalid schema cases;
- unknown schema-version cases;
- unknown-field cases;
- missing-required-field cases;
- target-identity and registered-region representation cases;
- expected parser and validator results;
- explicit PASS, FAIL and PARTIAL criteria;
- bounded evidence schema;
- exact later command sequence;
- cleanup rules;
- repeatability rules;
- limitations and unresolved main-repository mappings.

Preparation does not establish parser compatibility.

#### A3. Prepare PROBE-002 completely

PROBE-002 preparation MUST include:

- immutable mutation-plan fixtures;
- acceptance-state fixtures;
- expected lifecycle phases;
- Workspace-resolution cases;
- local-lock and stale-plan cases;
- Write and post-Write verification cases;
- interruption and recovery cases;
- conditional accepted-base persistence;
- base-independent post-acceptance evaluation;
- gate-set re-acceptance without renderer invocation or target mutation;
- layered acceptance for registered-region projections;
- authorized non-lifecycle-owner evolution;
- out-of-band lifecycle-byte mutation;
- ambiguous ownership failure;
- expected findings, drift classes, trust-state consequences and gate decisions;
- evidence ordering expectations;
- rollback and cleanup contracts;
- explicit boundaries between observed capability and architecture conformance.

Preparation does not establish lifecycle or persistence conformance.

#### A4. Prepare the DPA-400 renderer Probe package

The package MUST cover:

- static renderer-map resolution;
- unknown renderer identifier;
- interface incompatibility;
- semantic-version mismatch;
- implementation-evidence-only change;
- immutable lifecycle-resolved inputs;
- deterministic repeat execution;
- output-type and target-scope validation;
- prohibited filesystem writes;
- prohibited network access;
- prohibited subprocess execution;
- prohibited lock, workflow, state and evidence writes;
- nested-renderer prohibition;
- deterministic semantic resource bounds;
- non-semantic operational abort;
- bounded failure diagnostics;
- negative evidence for prohibited capabilities.

#### A5. Complete the CSC and namespace-profile checklist

At minimum, the checklist MUST inspect:

- documentation-registry literal sweep;
- Workspace resolution;
- boot-source classification and boot contract;
- namespace-profile behavior;
- lifecycle report completeness, including per-entry data;
- transfer and handoff behavior;
- state and lock paths;
- GUI readiness;
- removed-source audit;
- protected planning paths;
- absence of silent legacy fallback;
- repeatability by a second run or operator.

### Track B — Probe-independent portability slice planning

During the iPhone/remote phase, Track B is specification only, not implementation.

For every proposed portability slice, record:

- affected file and symbol;
- historical finding and baseline;
- current remote revalidation result;
- exact Workspace or resolver authority that should replace the direct path;
- smallest bounded code change;
- focused legacy-profile tests;
- namespace-profile negative tests;
- expected no-change areas;
- impact on planned Probe fixtures and validation refs;
- reason the slice does not alter registry schema, lifecycle semantics, writer semantics, acceptance state or gate authority.

Implementation moves to Phase B, where a real local test environment is available.

## 6. Hard mutation freeze before PROBE-002 adjudication

The following MUST NOT be changed as quick fixes before PROBE-002 execution and subsequent architecture revalidation:

- `transfer_repo_actions._refresh_operational_handoff_docs()`;
- every current or newly discovered writer of `docs/handoff/CURRENT_HANDOFF.md`;
- Doc Lifecycle Apply content-writing behavior;
- governed content-writer semantics;
- mutation-plan execution semantics;
- acceptance-state schema or persistence;
- recovery completion semantics;
- gate-set re-acceptance;
- layered-acceptance mechanics;
- projection-specific freshness and gate integration.

A current writer inventory MAY be rebuilt read-only before PROBE-002. Writers themselves remain frozen.

## 7. Phase B — Mac and exact-ref reality contact

Phase B begins with execution, not preparation.

### B1. Establish the local baseline

- synchronize the local repository with `origin/main`;
- record local HEAD, remote head and worktree cleanliness;
- confirm the remote revalidation matrix against local source;
- resolve any remote/local discrepancy before mutation;
- freeze the exact Probe validation ref.

### B2. Execute PROBE-001

Run the prepared registry-parser and validator compatibility suite against the exact Probe ref.

Evidence MUST record:

- repository and exact SHA;
- fixture revision;
- commands;
- expected results;
- actual results;
- return codes;
- bounded logs or report paths;
- limitations;
- PASS, FAIL or PARTIAL conclusion.

### B3. Execute PROBE-002

Run the prepared lifecycle, plan, lock, Write, Verify, acceptance, recovery, re-acceptance and layered-acceptance Probe cases against the exact Probe ref.

PROBE-002 MUST distinguish:

- current observed implementation capability;
- missing implementation;
- incompatible implementation;
- proposed architecture behavior;
- unavailable measurement.

### B4. Execute DPA-400 renderer Probes

Run the prepared renderer-map, determinism, immutable-input, purity, capability-boundary and failure-path cases against the same or an explicitly justified exact ref.

### B5. Execute prepared portability slices in parallel

After local revalidation, pure portability slices MAY run in parallel with Probe work when they:

- do not touch any frozen DPA-critical path;
- do not modify registry schema;
- do not change Probe fixture semantics;
- include focused tests and namespace negative tests;
- document whether a later Probe ref must move.

A portability merge that changes code observed by a Probe requires the affected Probe ref to be re-frozen and the relevant Probe rerun.

## 8. Probe result classification and adjudication

Every discrepancy MUST be assigned to exactly one primary class:

1. implementation conforms to the tested DPA requirement;
2. required implementation is missing;
3. implementation exists but differs from the DPA proposal;
4. a DPA assumption is falsified or incomplete;
5. the Probe or fixture is defective;
6. an additional main-repository reader, writer, parser, resolver or workflow path was discovered;
7. evidence is insufficient or execution is blocked.

For each discrepancy, record:

- exact ref;
- Probe and case identifier;
- affected DPA requirement and ADR;
- observed behavior;
- expected behavior;
- classification;
- whether architecture, implementation, fixture or evidence must change;
- Maintainer decision required;
- verification and rerun obligations.

Probe evidence MUST NOT silently change normative architecture.

## 9. Phase C — DPA revalidation and bounded amendments

After Probe evidence is complete enough for adjudication:

1. revalidate DPA-300 through DPA-500 against exact-ref results;
2. preserve clauses that remain valid;
3. amend only the bounded correction surface established by evidence;
4. update ADRs, traceability, diagrams, Probe mappings and status surfaces together;
5. rerun affected Probes when an amendment changes tested expectations;
6. release the DP2 implementation baseline only after the architecture and evidence are synchronized.

### 9.1 Mandatory amendment verification path

Every normative bounded amendment to a `review-ready` DPA-300, DPA-400 or DPA-500 specification MUST follow the established governance path:

1. exact amendment ref;
2. synchronized normative and derived artifacts;
3. Maintainer adjudication;
4. independent post-adjudication verification;
5. disposition of all verification findings;
6. status decision.

A narrower path is permitted only for changes proven to be non-normative metadata or purely editorial text without contract effect. Unproven equivalence defaults to the full path.

### 9.2 Parked DPA-500 editorials

At the next otherwise-required bounded DPA-300/DPA-500 amendment, disposition:

- **V5-e01** — clarify DPA-500 §9 and DPA-300 §16 so gate-set re-acceptance is described as an acceptance-record update for already-accepted unchanged bytes, not a second transition path into `accepted`;
- **V5-e02** — order or annotate the DPA-500 diagram so re-acceptance eligibility is checked before gate evaluation.

Rules:

- no isolated normative slice is required solely for these editorials;
- they do not block Probe preparation or execution;
- they MUST be included at the next suitable bounded amendment;
- they remain open until committed and synchronization-checked.

## 10. Meaning of review-ready

`review-ready` is sufficient for Probe preparation and later implementation planning.

It is not evidence of:

- production implementation;
- main-repository conformance;
- successful Probe execution;
- adoption;
- operational safety;
- stability.

DP2 implementation MUST begin only after exact-ref Probe execution, result adjudication and any required revalidation of DPA-300 through DPA-500.

## 11. Phase D — DP2 implementation

After the DP2 baseline is released:

1. implement the governed content writer by extending existing registry, lifecycle, Workspace, findings, gates and evidence systems;
2. convert the current writer inventory into a complete migration list;
3. route approved handoff writers through lifecycle-owned bounded replacement;
4. implement immutable plan, under-lock revalidation, Write and post-Write Verify;
5. implement acceptance-state persistence and recovery;
6. implement conditional base persistence;
7. implement gate-set re-acceptance without target mutation;
8. implement layered acceptance and owner provenance for registered regions;
9. integrate projection findings with the existing gate authority;
10. add staged observe, warn, block-new and strict adoption controls without activating strict mode by elapsed time;
11. produce focused, negative, recovery, concurrency and integration evidence.

No second registry, lifecycle, state store, evidence system, Workspace abstraction, writer authority, renderer authority or gate system may be introduced.

## 12. Phase E — external-repository habitability

After the relevant DP2 mechanisms and portability slices are complete:

1. perform controlled adoption in `Comm-SCI-Control-private` or another approved external repository;
2. activate and validate the namespace profile;
3. run the CSC/namespace checklist;
4. verify boot behavior, registry resolution, lifecycle reports, transfer, handoff, GUI, audit, locks, state and recovery;
5. prove absence of silent legacy fallback and kit-internal path assumptions;
6. produce bounded habitability evidence;
7. repeat with a second independent run or operator where feasible.

The adoption test is evidence for external habitability, not automatic proof that every repository is compatible.

## 13. Stability and later specification work

DPA-200 through DPA-500 may be considered for `stable` only after their applicable exact-ref Probe evidence is:

- executed;
- recorded;
- adjudicated;
- reflected in bounded amendments where required;
- independently verified when normative amendments occur.

DPA-600 through DPA-900 continue under `ROADMAP.md` and `LAB_EXECUTION_CONTRACT.md`. Probe evidence SHOULD bound their correction surface before extensive downstream specification work expands it.

## 14. Canonical dependency flow

```text
current remote main ref
→ remote revalidation matrix
→ ┬→ complete Probe fixtures and CSC checklist
  └→ specify pure portability slices
→ local synchronization and confirmation
→ freeze exact Probe ref
→ execute PROBE-001, PROBE-002 and renderer Probes
→ classify and adjudicate evidence
→ revalidate and, where necessary, amend DPA-300 through DPA-500
→ mandatory independent verification of normative amendments
→ release DP2 baseline
→ implement DP2 and pure portability slices
→ external-repository adoption
→ habitability evidence
→ evidence-qualified stability decisions
```

## 15. Governing freeze statement

```text
No handoff-writer, lifecycle-apply, acceptance-state,
re-acceptance, layered-acceptance or projection-gate quick fix
before PROBE-002 and the subsequent architecture revalidation.
```

## 16. Completion criteria for this masterplan

This masterplan is complete when:

- all planned Probes have exact-ref evidence and adjudication;
- historical code findings have current-ref dispositions;
- required bounded DPA amendments and independent verification are complete;
- DP2 is implemented through existing authorities;
- external namespace-profile habitability is evidenced;
- remaining DPA-600 through DPA-900 work is synchronized with the resulting evidence;
- no unresolved blocker is hidden by status wording.