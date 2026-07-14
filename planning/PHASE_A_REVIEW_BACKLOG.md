# Phase A Review Backlog

Status: active
Status-date: 2026-07-14
Source-review: `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md`
Reviewed-ref: `1a73ec435a09d0367cb7e9f123241d9f61550b0f`

This backlog integrates every actionable Claude Fable 5 finding into project planning. It is non-normative. A finding becomes normative only after multi-review adjudication and an accepted decision or specification change.

## State vocabulary for this backlog

- `RECORDED`: captured without disposition.
- `AWAITING_REVIEWS`: requires ChatGPT and Gemini input before consolidated adjudication.
- `MAINTAINER_DECISION`: requires an explicit maintainer choice.
- `ADJUDICATE`: ready for consolidated assessment.
- `DEFERRED_TO_SPEC`: accepted only as a planning obligation for a later DPA document after adjudication.
- `REJECTED`: explicitly rejected with rationale.
- `DONE`: implemented and traceably verified in the lab.

## Major findings

| ID | Priority | Finding | Planned disposition | Affected artifacts | Decision | Maintainer | Main-repo validation | State |
|---|---|---|---|---|---|---|---|---|
| F-M01 | P0 | Repository-fact classifications, document statuses and progress states are not a closed, separated model. | Compare extend-lattice and normalize/separate alternatives; define one closed model and migrate all compound usages. | README, LAB_BOOTSTRAP, LAB_EXECUTION_CONTRACT §6/§14, DPA-100, DPA-000 validation wording, traceability, STATUS | ADR-009 | YES | NO | MAINTAINER_DECISION |
| F-M02 | P0 | Binding invariants are duplicated across LEC, DPA-000 and grouped traceability IDs with numbering drift. | Select one canonical invariant owner with stable IDs; make all other artifacts derived references; keep lab-only governance outside the DPA register. | DPA-000, LAB_EXECUTION_CONTRACT §7, traceability, review templates | ADR-010 | YES | NO | MAINTAINER_DECISION |
| F-M03 | P0 | Recorded-baseline claims lack the minimal repo-fact records required by lab governance. | Define the evidence bar; create minimal static records only; relabel claims according to ADR-009; prohibit evidence tooling expansion. | evidence/repo-facts/, MAIN_REPOSITORY_CONTEXT, DPA-000, ADR-001, traceability | ADR-011 or ADR-009 scope | YES | NO for classification repair; YES later for DP1 revalidation | MAINTAINER_DECISION |

## Minor findings

| ID | Priority | Finding | Planned disposition | Owner | Maintainer | Validation | State |
|---|---|---|---|---|---|---|---|
| F-m01 | P1 | Phase A exit criteria have three divergent owners. | Declare LEC phase model as single owner; STATUS becomes a tracking view; review templates reference the owner. | LAB_EXECUTION_CONTRACT §9 | YES | NO | AWAITING_REVIEWS |
| F-m02 | P2 | `runtime truth source` conflicts with defined `runtime authority`. | Replace deprecated phrase without semantic change. | GOVERNANCE, LAB_BOOTSTRAP, LEC | NO | NO | AWAITING_REVIEWS |
| F-m03 | P1 | Invariant traceability lacks direct decision links. | Add one-to-one invariant-to-decision column after ADR-010 resolves IDs. | traceability | NO | NO | BLOCKED BY F-M02 |
| F-m04 | P1 | `fresh` is overloaded between projection freshness and newly fetched repository state. | Define `validation ref` or equivalent and replace unqualified `fresh main` in normative/planning text. | DPA-100 and dependent artifacts | NO | NO | AWAITING_REVIEWS |
| F-m05 | P1 | Document statuses `planned` and `active` are undefined. | Define document-lifecycle/status vocabulary separately from repository-fact classification and progress assessment. | DPA-100 or LEC §14 | NO after ADR-009 | NO | BLOCKED BY F-M01 |
| F-m06 | P1 | `canonical source` is used but not defined relative to `declared source`. | Define containment and permitted configuration exception. | DPA-100; later DPA-400 | NO | NO | AWAITING_REVIEWS |
| F-m07 | P2 | Standalone architecture diagram diverges from DPA-100 relationship model. | Align it or mark it explicitly simplified and non-normative. | diagrams/architecture.mmd | NO | NO | AWAITING_REVIEWS |

## Terminology prerequisites

| Term | Required before | Planning requirement | State |
|---|---|---|---|
| `registered region` | DPA-200 | Define boundaries, ownership, registration and drift behavior. | RECORDED |
| `target semantics` | DPA-200 | Define replacement mode, encoding, normalization and region behavior. | RECORDED |
| `validation ref` | DPA-200 compatibility language | Identify the exact fetched ref against which repository claims are validated. | RECORDED |
| `canonical source` | DPA-200 / DPA-400 | Define as declared canonical input and prohibit evidence as semantic input. | RECORDED |
| `contract-declared configuration` | DPA-400 | Define versioning, declaration, authority and fingerprint inclusion. | RECORDED |
| qualified adoption terms | governance / later import | Distinguish lab adoption, contract adoption and controlled import. | RECORDED |

## Later-spec failure-mode obligations

| Obligation | Target owner | Required outcome | Related DP slice | State |
|---|---|---|---|---|
| Missing canonical source | DPA-300 / DPA-400 | Fail-loud validation and renderer precondition. | DP1–DP2 | RECORDED |
| Lifecycle bypass / direct target write | DPA-300 / DPA-500 | Detect as target drift and map to an existing finding/gate path. | DP2–DP5 | RECORDED |
| Partial or interrupted mutation | DPA-300 | Define atomicity and crash-recovery obligations. | DP2 | RECORDED |
| Projection consumed before validation | DPA-200 / DPA-500 | Define consumer assumption and gate placement; unvalidated bytes are not accepted state. | DP2–DP5 | RECORDED |
| Rollback requires unavailable history | DPA-700 | Require rollback inputs from Git history or another already-authoritative source. | DP2–DP4 | RECORDED |
| Historical-region write ownership | DPA-200 / DPA-700 | Assign permitted writer and conflict behavior. | DP1–DP4 | RECORDED |
| Multi-PR use before serialization | DPA-600 / DPA-800 | State DP2 local integration is not authorization for concurrent refresh. | DP2–DP5 | RECORDED |

## Traceability gaps

| Gap | Planned correction | Dependency | State |
|---|---|---|---|
| Dry-run motivation row missing | Add motivation-to-requirement row. | consolidated adjudication | RECORDED |
| Manual-document backwards compatibility row missing | Add motivation-to-requirement row. | consolidated adjudication | RECORDED |
| Invariant-to-decision links missing | Regenerate table one invariant per row with Decision column. | ADR-010 | BLOCKED |
| Baseline reproduction source circular | Point to minimal exact-ref evidence records. | ADR-009/011 and evidence commit | BLOCKED |
| DP2 historical-prose assignment may be conditional | Make DP assignment conditional on DP1 document-form result. | DPA-200/DPA-800 | RECORDED |
| Rollback recovery source unstated | Add DPA-700 obligation. | later spec | DEFERRED_TO_SPEC |

## Explicitly rejected review alternatives

These alternatives are already captured as review recommendations and remain rejected unless consolidated adjudication records a contrary maintainer decision:

1. Rich evidence tooling or a new evidence store in the lab.
2. Maintaining `MAIN_REPOSITORY_CONTEXT.md` as a live mirror of the main repository.
3. Making traceability the owner of normative invariants.
4. Prototyping production renderer or registry code in the lab.
5. Predeclaring the migration form of any candidate document before DP1.
6. Fixed time-only blocking expiry.
7. Renderer-emitted lifecycle findings.
8. Automatic merge or reconstruction of historical prose.
9. Weakening derivational freshness to preserve ambiguous `fresh main` wording.

## Review and adjudication gates

- ChatGPT Phase A review against a pinned common baseline: REQUIRED.
- Gemini Phase A review against the same pinned baseline: REQUIRED.
- Consolidated finding-by-finding adjudication: REQUIRED.
- ADR-009 and ADR-010 accepted before changing affected normative text: REQUIRED.
- Evidence-bar decision accepted before marking recorded-baseline claims verified: REQUIRED.
- Phase A stability assessment after all accepted changes and traceability regeneration: REQUIRED.
