# DPA-200 — Document-Form Decision Matrix

Status: draft
Status-date: 2026-07-15
Owner: `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
Superseded-by: n/a

## 1. Purpose and authority

This matrix is a normative companion to DPA-200. It makes permitted and prohibited combinations of document form, target identity, region ownership, source authority, write ownership, trust state and rollback explicit.

DPA-200 remains the normative owner of the document model. This matrix MUST NOT redefine DPA-000, DPA-100 or DPA-200 terms. A conflict is resolved in favor of DPA-000, DPA-100 and then DPA-200, in that order, until the matrix is reconciled.

Concrete main-repository schemas, marker conventions, candidate documents, readers, writers and lifecycle behavior remain `NEEDS_MAIN_REPO_VALIDATION`.

## 2. Decision symbols

- `PERMITTED`: structurally conforming when all listed preconditions are satisfied.
- `CONDITIONAL`: permitted only after the named evidence and later-spec obligations are satisfied.
- `PROHIBITED`: violates the DPA authority or ownership model.
- `NOT_APPLICABLE`: the dimension does not apply to that form.

A `PERMITTED` or `CONDITIONAL` entry is not a production-form selection. DP1 MUST still prove the authority, reader, writer, compatibility and rollback graph at an exact validation ref.

## 3. Document-form matrix

| Form | Projection target | Required regions | Semantic source | Projected write owner | Manual/history write owner | Consumer trust | Selection status |
|---|---|---|---|---|---|---|---|
| Manual document | none | none required by DPA | existing authoritative state, outside a projection contract | NOT_APPLICABLE | governed manual editing under existing lifecycle rules | existing behavior preserved | PERMITTED |
| Full projection | complete registered document | one full-target ownership domain | declared canonical sources plus contract-declared configuration | existing document lifecycle | none inside target | accepted only after lifecycle validation and required gates | CONDITIONAL |
| Split projection | separate target or disjoint registered regions | projected current component plus separately owned historical/manual component | projected component from declared canonical sources only | existing document lifecycle | explicit governed owner for non-projected component | each consumed component must expose its trust and authority role | CONDITIONAL |
| Managed-head projection | one leading registered region | projected head plus following historical region | head from declared canonical sources; history is not semantic renderer input | existing document lifecycle for head | explicit governed historical writer | current-state consumers must not treat history as current authority | EXCEPTIONAL / CONDITIONAL |
| Hybrid document | one or more projected regions within one document | complete, non-overlapping region partition | each projected region from its own declared canonical sources | existing document lifecycle for projected regions | explicit governed owner for every manual region | consumer contract must identify authoritative current region | EXCEPTIONAL / CONDITIONAL |

## 4. Form-selection preconditions

### 4.1 Manual document

A manual document is conforming when:

- no projection contract is present;
- existing registry and lifecycle behavior remains unchanged;
- no DPA path silently treats the document as projected;
- malformed optional projection metadata fails explicitly rather than falling back silently.

### 4.2 Full projection

Full projection is permitted only when:

- every target byte is reproducible from declared canonical sources and contract-declared configuration;
- no independently maintained prose remains inside the target;
- the complete reader and writer graph is known;
- rollback can restore the prior tracked target and registry state;
- target identity and target semantics are unambiguous;
- required gates establish the consumer trust boundary.

Full projection is prohibited when any target byte depends on undocumented manual knowledge or non-canonical historical prose.

### 4.3 Split projection

Split projection is permitted only when:

- current deterministic representation and non-canonical history can be assigned separate target identities or disjoint registered regions;
- each component has one write owner;
- consumers can distinguish current authoritative representation from historical material;
- normalization and boundary rules cannot cause cross-component mutation;
- rollback preserves both components without inventing a history source.

### 4.4 Managed-head projection

Managed-head projection is permitted only as a justified exception when:

- the head is a precisely bounded registered region;
- the following historical region has an explicit writer and edit policy;
- append behavior cannot change the projected head or its boundaries;
- source, target, base and contract drift are checked before integration;
- competing branches or pull requests cannot integrate stale head assumptions;
- drift recovery regenerates the head and never auto-merges historical prose;
- rollback inputs are recoverable from Git history or another already-authoritative source.

### 4.5 Hybrid document

A hybrid document is permitted only when:

- all bytes belong to exactly one declared region ownership domain;
- projected and manual regions are non-overlapping;
- every projected region is one independently registered target;
- a renderer invocation computes exactly one registered region;
- manual edits cannot alter projected boundaries or projected bytes;
- consumers know which region carries current authoritative representation;
- DPA-300, DPA-500, DPA-600 and DPA-700 define the required lifecycle, gate, serialization and rollback behavior.

## 5. Region-combination matrix

| Projected region | Manual region | Historical region | Boundary ownership | Result |
|---|---|---|---|---|
| absent | complete document | optional within manual ownership | existing manual contract | PERMITTED manual document |
| complete document | absent | absent | full target | CONDITIONAL full projection |
| one disjoint region | one disjoint region | optional within manual region | explicit and non-overlapping | CONDITIONAL hybrid or split projection |
| leading region | absent | one following region | explicit projected/history boundary | EXCEPTIONAL managed-head projection |
| multiple projected regions | absent | absent | each region independently registered and non-overlapping | CONDITIONAL hybrid projection |
| projected region | overlapping manual region | any | ambiguous | PROHIBITED |
| projected region | unowned bytes | any | incomplete | PROHIBITED |
| projected region | any | history used as undeclared semantic input | any | PROHIBITED |
| multiple projected regions computed by one renderer invocation | any | any | any | PROHIBITED |
| projected append into historical region | any | any | shared or moving boundary | PROHIBITED |

## 6. Authority and write-owner matrix

| Region class | Runtime authority role | Semantic renderer input | Permitted write owner | Prohibited owner or behavior |
|---|---|---|---|---|
| Canonical source | owns declared domain facts | yes, when declared | existing authoritative mechanism | renderer mutation; target-derived circular authority |
| Contract-declared configuration | representation input, not domain-fact authority | yes, when declared and versioned | governed configuration owner | hidden input; unversioned output-affecting state |
| Projected target or region | bounded authoritative representation after acceptance | no, unless independently declared canonical by another accepted contract | existing document lifecycle | renderer, workflow, evidence producer or ad hoc manual writer |
| Manual region | human-maintained content under explicit ownership | no by default | governed manual editor | lifecycle projection write without contract |
| Historical region | evidentiary or human history, not canonical by default | no | explicit governed historical writer | automatic merge, reconstruction as authority or renderer semantic input |
| Evidence record | supports inspection and audit | no | evidence-producing governed mechanism | production runtime input or target write ownership |

## 7. Trust-state transition matrix

| From | To | Permitted by | Required condition | Consumer representation |
|---|---|---|---|---|
| none | computed | renderer | declared inputs resolved; no repository mutation | not accepted |
| computed | planned | lifecycle planner | contract and expected output validated for planning | not accepted |
| planned | written-unverified | lifecycle writer | explicit mutation authorization, lock and stale-plan revalidation | not accepted |
| written-unverified | accepted | lifecycle plus governing gates | post-write reproducibility and required checks complete | accepted for stated scope |
| any pre-accepted state | rejected/abandoned | lifecycle or workflow | failed validation, drift, cancellation or supersession | must not be presented as accepted |
| accepted | planned replacement | lifecycle planner | new source, target, base or contract context | existing accepted bytes remain accepted until governed replacement |

No renderer, manual editor or workflow coordinator may directly declare output `accepted`.

## 8. Invalid combinations

The following combinations are unconditionally prohibited:

1. A projection target with no declared canonical source for a rendered fact.
2. A renderer that writes its own output.
3. A target or region with multiple write owners.
4. Overlapping registered regions.
5. A byte range not covered by any ownership domain in a hybrid document.
6. Historical prose used as semantic input without an independent accepted authority decision.
7. Evidence used as production runtime input.
8. A workflow treated as semantic write owner.
9. A target considered accepted before required validation and gates complete.
10. Automatic textual merge of projected output and historical prose during drift recovery.
11. Rollback that depends on a newly invented or unavailable history source.
12. Silent fallback from malformed projection metadata to manual behavior.
13. One renderer invocation computing multiple independently registered targets.
14. A region boundary controlled by both projected and manual writers.
15. Append-only renderer behavior that moves or consumes a historical boundary.
16. Selection of a production form solely from a candidate-document label or model opinion.

## 9. Delegated enforcement ownership

| Obligation | Normative owner |
|---|---|
| Registry representation and contract validation | DPA-300 |
| Lifecycle planning, locking, atomic write and direct-write detection | DPA-300 |
| Renderer input, purity and one-target behavior | DPA-400 |
| Trust-state gates, drift findings and acceptance criteria | DPA-500 |
| Cross-branch and cross-PR serialization | DPA-600 |
| Migration choice, historical ownership and rollback | DPA-700 |
| DP1 evidence and DP2–DP5 implementation sequence | DPA-800 |

Delegation MUST NOT weaken the DPA-200 authority or ownership model.

## 10. DP1 evidence checklist for form selection

Before selecting any production document form, DP1 MUST record:

- exact validation ref;
- registry identity and compatibility evidence;
- complete byte-level or region-level target identity;
- canonical authority for every rendered fact;
- contract-declared configuration and fingerprint domain;
- all readers and their read order;
- all writers and mutation paths;
- region boundaries and malformed-boundary behavior;
- current and historical content classification;
- consumer trust and gate placement;
- local and cross-ref concurrency requirements;
- rollback source and demonstrated recoverability;
- reason lower-risk forms were accepted or rejected.

If this evidence is incomplete or contradictory, the required decision is `no migration`.

## 11. Traceability

This matrix primarily operationalizes:

- `DPA-INV-001` through canonical-source separation;
- `DPA-INV-002` through `DPA-INV-004` through renderer/lifecycle write separation;
- `DPA-INV-005` through cross-ref requirements for exceptional forms;
- `DPA-INV-008` and `DPA-INV-009` through one-target and no-chaining constraints;
- `DPA-INV-010` through evidence exclusion;
- `DPA-INV-011` and `DPA-INV-012` through existing-system ownership;
- `DPA-INV-014` through historical-prose merge prohibition;
- `DPA-INV-015` through dry-run planning before mutation;
- `DPA-INV-017` through exact-ref DP1 evidence.

Relevant decisions include DPA-ADR-001, DPA-ADR-002, DPA-ADR-003, DPA-ADR-005, DPA-ADR-006, DPA-ADR-007, DPA-ADR-009 and DPA-ADR-010.

## 12. Review obligations

This matrix remains `draft` until:

- DPA-200 and this matrix use identical form and trust-state terminology;
- every `CONDITIONAL` entry has a named later-spec owner;
- negative combinations map to planned validation tests;
- rollback obligations cover every permitted projected form;
- no entry implies a current main-repository capability without exact evidence;
- the matrix and DPA-200 are reviewed against one exact ref.
