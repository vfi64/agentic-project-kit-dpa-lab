# Claude Primary Architecture Review — DPA-200 Document Model

Review status: COMPLETE
Review role: primary architecture review
Reviewer: Claude Fable 5
Reviewed repository: `vfi64/agentic-project-kit-dpa-lab`
Reviewed ref: `44a87127fca7f482bc2991f0c258af0a386a7048`
Access outcome: `accessible`
Overall verdict: `ACCEPT_WITH_CHANGES`

This artifact records the maintainer-provided Claude review against the exact immutable ref above. The reviewer cloned the repository, checked out the exact ref, read the complete mandatory bootstrap set in order, inspected the DPA-200 draft, form matrix, traceability, diagrams and pre-review audit, and made no repository writes. No main-repository content was inspected and no implementation claim was upgraded.

## Executive assessment

DPA-200 is substantively complete and may advance to `review-ready` after adjudication. No blocker, hidden parallel system, new runtime authority or false implementation claim was found. The four Phase A obligations delegated to DPA-200—registered regions, target semantics, pre-validation consumer assumptions and historical-region ownership—are discharged.

## Major findings

### R-M01 — Document-form taxonomy is not a partition

Split projection, hybrid document and managed-head projection overlap. The draft permits split projection through separate target identities or disjoint regions, while hybrid also means projected and non-projected regions in one document. The matrix contains the dual result `CONDITIONAL hybrid or split projection`.

Recommended disposition:

- split projection is exclusively a multi-target arrangement;
- any single document with projected and non-projected regions is a hybrid document;
- managed-head is an exceptional hybrid subtype with exactly one leading projected region and one following historical region;
- every legal combination yields exactly one classification.

Maintainer decision required: YES.
Main-repository validation required: NO.

### R-M02 — Boundary-byte ownership is unassigned

The model requires exhaustive non-overlapping byte ownership but does not assign marker, separator or delimiter bytes. Shared boundary control is prohibited, yet no permitted owner exists.

Recommended disposition:

- boundary bytes belong to a document-level partition contract;
- the existing document lifecycle is the exclusive writer of partition bytes;
- renderer output excludes boundary bytes;
- manual or historical edits to boundaries are boundary drift and fail loud.

Maintainer decision required: YES.
Main-repository validation required: NO for the model; concrete marker syntax remains DP1-fenced.

### R-M03 — Trust-state model is inconsistent

DPA-200 owns four states while the matrix and diagram introduce `rejected/abandoned`. The matrix says accepted bytes remain accepted until governed replacement, while the diagram transitions `accepted` to `computed` on drift. The artifacts conflate accepted byte state with a new refresh attempt.

Recommended disposition:

- define one closed trust-state vocabulary;
- add a terminal `abandoned` state for non-accepted attempts;
- accepted bytes remain accepted for the recorded acceptance scope until governed replacement or explicit invalidation by an accepted gate contract;
- detected drift creates findings and starts a new refresh attempt at `computed`; it does not silently mutate the previous byte-state classification;
- distinguish target-byte trust state from refresh-attempt execution state where necessary.

Maintainer decision required: YES.
Main-repository validation required: NO.

### R-M04 — Trust vocabulary is unregistered and collides with `planned`

The consumer trust dimension was not registered under the closed vocabulary model and reused the document-status token `planned`.

Recommended disposition:

- DPA-200 owns the consumer-trust-state dimension through an accepted ADR;
- rename trust `planned` to `plan-captured`;
- use exactly: `computed`, `plan-captured`, `written-unverified`, `accepted`, `abandoned`.

Maintainer decision required: YES.
Main-repository validation required: NO.

## Minor findings

- R-m01: bound the third write-owner class so it can never apply to projected targets or projected regions.
- R-m02: DPA-200 §12 must be the sole normative invalid-state catalog; matrix and tests must cite it.
- R-m03: clarify that DPA trust states apply to generated/projected bytes; manual and historical bytes retain their own authority and are combined at document-level acceptance by DPA-500.
- R-m04: add DM-011 for target-semantics contract completeness.
- R-m05: amend ADR-007 or record that `no migration` is the fourth accepted outcome when evidence is insufficient.

## Editorial findings

- Replace `its own declared canonical sources` with `its declared canonical sources`.
- Use `independently registered` rather than `independently owned` where target identity is intended.
- DPA-ADR-012 need not be listed as a document-model constraint.
- Add DPA-INV-002, DPA-INV-003 and DPA-INV-015 to the direct DPA-200 anchor list.

## Audit conclusions

- Manual document: coherent.
- Full projection: coherent.
- Split projection: coherent constraints but defective classifier until R-M01 is resolved.
- Managed-head: coherent and adequately exceptional; should be a hybrid subtype.
- Hybrid document: coherent after R-M01 and R-M02.
- Registered-region identity: sound and correctly fenced as `NEEDS_MAIN_REPO_VALIDATION` for concrete registry support.
- Canonical-source, configuration, projection-target and historical-region authority: sound.
- Write-owner exclusivity: sound after R-m01.
- Target semantics: sound after DM-011 and boundary ownership.
- Consumer trust boundary: sound architecture with R-M03/R-M04 corrections required.
- Canonical invariants DPA-INV-001 through DPA-INV-017: no contradiction found.
- Accepted ADRs: conforming except ADR-009 is only partial until R-M04 is fixed.
- Traceability: complete in structure; requires DM-011 and re-keying after taxonomy/trust adjudication.
- Main-repository classifications: correct; no invented implementation facts found.

## Final verdict

`ACCEPT_WITH_CHANGES`

DPA-200 may become `review-ready` after adjudication and application of R-M01 through R-M04 plus the bounded cleanup batch. No main-repository evidence is needed for those decisions.