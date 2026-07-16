# DPA-300 Restructure — Independent Equivalence Verification

Status: COMPLETE
Date: 2026-07-16
Result: PASS_WITH_EXPLICIT_RATIFICATION

## 1. Metadata

- Repository: `vfi64/agentic-project-kit-dpa-lab`
- Certified baseline: `a86aa49851c96c39380a8eb4afad17763263fe00`
- Restructured target: `e3f8b85c5eb76b8c6cae76dde317fd33f236ce88`
- Verifier: Claude Fable 5
- Role: independent equivalence verifier under DPA-ADR-020
- Main-repository access: none
- Repository writes by verifier: none

This verification is bounded to semantic equivalence of the DPA-300 normative body. It is not a new architecture review, adjudication or implementation assessment.

## 2. Method

The verifier:

1. extracted both DPA-300 versions verbatim;
2. mechanically compared all normative sentences containing `MUST`, `MUST NOT`, `MAY` or `SHOULD`;
3. compared every structured field and requirement list item by item;
4. classified each non-verbatim mapping as `UNCHANGED`, `EDITORIAL_ONLY`, `STRENGTHENED`, `WEAKENED`, `REMOVED` or `CHANGED_MEANING`;
5. checked that traceability, diagrams, DPA-000/100/200, ADRs and evidence artifacts were byte-identical between the compared refs where claimed.

Mechanical result: 78 normative sentences in the certified text and 66 in the restructured text. Every difference was adjudicated.

## 3. Overall finding

No load-bearing architecture rule was lost or changed in a way that alters registry authority, lifecycle authority, renderer boundaries, gates, drift classes, recovery, acceptance state, partition ownership, evidence authority or Probe boundaries.

The restructure is not fully semantically identical. It contains a bounded and exhaustively enumerated set of weakenings, relocations, keyword relaxations and strengthenings requiring explicit Maintainer disposition.

## 4. Required dispositions

### 4.1 Weakened details

- **R-W1 — target identity:** the standalone mutation-plan field `target identity` was removed. Reinstate it because one parent entry may contain multiple region targets and recovery must match the same target explicitly.
- **R-W2 — missing required fields:** the generic validation rejection for missing required fields was removed. Reinstate it.
- **R-W3 — partition-byte encoding:** explicit partition-byte encoding was replaced by line-ending behavior. Reinstate encoding while retaining line-ending behavior.
- **R-W4 — policy identifiers:** lifecycle, freshness and evidence policy fields no longer require identifiers. Maintainer must either permit inline policies explicitly or restore identifier semantics.

### 4.2 Changed with preserved coverage

- **R-C1 — undeclared versus missing sources:** validation changed from undeclared canonical sources to missing canonical sources. Undeclared input use remains prohibited at the renderer boundary. Ratification must record this ownership split.
- **R-C2 — review-ready self-assessment:** the sentence claiming all review-ready criteria are satisfied was not true for the restructured text at promotion time. It may become true only after this verification and explicit ratification, or must be rewritten to cite the equivalence-verification record.

### 4.3 Removed sections with surviving distributed content

- **R-R1 — planned DP1 Probes:** the consolidated Probe section was removed while equivalent obligations remain in the Probe backlog and traceability. Reinstate at least a normative pointer and the rule that falsified mappings return to adjudication.
- **R-R2 — conformance checklist:** the consolidated seventeen-item checklist was removed while its requirements remain distributed. Reinstatement is recommended because the checklist is valuable for DP2 planning.

### 4.4 Normative-keyword relaxations

Restore explicit normative force for:

- **R-K1:** the existing registry `MUST remain` the sole registry authority;
- **R-K2:** validation `MUST be` side-effect free;
- **R-K3:** failure before Write `MUST leave` target bytes unchanged;
- **R-K4:** validation must explicitly reject unknown contract **or partition** schema versions;
- **R-K5:** later inspection `MUST compare` current observations with accepted state.

### 4.5 Strengthenings and additions

Explicit acceptance is recommended for:

- the 27-item invalid-state catalog;
- source-drift anti-mislabeling;
- prohibition of a second render for the same valid plan;
- explicit Workspace path coverage and hard-coded-path prohibition;
- DISC-003b writer-inventory rebuild requirement;
- added schema, configuration, ownership, acceptance-scope and gate-set fields;
- identity-critical evidence `MUST` versus contextual `SHOULD` split;
- expanded fail-loud conditions.

## 5. Mapping summary

The full comparison established:

- authority boundaries: preserved;
- registry and lifecycle sole-writer model: preserved;
- renderer prohibitions: preserved or strengthened;
- parent-entry PartitionContract and byte ownership: preserved or strengthened;
- lifecycle phases and trust transitions: preserved;
- stale-plan and drift model: preserved;
- locking, atomic replacement and preserved-region rules: preserved;
- acceptance-state record and direct-write detection: preserved or strengthened;
- interrupted-refresh recovery: preserved;
- evidence non-authority: preserved;
- command adaptation and no-parallel-writer rule: preserved or strengthened;
- main-repository validation fence: preserved or strengthened;
- traceability, diagrams and referenced ADR relationships: byte-identical between compared refs except for the DPA-300 body changes enumerated above.

## 6. Verdict

`PASS_WITH_EXPLICIT_RATIFICATION`

The certified verification chain may extend to the restructured DPA-300 text only after the Maintainer explicitly disposes R-W1 through R-W4, R-C1 through R-C2, R-R1 through R-R2 and R-K1 through R-K5, and accepts the enumerated strengthenings.

The natural implementation vehicle is a governed normative amendment commit. It must not be a promotion commit.
