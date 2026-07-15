# Phase A Consolidated Adjudication

Status: active
Status-date: 2026-07-15
Architecture baseline: `1a73ec435a09d0367cb7e9f123241d9f61550b0f`
Review-integration baseline: `1bf72d1313335b6acfe5af960dd7315f42a7756a`

## Inputs

- Primary architecture review: `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md`
- Secondary technical verification: `reviews/chatgpt/CHATGPT_PHASE_A_TECHNICAL_VERIFICATION_AUDIT.md`
- Maintainer instruction: implement the recommended adjudication decisions

Gemini access attempts are classified `access-blocked`; they are not architecture reviews and are not adjudication inputs.

## Executive disposition

- Foundational architecture contradiction: none.
- Hidden parallel subsystem: none.
- New runtime authority: none.
- Overall architecture disposition: `ACCEPT_WITH_CHANGES`.
- Phase A stability: not yet granted; final consistency and remaining cleanup are required.

## Major findings

### F-M01 — Status vocabulary

Disposition: ACCEPTED.

Resolution: DPA-ADR-009 separates repository-fact classifications, document status, progress status and access outcome. DPA-100 owns the closed vocabularies.

### F-M02 — Invariant ownership

Disposition: ACCEPTED.

Resolution: DPA-ADR-010 makes DPA-000 §7 the sole canonical invariant owner with stable IDs `DPA-INV-001` through `DPA-INV-017`. LEC and traceability are derived references.

### F-M03 — Baseline evidence records

Disposition: ACCEPTED WITH SEVERITY CLARIFICATION.

The defect is major for governance and evidence discipline but is not a foundational architecture defect. DPA-ADR-011 requires bounded static records and prohibits richer lab evidence tooling.

## Minor findings

- F-m01: ACCEPTED. LAB_EXECUTION_CONTRACT §9 owns phase exit criteria; STATUS is a tracking view.
- F-m02: ACCEPTED editorially. Use `runtime authority` rather than `runtime truth source`.
- F-m03: ACCEPTED. Traceability now has one row per canonical invariant with decision links.
- F-m04: ACCEPTED. DPA-100 defines `validation ref`.
- F-m05: ACCEPTED. DPA-100 defines `planned` and `active` separately from fact classifications.
- F-m06: PARTIALLY ACCEPTED. The declared-source definition already implied canonical input; DPA-100 now makes the alias and containment rule explicit.
- F-m07: ACCEPTED. Standalone diagram alignment remains a cleanup task.

## TVA findings

- TVA-M01: ACCEPTED. DPA-ADR-012 establishes role-based review governance.
- TVA-m01: ACCEPTED. Architecture baseline and later planning/adjudication refs must remain distinct in review records.
- TVA-m02: ACCEPTED. Access outcome is separate from architecture verdict.
- TVA-m03: ACCEPTED. DPA-100 records the consumer trust boundary; DPA-200 and DPA-500 own its complete contract.

## Accepted decisions

- DPA-ADR-009 — separate vocabulary dimensions.
- DPA-ADR-010 — canonical invariant register ownership.
- DPA-ADR-011 — minimal static recorded-baseline evidence.
- DPA-ADR-012 — role-based review governance.

## Rejected alternatives

- Named-model review requirements.
- Treating access failure as an architecture `REJECT`.
- Traceability or LEC as competing invariant owners.
- Rich lab evidence databases or services.
- Downgrading all exact-ref baseline facts to assumptions when bounded static evidence exists.
- Automatic historical-prose merge, renderer-owned writes or dynamic registry imports.

## Normative changes applied

- `DECISIONS.md`
- `specs/dpa/DPA-000-VISION.md`
- `specs/dpa/DPA-100-FOUNDATIONS.md`
- `LAB_EXECUTION_CONTRACT.md`
- `traceability/PHASE_A_TRACEABILITY.md`
- minimal records under `evidence/repo-facts/`

## Remaining Phase A work

1. Align governance/bootstrap wording with `runtime authority` and role-based reviews.
2. Align or explicitly demote `diagrams/architecture.mmd`.
3. Update planning backlog and status to completed dispositions.
4. Run a final exact-ref consistency review.
5. Decide whether DPA-000 and DPA-100 may advance from `review-ready` to `stable`.

## Adjudication verdict

`ACCEPT_WITH_CHANGES`
