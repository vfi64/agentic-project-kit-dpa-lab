# Decisions

Status: active
Status-date: 2026-07-15

## DPA-ADR-001 — Extend the existing document-management system

Status: ACCEPTED

**Context:** The recorded main-repository baseline already contains registry, lifecycle, freshness, evidence, Workspace and gate mechanisms.

**Decision:** The DPA SHALL extend those mechanisms and SHALL NOT create a parallel projection-management system.

**Alternatives considered:** A standalone projection registry and independent projection CLI.

**Rationale:** A parallel system would duplicate authority, drift behavior and gates and would violate the lab mandate.

**Consequences:** Every implementation proposal requires a validation-ref integration map. Repository-specific field and module names remain `NEEDS_MAIN_REPO_VALIDATION`.

**Validation status:** The existence of the recorded architecture families is `VERIFIED_AT_RECORDED_BASELINE` at main refs `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` and `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`, subject to the minimal evidence records required by DPA-ADR-011. Exact integration points require DP1.

**Affected specifications:** DPA-000 through DPA-900.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-002 — Lab is non-authoritative

Status: ACCEPTED

**Context:** The lab is a temporary architecture workspace and cannot represent current production state.

**Decision:** The lab owns planning history, accepted design decisions and pre-import normative specifications only. Runtime authority remains exclusively in the main repository.

**Alternatives considered:** Treating the lab as an upstream runtime contract repository.

**Rationale:** Upstream runtime authority would create circular ownership and a second runtime authority.

**Consequences:** Lab evidence cannot prove implementation completion. Controlled import is selective; the lab is never imported wholesale.

**Validation status:** NORMATIVE lab governance decision.

**Affected specifications:** all.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-003 — Renderer responsibility boundary

Status: ACCEPTED

**Context:** Rendering, writing and cross-ref serialization require distinct failure and authority boundaries.

**Decision:** Renderers compute text or bytes only. The existing document lifecycle validates, plans, locks and writes. Workflow orchestration serializes across branches and pull requests.

**Alternatives considered:** Self-writing renderers; renderer-owned locking; lifecycle-owned cross-PR semantics.

**Rationale:** Pure renderers are deterministic and testable. Existing lifecycle ownership avoids a second mutation path. Local locks cannot serialize independent refs.

**Consequences:** Renderer APIs prohibit repository mutation and nested renderer invocation. Exact lifecycle and workflow integration remains `NEEDS_MAIN_REPO_VALIDATION`.

**Validation status:** NORMATIVE architecture decision; implementation mapping pending DP1.

**Affected specifications:** DPA-000, DPA-100, DPA-300, DPA-400, DPA-600.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-004 — Define freshness by reproducibility

Status: ACCEPTED

**Context:** File existence, markers and timestamps do not prove that consumed content represents current canonical sources.

**Decision:** Projection freshness means reproducibility from declared canonical sources, renderer identity and contract-declared versioned configuration under the active contract.

**Alternatives considered:** Timestamp-only freshness; marker-only freshness; writer-success-only freshness.

**Rationale:** Derivational freshness directly tests the projection claim.

**Consequences:** DPA-500 must define source, target, base and contract drift. Time may signal review but cannot alone hard-fail.

**Validation status:** NORMATIVE architecture decision.

**Affected specifications:** DPA-000, DPA-100, DPA-500.

**Affected DP slices:** DP1, DP2, DP5.

## DPA-ADR-005 — Use static fail-loud renderer resolution

Status: ACCEPTED

**Context:** Registry-driven arbitrary imports would turn document metadata into an executable plugin surface.

**Decision:** Registry contracts store stable renderer identifiers. Reviewed code resolves identifiers through a static mapping. Unknown identifiers fail loud.

**Alternatives considered:** Import strings; entry points; filesystem-discovered plugins; silent fallback to manual behavior.

**Rationale:** Static resolution keeps execution reviewable, bounded and compatible with registry governance.

**Consequences:** DPA-300 and DPA-400 must specify compatibility and failure behavior. Exact identifier schema requires validation-ref evidence.

**Validation status:** NORMATIVE architecture decision; schema compatibility pending DP1.

**Affected specifications:** DPA-000, DPA-100, DPA-300, DPA-400.

**Affected DP slices:** DP1–DP2.

## DPA-ADR-006 — Separate local locking from cross-ref serialization

Status: ACCEPTED

**Context:** A workspace mutation lock protects local writes but cannot prevent two branches or pull requests from producing conflicting plans.

**Decision:** Local mutation locking remains a lifecycle responsibility. Base/source/target/contract drift guards and merge-time regeneration are workflow-orchestration responsibilities.

**Alternatives considered:** Treating the local lock as sufficient; optimistic textual merge of generated targets.

**Rationale:** Concurrency boundaries follow repository refs, not only processes.

**Consequences:** DPA-600 must define captured fingerprints, stale-plan blocking and regeneration from the validation ref.

**Validation status:** NORMATIVE architecture decision; concrete workflow mechanism pending main-repository validation.

**Affected specifications:** DPA-000, DPA-100, DPA-600.

**Affected DP slices:** DP1, DP3, DP5.

## DPA-ADR-007 — Do not invent canonical history for migration convenience

Status: ACCEPTED

**Context:** Mixed current and historical prose can make full projection difficult.

**Decision:** Migration SHALL prefer full projection when existing canonical sources are sufficient, then split current projection from historical evidence, and SHALL use managed-head-plus-history only as a justified exception. No new canonical history store may be created merely to enable rendering.

**Alternatives considered:** New canonical history database; automatic reconstruction from historical prose; unconditional hybrid documents.

**Rationale:** Migration convenience does not justify a new authority source.

**Consequences:** DP1 must discover the real authority graph before migration form is selected. Drift recovery never auto-merges historical prose.

**Validation status:** NORMATIVE architecture decision.

**Affected specifications:** DPA-000, DPA-100, DPA-200, DPA-700.

**Affected DP slices:** DP1, DP4.

## DPA-ADR-008 — Time alone cannot create a hard projection failure

Status: ACCEPTED

**Context:** Age may indicate review need but does not prove semantic drift.

**Decision:** Elapsed wall-clock time MAY produce a lifecycle warning or review signal but MUST NOT by itself produce a hard projection failure.

**Alternatives considered:** Fixed expiry as a blocking gate.

**Rationale:** Projection validity is derivational; chronological expiry alone creates false failures.

**Consequences:** DPA-500 must integrate temporal signals with existing lifecycle severity and staged strict adoption.

**Validation status:** NORMATIVE architecture decision; concrete finding mapping pending main-repository validation.

**Affected specifications:** DPA-000, DPA-100, DPA-500.

**Affected DP slices:** DP5.

## DPA-ADR-009 — Separate classification, document status, progress and evidence scope

Status: ACCEPTED

**Context:** Phase A used repository-fact classifications, document lifecycle states, review progress and recorded-baseline scope as if they were one vocabulary. Compound values such as `VERIFIED at recorded baseline` and `SATISFIED FOR INTERNAL BASELINE` were therefore ambiguous.

**Decision:** The lab SHALL use four separate closed vocabularies:

1. Repository-fact and architecture classifications: `VERIFIED`, `VERIFIED_AT_RECORDED_BASELINE`, `ASSUMPTION`, `NORMATIVE`, `PROPOSAL`, `REJECTED`, `NEEDS_MAIN_REPO_VALIDATION`.
2. Document status: `planned`, `draft`, `review-ready`, `stable`, `adopted`, and `active` for living governance or planning documents.
3. Progress status: `pending`, `partial`, `complete`, `blocked`, `not-required`.
4. Access outcome: `accessible`, `access-blocked`.

`VERIFIED_AT_RECORDED_BASELINE` means an exact historical ref and minimum static evidence record exist, while revalidation against a later validation ref remains mandatory before implementation.

**Alternatives considered:** Add all progress states to the epistemic lattice; keep only six classifications and downgrade exact-ref baseline facts to assumptions; continue using compound prose statuses.

**Rationale:** Separate dimensions prevent progress labels from masquerading as evidence classifications and preserve useful exact-ref historical context without claiming present implementation truth.

**Consequences:** DPA-100 owns the vocabulary definitions. Governance, status, traceability and review artifacts must use the correct dimension explicitly. `VERIFIED_AT_RECORDED_BASELINE` cannot be used without satisfying DPA-ADR-011.

**Validation status:** NORMATIVE lab governance and terminology decision.

**Affected specifications:** DPA-000, DPA-100 and all later DPA specifications.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-010 — DPA-000 owns the canonical invariant register

Status: ACCEPTED

**Context:** LAB_EXECUTION_CONTRACT §7, DPA-000 and traceability contained overlapping invariant lists with numbering and grouping drift.

**Decision:** DPA-000 SHALL own the single canonical DPA invariant register with stable IDs `DPA-INV-001` through `DPA-INV-017`. LAB_EXECUTION_CONTRACT SHALL reference that register rather than duplicate it. Traceability SHALL contain one row per canonical invariant and MUST NOT redefine or group invariant identities. The rule that lab decisions are planning authority rather than production truth remains a lab-governance rule outside the DPA invariant register.

**Alternatives considered:** LEC ownership; a new standalone invariant file; traceability ownership; continued duplicated lists.

**Rationale:** The normative specification series is the correct owner of architecture meaning. Derived governance and traceability views must not become competing sources.

**Consequences:** Later DPA documents, reviews, tests and gates cite stable invariant IDs. Any invariant meaning change requires an accepted ADR and synchronized DPA-000 update.

**Validation status:** NORMATIVE architecture-governance decision.

**Affected specifications:** DPA-000 through DPA-900.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-011 — Require minimal static evidence records for recorded baselines

Status: ACCEPTED

**Context:** The lab recorded exact main-repository refs but cited MAIN_REPOSITORY_CONTEXT.md as the reproduction source for its own claims, while governance required records under `evidence/repo-facts/`.

**Decision:** A claim classified `VERIFIED_AT_RECORDED_BASELINE` MUST reference a minimal static record under `evidence/repo-facts/`. Each record MUST contain:

- repository and exact ref;
- commit subject;
- fact family or inspected claim;
- inspected source paths or reproduction method;
- inspection date;
- limitations;
- mandatory revalidation note.

The lab MUST NOT build a parallel evidence database, generator or runtime evidence service. Missing records require classification as `ASSUMPTION` or `NEEDS_MAIN_REPO_VALIDATION`, not baseline verification.

**Alternatives considered:** No records and downgrade all baseline facts; rich generated evidence tooling; treating MAIN_REPOSITORY_CONTEXT.md as self-authenticating evidence.

**Rationale:** Minimal records remove circular citation while keeping evidence bounded and non-authoritative.

**Consequences:** Baseline records must be added before the recorded main-repository facts retain `VERIFIED_AT_RECORDED_BASELINE`. DP1 still revalidates all implementation-relevant facts against its validation ref.

**Validation status:** NORMATIVE evidence-governance decision.

**Affected specifications:** DPA-000, DPA-100, DPA-800.

**Affected DP slices:** DP1.

## DPA-ADR-012 — Govern reviews by roles and evidence quality

Status: ACCEPTED

**Context:** A model-name-specific review requirement became unsatisfiable when one model environment lacked repository access. Access failures were also at risk of being misread as architecture verdicts.

**Decision:** Phase reviews SHALL be governed by roles rather than named products:

1. Primary architecture review.
2. Secondary technical verification.
3. Maintainer adjudication.
4. Consolidated review record.

A reviewer may be a model or human. A qualifying review MUST identify an exact ref, reviewed files, method, findings and limitations. `access-blocked` is an access outcome, not an architecture verdict. A named-model review MAY be collected but SHALL NOT be required when the required review role is already satisfied by a qualifying review.

**Alternatives considered:** Require Claude, ChatGPT and Gemini by name; count access-blocked outputs as reviews; require model consensus without maintainer adjudication.

**Rationale:** Stable governance roles outlive product availability and focus review quality on evidence, method and adjudication.

**Consequences:** Phase A is satisfied by the Claude primary architecture review and ChatGPT technical verification audit, followed by maintainer adjudication and consolidation. Gemini is not required. Review directories may retain model names as storage categories without making those names normative roles.

**Validation status:** NORMATIVE review-governance decision.

**Affected specifications:** none directly; governs all reviews and phase exits.

**Affected DP slices:** none directly.
