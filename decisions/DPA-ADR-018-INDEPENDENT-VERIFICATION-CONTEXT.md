# DPA-ADR-018 — Independent Verification Context for High-Risk Changes

Status: PROPOSED
Date: 2026-07-15

## Context

Across the Phase A, DPA-200 and DPA-300 review cycles, implementation sessions reliably verified their intended invariant and decision changes but repeatedly missed cross-artifact residues and evidence-discipline defects. A fresh session from the same model family found those defects by reading the committed artifact without having authored the change.

The relevant separation is therefore not product identity. It is separation between authorship context and verification context.

The main repository already treats chat memory as non-authoritative and requires exact-ref evidence for governed work. Later DP2–DP5 implementation will introduce mutation-capable slices whose gate evidence must not merely restate the implementing session's intent.

## Proposed decision

For a high-risk governed change, the session that authors or applies the mutation MUST NOT be the sole session that certifies its final gate evidence.

A qualifying independent verification context MUST:

- start from the exact immutable implementation or adjudication ref;
- read the applicable bootstrap, contracts and evidence without relying on the author's chat memory;
- disclose prior exposure and whether it authored the verified change;
- verify committed artifacts and outputs rather than the author's stated intent;
- report PASS or FAIL with exact findings and limitations;
- remain distinct in context from the authoring session, even when the same model family or product is used.

This rule applies by default to:

- normative contract or governance changes;
- changes to registries, lifecycle writers, locks, gates, evidence contracts or protected workflow behavior;
- mutation-capable DP2–DP5 slices;
- post-adjudication or post-remediation verification that authorizes promotion, merge or strict enforcement.

It does not apply automatically to low-risk editorial changes, spelling fixes or mechanically generated changes whose correctness is fully covered by deterministic tests and an existing gate. The governing workflow MUST classify the verification requirement by risk rather than require a full second bootstrap for every commit.

## Alternatives considered

1. Require a different named AI product — rejected because product identity does not guarantee contextual independence.
2. Allow the authoring session to self-certify every change — rejected because repeated lab evidence shows an authorship blind spot for cross-artifact residues.
3. Require independent verification for every commit — rejected as disproportionate and likely to create process inflation.
4. Replace maintainer adjudication or real-repository Probes with model independence — rejected because context separation does not protect against shared model blind spots or incorrect architecture assumptions.

## Rationale

Authors tend to verify the intended transformation. A fresh context must reconstruct the actual state and is more likely to detect residue, stale references and classification drift.

Context independence is complementary to, not a replacement for:

1. deterministic tests and gates;
2. independent artifact verification;
3. maintainer adjudication;
4. exact-ref Probes against the real repository.

## Consequences

- DPA-800 SHOULD define the concrete risk classes, evidence fields and workflow handoff for DP2–DP5.
- The main-repository implementation plan SHOULD add an independent-verifier identity or context field to qualifying gate evidence.
- Review governance remains role-based under DPA-ADR-012; no model vendor becomes mandatory.
- Low-risk work retains a bounded fast path.
- The cost of a second bootstrap is accepted only where an incorrect promotion, mutation or enforcement decision has material consequences.

## Validation status

PROPOSAL based on repeated lab review evidence. It becomes normative only after maintainer adjudication and synchronization with DPA-800 and the eventual main-repository governance contracts.

## Affected specifications and phases

- DPA-800 — DP1–DP5 implementation specification;
- DP2–DP5 gate and evidence workflow;
- controlled import planning;
- future main-repository mutation and review governance.
