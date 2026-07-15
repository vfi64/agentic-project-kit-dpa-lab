# Phase A Review Backlog

Status: active
Status-date: 2026-07-15
Primary review: `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md`
Technical verification: `reviews/chatgpt/CHATGPT_PHASE_A_TECHNICAL_VERIFICATION_AUDIT.md`
Consolidated adjudication: `reviews/consolidated/PHASE_A_ADJUDICATION.md`
Architecture baseline: `1a73ec435a09d0367cb7e9f123241d9f61550b0f`

This backlog records the disposition of Phase A review findings. It remains a planning artifact; normative outcomes live in accepted decisions and specifications.

## State vocabulary

- `DONE`: adjudicated and incorporated where required.
- `DEFERRED_TO_SPEC`: accepted obligation owned by a later DPA specification.
- `REJECTED`: explicitly rejected with rationale.
- `OPEN`: still requires bounded work before Phase A stability.

## Major findings

| ID | Disposition | Decision / owner | State |
|---|---|---|---|
| F-M01 | Accept with clarification: repository classifications, document statuses, progress statuses and access outcomes are separate closed namespaces. | ADR-009; DPA-100 | DONE |
| F-M02 | Accept: DPA-000 owns one canonical invariant register with stable IDs; LEC and traceability reference it. | ADR-010; DPA-000 | DONE |
| F-M03 | Accept with severity qualification: major governance/evidence defect, not foundational architecture failure. Minimal static records only. | ADR-011; `evidence/repo-facts/` | DONE |
| TVA-M01 | Accept: review governance is role-based and evidence-qualified, not vendor-bound. | ADR-012; LEC/GOVERNANCE | DONE |

## Minor findings

| ID | Disposition | Owner | State |
|---|---|---|---|
| F-m01 | LEC owns Phase A exit criteria; STATUS is a tracking view. | LAB_EXECUTION_CONTRACT §9 | DONE |
| F-m02 | Replace `runtime truth source` with defined `runtime authority`. | Bootstrap/Governance/LEC | DONE |
| F-m03 | One invariant per traceability row with direct decision links. | Traceability | DONE |
| F-m04 | Use `validation ref` for exact fetched repository state; preserve `fresh` for derivational freshness. | DPA-100 and dependent text | DONE |
| F-m05 | Define `planned`, `active`, `draft`, `review-ready`, `stable`, `adopted` as document-status values. | DPA-100 | DONE |
| F-m06 | Define `canonical source` explicitly as a declared canonical input; configuration is a separate contract-declared input. | DPA-100 | DONE |
| F-m07 | Align standalone diagram with the DPA-100 relationship model. | `diagrams/architecture.mmd` | DONE |
| TVA-m01 | Preserve distinction between reviewed architecture baseline and later integration/adjudication refs. | Consolidated adjudication and STATUS | DONE |
| TVA-m02 | Separate access outcomes from review verdicts. | DPA-100/ADR-012 | DONE |
| TVA-m03 | Define consumer trust before validation in DPA-200/DPA-500. | DPA-200/DPA-500 | DEFERRED_TO_SPEC |

## Terminology prerequisites for Phase B

| Term | Owner | State |
|---|---|---|
| `registered region` | DPA-100 foundation; detailed model in DPA-200 | DONE / DEFERRED DETAIL |
| `target semantics` | DPA-100 foundation; detailed model in DPA-200 | DONE / DEFERRED DETAIL |
| `validation ref` | DPA-100 | DONE |
| `canonical source` | DPA-100 | DONE |
| `contract-declared configuration` | DPA-100 foundation; detailed renderer contract in DPA-400 | DONE / DEFERRED DETAIL |
| qualified adoption terms | DPA-100 / import governance | DONE |
| review verdict versus access outcome | DPA-100 / ADR-012 | DONE |

## Later-spec obligations

| Obligation | Target owner | State |
|---|---|---|
| Missing canonical source must fail loud. | DPA-300 / DPA-400 | DEFERRED_TO_SPEC |
| Lifecycle bypass/direct target write must map to target drift and existing findings/gates. | DPA-300 / DPA-500 | DEFERRED_TO_SPEC |
| Atomicity and interrupted-mutation recovery must be defined. | DPA-300 | DEFERRED_TO_SPEC |
| Unvalidated projection bytes are not accepted repository state. | DPA-200 / DPA-500 | DEFERRED_TO_SPEC |
| Rollback inputs must be recoverable from Git history or another existing authority. | DPA-700 | DEFERRED_TO_SPEC |
| Historical-region writer ownership and conflicts must be explicit. | DPA-200 / DPA-700 | DEFERRED_TO_SPEC |
| DP2 local integration does not authorize concurrent multi-PR refresh. | DPA-600 / DPA-800 | DEFERRED_TO_SPEC |

## Rejected alternatives

1. Rich evidence tooling or a new evidence store in the lab.
2. Maintaining `MAIN_REPOSITORY_CONTEXT.md` as a live mirror of the main repository.
3. Making traceability the owner of normative invariants.
4. Prototyping production renderer or registry code in the lab.
5. Predeclaring a candidate document's migration form before DP1.
6. Fixed time-only blocking expiry.
7. Renderer-emitted lifecycle findings.
8. Automatic merge or reconstruction of historical prose.
9. Weakening derivational freshness to preserve ambiguous `fresh main` wording.
10. Treating access-blocked outputs as architecture reviews or verdicts.
11. Requiring a named model instead of evidence-qualified review roles.

## Remaining Phase A closure work

- Final exact-ref consistency audit of Phase A governance, specifications, decisions, traceability and evidence records. — OPEN
- Record final Phase A stability assessment at the resulting exact ref. — OPEN

All finding-specific normative work is otherwise complete. Phase B may begin only after the final Phase A stability assessment confirms no contradiction.
