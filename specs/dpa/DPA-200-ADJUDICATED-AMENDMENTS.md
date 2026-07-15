# DPA-200 — Adjudicated Amendments

Status: review-ready
Status-date: 2026-07-15
Owner: `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
Decisions: DPA-ADR-013, DPA-ADR-014

## 1. Authority and precedence

This normative companion records the adjudicated amendments to the DPA-200 draft after the primary architecture review and secondary technical verification.

Until the owning DPA-200 text and matrix are mechanically consolidated, this file has precedence over conflicting statements in:

- `specs/dpa/DPA-200-DOCUMENT-MODEL.md`;
- `specs/dpa/DPA-200-DOCUMENT-FORM-MATRIX.md`;
- `diagrams/dpa-200-region-ownership.mmd`;
- `diagrams/dpa-200-trust-states.mmd`;
- `traceability/DPA-200_TRACEABILITY.md`.

It MUST NOT override DPA-000, DPA-100 or an accepted ADR.

## 2. Primary document-form classifier

Every document instance MUST resolve to exactly one primary form:

1. **manual document** — no projection contract;
2. **full projection** — one complete registered document is one projected target;
3. **split projection** — two or more independently registered target identities separate current projected representation from non-canonical historical or explanatory material;
4. **hybrid document** — one registered document contains one or more projected registered regions and one or more non-projected regions;
5. **managed-head projection** — an exceptional hybrid subtype with exactly one leading projected region and exactly one following historical region.

A single document containing projected and non-projected regions MUST NOT be classified as split projection.

Subtype information MAY accompany the primary form but MUST NOT produce two primary outputs.

## 3. Partition and boundary ownership

A multi-region document MUST have one document-level partition contract.

The partition contract owns:

- boundary markers;
- separators and delimiters between regions;
- boundary normalization;
- ordering and adjacency constraints;
- malformed, missing or duplicate boundary behavior.

Partition bytes are written exclusively by the existing document lifecycle.

Renderers MUST return region payload bytes only and MUST NOT emit partition bytes.

Manual and historical writers MUST NOT modify partition bytes.

Any out-of-band partition-byte change is boundary drift and MUST fail loud through DPA-300/DPA-500.

All document bytes MUST belong to exactly one of:

- one projected region;
- one manual region;
- one historical region;
- the partition contract.

No byte may have multiple owners or no owner.

## 4. Write-owner extension bound

No later DPA contract may assign a projected target or projected region to a writer other than the existing document lifecycle.

Any extensible write-owner class applies only to non-projected regions and MUST preserve DPA-INV-004.

## 5. Consumer trust-state dimension

DPA-200 owns the closed consumer-trust-state dimension:

- `computed`;
- `plan-captured`;
- `written-unverified`;
- `accepted`;
- `abandoned`.

The token `planned` MUST NOT be used as a consumer trust state.

### 5.1 State meanings

- `computed`: renderer output exists in memory; lifecycle validation is incomplete.
- `plan-captured`: a governed mutation plan exists; no accepted repository state is claimed.
- `written-unverified`: lifecycle-owned bytes exist in a governed workspace; post-write validation or gates are incomplete.
- `accepted`: required validation, reproducibility checks and governing gates completed for the stated acceptance scope.
- `abandoned`: a non-accepted refresh attempt ended through failure, cancellation or supersession; its bytes MUST NOT be represented as accepted.

### 5.2 Drift semantics

Detected drift MUST produce findings and MAY block integration under DPA-500.

A new refresh attempt starts at `computed`.

Drift MUST NOT silently or retroactively rewrite the recorded trust state of previously accepted bytes.

A later accepted DPA-500 contract MAY explicitly invalidate an acceptance scope through a governed finding/gate rule.

### 5.3 Mixed-document acceptance

Trust states apply to generated/projected bytes.

Manual and historical bytes retain their declared authority and ownership semantics. DPA-500 MUST define document-level acceptance for a hybrid document from:

- projected-region trust states;
- partition-contract validity;
- manual/historical region validation obligations;
- consumer read assumptions.

## 6. Invalid-state ownership

DPA-200 owns the sole normative invalid document-model catalog. The following are invalid:

1. missing or ambiguous canonical authority;
2. ambiguous target identity;
3. overlapping registered regions;
4. unowned bytes;
5. duplicate write ownership;
6. missing, duplicate, malformed or shared-control partition boundaries;
7. renderer output containing partition bytes;
8. manual or historical mutation of partition bytes;
9. undeclared semantic renderer input;
10. evidence or historical prose used as runtime authority without an accepted authority decision;
11. consumer acceptance asserted before required validation;
12. automatic historical-prose merge;
13. unavailable or invented rollback source;
14. silent fallback from malformed projection metadata to manual behavior;
15. one renderer invocation computing multiple independently registered targets;
16. production form selection without DP1 evidence;
17. a model requiring a parallel registry, lifecycle, freshness, evidence, Workspace or gate system.

The matrix and traceability negative tests are derived mappings and MUST cite these items rather than define competing catalogs.

## 7. Target-semantics completeness

A target-semantics contract missing any required DPA-200 declaration is invalid and MUST fail loud.

Traceability requirement `DM-011` owns planned completeness validation for:

- replacement mode;
- encoding;
- line endings;
- normalization;
- terminal newline;
- partition-boundary handling;
- empty-output validity;
- malformed-boundary behavior;
- append prohibition;
- fingerprint input domain.

## 8. Migration hierarchy

The accepted hierarchy is:

1. full projection;
2. split projection;
3. managed-head projection as an exceptional hybrid subtype;
4. no migration when authority, ownership, compatibility, trust or rollback cannot be established.

The fourth outcome is an accepted additive consequence of DPA-ADR-007.

## 9. Delegated obligations

- DPA-300: partition validation, lifecycle transitions, direct-write detection and atomic mutation.
- DPA-400: payload-only renderer output and partition-byte rejection.
- DPA-500: boundary drift, trust-state gates, explicit acceptance invalidation and mixed-document acceptance.
- DPA-600: stale active-attempt and cross-ref behavior.
- DPA-700: partition-preserving migration and rollback.
- DPA-800: DP1 evidence and form-selection output.

## 10. Review-ready consequence

DPA-200 may be promoted to `review-ready` only after the owning text, matrix, diagrams and traceability are mechanically synchronized with this amendment and a bounded post-adjudication verification reports no remaining contradiction.