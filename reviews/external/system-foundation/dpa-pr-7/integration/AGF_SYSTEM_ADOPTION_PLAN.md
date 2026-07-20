# AGF System Adoption Plan

Status: proposal
Status-date: 2026-07-20

## Purpose

Assess and prepare bounded DPA adoption of the Agentic Governance Framework system model without changing current DPA authority, phase gates or the canonical `MASTERPLAN.md` sequence.

## Authority

- AGF is authoritative only for reusable governance-method definitions.
- This DPA Lab remains authoritative for DPA architecture specifications, reviews and adjudication within its documented scope.
- `vfi64/agentic-project-kit` remains authoritative for runtime implementation and repository facts.
- This document does not constitute adoption, stability or implementation.

## Candidate adoptions

1. Common typed-object vocabulary for rule, evidence, decision, adoption and projection relations.
2. Repository-local append-only capture ledger for still-ungoverned DPA ideas and questions.
3. Explicit separation of capture, DPA planning, review evidence and implementation evidence.
4. Bounded LLM-context projections with source refs, authority, freshness and unresolved-conflict metadata.
5. Federated relation model connecting DPA specifications to AGF rules and later Kit implementation evidence without copying authority.

## DPA-specific work required

- map AGF object and relation types to DPA-100 terminology;
- determine whether DPA-200 through DPA-900 require bounded amendments;
- define canonical object-to-document and object-to-LLM-context projection contracts;
- define semantic-equivalence, freshness and provenance validation;
- ensure no second document registry or lifecycle system is introduced;
- add traceability from adopted AGF requirements to DPA specifications and reviews;
- preserve the existing exact-ref Probe and adjudication requirements.

## Legacy-note treatment

Existing DPA plans, ADRs, decisions, assumptions, evidence and review records are already governed artifacts and must not be bulk-imported as active captures. Mixed documents require classification; only still-ungoverned material may enter a capture ledger.

## Kit dependency hold

Any DPA conclusion requiring Kit planning or implementation must be recorded as `NEEDS_MAIN_REPO_VALIDATION` and deferred. Kit documentation changes are blocked until the Maintainer has Mac access and can use the Kit's native document-lifecycle, planning and gate commands.

## Proposed sequence

1. AGF foundation review and adjudication.
2. DPA terminology and invariant compatibility review.
3. Bounded specification amendment plan.
4. Independent primary review and technical verification.
5. Maintainer adjudication.
6. Integration into the canonical DPA `MASTERPLAN.md` only through its governed update process.
7. Later controlled import into the Kit after exact-ref validation.

## Exit criteria

- no authority leakage;
- no parallel DPA lifecycle or registry;
- exact mapping of adopted terms and relations;
- explicit rejected or adapted AGF elements;
- all Kit-dependent claims remain evidence-gated;
- local DPA masterplan remains the sole execution authority.