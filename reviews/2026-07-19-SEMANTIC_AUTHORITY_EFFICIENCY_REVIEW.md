# Semantic Authority and Architecture-Efficiency Review

Status: complete

Review-date: 2026-07-19

Reviewed repository: `vfi64/agentic-project-kit-dpa-lab`

Reviewed ref: `8ac3b1b7a97915220232a9d8c2164e03a9c10619`

Reviewer: GPT-5.6 Thinking

Access method: exact-ref GitHub repository inspection

Prior exposure: the reviewer participated in the preceding conceptual discussion; this review therefore does not count as independent post-adjudication verification.

## 1. Scope

This review evaluates the proposal to introduce:

- `DPA-150 — Information Authority Model`;
- `DPA-160 — Semantic Authority Architecture`;
- stable semantic-fact identities;
- semantic dependency graphs;
- fact-level freshness, acceptance and traceability;
- a possible normative-knowledge layer.

The review asks whether those concepts close a real architecture gap and whether they improve the DPA's correctness, simplicity, implementation efficiency and future review economics.

## 2. Governing baseline

The reviewed baseline already establishes:

- canonical state as repository-backed runtime authority for defined domain facts;
- projection authority as bounded authority to derive one target from declared canonical sources;
- projection contracts binding targets, renderers, declared sources, target semantics and lifecycle/freshness policy;
- renderers that must not invent canonical facts;
- derivational freshness from currently authoritative declared sources;
- traceability across requirements, decisions, implementation work, tests, gates, evidence and rollback;
- a closed DPA-000 through DPA-900 specification sequence;
- DPA-000 as the sole owner of architectural invariants;
- DPA-100 as the sole owner of foundational terminology;
- a prohibition against parallel registries, lifecycle systems, freshness systems, evidence systems, state systems and runtime authorities.

## 3. Verdict

**ACCEPT_WITH_CHANGES**

The motivating concern is valid: several documents may represent the same authoritative repository-backed facts, and mutation analysis should identify which authority and writer govern those facts rather than treating filenames as the only architectural unit.

However, separate DPA-150 and DPA-160 normative specifications are not justified on the reviewed baseline.

They would duplicate existing DPA-000 and DPA-100 responsibilities, introduce a second invariant namespace, disturb the established DPA-000 through DPA-900 sequence and increase synchronization and review cost before measurable operational value is demonstrated.

The useful concepts should instead be integrated narrowly into existing contracts and future work only when they replace ambiguity, remove special cases or enable mechanically checkable improvements.

## 4. Accepted claims

### A-01 — Fact authority is a valid analysis dimension

A repository fact may be represented in multiple targets while remaining owned by one canonical authority. Writer and projection analysis should therefore identify the governed fact set and its canonical sources, not merely the target path.

Disposition: accepted as a bounded analytical refinement of existing `canonical state`, `declared source`, `canonical source` and `projection authority` terms.

### A-02 — Duplicate semantic authority is the real prohibited condition

Multiple projections or storage locations are not inherently defects. The defect is conflicting authority or independently maintained representations that claim authority over the same fact set.

Disposition: accepted as a clarification of existing authority rules, not as a new subsystem.

### A-03 — Freshness propagation can improve efficiency

When source-to-target dependencies are declared, a later implementation may determine affected projections and run only relevant regeneration, validation and gates.

Disposition: accepted as a future optimization objective. It requires exact-ref proof that the existing registry and lifecycle can express and consume the necessary dependency information without a second graph or registry.

### A-04 — Semantic diff and impact analysis can improve review quality

A review can be more useful when it explains which governed facts and dependent projections changed, rather than reporting only modified files.

Disposition: accepted as a DPA-900 review-economics objective and possible later main-repository enhancement after evidence and bounded design.

### A-05 — New concepts require measurable simplification

A new term, layer or contract is justified only when it replaces existing ambiguity or special-case rules, enables a mechanical check, reduces mutation or review cost, or materially improves safety.

Disposition: accepted as the primary efficiency criterion for this proposal.

## 5. Rejected or deferred claims

### R-01 — Separate DPA-150 and DPA-160 specifications

Disposition: rejected for the current architecture.

Reasons:

- DPA-100 already owns foundational authority terminology.
- DPA-000 already owns the authority model and all architectural invariants.
- The execution contract and roadmap define a closed DPA-000 through DPA-900 sequence.
- A new pair of foundation documents would create additional synchronization surfaces across DPA-000, DPA-100, traceability, diagrams, ADRs and later specifications.
- No exact-ref evidence demonstrates that this additional layer is required for DP1, Probe preparation or DP2.

### R-02 — A new Semantic Fact registry

Disposition: rejected.

The proposal must not create a second registry, graph store, state model, lifecycle or evidence system. Any later fact identity or dependency metadata must extend an existing accepted authority after main-repository validation.

### R-03 — A separate semantic lifecycle

Disposition: rejected.

`proposed`, `reviewed`, `accepted`, `projected`, `verified`, `historical` and `retired` must not be introduced as a new lifecycle vocabulary. Existing document status, progress status, consumer trust state, lifecycle state and architecture classifications already form closed namespaces.

### R-04 — Fact-level acceptance as a new runtime transition system

Disposition: deferred and currently rejected as an independent mechanism.

DPA-300 and DPA-500 already govern mutation plans, acceptance state, re-acceptance and gate consequences for projected bytes. Any broader interpretation must be proven necessary by Probe evidence and integrated into those existing contracts rather than layered above them.

### R-05 — Normative Knowledge as a new architectural domain

Disposition: deferred to DPA-900 at most.

ADRs, contracts, assumptions, requirements and invariants already have distinct governance roles. A new umbrella domain is not yet shown to simplify implementation or review.

## 6. Confirmed architecture gap

### GAP-SA-01 — Mutation-authority analysis is not yet explicitly tied to governed fact sets

Classification: confirmed architecture-planning gap.

The current DPA clearly separates canonical state, projection authority, lifecycle writing, renderer purity and evidence. The remaining planning gap is narrower: planned command and writer inventory should record which declared canonical fact set each operating mode reads or changes and which projections become affected.

This gap does not require DPA-150 or DPA-160. It can be closed through bounded additions to the command/writer integration plan, Probe fixtures, traceability and later DPA-800 implementation planning.

## 7. Efficiency requirements

Any later adoption of semantic identity, dependency or impact analysis MUST satisfy all of the following:

1. reuse the existing documentation registry, lifecycle, Workspace, findings, gates and evidence authorities;
2. introduce no second registry, state store, lifecycle or gate suite;
3. replace at least one existing ambiguous or duplicated mapping;
4. enable a mechanical check or a bounded reduction in required work;
5. fail loud when authority or ownership is ambiguous;
6. preserve manual-document compatibility;
7. remain optional until exact-ref compatibility is proven;
8. show measurable benefit through at least one of:
   - fewer independently maintained status or handoff facts;
   - fewer writer-specific exceptions;
   - narrower regeneration scope;
   - narrower gate scope without reduced assurance;
   - faster or more precise review;
   - reduced synchronization defects.

## 8. Recommended bounded integration

### 8.1 Current remote preparation

Add governed fact-set and affected-projection fields to the planned command/writer inventory and Probe fixtures as analysis metadata only.

Suggested fields:

- authority scope identifier;
- canonical source set;
- mutation operating mode;
- affected projection targets;
- writer owner;
- ambiguity outcome;
- required post-write verification.

These fields remain proposals until compatibility with the current main-repository structures is revalidated.

### 8.2 DPA-300 through DPA-500

Do not amend these review-ready specifications solely for this proposal.

At the next otherwise-required Probe-driven bounded amendment, evaluate whether a small clarification is necessary. Any normative change must follow the existing Maintainer-adjudication and independent-verification path.

### 8.3 DPA-800

Use the complete writer and command inventory to bind operating modes to canonical source sets, lifecycle-owned targets and verification obligations. This is the primary future home for implementation mapping.

### 8.4 DPA-900

Evaluate semantic impact analysis as a review-economics mechanism. Define measurable success criteria and retain a fallback to full file- and contract-level verification whenever equivalence or dependency completeness cannot be proven.

## 9. Required main-repository validation

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- whether the current documentation registry can express stable authority-scope identifiers without incompatible schema changes;
- whether existing lifecycle reports expose enough per-entry source and target data for dependency analysis;
- whether command operating modes can be inventoried completely from existing command governance;
- whether affected-projection selection can be computed without a parallel dependency database;
- whether selective gates can be safely narrowed without weakening existing assurance;
- whether current handoff and status writers share facts that can be demonstrably consolidated.

## 10. Review limitations

- This is not independent verification because the reviewer participated in the preceding conceptual discussion.
- No Probe was executed.
- No main-repository mutation or production implementation was inspected beyond the lab's recorded exact-ref evidence.
- The review does not authorize normative amendments to stable or review-ready specifications.

## 11. Required next action

Create a bounded non-normative integration plan that translates GAP-SA-01 and the efficiency requirements into the active Package-M remote-preparation work without changing DPA-000 through DPA-500, DPA-600 or DPA-700.
