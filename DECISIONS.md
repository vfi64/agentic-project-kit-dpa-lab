# Decisions

Status: active
Status-date: 2026-07-14

## DPA-ADR-001 — Extend the existing document-management system

Status: ACCEPTED

**Context:** The recorded main-repository baseline already contains registry, lifecycle, freshness, evidence, Workspace and gate mechanisms.

**Decision:** The DPA SHALL extend those mechanisms and SHALL NOT create a parallel projection-management system.

**Alternatives considered:** A standalone projection registry and independent projection CLI.

**Rationale:** A parallel system would duplicate authority, drift behavior and gates and would violate the lab mandate.

**Consequences:** Every implementation proposal requires a fresh-main integration map. Repository-specific field and module names remain `NEEDS_MAIN_REPO_VALIDATION`.

**Validation status:** Recorded baseline refs are `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` and `5d4ea12d2f87393bdffdfbc53d79bc79d8670f1d`; the classification and minimum evidence bar for those recorded facts are pending DPA-ADR-009 and DPA-ADR-011. Exact integration points require DP1.

**Affected specifications:** DPA-000 through DPA-900.

**Affected DP slices:** DP1–DP5.

## DPA-ADR-002 — Lab is non-authoritative

Status: ACCEPTED

**Context:** The lab is a temporary architecture workspace and cannot represent current production state.

**Decision:** The lab owns planning history, accepted design decisions and pre-import normative specifications only. Runtime authority remains exclusively in the main repository.

**Alternatives considered:** Treating the lab as an upstream runtime contract repository.

**Rationale:** Upstream runtime authority would create circular ownership and a second source of truth.

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

**Decision:** Projection freshness means reproducibility from declared canonical sources, renderer identity and relevant versioned configuration under the active contract.

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

**Consequences:** DPA-300 and DPA-400 must specify compatibility and failure behavior. Exact identifier schema requires fresh-main validation.

**Validation status:** NORMATIVE architecture decision; schema compatibility pending DP1.

**Affected specifications:** DPA-000, DPA-100, DPA-300, DPA-400.

**Affected DP slices:** DP1–DP2.

## DPA-ADR-006 — Separate local locking from cross-ref serialization

Status: ACCEPTED

**Context:** A workspace mutation lock protects local writes but cannot prevent two branches or pull requests from producing conflicting plans.

**Decision:** Local mutation locking remains a lifecycle responsibility. Base/source/target/contract drift guards and merge-time regeneration are workflow-orchestration responsibilities.

**Alternatives considered:** Treating the local lock as sufficient; optimistic textual merge of generated targets.

**Rationale:** Concurrency boundaries follow repository refs, not only processes.

**Consequences:** DPA-600 must define captured fingerprints, stale-plan blocking and regeneration from fresh main.

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

## Planned adjudication decisions

The following records are decision placeholders only. They capture the decision scope exposed by the Claude review and MUST NOT be treated as accepted normative outcomes before the required reviews and consolidated adjudication are complete.

### DPA-ADR-009 — Close and separate status vocabularies

Status: PROPOSAL

**Review origin:** Claude Fable 5 finding F-M01.

**Decision question:** Shall the lab extend the repository-fact classification lattice, or keep the six epistemic classifications closed while defining separate document-status, review-progress and evidence-scope vocabularies?

**Alternatives to adjudicate:**

1. Extend the classification lattice with `PLANNED` and a qualified recorded-baseline status.
2. Keep the six repository-fact classifications closed; define `planned`, `active`, `review-ready`, `stable`, progress assessments and recorded-baseline scope separately.
3. Downgrade all recorded-baseline facts to `ASSUMPTION` despite exact refs.

**Required outcome:** One closed vocabulary model, explicit ownership, valid transitions and removal of undeclared compound statuses.

**Maintainer decision:** REQUIRED.

**Main-repository validation:** NOT REQUIRED for the vocabulary decision.

**Affected artifacts:** README, LAB_BOOTSTRAP, LAB_EXECUTION_CONTRACT, DPA-000, DPA-100, MAIN_REPOSITORY_CONTEXT, STATUS, traceability.

### DPA-ADR-010 — Own one canonical invariant register

Status: PROPOSAL

**Review origin:** Claude Fable 5 finding F-M02.

**Decision question:** Which normative artifact owns stable DPA invariant IDs, and where does the lab-only rule that decision artifacts are not production truth live?

**Alternatives to adjudicate:**

1. DPA-000 owns the canonical DPA invariant register; LEC references it; the lab-only rule remains governance outside the register.
2. LEC owns the register and DPA-000 references it.
3. Create a new standalone invariant register.
4. Let traceability own the invariant IDs.

**Required outcome:** Exactly one owner, stable one-to-one IDs, no grouped replacement IDs in traceability and no numbering drift.

**Maintainer decision:** REQUIRED.

**Main-repository validation:** NOT REQUIRED.

**Affected artifacts:** DPA-000, LAB_EXECUTION_CONTRACT, traceability, review templates and all later DPA specifications.

### DPA-ADR-011 — Set the recorded-baseline evidence bar

Status: PROPOSAL

**Review origin:** Claude Fable 5 finding F-M03.

**Decision question:** What minimum static evidence must exist before a recorded main-repository fact may carry the classification selected under ADR-009?

**Alternatives to adjudicate:**

1. Minimal static records under `evidence/repo-facts/` with exact ref, subject, inspected source or method, date and mandatory revalidation note.
2. No in-lab records; downgrade recorded baseline facts to assumptions.
3. Rich evidence tooling or a generated evidence database.

**Required outcome:** A bounded evidence rule that avoids circular self-citation and does not create a parallel evidence system.

**Maintainer decision:** REQUIRED.

**Main-repository validation:** NOT REQUIRED to choose the evidence bar; all facts remain subject to fresh DP1 validation.

**Affected artifacts:** MAIN_REPOSITORY_CONTEXT, LAB_EXECUTION_CONTRACT §15, DPA-000 validation sections, ADR-001 and traceability.
