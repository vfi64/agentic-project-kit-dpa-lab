# Package M Synchronized Amendment — Consistency Correction

Status: review-candidate
Status-date: 2026-07-20
Authority: non-normative bounded correction to the synchronized DPA-200–DPA-500 amendment draft

Resolves:

- `IC-m01`;
- `IC-m02`.

## 1. Boundary and precedence

This correction resolves the two minor findings in:

`reviews/PACKAGE_M_SYNCHRONIZED_AMENDMENT_INTERNAL_CONSISTENCY_AUDIT_20260720.md`.

It does not amend DPA-200 through DPA-500, change ADR-022 status, authorize implementation, execute or amend a Probe, continue DPA-600 or begin DPA-700.

For independent review, this correction controls wherever it narrows or clarifies:

`integration/PACKAGE_M_SYNCHRONIZED_DPA_200_500_AMENDMENT_DRAFT_20260720.md`.

## 2. IC-m01 — Generated-surface repair cannot be accepted by re-acceptance

### 2.1 Correct shared definition

Replace the final sentence of the shared `Generated edit surface` definition with:

> It is not a normal primary edit surface. A durable correction MUST change an authorized canonical source, contract or governed generator path and then regenerate the target through the governed lifecycle. Mutation-free re-acceptance is available only where DPA-500 independently permits it for unchanged target bytes and MUST NOT legitimize a direct repair that changed generated or projected bytes.

### 2.2 Correct DPA-200 emergency-repair condition

Replace the final emergency-repair bullet with:

> - require governed regeneration from the corrected canonical authority before the repaired target can become accepted; mutation-free re-acceptance MUST NOT be used to accept directly repaired generated or projected bytes.

### 2.3 Consequence

A direct repair may preserve operational continuity only under a separately permitted emergency rule. It remains:

- temporary;
- non-accepted;
- non-canonical;
- unable to seed later projection input;
- subject to governed regeneration.

DPA-500 §15.6 remains limited to gate-set-only re-evaluation where all target and source dimensions other than gate-set freshness remain fresh.

## 3. IC-m02 — Aggregate recovery identity remains inside existing authority

Replace the first two insertion-ready DPA-300 recovery paragraphs with:

> Target recovery remains lifecycle-owned per registered target.
>
> For a composed mutation or synchronized projection set, workflow orchestration MAY represent one bounded aggregate recovery identity only through an existing exact-ref-validated workflow or lifecycle recovery structure. That identity references, but does not replace, actual per-target lifecycle outcomes and declared secondary effects.
>
> The aggregate recovery identity MUST NOT establish an independent recovery store, recovery owner, consumer trust state, acceptance state, canonical history, target state or persistence authority. Concrete representation remains `NEEDS_MAIN_REPO_VALIDATION`.

### 3.1 Consequence

The derived aggregate identity may coordinate disposition of unresolved members and effects, but:

- target recovery remains target-scoped and lifecycle-owned;
- per-target acceptance records remain authoritative for their targets;
- existing workflow or lifecycle recovery structures remain the only candidate runtime homes;
- no Package-M or DPA-owned aggregate recovery subsystem is authorized.

## 4. Traceability effect

The existing proposal-local rows remain valid with these clarified interpretations:

- `DMA-002`: direct generated-surface repair requires governed regeneration and cannot be accepted through gate-set-only re-acceptance;
- `DMA-009`: aggregate recovery identity is derived orchestration coordination represented only through an existing validated workflow or lifecycle recovery authority.

No new requirement ID is required.

## 5. Diagram effect

No new diagram node or edge is required.

The existing `workflow orchestration -> derived aggregate attempt result` relationship MUST be interpreted as using existing workflow or lifecycle recovery structures only. It MUST NOT imply a new aggregate recovery store.

## 6. Resolution

### IC-m01

Resolved by excluding direct-repair acceptance through mutation-free re-acceptance and requiring governed regeneration from canonical authority.

### IC-m02

Resolved by fencing the aggregate recovery identity to one existing exact-ref-validated workflow or lifecycle recovery structure and expressly prohibiting independent recovery persistence or ownership.

## 7. Review state

With this correction controlling, the synchronized Package-M amendment package is internally ready for independent review.

It remains non-normative. Repository-specific application still requires local exact-ref validation, explicit Probe-contract disposition, independent review of the exact package and Maintainer acceptance.
