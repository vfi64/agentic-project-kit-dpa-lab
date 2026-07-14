# Claude Fable 5 Review — DPA Phase A Foundation

Reviewed repository: `vfi64/agentic-project-kit-dpa-lab`
Reviewed ref: `1a73ec435a09d0367cb7e9f123241d9f61550b0f` (branch `spec/phase-a-foundation`, commit subject: `Advance Phase A foundation status`)
Model: Claude Fable 5
Review status: COMPLETE

Method note: the repository was cloned and checked out at the exact reviewed ref. All files in the tree were read in the LAB_BOOTSTRAP read order. DPA-200 through DPA-900 exist only as three-line stubs (`Status: planned`); `reviews/` contains only its README. No main-repository content was inspected; no repository-specific claim in this review is upgraded beyond the classifications already recorded in the lab.

## 1. Executive assessment

- Overall result: **ACCEPT_WITH_CHANGES**
- Phase A may proceed to adjudication: **YES**
- Foundational contradiction present: **NO**
- Hidden parallel system implied: **NO**
- New runtime authority implied: **NO**
- Fresh main-repository evidence required before adjudication: **NO** (required before DP1/implementation, per the lab's own contracts; no finding below needs a main-repo fetch to be adjudicated)

The Phase A baseline is architecturally coherent. The authority model (runtime / projection / planning / evidentiary / historical) is clean, the renderer–lifecycle–workflow boundary is consistently enforced across DPA-000, DPA-100, DECISIONS and the traceability matrix, and there are no false implementation claims: everything repository-specific is fenced with `NEEDS_MAIN_REPO_VALIDATION` and the lab consistently resists promoting itself to authority. No proposal creates a parallel registry, lifecycle, freshness, evidence, workspace or gate system.

The changes required before Phase A can be declared stable are classification-discipline and single-ownership problems, not architecture problems: (a) the six-value status vocabulary is not closed — documents use undeclared compound and extra statuses (`VERIFIED at recorded baseline`, `PLANNED`, `SATISFIED FOR INTERNAL BASELINE`); (b) the binding invariant catalog exists twice (LAB_EXECUTION_CONTRACT §7 and DPA-000 §7) with numbering drift from item 11 onward and a third, grouped ID scheme (INV-01…INV-13) in traceability; (c) the `VERIFIED at recorded baseline` claims have no in-lab evidence records although `MAIN_REPOSITORY_CONTEXT.md` itself mandates `evidence/repo-facts/` records — that directory does not exist at the reviewed ref.

## 2. Blocking findings

None.

No finding contradicts a foundational contract, implies a hidden parallel system, or introduces a new runtime authority. The findings below weaken classification and traceability discipline but do not invalidate the Phase A architecture.

## 3. Major findings

### F-M01 — Status vocabulary is not closed

- ID: F-M01
- Severity: MAJOR
- Files and sections: `README.md` (Working status vocabulary); `LAB_BOOTSTRAP.md` (Classification requirement); `LAB_EXECUTION_CONTRACT.md` §6; `DPA-100` §2; versus actual usage in `DPA-000` §16 (`VERIFIED at recorded baseline`), `MAIN_REPOSITORY_CONTEXT.md` (`VERIFIED AT THE RECORDED BASELINE`, `VERIFIED OR RECORDED AS MAINTAINER-GATED AT THE BASELINE`, `NEEDS_MAIN_REPO_VALIDATION BEFORE IMPLEMENTATION`), `traceability/PHASE_A_TRACEABILITY.md` (legend adds `PLANNED`; Phase A completion mapping uses `SATISFIED FOR INTERNAL BASELINE`, `REVIEW-READY`, `PARTIAL`).
- Analysis: Four governance documents define exactly six repository-fact classifications and require every repository-specific statement to carry one of them. In practice the lab uses at least five additional or compound statuses. `PLANNED` is load-bearing in the traceability legend but undefined in the vocabulary. `VERIFIED at recorded baseline` is a genuinely different epistemic state than `VERIFIED` as defined in DPA-100 §2 (which requires reproducible evidence), yet it is written as a qualified form of `VERIFIED`.
- Violated or weakened contract: LAB_BOOTSTRAP "Classification requirement"; DPA-100 §2; LAB_EXECUTION_CONTRACT §6.
- Proposed normative change: extend DPA-100 §2 to a closed lattice: add `PLANNED` (future obligation, no evidence claimed) and a defined qualified status for baseline facts (e.g. `VERIFIED_AT_RECORDED_BASELINE`: exact ref recorded, reproduction source recorded, revalidation mandatory before implementation, weaker than `VERIFIED`). Alternatively normalize all usage down to the existing six values (baseline facts become `ASSUMPTION` with recorded refs). Either way, one accepted decision must fix the lattice.
- Affected decisions: DPA-ADR-001 (validation status wording); a new decision (suggested DPA-ADR-009) to fix the status lattice.
- Affected traceability entries: legend; "Main-repository evidence boundary" table; "Phase A completion mapping" table.
- Main-repository validation required: NO.
- Maintainer decision required: YES (choice between extending the lattice and normalizing down).

### F-M02 — Duplicated invariant catalog with numbering drift and no declared single owner

- ID: F-M02
- Severity: MAJOR
- Files and sections: `LAB_EXECUTION_CONTRACT.md` §7 (17 invariants); `DPA-000` §7 (17 invariants); `traceability/PHASE_A_TRACEABILITY.md` (13 grouped IDs INV-01…INV-13).
- Exact divergence: items 1–10 align in substance. From item 11 the lists diverge: LEC §7.11 ("Lab decision artifacts are planning evidence, not production truth") has no DPA-000 §7 counterpart; DPA-000 §7.17 ("Repository-specific field names … MUST remain NEEDS_MAIN_REPO_VALIDATION …") has no LEC §7 counterpart; all intermediate items are offset by one (LEC §7.12 ≙ DPA-000 §7.11, LEC §7.17 ≙ DPA-000 §7.16, with wording drift, e.g. "must eventually resolve" vs "MUST resolve … after validated implementation"). Traceability then introduces a third scheme in which one INV ID covers up to two DPA-000 items (e.g. INV-08 = §7.11–7.12).
- Violated or weakened contract: DPA-100 §1 ("A later specification … MUST NOT change its meaning without an accepted decision"); the review-template requirement that invariants be individually addressable presupposes stable identifiers.
- Architectural consequence: any future correction to one invariant list can silently desynchronize the other; findings and tests keyed to "invariant N" become ambiguous.
- Proposed normative change: declare exactly one canonical invariant register with stable IDs (recommendation: DPA-000 §7, since specifications are the normative series), renumber or ID-tag it (INV-01…INV-17), make LAB_EXECUTION_CONTRACT §7 an explicit reference ("the binding invariants are defined in DPA-000 §7") retaining at most the lab-only invariant (current LEC §7.11) as a governance rule outside the DPA register, and regenerate the traceability table 1:1 against the canonical IDs (no grouping).
- Affected decisions: new decision (suggested DPA-ADR-010, invariant register ownership).
- Affected traceability entries: entire "Invariant traceability" table.
- Main-repository validation required: NO.
- Maintainer decision required: YES (owner choice and whether LEC §7.11 stays a separate governance rule).

### F-M03 — `VERIFIED at recorded baseline` claims have no in-lab evidence records; `evidence/repo-facts/` does not exist

- ID: F-M03
- Severity: MAJOR
- Files and sections: `MAIN_REPOSITORY_CONTEXT.md` ("Revalidation rule" step 4: record results under `evidence/repo-facts/`); `LAB_EXECUTION_CONTRACT.md` §15 step 4 (same obligation); `DPA-000` §16 and `traceability` "Main-repository evidence boundary" (reproduction source: `MAIN_REPOSITORY_CONTEXT.md`); repository tree at the reviewed ref (no `evidence/` directory).
- Analysis: The baseline facts (refs `6a9da7d…`, `5d4ea12…`, `8c970ad…`; release `0.4.12`; existence of the registry/lifecycle/freshness/workspace/gate stack) are cited with exact refs, which is good. But the declared reproduction source for these facts is the context document itself — a circular reference: the document is evidence for its own claims. The lab's own VERIFIED definition (DPA-100 §2) requires "an exact repository ref **and** reproducible evidence". No evidence record exists in the lab, and the directory both governance documents mandate for such records was never created. This is not fabrication — nothing false is claimed — but the classification is currently stronger than the stored evidence supports (see §10.3).
- Violated or weakened contract: MAIN_REPOSITORY_CONTEXT revalidation rule; LAB_EXECUTION_CONTRACT §15; DPA-100 §2 VERIFIED definition.
- Proposed normative change (smallest coherent resolution): create `evidence/repo-facts/` with one minimal static record per baseline fact family (ref, commit subject, inspection method, date), and re-label the affected claims with the qualified status decided under F-M01. Do not build any richer evidence tooling in the lab (see §13).
- Affected decisions: DPA-ADR-001 validation-status wording.
- Affected traceability entries: "Main-repository evidence boundary" table, row 1.
- Main-repository validation required: NO for the classification fix (the facts themselves remain subject to DP1 revalidation regardless).
- Maintainer decision required: YES (evidence bar for the recorded baseline; interacts with F-M01).

## 4. Minor findings

### F-m01 — Phase A exit criteria defined divergently in three places

- ID: F-m01; Severity: MINOR
- Files and sections: `LAB_EXECUTION_CONTRACT.md` §9 Phase A (5 criteria); `STATUS.md` "Phase A exit assessment" (7 criteria, adds "DPA-000 and DPA-100 review-ready or stable", "Initial traceability exists", "First review baseline exists", "Required reviews adjudicated"); the committed review template §16 (9 criteria).
- Analysis: STATUS and the review template are each stricter than the contract that formally owns the phase model. None of the three lists contradicts another, but no document says which list is normative.
- Proposed normative change: LAB_EXECUTION_CONTRACT §9 owns exit criteria; extend it to the union actually applied (the STATUS list is the best candidate), and mark STATUS's table explicitly as a tracking view of LEC §9.
- Affected decisions: none new required; can be folded into adjudication of F-M01/F-M02 batch. Affected traceability: "Phase A completion mapping". Main-repository validation: NO. Maintainer decision: YES (which list is normative).

### F-m02 — "truth source" phrasing contradicts DPA-100 §4.3

- ID: F-m02; Severity: MINOR
- Files and sections: `GOVERNANCE.md` ("No second runtime truth source"); `LAB_BOOTSTRAP.md` stop conditions ("a new runtime truth source"); `LAB_EXECUTION_CONTRACT.md` §19; versus `DPA-100` §4.3 ("Source of truth is an informal phrase and SHOULD be avoided in normative text").
- Proposed normative change: replace with "runtime authority" (the defined term) in all three governance documents. Purely editorial; no semantic change. Main-repository validation: NO. Maintainer decision: NO.

### F-m03 — Invariant traceability table lacks invariant-to-decision links

- ID: F-m03; Severity: MINOR
- Files and sections: `traceability/PHASE_A_TRACEABILITY.md`, "Invariant traceability" table (columns: ID, invariant, primary spec, later owner, DP slice, evidence/tests — no decision column).
- Analysis: The motivation matrix carries decisions, but per-invariant decision links (e.g. INV-09→ADR-008, INV-05→ADR-005, INV-10→ADR-007) exist only implicitly. The review template §9 treats this as a required link class.
- Proposed change: add a Decision column when the table is regenerated under F-M02. Main-repository validation: NO. Maintainer decision: NO.

### F-m04 — "fresh" is overloaded: derivational freshness vs "fresh origin/main"

- ID: F-m04; Severity: MINOR
- Files and sections: `DPA-100` §7.3 and §13 (derivational definition; "fresh" flagged as requiring qualification); versus `DPA-000` §11 ("reproducibility against fresh `origin/main`"), `LAB_EXECUTION_CONTRACT.md` §18, traceability rollback column, `ASSUMPTIONS.md` header ("current `origin/main`").
- Analysis: "fresh main" means "a newly fetched origin/main at validation time" — a different concept from projection freshness, in exactly the word DPA-100 §13 restricts.
- Proposed change: define one term in DPA-100 (e.g. **validation ref**: the exact `origin/main` commit fetched at validation time) and use it in DPA-000 §11, LEC §18 and traceability. Main-repository validation: NO. Maintainer decision: NO.

### F-m05 — Document status values `planned` and `active` are undefined

- ID: F-m05; Severity: MINOR
- Files and sections: `DPA-100` §10 defines draft / review-ready / stable / adopted; DPA-200 through DPA-900 carry `Status: planned`; STATUS.md, DECISIONS.md, LAB_BOOTSTRAP.md and others carry `Status: active`; neither value is defined anywhere.
- Proposed change: extend DPA-100 §10 (or the execution contract's completion semantics, §14) with `planned` (stub exists, no reviewable content) and `active` (living governance document, not a staged specification). Main-repository validation: NO. Maintainer decision: NO.

### F-m06 — "canonical source" used pervasively but never defined; relation to "declared source" implicit

- ID: F-m06; Severity: MINOR
- Files and sections: "canonical sources" appears throughout DPA-000 (§§3, 4, 9, 12) and DPA-100 (§§5.3, 5.5, 9.5); DPA-100 defines **canonical state** (§4.2) and **declared source** (§5.4) but not **canonical source**.
- Analysis: The intended reading is clearly "a declared source is a canonical input", i.e. declared sources ⊆ canonical state, but this containment is never stated as a rule. A reviewer of DPA-200 could otherwise ask whether a declared source may be non-canonical (e.g. evidence) — which invariant DPA-000 §7.10 forbids only for evidence.
- Proposed change: add one sentence to DPA-100 §5.4: a declared source MUST be canonical state (or configuration fixed by contract per the incidental-input rule); "canonical source" is then defined as synonym for a declared source. Main-repository validation: NO. Maintainer decision: NO.

### F-m07 — `diagrams/architecture.mmd` diverges from the DPA-100 §14 relationship model

- ID: F-m07; Severity: MINOR
- Files and sections: `diagrams/architecture.mmd`; `DPA-100` §14.
- Analysis: The standalone diagram omits the Evidence node entirely (and thus the "no runtime authority" edge), omits the Registry→Renderer contract edge, and adds a `Projection --> Gates` edge suggesting gates evaluate the projection alone, whereas freshness gates need sources, contract and renderer identity to test reproducibility. As two normatively adjacent diagrams they tell slightly different stories.
- Proposed change: either regenerate the .mmd from DPA-100 §14, or annotate it as a simplified reader-orientation overview that is explicitly non-normative. Main-repository validation: NO. Maintainer decision: NO.

## 5. Terminology audit

### 5.1 Coherent terms

canonical state; runtime authority; projection authority; planning authority; evidence; historical record; registered document; projection target (modulo the region caveat, correctly fenced); projection contract; declared source; projection; full / split / managed-head projection; manual document; hybrid document; renderer; renderer identifier; renderer resolution; document lifecycle; workflow orchestration; Workspace; gate; deterministic; reproducible; fresh (in its derivational projection sense); drift and its four classes (source / target / base / contract); temporal signal; fingerprint (with the commendable requirement that every fingerprint contract state input domain and algorithm); dry-run; mutation plan; mutation lock; atomic write; stale plan; local / cross-branch / cross-PR serialization; refresh workflow; regeneration; individual and consolidated review; draft / review-ready / stable / adopted; adoption vs controlled import (defined distinctly in §3.3/§3.4 — see ambiguity note on unqualified use); DP1–DP5.

### 5.2 Ambiguous terms

1. **fresh (unqualified, applied to refs)** — current use: "fresh `origin/main`" in DPA-000 §11, LEC §18, traceability. Ambiguity: collides with the derivational freshness definition (DPA-100 §7.3) in the exact word §13 restricts. Affected documents: DPA-000, LEC, traceability, ASSUMPTIONS ("current origin/main"). Correction: define **validation ref** (F-m04).
2. **adoption (unqualified)** — current use: DPA-100 §3.3 (lab operated with the kit) vs §10.6 (contract accepted into the main repository) vs README "After adoption, the authoritative architecture and runtime contracts live only in `agentic-project-kit`", where the README sentence semantically matches controlled-import completion, not lab adoption. Ambiguity: two governed acts share one root word. Affected: README, DPA-100, LEC Phase D/E. Correction: use "lab adoption" and "contract adoption" (or "import acceptance") as the qualified forms everywhere outside §3.3/§10.6.
3. **relevant versioned configuration** — current use: DPA-100 §§5.3, 5.5, 7.1; DPA-000 §6.3, §10. Ambiguity: it is a third renderer-input channel beside declared sources and incidental process inputs, but no rule states where it is declared, who versions it, and how it interacts with authority rule 12.4 ("renderers MUST read declared sources only for semantic output"). Affected: DPA-100, DPA-000, future DPA-400. Correction: define it as contract-declared, versioned, non-canonical input, and reconcile rule 12.4 to "declared sources and contract-declared configuration only".
4. **canonical source** — see F-m06.
5. **status compounds** — see F-M01.

### 5.3 Duplicate or circular terms

- Invariant catalog duplicated with drift: LEC §7 vs DPA-000 §7 vs INV-IDs (F-M02).
- Circular evidence reference: `MAIN_REPOSITORY_CONTEXT.md` named as reproduction source for its own claims (F-M03).
- Exit criteria triplicated: LEC §9 / STATUS / review template (F-m01).
- "runtime truth source" vs deprecated "source of truth" vs defined "runtime authority" (F-m02).
- Repository-fact statuses vs document statuses vs exit-assessment statuses form three partially overlapping vocabularies; only the first is formally defined (F-M01, F-m05).

No recursive definitions were found; the definition graph in DPA-100 is acyclic.

### 5.4 Missing terms required before DPA-200

- **registered region** — DPA-100 §5.2 permits region-level targets and §5.10 permits hybrid documents, but "region" has no definition of boundary representation, ownership, and drift semantics. DPA-200 cannot specify document forms without it.
- **target semantics** — a required field of every projection contract (§5.3) with no definition of its value space (full-replace vs region-replace vs append-guarded, encoding, normalization). DPA-200's document model consumes this directly.
- **validation ref** (or equivalent) — needed so DPA-200's compatibility statements can bind claims to an exact ref class rather than "fresh main" prose (F-m04).

Deliberately not listed: "relevant versioned configuration" materially obstructs DPA-400, not DPA-200; it can be fixed in the same DPA-100 amendment batch but is not a DPA-200 blocker.

## 6. Authority and boundary audit

1. **Canonical state** — PASS. Owner: main repository (accepted state). Permitted: own domain facts. Prohibited: rendering logic, renderer selection, formatting, target writes. Support: DPA-000 §6.1, §7.1; DPA-100 §4.2. Correction: none.
2. **Canonical source** — NEEDS_CLARIFICATION. Owner: as canonical state. Support: used in DPA-000 §§3–4, DPA-100 §5.3. Correction: define term / containment rule (F-m06).
3. **Projection contract** — PASS. Owner: existing documentation registry (post-validated-adoption). Permitted: declare target, renderer identifier, sources, target semantics, lifecycle/freshness policy, version info. Prohibited: executable import paths. Support: DPA-100 §5.3; DPA-000 §6.2, §7.6. Correction: define "target semantics" (§5.4 above) — deferred content, not an authority defect.
4. **Projection target** — PASS with fenced open point. Owner: registry (registration), lifecycle (writes). Permitted: be a deterministic view. Prohibited: independent canonical authority for rendered facts (DPA-100 §12.1). Support: DPA-100 §§4.4, 5.2; DPA-000 §8. Correction: region compatibility correctly `NEEDS_MAIN_REPO_VALIDATION`; keep.
5. **Registry** — PASS. Owner: main repository. Permitted: reviewed declarative contracts. Prohibited: arbitrary plugins, second registry. Support: DPA-000 §6.2, §7.6, §7.12; ADR-001, ADR-005. Correction: none.
6. **Renderer** — PASS. Owner: static reviewed code in the main repository (post-import). Permitted: read declared inputs, return text/bytes for exactly one target. Prohibited: write, lock, commit, invoke workflows, trigger renderers, invent facts. Support: DPA-000 §6.3, §7.2–7.3, §7.8–7.9; DPA-100 §6.1; ADR-003. Correction: reconcile configuration input channel (§5.2 item 3).
7. **Lifecycle** — PASS. Owner: existing main-repository lifecycle. Permitted: validate, plan, lock, write, emit findings/evidence; sole writer of projection targets. Prohibited: cross-ref serialization semantics (ADR-003 alternatives), being duplicated. Support: DPA-000 §6.4, §7.4; DPA-100 §6.4. Correction: none.
8. **Mutation lock** — PASS. Owner: lifecycle. Permitted: local workspace mutation boundary. Prohibited: being treated as branch/PR serialization. Support: DPA-100 §8.3; DPA-000 §11; ADR-006. Correction: none.
9. **Workflow orchestration** — PASS. Owner: main-repository workflows (mechanism `NEEDS_MAIN_REPO_VALIDATION`). Permitted: cross-branch/PR serialization, stale-plan guards, merge-time revalidation. Prohibited: defining document semantics. Support: DPA-000 §6.5, §7.5; DPA-100 §§6.5, 9. Correction: none.
10. **Evidence** — PASS. Owner: lifecycle emission; evidentiary value only. Permitted: audit, reproduction, review support. Prohibited: runtime authority, canonical source, runtime input to production behavior. Support: DPA-000 §6.6, §7.10; DPA-100 §§4.6, 12.2. Correction: none — note that F-M03 concerns lab evidence records, not this boundary.
11. **Historical record** — NEEDS_CLARIFICATION. Owner: unassigned for the append-only region of a managed-head projection — who may write that region (lifecycle? manual edit under which contract?) is unstated. Permitted: human/evidentiary value. Prohibited: auto-merge on drift, automatic canonicity. Support: DPA-100 §4.7, §5.8; DPA-000 §7.14, §12. Correction: DPA-200/DPA-700 must assign write ownership of historical regions; acceptable as deferred content if recorded as an open obligation.
12. **Consumer** — PASS. Owner: n/a (role). Permitted: read registered targets. Obligation: read order included in migration analysis where stale-leading-content risk exists. Support: DPA-000 §6.7. Correction: none.
13. **Lab authority** — PASS. Owner: lab, for planning history, decisions, pre-import normative specs only. Prohibited: runtime authority, implementation claims, `.agentic/` state. Support: GOVERNANCE.md; DPA-100 §3.2, §4.5; ADR-002. Correction: none.
14. **Main-repository authority** — PASS. Owner: `vfi64/agentic-project-kit`, exclusively, for implementation, Direction, registry contents, lifecycle behavior, gates, releases, handoff state. Support: README; LAB_BOOTSTRAP; DPA-100 §3.1. Correction: none.

## 7. Invariant-by-invariant audit

Audited against the DPA-000 §7 numbering (subject to F-M02's single-register resolution).

| # | Invariant (condensed exact wording) | Result | Supporting file/section | Conflict | Required correction |
|---|---|---|---|---|---|
| 7.1 | Canonical state MUST NOT own rendering logic. | PASS | DPA-100 §4.2; ADR-003 | none | none |
| 7.2 | Renderers MUST NOT own write logic. | PASS | DPA-100 §6.1; ADR-003 | none | none |
| 7.3 | Renderers MUST return text or bytes only. | PASS | DPA-100 §6.1; traceability INV-02 | none | none |
| 7.4 | The lifecycle MUST validate, plan, lock and write projection targets. | PASS | DPA-100 §6.4; DPA-000 §9 | none | none |
| 7.5 | Workflow orchestration MUST serialize refresh activity across branches and PRs. | PASS | DPA-100 §9; ADR-006 | none | none |
| 7.6 | The registry MUST describe reviewed contracts, not arbitrary plugins. | PASS | DPA-100 §5.3; ADR-005 | none | none |
| 7.7 | Renderer identifiers MUST resolve through static, reviewed code. | PASS | DPA-100 §6.2–6.3; ADR-005 | none | none |
| 7.8 | One renderer invocation MUST compute exactly one registered target. | PASS | DPA-100 §6.1 | none | region-target definition deferred to DPA-200 (compatible) |
| 7.9 | A renderer MUST NOT trigger another renderer. | PASS | DPA-100 §6.1; traceability INV-06 | none | none |
| 7.10 | Evidence MUST NOT be runtime authority. | PASS | DPA-100 §§4.6, 12.2; ADR-002/007 | none | none |
| 7.11 | Runtime projection contracts MUST live only in the main repository's existing registry/lifecycle system. | PASS | DPA-100 §3.1; LEC §7.12 | numbering drift vs LEC (F-M02), no semantic conflict | resolve register ownership |
| 7.12 | No parallel registry/lifecycle/freshness/evidence/workspace/gate subsystem. | PASS | ADR-001; GOVERNANCE prohibitions | none | none |
| 7.13 | Time-based findings MUST NOT become hard failures solely because time elapsed. | PASS | DPA-100 §7.9; ADR-008 | none | none |
| 7.14 | Historical prose MUST NOT be automatically merged during drift recovery. | PASS | DPA-100 §4.7, §9.5; ADR-007 | none | none |
| 7.15 | Mutation commands MUST default to dry-run. | PASS | DPA-100 §8.1; traceability INV-11 | none | none |
| 7.16 | Production paths MUST resolve through the existing Workspace abstraction after validated implementation. | PASS | DPA-100 §6.6 | wording drift vs LEC §7.17 ("must eventually") — F-M02 | align wording in single register |
| 7.17 | Repository-specific names/behaviors MUST remain `NEEDS_MAIN_REPO_VALIDATION` until verified against an exact fresh ref. | PASS | DPA-100 §§12.8, 15; ASSUMPTIONS.md | no LEC counterpart (F-M02); "fresh ref" wording touches F-m04 | carry into single register; use "validation ref" |

Additionally, LEC §7.11 ("Lab decision artifacts are planning evidence, not production truth") — PASS on substance (ADR-002 embodies it) but currently homeless in the DPA register; F-M02 must decide where it lives.

## 8. Decision audit

| Decision | Verdict | Context | Alternatives | Rationale | Consequences | Validation status | Consistent with DPA-000 | Consistent with DPA-100 | Required correction |
|---|---|---|---|---|---|---|---|---|---|
| DPA-ADR-001 | REVISE (wording only) | complete | adequate (standalone registry/CLI) | adequate | complete | uses undefined compound status "VERIFIED only for the existence …" (F-M01/F-M03) | yes (§7.11–7.12) | yes (§3, §6.7) | re-express validation status in the fixed lattice; reference evidence records once created |
| DPA-ADR-002 | ACCEPT | complete | adequate | adequate | complete | NORMATIVE, correct | yes (§8) | yes (§3.2, §4.5) | none |
| DPA-ADR-003 | ACCEPT | complete | good (three rejected placements) | adequate | complete, correctly fenced | NORMATIVE + pending mapping, correct | yes (§6, §7.1–7.5) | yes (§6) | none |
| DPA-ADR-004 | ACCEPT | complete | good (three rejected freshness models) | adequate | complete | NORMATIVE, correct | yes (§10) | yes (§7.3) | none |
| DPA-ADR-005 | ACCEPT | complete | good (four alternatives incl. silent fallback) | adequate | complete | NORMATIVE + schema pending, correct | yes (§7.6–7.7, §14) | yes (§6.2–6.3) | none |
| DPA-ADR-006 | ACCEPT | complete | adequate | adequate | complete | NORMATIVE + mechanism pending, correct | yes (§11) | yes (§§8.3, 9) | none |
| DPA-ADR-007 | ACCEPT | complete | good (three alternatives) | adequate | complete | NORMATIVE, correct | yes (§12) | yes (§4.7, §5.8) | none |
| DPA-ADR-008 | ACCEPT | complete | thin (one alternative: fixed expiry) but sufficient for the decision's scope | adequate | complete | NORMATIVE + finding mapping pending, correct | yes (§7.13, §10) | yes (§7.9) | optionally record "warn-with-escalation-schedule" as a considered alternative during adjudication |

No decision is inconsistent with DPA-000 or DPA-100. The set covers all binding invariants except the purely structural ones (7.8/7.9 single-target purity is embedded in ADR-003/005 rather than owning its own ADR — acceptable).

## 9. Traceability audit

- **Missing motivation-to-requirement links:** dry-run default (INV-11) and backwards compatibility for manual documents (DPA-000 §13) have no motivation row; they surface only at invariant level. Low risk, worth one added row each on regeneration.
- **Missing invariant-to-decision links:** the invariant table has no decision column (F-m03).
- **Missing decision-to-DP links:** none — present in both DECISIONS.md and the decision table, mutually consistent.
- **Missing test or gate obligations:** none at the planned level appropriate for Phase A; every invariant row names planned tests. Gate obligations exist for DP5 (staged strict adoption) and INV-09.
- **Missing evidence obligations:** the `evidence/repo-facts/` obligation is declared twice but never instantiated (F-M03); no evidence-record template exists.
- **Missing rollback obligations:** motivation matrix covers rollback per row; the invariant table does not carry rollback, which is acceptable since rollback is motivation-scoped. One substantive gap: no rollback row states the precondition that rollback inputs (prior target, prior registry entry) must be recoverable from Git history alone — see §11 failure mode "rollback requiring unavailable history source".
- **False implementation or completion claims:** none found. This is the strongest property of the baseline: every table consistently distinguishes PLANNED/NORMATIVE from VERIFIED, and STATUS.md explicitly refuses to close Phase A.
- **DP1–DP5 sequencing risks:** (a) INV-10 (no auto-merge of historical prose) is assigned DP3–DP4 evidence, but if DP2's first production projection targets a mixed document (the candidate list is dominated by handoff documents), the historical-prose drift scenario arrives at DP2 — the assignment should be conditional on DP1's target choice. (b) Cross-PR serialization (DPA-600, Phase C) is required by DP3/DP5; the phase model orders Phase C before Phase E, so no real risk, but DP2's "local write guard" row should state explicitly that DP2 alone does not license multi-PR refresh.
- **Items incorrectly presented as verified rather than planned:** only the recorded-baseline family (F-M03/§10.3); no planned DP slice or test is presented as executed.

## 10. Main-repository validation obligations

### 10.1 Adequately classified claims

- A-001 through A-005 in `ASSUMPTIONS.md` (registry `projection` block compatibility; CURRENT_HANDOFF mixed content; handoff state sufficiency; lifecycle drift absorption; refresh workflow cross-PR guards) — each names its required validation. Correct.
- The candidate document list in `MAIN_REPOSITORY_CONTEXT.md` — explicitly `NEEDS_MAIN_REPO_VALIDATION BEFORE IMPLEMENTATION` with the correct caveat that listing is not approval (compound status wording falls under F-M01, classification substance correct).
- DPA-000 §16 and §18, DPA-100 §15 open-validation lists — correct and commendably explicit.
- Region-level target compatibility (DPA-100 §5.2) and atomic-write filesystem behavior (§8.4) — correctly fenced.

### 10.2 Claims that must remain `NEEDS_MAIN_REPO_VALIDATION`

For each, the exact later evidence required:

1. Optional `projection` block schema compatibility — run the actual registry parser/validator at a recorded validation ref against a sample extended entry; store parser output.
2. CURRENT_HANDOFF (and each candidate document) reader/writer/authority graph — enumerate all code and workflow readers/writers with file/line references at the validation ref.
3. Sufficiency of existing handoff state to render current state — inventory of state files and refresh helpers, mapped to the fields the projection must render.
4. Lifecycle finding absorption of projection drift — list of existing finding types and severities, plus the gate mapping that would carry the four drift classes.
5. Cross-PR stale-plan guard feasibility — inventory of existing refresh workflows and pre-merge checks, plus the mechanism (merge queue, required check, bot) that can enforce regeneration.
6. Region-level targets — registry schema evidence for region addressing, or a negative result forcing full-target-only in DPA-200.
7. Atomic write behavior — the actual write path implementation (temp-file+rename or otherwise) at the validation ref.
8. Workspace API surface for DPA paths — method list evidence.
9. Mutation-lock API and scope — lock implementation evidence.
10. Finding identifiers and severity mapping — enumeration evidence.

### 10.3 Misclassified claims

- The `VERIFIED at recorded baseline` family (DPA-000 §16; MAIN_REPOSITORY_CONTEXT evidence baseline; traceability evidence-boundary row 1; DPA-ADR-001 validation status): presented with a qualified `VERIFIED` although the lab's own VERIFIED definition requires reproducible evidence and the declared reproduction source is the claiming document itself, with the mandated `evidence/repo-facts/` records absent. The claims are plausibly true and carry exact refs; the defect is that the label is stronger than the stored evidence. Resolution per F-M01 + F-M03 (define the qualified status and back it with minimal records, or downgrade to `ASSUMPTION` with recorded refs).

No other claim was found carrying stronger authority than its evidence allows. No implementation facts were invented in this review.

## 11. Failure-mode audit

| Failure mode | Coverage | Document that should own the complete contract |
|---|---|---|
| Missing canonical source | addressed (fail loud, DPA-000 §10, §13) | DPA-300 (validation), DPA-400 (renderer precondition) |
| Ambiguous authority | addressed (DPA-000 §8; DPA-100 §4, §12) | DPA-100 |
| Unknown renderer identifier | addressed (DPA-000 §10, §13; DPA-100 §6.2) | DPA-400 |
| Undeclared renderer input | partially addressed (prohibition + incidental-input rule, DPA-100 §5.4; enforcement/test mechanism open; configuration channel ambiguity §5.2-3) | DPA-400 |
| Renderer side effects | addressed (DPA-100 §6.1; INV-02 negative tests planned) | DPA-400 |
| Renderer recursion or chaining | addressed (DPA-000 §7.9; call-graph tests planned) | DPA-400 |
| Lifecycle bypass | partially addressed (sole-writer invariant; no stated detection mechanism for out-of-band writes to a target) | DPA-300 (detection = target drift), DPA-500 (gate consequence) |
| Direct target writes | partially addressed (same as above; detected as target drift, but the detection-to-finding path is DPA-500 content) | DPA-300 / DPA-500 |
| Stale base SHA | addressed (base drift §7.7; stale plan §8.5; LEC §18) | DPA-600 |
| Source drift | addressed (§7.5; ADR-004) | DPA-500 (definition/gates), DPA-600 (workflow) |
| Target drift | addressed (§7.6) | DPA-500 / DPA-600 |
| Concurrent pull-request refreshes | addressed in principle (cross-PR serialization; ADR-006); mechanism correctly `NEEDS_MAIN_REPO_VALIDATION` | DPA-600 |
| Automatic historical prose merging | addressed (prohibited: §7.14; ADR-007; LEC §18) | DPA-700 |
| Evidence used as runtime input | addressed (§7.10; DPA-100 §12.2; negative test planned) | DPA-300 |
| Time-only hard failure | addressed (§7.13; ADR-008) | DPA-500 |
| Rollback requiring an unavailable history source | partially addressed (reversibility required, DPA-000 §12; no-new-history-store, ADR-007; but the precondition that rollback inputs be recoverable from Git history alone is nowhere stated) | DPA-700 |
| Partial write or interrupted mutation | partially addressed (atomic write defined §8.4; filesystem behavior correctly fenced; crash-between-lock-and-write recovery unspecified) | DPA-300 |
| Projection output consumed before validation | missing as an explicit contract. Merge-time reproducibility (DPA-000 §11) covers integration, and consumer read order is flagged for migration analysis (§6.7), but nothing addresses a consumer (human, bootloader, LLM) reading a target inside a branch after render but before validation/merge gates run. | DPA-500 (gate placement) with a consumer-assumption clause in DPA-200 |

## 12. Accepted findings

Recommended for formal adjudication and possible normative incorporation:

- F-M01 (status lattice closure) — adjudicate first; touches DPA-100 §2, LEC §6, README, LAB_BOOTSTRAP.
- F-M02 (single canonical invariant register) — adjudicate second; touches DPA-000 §7, LEC §7, traceability.
- F-M03 (evidence records for the recorded baseline) — adjudicate with F-M01; touches MAIN_REPOSITORY_CONTEXT, DPA-000 §16, ADR-001, traceability.
- F-m01 (exit-criteria ownership), F-m02 ("runtime authority" wording), F-m03 (invariant→decision column), F-m04 (validation-ref term), F-m05 (`planned`/`active` document statuses), F-m06 (canonical source definition), F-m07 (diagram alignment).
- Terminology additions from §5.4 (registered region, target semantics) as recorded DPA-200 prerequisites.
- Failure-mode gaps from §11 (rollback-input availability → DPA-700 obligation; consumed-before-validation → DPA-500/DPA-200 obligation; crash-recovery → DPA-300 obligation) as recorded later-spec obligations, not Phase A text changes.

None of these is normative by virtue of appearing here; each requires adjudication and, where marked, a maintainer decision.

## 13. Rejected alternatives

Changes this review considered and explicitly rejects:

1. **Building a richer evidence store or evidence tooling in the lab to "prove" the baseline** — rejected: it would grow lab evidence toward a parallel evidence system and tempt evidence-as-authority. Minimal static records under `evidence/repo-facts/` are the ceiling (F-M03).
2. **Promoting `MAIN_REPOSITORY_CONTEXT.md` to a maintained mirror of main-repository state** — rejected: a maintained mirror is a second runtime truth surface; the document must remain a dated snapshot with mandatory revalidation.
3. **Making the traceability matrix the owner of the invariant register** — rejected: traceability is a derived view; making it normative would invert authority and weaken the specification series (F-M02 resolution must pick a specification owner).
4. **Prototyping a renderer or registry parser in the lab to de-risk A-001/renderer determinism now** — rejected: production kit code in the lab is prohibited and would prejudge DP1's schema and integration findings.
5. **Predeclaring the migration form (full / split / managed-head) for CURRENT_HANDOFF in Phase A** — rejected: prejudges DP1; the decision hierarchy (LEC §17, DPA-000 §12) exists precisely to defer this to evidence.
6. **Introducing a fixed staleness expiry to simplify DPA-500** — rejected: violates ADR-008 and invariant 7.13; time may only signal.
7. **Letting renderers emit lifecycle findings directly to shorten the pipeline** — rejected: moves lifecycle authority into renderers and breaks purity (ADR-003); weakens static, reviewable renderer resolution.
8. **Auto-merge or auto-reconstruction tooling for historical prose during drift recovery** — rejected: violates invariant 7.14 / ADR-007; regeneration from authoritative sources is the only permitted recovery.
9. **Resolving the "fresh" overload by weakening the derivational freshness definition** — rejected: the derivational definition is the load-bearing correction the DPA exists to make; the ref-sense gets the new term instead (F-m04).

## 14. Unresolved questions

Three questions genuinely gate adjudication closure (none blocks starting the adjudication itself; all block declaring Phase A stable):

1. **Which status lattice applies?** (extend to include `PLANNED` and a qualified baseline status, or normalize down to six values). Unresolved because both options are coherent and the choice propagates into every table. Maintainer decision: YES. Fresh main-repository evidence: NO. Dependent later document: all of DPA-200+ (every repository-specific claim carries a status).
2. **Which document owns the canonical invariant register, and does the lab-only invariant (LEC §7.11) live inside or beside it?** Maintainer decision: YES. Fresh evidence: NO. Dependent: DPA-200 through DPA-900 (all cite invariants), traceability.
3. **What is the evidence bar for `recorded baseline` facts** (minimal static records vs downgrade to ASSUMPTION)? Maintainer decision: YES. Fresh evidence: NO (the facts are re-verified at DP1 regardless). Dependent: DPA-800 (DP1 entry conditions reference the recorded baseline).

No question requires fresh main-repository evidence before adjudication, and no question blocks the start of DPA-200 outlining once questions 1–2 are decided.

## 15. Recommended adjudication order

1. Confirm the no-blocker assessment (this review §2) and record the review as an evidence input under `reviews/claude/`.
2. Decide F-M01 (status lattice) — authority/terminology before anything else; record as an accepted decision (suggested DPA-ADR-009).
3. Decide F-M02 (invariant register ownership; disposition of LEC §7.11) — record as DPA-ADR-010.
4. Apply terminology corrections in DPA-100 in one batch: F-m04 (validation ref), F-m05 (`planned`/`active`), F-m06 (canonical source), plus the §5.4 additions (registered region, target semantics — definitions may be stubs pointing to DPA-200 ownership); apply F-m02 wording in GOVERNANCE/BOOTSTRAP/LEC.
5. Only after 2–4: update dependent normative text — DPA-000 §7 (canonical register form), DPA-000 §16 and ADR-001 (status wording), LEC §7 (reference form), LEC §9 / STATUS (F-m01 exit-criteria ownership).
6. Separately from all internal contract work: execute F-M03's repository-evidence slice — create `evidence/repo-facts/` with minimal records for the three baseline refs; relabel affected claims per the ADR-009 lattice. Keep this commit free of normative text changes.
7. Regenerate `traceability/PHASE_A_TRACEABILITY.md` against the canonical invariant IDs, adding the decision column (F-m03), the two missing motivation rows (§9), and the recorded later-spec obligations from §11.
8. Align or demote `diagrams/architecture.mmd` (F-m07).
9. Reassess Phase A exit criteria against the (now single-owner) criteria list; update STATUS.md.

## 16. Phase A exit-criteria assessment

Assessed at the reviewed ref, against the template's nine criteria:

| Criterion | Assessment |
|---|---|
| Terminology is internally coherent | SATISFIED_WITH_CHANGES (F-M01, F-m04, F-m05, F-m06; core vocabulary in §5.1 is sound) |
| No hidden parallel system is implied | SATISFIED |
| Main-repository claims are classified | SATISFIED_WITH_CHANGES (classification discipline is excellent; the recorded-baseline family needs the F-M01/F-M03 relabel) |
| Review inputs exist | NOT_SATISFIED at the reviewed ref (`reviews/` contains only its README; this document is the first review input and satisfies the criterion once committed) |
| Accepted decisions are recorded | SATISFIED |
| DPA-000 is review-ready | SATISFIED |
| DPA-100 is review-ready | SATISFIED |
| Initial traceability exists | SATISFIED_WITH_CHANGES (F-m03; two missing motivation rows) |
| Decisions, assumptions and status are synchronized | SATISFIED_WITH_CHANGES (F-m01 exit-criteria triplication; ADR-001 status wording; otherwise DECISIONS/ASSUMPTIONS/STATUS are mutually consistent) |

No criterion is BLOCKED_BY_MAIN_REPO_EVIDENCE.

## 17. Final verdict

The reviewed ref is **review-ready with changes**. It is **ready for Phase A adjudication**: the required inputs for adjudication exist once this review is committed, no foundational contradiction blocks it, and no fresh main-repository evidence is needed to adjudicate any finding. It is **not yet eligible for Phase A stability** — stability requires adjudication of F-M01 through F-M03 and the minor batch, plus the ChatGPT and Gemini reviews the lab's own plan requires before Phase A closure.

**Exact next governed action:** commit this review under `reviews/claude/` with its reviewed-ref binding (satisfying STATUS.md active work item 1–2 for the Claude input), then collect the remaining model reviews, then open the consolidated adjudication record resolving F-M01 and F-M02 as accepted decisions (DPA-ADR-009/010) before any normative text under `specs/dpa/` is modified.
