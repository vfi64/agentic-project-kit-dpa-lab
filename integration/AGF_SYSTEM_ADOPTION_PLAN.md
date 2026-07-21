# AGF System Adoption Plan

Status: proposal
Status-date: 2026-07-21

## Purpose

Assess and prepare bounded DPA adoption of selected Agentic Governance Framework method concepts without changing current DPA authority, phase gates, stable/review-ready specifications or the canonical `MASTERPLAN.md` sequence.

## Authority

- AGF is authoritative only for reusable governance and reasoning method definitions within its adopted scope.
- The DPA Lab remains authoritative for representation, document and projection architecture specifications, reviews and adjudication within its documented scope.
- `vfi64/agentic-project-kit` remains authoritative for runtime implementation and repository facts.
- ROS may state operating-profile requirements but does not own DPA projection semantics or Kit runtime state.
- This document does not constitute adoption, stability, implementation or authorization to amend DPA specifications.

## Governance boundary

AGF may contribute method concepts such as evidence, challenge, review, adjudication, adoption and falsification. DPA owns:

- canonical representation and document-region semantics;
- projection contracts and projection acceptance;
- freshness, provenance and semantic-equivalence rules;
- DPA trust and lifecycle states;
- renderer and writer implications within DPA scope.

AGF method terms must be mapped explicitly and may not silently redefine DPA-100 terminology or DPA acceptance states.

## Candidate adoptions

1. Minimal method-level interchange fields for evidence, review, adjudication and adoption references.
2. Explicit separation of capture, DPA planning, review evidence and implementation evidence.
3. A repository-local intake mechanism only for still-ungoverned ideas, subject to later Kit-local adjudication.
4. One parameterized bounded context-projection contract carrying source refs, authority, freshness, conflicts, purpose, active role, token budget and priority/eviction policy.
5. Loose federation through validated, versioned interchange records connecting repository-local canonical state without copying authority.
6. Derived cross-repository indexes or system views only as rebuildable, non-authoritative projections.

## Rejected architecture elements

The following are not adopted by this plan:

- a shared live cross-repository graph;
- AGF ownership of DPA object or relation schemas;
- a second DPA document registry or lifecycle system;
- ROS ownership of DPA projection types;
- automatic Kit or application adoption;
- treating a coordination plan or context projection as canonical state.

## DPA-specific work required

- map only the selected AGF method terms to DPA-100 terminology;
- identify exact AGF↔DPA governance boundaries and collision cases;
- determine whether any DPA-200 through DPA-900 amendment is necessary after the existing probe, review and adjudication gates;
- define the parameterized canonical-object-to-context-projection contract;
- define semantic-equivalence, freshness, provenance and authority validation for interchange records and derived views;
- define priority and eviction behavior under token budgets;
- ensure no second registry, lifecycle or acceptance authority is introduced;
- add traceability from explicitly adopted AGF method requirements to DPA specifications and reviews;
- preserve exact-ref probe, review and adjudication requirements.

Stable or review-ready DPA specifications remain unchanged until a separate governed amendment plan satisfies their existing gates.

## Legacy-note treatment

Existing DPA plans, ADRs, decisions, assumptions, evidence and review records are already governed artifacts and must not be bulk-imported as active captures. Mixed documents require classification; only still-ungoverned material may enter an intake mechanism.

## Federation and interchange

Each repository retains its canonical graph or structured state. DPA projections may consume exact-ref, schema-versioned interchange records. Any cross-repository index is a derived projection and must report source refs, schema owners, freshness and unresolved conflicts. It cannot write back authority or replace repository-local state.

## Kit dependency hold

Any DPA conclusion requiring Kit planning or implementation must be recorded as `NEEDS_MAIN_REPO_VALIDATION` and deferred. Pre-existing Kit PR #1867 is unadjudicated work and creates no DPA or Kit adoption. Kit changes remain blocked until the Maintainer has Mac access and can use native document-lifecycle, planning and gate commands.

## Experimental pilot boundary

A future pilot may test the projection and interchange concepts only if it is isolated, reversible, exact-ref bound and marked `NON_ADOPTED_EXPERIMENT`. Pilot artifacts must not modify stable DPA authority or become production state by accretion. Measures and baseline comparisons must be pre-registered.

## Proposed sequence

1. Complete AGF scope correction and maintainer adjudication.
2. Perform DPA terminology and invariant compatibility analysis.
3. Define a bounded, non-mutating projection/interchange experiment plan.
4. Complete the existing DPA probe, review and adjudication gates relevant to any affected specification.
5. Prepare a bounded specification amendment plan only where evidence requires it.
6. Run independent primary review and technical verification.
7. Obtain maintainer adjudication.
8. Integrate approved work into the canonical DPA `MASTERPLAN.md` only through its governed update process.
9. Later perform controlled Kit import after exact-ref validation and local Kit adoption.

## Exit criteria

- no authority leakage;
- loose federation selected and shared-live-graph semantics excluded;
- no parallel DPA lifecycle, registry or acceptance authority;
- exact mapping of adopted, adapted and rejected AGF elements;
- one parameterized projection contract rather than premature projection-system proliferation;
- all Kit-dependent claims remain evidence-gated;
- stable/review-ready DPA specifications remain protected until governed amendment;
- the local DPA masterplan remains the sole DPA execution authority.