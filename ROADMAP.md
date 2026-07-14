# Roadmap

Status: active
Status-date: 2026-07-14

## Specification sequence

1. DPA-000 — Vision and architectural principles
2. DPA-100 — Foundations and terminology
3. DPA-200 — Document model
4. DPA-300 — Registry and lifecycle integration
5. DPA-400 — Renderer contract
6. DPA-500 — Freshness and gates
7. DPA-600 — Concurrency and workflow serialization
8. DPA-700 — Migration and rollback
9. DPA-800 — DP1–DP5 implementation specification
10. DPA-900 — Future evolution
11. Main-repository validation
12. Lab adoption with agentic-project-kit
13. Controlled import into `vfi64/agentic-project-kit`

## Phase A adjudication work order

The Claude Fable 5 review at reviewed ref `1a73ec435a09d0367cb7e9f123241d9f61550b0f` is a non-normative review input. The following work order governs its integration. No item becomes normative before adjudication.

1. Record the complete Claude review under `reviews/claude/`. — COMPLETE
2. Record every finding and deferred obligation in `planning/PHASE_A_REVIEW_BACKLOG.md`. — COMPLETE
3. Collect separate ChatGPT and Gemini Phase A reviews against an exact common baseline. — PLANNED
4. Adjudicate F-M01 and record the accepted classification/status model as DPA-ADR-009. — PLANNED; MAINTAINER DECISION REQUIRED
5. Adjudicate F-M02 and record canonical invariant-register ownership as DPA-ADR-010. — PLANNED; MAINTAINER DECISION REQUIRED
6. Adjudicate F-M03 and record the recorded-baseline evidence bar as DPA-ADR-011 or an explicit part of ADR-009. — PLANNED; MAINTAINER DECISION REQUIRED
7. Adjudicate the minor terminology, phase-gate, traceability and diagram findings. — PLANNED
8. Apply accepted normative changes only after the consolidated adjudication record exists. — BLOCKED BY STEPS 3–7
9. Create only minimal static baseline evidence records; do not introduce lab evidence tooling or a second evidence system. — PLANNED
10. Regenerate Phase A traceability against the accepted invariant IDs and status model. — PLANNED
11. Reassess Phase A exit criteria from their declared single owner and update `STATUS.md`. — PLANNED

## Review-derived specification obligations

These items are planning obligations, not accepted normative requirements until adjudicated.

### DPA-200 — Document model

- Define `registered region`, including boundary representation, ownership and drift semantics.
- Define `target semantics`, including full replacement, region replacement, encoding and normalization responsibilities.
- Define consumer assumptions for projection output that exists before validation and merge gates complete.
- Assign ownership rules for historical regions in hybrid or managed-head documents.

### DPA-300 — Registry and lifecycle integration

- Specify missing-canonical-source validation and fail-loud behavior.
- Specify detection and findings for lifecycle bypass and direct target writes.
- Specify partial-write and interrupted-mutation recovery obligations.
- Preserve the existing lifecycle as the sole projection writer.

### DPA-400 — Renderer contract

- Define contract-declared versioned configuration as an explicit renderer input channel.
- Reconcile declared sources, canonical sources and contract-declared configuration.
- Specify undeclared-input, side-effect, recursion and static-resolution negative tests.

### DPA-500 — Freshness and gates

- Define the gate placement that prevents unvalidated projection output from being treated as accepted repository state.
- Map structural, source, target, base and contract drift into existing findings and staged gate behavior.
- Preserve the rule that time alone cannot hard-fail.

### DPA-600 — Concurrency and workflow serialization

- State explicitly that DP2 local lifecycle integration does not authorize multi-PR refresh before workflow serialization exists.
- Specify stale-base, competing-PR and regeneration behavior.

### DPA-700 — Migration and rollback

- Require rollback inputs to be recoverable from Git history or another already-authoritative source.
- Specify write ownership for retained historical regions.
- Preserve the prohibition on automatic historical-prose merging.

### DPA-800 — DP1–DP5 implementation specification

- Include exact-ref evidence-record obligations.
- Carry all `NEEDS_MAIN_REPO_VALIDATION` items into DP1 entry and exit criteria.
- Distinguish recorded baseline context from fresh implementation validation.

## Prohibitions during adjudication

- Do not modify normative DPA meaning from a single model review.
- Do not mark Phase A stable before required reviews are collected and adjudicated.
- Do not create production kit code in the lab.
- Do not create a richer evidence store, generator or parallel governance system.
