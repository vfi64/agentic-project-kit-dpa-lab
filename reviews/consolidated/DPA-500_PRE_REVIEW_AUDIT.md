# DPA-500 Pre-Review Cross-Artifact Audit

Status: complete
Status-date: 2026-07-17

## 1. Scope

This audit compares the initial DPA-500 draft, traceability and diagram against the current normative contracts in DPA-000 through DPA-400, with particular attention to vocabulary ownership, authority boundaries, acceptance state, renderer consequences and gate integration.

Audited branch baseline before this record:

`bd55da39328c3d8ae7b2c747dfb0639360e94e8b`

The audit is internal pre-review quality control. It is not an external architecture verdict and does not authorize promotion.

## 2. Overall result

**BOUNDED_CORRECTION_REQUIRED**

The DPA-500 architecture direction is coherent, but two vocabulary conflicts and one classification overloading issue must be corrected before an immutable primary-review baseline is frozen.

No parallel lifecycle, renderer, evidence store or production gate authority was found.

## 3. Blocking findings

### A5-M01 — Consumer trust-state vocabulary is reopened

DPA-100 §2.5 owns a closed consumer trust-state vocabulary:

- `computed`;
- `plan-captured`;
- `written-unverified`;
- `accepted`;
- `abandoned`.

The initial DPA-500 §8 additionally uses `stale`, `invalid` and `unknown` as trust states. This contradicts DPA-100's sole vocabulary ownership and combines freshness/evaluation classifications with lifecycle consumer trust state.

Required correction:

1. Preserve the DPA-100 trust-state vocabulary unchanged.
2. Define a separate DPA-500 freshness-evaluation classification, for example:
   - `fresh`;
   - `stale`;
   - `invalid`;
   - `indeterminate`.
3. State explicitly that freshness classification does not replace or silently rewrite consumer trust state.
4. Retain `abandoned` only as the terminal refresh-attempt trust state defined by DPA-100/DPA-300.
5. Update finding fields, renderer consequences, tests, traceability and diagram wording accordingly.

### A5-M02 — Gate outcome vocabulary conflicts with DPA-100

DPA-100 §6.6 defines an existing governed gate as a pass, warning or failure decision. The initial DPA-500 §11 introduces four abstract outcomes: `pass`, `warn`, `block`, `error`.

This creates a competing gate vocabulary and risks turning an evaluation-mechanism error into a fourth production gate result.

Required correction:

1. Use the DPA-100 gate-decision vocabulary:
   - `pass`;
   - `warning`;
   - `failure`.
2. Treat inability to evaluate reliably as an evaluation failure that maps fail-closed to gate decision `failure` for mutation, acceptance, integration and strict validation.
3. Preserve a structured reason or finding distinguishing policy failure from machinery/input evaluation failure.
4. Update traceability, conformance tests and diagram labels.

### A5-M03 — Closed drift vocabulary is mixed with findings and failure conditions

DPA-100 §7.5 owns the closed drift classes:

- base drift;
- source drift;
- target drift;
- contract drift;
- renderer drift;
- partition drift;
- ownership drift.

The initial DPA-500 §9 labels twenty-two heterogeneous items as drift classes. Several are valid refinements, but others are missing-state conditions, renderer failures, write-verification failures or evidence failures rather than drift.

Required correction:

1. Preserve DPA-100's seven drift classes as the only top-level drift vocabulary.
2. Define DPA-500 finding categories or reason codes beneath them.
3. Map examples explicitly:
   - projection/partition contract mismatch → contract drift;
   - configuration or target-semantics mismatch → contract drift unless a later accepted DPA-100 amendment creates another top-level class;
   - renderer identifier/interface/semantic mismatch → renderer drift;
   - preserved-region or partition-boundary mismatch → partition drift or ownership drift as applicable;
   - gate-set mismatch and acceptance-state defects → state/gate findings, not new drift classes;
   - nondeterminism, capability violation, operational abort, diagnostics, write verification and evidence failure → lifecycle or renderer findings, not drift.
4. Keep independent subreasons separately reportable.

## 4. Non-blocking observations

### A5-m01 — Acceptance-state completeness

The draft correctly separates acceptance state from evidence and captures the required renderer, source, contract, target and gate-set identities. Review should specifically test whether base/ref identity belongs in persistent acceptance state or only in operation-scoped plans and integration evidence.

### A5-m02 — Gate-set freshness

The draft correctly requires gate-set identity, but the exact ownership and compatibility rule remains `NEEDS_MAIN_REPO_VALIDATION`. The review should check whether every gate-set change makes existing accepted bytes stale or whether some policy-only changes require re-evaluation without semantic target staleness.

### A5-m03 — Evidence-recording failure after verified Write

The draft appropriately avoids fabricating success, but exact ordering among verification, acceptance-state persistence and evidence persistence remains unresolved. This is correctly fenced for Probe/main-repository validation and must remain visible in DPA-500 and DPA-800.

### A5-m04 — Enforcement-stage vocabulary

`observe`, `warn`, `block-new` and `strict` are policy-stage names, not gate outcomes or trust states. The revised text must state this explicitly to prevent cross-dimension status composition.

## 5. Confirmed strengths

The audit confirms that the draft:

- reuses the existing main-repository lifecycle and gate authority;
- keeps renderers outside freshness, finding, severity, trust and acceptance authority;
- treats freshness as multidimensional and not time-based;
- preserves independent source, target, contract, renderer and partition comparisons;
- keeps acceptance state as lifecycle state rather than evidence;
- blocks unsafe new mutation and acceptance in every staged mode;
- distinguishes renderer semantic version from implementation evidence;
- preserves manual and historical bytes for registered-region projections;
- treats `written-unverified` as non-accepted and recovery-sensitive;
- keeps production mappings and switches behind `NEEDS_MAIN_REPO_VALIDATION`.

## 6. Required synchronized artifacts

The bounded correction must synchronize:

1. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`;
2. `traceability/DPA-500_TRACEABILITY.md`;
3. `diagrams/dpa-500-freshness-gates.mmd`;
4. `STATUS.md` only if the next-step wording changes;
5. PR #3 description if terminology in its summary becomes stale.

DPA-100 must not be changed merely to legitimize accidental vocabulary introduced by the DPA-500 draft. A DPA-100 amendment is warranted only if review demonstrates that the existing closed vocabulary is structurally insufficient.

## 7. Freeze decision

The Primary-Review baseline is **not frozen** at `bd55da39328c3d8ae7b2c747dfb0639360e94e8b`.

Freeze is permitted only after:

- A5-M01 through A5-M03 are corrected;
- traceability and diagram are synchronized;
- the durable Lab gates pass on the corrected head;
- a final targeted vocabulary search finds no conflicting current normative usage.

## 8. Next action

Apply the bounded correction set, run the deterministic Lab gates, commit an immutable review-baseline record, and then issue the independent Claude primary-review prompt bound to that exact commit.