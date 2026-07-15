# Phase A Review Backlog

Status: active
Status-date: 2026-07-15
Primary review: `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md`
Technical verification: `reviews/chatgpt/CHATGPT_PHASE_A_TECHNICAL_VERIFICATION_AUDIT.md`
Architecture baseline: `1a73ec435a09d0367cb7e9f123241d9f61550b0f`
Review-integration ref: `1bf72d1313335b6acfe5af960dd7315f42a7756a`

This backlog integrates every actionable Claude finding and ChatGPT technical-verification finding into project planning. It is non-normative. A finding becomes normative only after maintainer adjudication and an accepted decision or specification change.

## State vocabulary for this backlog

- `RECORDED`: captured without disposition.
- `MAINTAINER_DECISION`: requires an explicit maintainer choice.
- `ADJUDICATE`: sufficient review evidence exists for consolidated assessment.
- `DEFERRED_TO_SPEC`: accepted only as a planning obligation for a later DPA document after adjudication.
- `BLOCKED`: depends on an unresolved earlier decision.
- `REJECTED`: explicitly rejected with rationale.
- `DONE`: implemented and traceably verified in the lab.

## Major findings

| ID | Priority | Finding | Verification | Planned disposition | Decision | State |
|---|---|---|---|---|---|---|
| F-M01 | P0 | Repository-fact classifications, document statuses and progress states are not a closed, separated model. | TVA: VERIFIED | Define three separate closed namespaces; use evidence scope/ref metadata for recorded baselines rather than qualified `VERIFIED`. | ADR-009 | MAINTAINER_DECISION |
| F-M02 | P0 | Binding invariants are duplicated across LEC, DPA-000 and grouped traceability IDs with numbering drift. | TVA: VERIFIED | DPA-000 owns stable one-to-one invariant IDs; LEC references; traceability remains derived. | ADR-010 | MAINTAINER_DECISION |
| F-M03 | P0 governance | Recorded-baseline claims lack the minimal repo-fact records required by lab governance. | TVA: VERIFIED WITH SEVERITY QUALIFICATION | Define minimal static evidence bar; prohibit evidence tooling or maintained mirrors; classify as major governance defect, not architecture defect. | ADR-011 | MAINTAINER_DECISION |
| TVA-M01 | P0 governance | Review governance is bound to named models rather than review roles and evidence quality. | New TVA finding | Define primary architecture review, secondary verification/independent review, maintainer adjudication and consolidated review as roles. Access-blocked attempts are not reviews. | ADR or LEC amendment | MAINTAINER_DECISION |

## Minor findings

| ID | Priority | Finding | Verification | Planned disposition | Dependency | State |
|---|---|---|---|---|---|---|
| F-m01 | P1 | Phase A exit criteria have divergent owners. | VERIFIED | LEC owns criteria; STATUS is tracking view; templates reference LEC. | adjudication | ADJUDICATE |
| F-m02 | P2 | `runtime truth source` conflicts with `runtime authority`. | VERIFIED | Editorial replacement without semantic change. | none | ADJUDICATE |
| F-m03 | P1 | Invariant traceability lacks direct decision links. | VERIFIED | Add one-to-one decision column after ADR-010. | ADR-010 | BLOCKED |
| F-m04 | P1 | `fresh` is overloaded between projection freshness and repository validation state. | VERIFIED | Define `validation ref`; preserve `fresh` for derivational freshness. | ADR-009 terminology batch | ADJUDICATE |
| F-m05 | P1 | Document statuses `planned` and `active` are undefined. | VERIFIED | Define separate document-status namespace. | ADR-009 | BLOCKED |
| F-m06 | P2 | `canonical source` is used without an explicit alias definition. | PARTIALLY VERIFIED | DPA-100 already defines declared source as canonical input; add alias or avoid phrase. | terminology batch | ADJUDICATE |
| F-m07 | P2 | Standalone architecture diagram diverges from DPA-100 relationship model. | VERIFIED | Align or mark simplified and non-normative. | adjudication | ADJUDICATE |
| TVA-m01 | P1 | Architecture baseline and later planning-integration ref are not explicitly separated in consolidation semantics. | New TVA finding | Record both refs and never claim identical reviewed trees unless true. | consolidated adjudication | ADJUDICATE |
| TVA-m02 | P1 | Review verdicts and access/execution outcomes use overlapping vocabularies. | New TVA finding | Separate review-result values from `COMPLETE`, `ACCESS_BLOCKED`, `INPUT_INCOMPLETE`. | review-governance decision | BLOCKED |
| TVA-m03 | P1 | Consumer trust before validation lacks an explicit requirement anchor. | New TVA finding | Add DPA-200/DPA-500 obligation: unvalidated branch-local output is not accepted trusted state. | later specs | DEFERRED_TO_SPEC |

## Terminology prerequisites

| Term | Required before | Planning requirement | State |
|---|---|---|---|
| `registered region` | DPA-200 | Define boundaries, ownership, registration and drift behavior. | RECORDED |
| `target semantics` | DPA-200 | Define replacement mode, encoding, normalization and region behavior. | RECORDED |
| `validation ref` | DPA-200 compatibility language | Identify the exact fetched ref against which repository claims are validated. | ADJUDICATE |
| `canonical source` | DPA-200 / DPA-400 | Define as alias for a declared canonical input or remove the phrase. | ADJUDICATE |
| `contract-declared configuration` | DPA-400 | Define versioning, declaration, authority and fingerprint inclusion. | RECORDED |
| qualified adoption terms | governance / later import | Distinguish lab adoption, contract adoption and controlled import. | RECORDED |
| review result | review governance | Define architecture verdict vocabulary separately from execution/access status. | BLOCKED |

## Later-spec failure-mode obligations

| Obligation | Target owner | Required outcome | Related DP slice | State |
|---|---|---|---|---|
| Missing canonical source | DPA-300 / DPA-400 | Fail-loud validation and renderer precondition. | DP1–DP2 | RECORDED |
| Lifecycle bypass / direct target write | DPA-300 / DPA-500 | Detect as target drift and map to an existing finding/gate path. | DP2–DP5 | RECORDED |
| Partial or interrupted mutation | DPA-300 | Define atomicity and crash-recovery obligations. | DP2 | RECORDED |
| Projection consumed before validation | DPA-200 / DPA-500 | Define consumer trust boundary and gate placement; unvalidated bytes are not accepted state. | DP2–DP5 | DEFERRED_TO_SPEC |
| Rollback requires unavailable history | DPA-700 | Require rollback inputs from Git history or another already-authoritative source. | DP2–DP4 | DEFERRED_TO_SPEC |
| Historical-region write ownership | DPA-200 / DPA-700 | Assign permitted writer and conflict behavior. | DP1–DP4 | RECORDED |
| Multi-PR use before serialization | DPA-600 / DPA-800 | State DP2 local integration is not authorization for concurrent refresh. | DP2–DP5 | RECORDED |

## Traceability corrections

| Gap | Planned correction | Dependency | State |
|---|---|---|---|
| Dry-run motivation row missing | Add motivation-to-requirement row. | adjudication | ADJUDICATE |
| Manual-document compatibility row missing | Add motivation-to-requirement row. | adjudication | ADJUDICATE |
| Consumer-before-validation motivation missing | Add motivation and later-spec anchors. | adjudication | ADJUDICATE |
| Invariant-to-decision links missing | Regenerate one invariant per row with Decision column. | ADR-010 | BLOCKED |
| Baseline reproduction source circular | Point to minimal exact-ref evidence records. | ADR-009/011 | BLOCKED |
| Reviewed baseline versus planning ref conflated | Record both refs in consolidation metadata and tables. | none | ADJUDICATE |
| DP2 historical-prose assignment may be conditional | Make DP assignment conditional on DP1 document-form result. | DPA-200/DPA-800 | RECORDED |

## Explicitly rejected alternatives

1. Rich evidence tooling or a new evidence store in the lab.
2. Maintaining `MAIN_REPOSITORY_CONTEXT.md` as a live mirror of the main repository.
3. Making traceability the owner of normative invariants.
4. Prototyping production renderer or registry code in the lab.
5. Predeclaring the migration form of any candidate document before DP1.
6. Fixed time-only blocking expiry.
7. Renderer-emitted lifecycle findings.
8. Automatic merge or reconstruction of historical prose.
9. Weakening derivational freshness to preserve ambiguous `fresh main` wording.
10. Treating access-blocked Gemini outputs as architecture reviews or verdicts.
11. Requiring a named model when it cannot inspect the exact review ref.

## Review and adjudication gates

- Primary architecture review against an exact ref: SATISFIED by Claude Fable 5.
- Secondary technical verification or independent review with exact-ref evidence: SATISFIED by ChatGPT TVA.
- Gemini review: NOT REQUIRED; two access attempts were `ACCESS_BLOCKED` and contain no architecture evidence.
- Consolidated finding-by-finding maintainer adjudication: REQUIRED.
- ADR-009, ADR-010, ADR-011 and review-governance outcome accepted before affected normative edits: REQUIRED.
- Phase A stability assessment after accepted changes, evidence records and traceability regeneration: REQUIRED.
