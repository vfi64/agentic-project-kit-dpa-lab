# Decisions

Status: active
Status-date: 2026-07-16

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

**Context:** Phase A used repository-fact classifications, document lifecycle states, review progress and recorded-baseline scope as if they were one vocabulary.

**Decision:** The lab SHALL use separate closed vocabularies for repository-fact classification, document status, progress status and access outcome. Consumer trust state is separately governed by DPA-ADR-014.

**Alternatives considered:** Combining all states into one lattice; continuing compound prose statuses.

**Rationale:** Separate dimensions prevent progress labels from masquerading as evidence classifications.

**Consequences:** DPA-100 owns the vocabulary definitions. Governance, status, traceability and review artifacts must use the correct dimension explicitly.

**Validation status:** NORMATIVE lab governance and terminology decision.

**Affected specifications:** DPA-000, DPA-100 and all later DPA specifications.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-010 — DPA-000 owns the canonical invariant register

Status: ACCEPTED

**Context:** LAB_EXECUTION_CONTRACT §7, DPA-000 and traceability contained overlapping invariant lists with numbering and grouping drift.

**Decision:** DPA-000 SHALL own the single canonical DPA invariant register with stable IDs `DPA-INV-001` through `DPA-INV-017`.

**Alternatives considered:** LEC ownership; a new standalone invariant file; traceability ownership.

**Rationale:** The normative specification series is the correct owner of architecture meaning.

**Consequences:** Later DPA documents, reviews, tests and gates cite stable invariant IDs.

**Validation status:** NORMATIVE architecture-governance decision.

**Affected specifications:** DPA-000 through DPA-900.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-011 — Require minimal static evidence records for recorded baselines

Status: ACCEPTED

**Context:** The lab recorded exact main-repository refs without the required minimal evidence records.

**Decision:** A claim classified `VERIFIED_AT_RECORDED_BASELINE` MUST reference a minimal static record under `evidence/repo-facts/`.

**Alternatives considered:** No records; rich generated evidence tooling; self-authenticating context documents.

**Rationale:** Minimal records remove circular citation while keeping evidence bounded and non-authoritative.

**Consequences:** DP1 still revalidates all implementation-relevant facts against its validation ref.

**Validation status:** NORMATIVE evidence-governance decision.

**Affected specifications:** DPA-000, DPA-100, DPA-800.

**Affected DP slices:** DP1.

## DPA-ADR-012 — Govern reviews by roles and evidence quality

Status: ACCEPTED

**Context:** A model-name-specific review requirement became unsatisfiable when one model environment lacked repository access.

**Decision:** Phase reviews SHALL be governed by roles rather than named products: primary architecture review, secondary technical verification, Maintainer adjudication and consolidated review record.

A reviewer may be a model or human. A qualifying review MUST identify an exact ref, reviewed files, method, findings and limitations. `access-blocked` is an access outcome, not an architecture verdict.

**Alternatives considered:** Require named products; count access-blocked outputs as reviews; require model consensus.

**Rationale:** Stable governance roles outlive product availability and focus review quality on evidence, method and adjudication.

**Consequences:** Review directories may retain model names as storage categories without making those names normative roles.

**Validation status:** NORMATIVE review-governance decision.

**Affected specifications:** none directly; governs all reviews and phase exits.

**Affected DP slices:** none directly.

## Decision-file index — DPA-ADR-013 through DPA-ADR-020

The following decisions are maintained in dedicated files and are normative according to their recorded status:

- DPA-ADR-013 — document-form partition and boundary ownership — ACCEPTED;
- DPA-ADR-014 — consumer trust-state model — ACCEPTED;
- DPA-ADR-015 — DP1 staged Discovery, Probe and Assessment — ACCEPTED;
- DPA-ADR-016 — acceptance state and interrupted recovery — ACCEPTED;
- DPA-ADR-017 — parent-entry PartitionContract — ACCEPTED;
- DPA-ADR-018 — independent verification context — DEFERRED PROPOSAL, non-normative;
- DPA-ADR-019 — renderer input, resource and version model — ACCEPTED;
- DPA-ADR-020 — promotion commits and equivalence verification — ACCEPTED.

Decision-status vocabulary for this register is `ACCEPTED`, `DEFERRED PROPOSAL` and `REJECTED`. A deferred proposal does not create a current normative obligation.
