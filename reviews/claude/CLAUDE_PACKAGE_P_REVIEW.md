# Independent Technical Review — Package P (Remote Probe Preparation)

## 1. Review identity

- Repository: `vfi64/agentic-project-kit-dpa-lab`
- Reviewed ref (exact, immutable): `18d0fd08b27d97aef1b06b5a75079527290ca8e4` (`Mark Package P ready for independent review`)
- Reviewed branch: `review/package-p-20260718`
- Draft PR for context only: `#5`
- Reviewer/model: Claude Fable 5 — independent technical verifier for Package P
- Review date: 2026-07-18
- Access method: HTTPS fetch; `git checkout` of the exact ref; ref-existence and identity verified (`git rev-parse HEAD` = the exact SHA — no `REVIEW_REF_MISMATCH`); unchanged core specs verified byte-identical to the audited main head via `git diff`; targeted repository searches; Lab-gate run page read via public web UI. No repository writes, no branch movement, no fixes, no implementation.
- Prompt provenance note: `reviews/PACKAGE_P_CLAUDE_REVIEW_PROMPT.md` is not present at the review ref; it exists on the working branch `spec/dpa-600-concurrency` (`8f344b2`) and binds explicitly and exclusively to `18d0fd0…`. This is the same benign pattern seen in prior cycles (the executable prompt is committed after its baseline is frozen) and does not affect the reviewed object. All findings derive solely from the review ref.
- Lab-gate evidence: workflow `DPA lab gates`, run `29660679403`, conclusion `success`, verified on the run page as bound to `18d0fd0…`. Treated as Lab repository-integrity evidence only — not Probe execution, not main-repository conformance.

## 2. Bootstrap confirmation

The mandatory bootstrap was completed in full at the review ref before assessment. Read and verified: the governance/authority chain (README, LAB_BOOTSTRAP, MAIN_REPOSITORY_CONTEXT, LAB_EXECUTION_CONTRACT, GOVERNANCE, STATUS, ROADMAP, MASTERPLAN, MASTERPLAN_REMOTE_PREPARATION, DECISIONS, ASSUMPTIONS); the normative specs DPA-000, 100, 200, 300, 400, 500 and the frozen DPA-600 draft, verified byte-identical to the last independently verified/ audited states (0-line diffs against the audited main head `8ac3b1b` for all six review-ready/stable specs); the accepted ADRs relevant to partition, lifecycle, acceptance, recovery, renderer, freshness, promotion and evidence boundaries (013, 014, 016, 017, 019, 020, 021); the full `probes/` set (README, shared execution/evidence contract, all three manuals, all three fixture manifests, all three internal audits, freeze, evidence-capture and adjudication procedures); `integration/MAIN_REPO_VALIDATION_CHECKLIST.md` and `integration/PORTABILITY_SLICE_PLAN.md`; `reviews/PACKAGE_P_INTERNAL_CONSISTENCY_AUDIT.md`; and the successor handoff. `reviews/PACKAGE_P_REVIEW_REQUEST.md` is not present at this ref (its content is carried by the internal consistency audit's "required next step" section and the handoff); this absence is recorded as editorial finding PPR-e02. Internal audits were read as non-independent evidence and their conclusions were re-derived, not trusted.

## 3. Executive verdict

**`ACCEPT_WITH_CHANGES`**

Package P is internally coherent, normatively aligned with DPA-300/400/500 and ADR-016/017/019/021, cleanly bounded, and safe: preparation is consistently distinguished from execution, the outcome vocabulary is closed and shared, observation/interpretation/adjudication are separated, every concrete main-repository mapping is fenced as `NEEDS_MAIN_REPO_VALIDATION`, no parallel authority is created, and no Probe execution, fixture materialization, adoption or conformance is claimed anywhere. The three internal Probe audits and the package audit are accurate as internal synchronization evidence and are correctly labelled as non-independent. The package is complete enough to proceed to Maintainer adjudication and, after adjudication, to begin local fixture-materialization *planning*, with Probe execution still barred until exact-ref and safety preconditions are met.

The verdict is `ACCEPT_WITH_CHANGES` rather than `ACCEPT` because of two MAJOR normative-anchor defects where a Probe case would, as written, under-test a mandatory DPA-300 rule (PPR-M01, PPR-M02) and one MAJOR coverage gap against the DPA-500 conformance surface (PPR-M03). None is a blocker: each is a bounded manual/manifest correction that changes no architecture and invalidates no executed evidence (nothing has executed). Minor and editorial findings follow.

## 4. Blockers

None. Package P may proceed to Maintainer adjudication. `blocker_count: 0`.

## 5. Major findings

### PPR-M01 — PROBE-001 C020 makes a mandatory partition field conditional ("Reject **when required by the claimed schema**")

- File/section: `probes/PROBE-001-MANUAL.md` §5, case P001-C020 ("Encoding/normalization declaration missing → Reject when required by the claimed schema"); fixture `F001-PARTITION-ENCODING-ABSENT`.
- Governing anchor: `DPA-300` §5.3 lists "encoding, normalization and line-ending behavior for partition bytes" as an unconditional required field of the parent-entry PartitionContract; ADR-017; the manifest's own §3.3 lists it among required representation with no conditionality.
- Observed defect: the case expectation is conditional ("when required by the claimed schema"), which contradicts the unconditional DPA-300 §5.3 obligation and the manifest's own required-model. A candidate PartitionContract that omits the encoding/normalization declaration MUST be rejected; the manual leaves room for a parser to accept it whenever the "claimed schema" is read as not requiring it. The manifest side (mutation M012 "remove encoding/normalization field; no default inserted") is correct — so manual and manifest disagree on the same case.
- Consequence: if executed as worded, C020 could record a `PASS`/compatibility observation for an implementation that silently tolerates a missing encoding declaration, which is exactly the "silent downgrade / unexplained bytes" class DPA-300 §5.3/§6 forbids. This weakens a mandatory rejection into an optional one.
- Smallest safe correction: reword C020 to "Reject: the partition contract MUST declare encoding, normalization and line-ending behavior (DPA-300 §5.3); a missing declaration fails loud with no inferred default," matching M012 and §3.3. No fixture change required beyond the expectation text.
- Affected artifacts: PROBE-001 manual (and, for symmetry, the C020 row wording only). New Lab ref required: yes (bounded manual edit). Independent rereview: no (mechanical anchor fix, re-checkable by the Maintainer against §5.3). Invalidates prior executed evidence: none exists.

### PPR-M02 — PROBE-001 C023 renderer-identifier rejection is anchored to an uncertainty instead of the DPA-300 §6 rule

- File/section: `probes/PROBE-001-MANUAL.md` §5, P001-C023 ("Unknown renderer identifier → Fail loud **if validation owns static identifier checking; otherwise record deferred validation without claiming support**"); manifest `F001-RENDERER-ID-UNKNOWN`, anchored `DPA-300 §§5.4,6`.
- Governing anchor: `DPA-300` §6 requires rejection of "unsupported renderer identifiers"; `DPA-400` §5 defines the closed static renderer mapping with fail-loud unknown resolution. Whether the *registry validator specifically* owns that check is a legitimate `NEEDS_MAIN_REPO_VALIDATION` question — but the normative expectation (an unknown renderer identifier must ultimately fail loud somewhere in resolve/validate/plan) is not conditional.
- Observed defect: the case folds a real main-repo uncertainty (which component performs the check) into the *outcome expectation*, so a run where the parser silently accepts an unknown renderer identifier and no later stage is exercised could be recorded as "deferred validation" rather than a finding. The prohibition in §7 ("unknown version silently treated as current") is analogous and is stated unconditionally; C023 should mirror it.
- Consequence: a genuine defect (unknown renderer identifier accepted with no fail-loud owner) could be masked as an acceptable deferral, producing false assurance about static-resolution safety.
- Smallest safe correction: split the concern — keep the location of the check as `NEEDS_MAIN_REPO_VALIDATION`, but make the case outcome unconditional: "An unknown renderer identifier MUST fail loud at some point in resolution/validation/planning; if the registry validator does not own the check, the case is `PARTIAL` and records which stage must, without recording `PASS`/support." This preserves the honest uncertainty while restoring the mandatory failure expectation.
- Affected artifacts: PROBE-001 manual C023 wording. New Lab ref required: yes. Independent rereview: no. Invalidates evidence: none.

### PPR-M03 — PROBE-002 does not cover DPA-500 staged-enforcement fail-closed transitions and gate-set-change re-acceptance trigger completely

- File/section: `probes/PROBE-002-MANUAL.md` §5 family P002-H (P002-C056 observe/warn/block-new/strict) and family P002-F (re-acceptance); measured against `DPA-500` §14 (staged enforcement) and §15.6 (gate-set re-acceptance) with ADR-021.
- Governing anchor: `DPA-500` §14 requires that legacy compatibility cannot weaken new-mutation/acceptance safety and that stage transitions are never time-activated; §15.6 defines gate-set re-acceptance as the operation triggered *by a gate-set change on unchanged bytes*. `DPA-500` conformance enumerates these as distinct testable obligations.
- Observed defect (two bounded gaps, one finding per the "do not merge unrelated defects" rule would separate them, but they share the single anchor DPA-500 staged/re-acceptance surface and one correction site): (a) P002-C056 exercises the four stages but does not include a case asserting that a `block-new`/`strict` stage MUST fail closed for a *new* projection while legacy already-accepted content remains readable — the §14 "compatibility cannot weaken new-mutation safety" rule is only implicitly covered; (b) family F tests re-acceptance context-drift rejection (C038) and pass/warn/fail (C037/C039/C040) but no case asserts that a **gate-set change is the actual trigger** that moves an otherwise-fresh projection to require re-acceptance (the §5.7/§15.6 staleness-then-re-acceptance path), as opposed to re-acceptance being invoked abstractly.
- Consequence: the Probe could report full lifecycle coverage while leaving the two DPA-500 behaviors most novel to ADR-021 — staged fail-closed-for-new and the gate-set-change→re-acceptance trigger — unmeasured, so a later `PASS` would overstate freshness/gate conformance.
- Smallest safe correction: add two bounded cases (or extend C056 and C037): C056b "block-new/strict fails closed for a new projection while prior accepted bytes stay readable"; C037-trigger "a gate-set change on unchanged accepted bytes is what marks the projection stale and eligible for gate-set re-acceptance," with matching fixtures (`F002-STAGE-BLOCK-NEW-VS-LEGACY`, `F002-REACCEPT-GATESET-TRIGGER`). Update the completeness check to reference them.
- Affected artifacts: PROBE-002 manual §5 and fixture manifest §6/§8. New Lab ref required: yes. Independent rereview: recommended (adds cases against the ADR-021 surface; a verifier should confirm the additions match §14/§15.6). Invalidates evidence: none.

## 6. Minor findings

### PPR-m01 — Portability plan cites `6a9da7d…` as "current remote head observed" without a fresh read
`integration/PORTABILITY_SLICE_PLAN.md` §2 states the current remote `main` head "observed during this preparation is `6a9da7d…`" and equals the Discovery baseline. The masterplan's own control 4 and the checklist require a fresh `origin/main` read as the first step; presenting the historical SHA as the current head risks treating a stale identity as current. §2 does add "does not replace local confirmation," which mitigates but does not remove the mislabel. Correction: state it as "the last recorded Discovery baseline; the current remote head MUST be re-read at Phase A/B start and may differ." New Lab ref: yes (one sentence). Rereview: no.

### PPR-m02 — Manual/manifest case-count drift is invisible to the completeness checks
Each completeness check asserts "every C001…Cnnn maps to a fixture," but nothing asserts the *inverse* (every fixture maps to a case) or a total count. Grep shows PROBE-001 = 27 cases, PROBE-002 = 58, renderer = 55, all internally consistent — but a future edit adding a fixture without a case (or vice versa) would pass the current check. Correction: add a bidirectional count assertion to each `Completeness check`. New Lab ref: yes. Rereview: no.

### PPR-m03 — Renderer C019 secret-isolation anchor is thinner than the manual implies
`DPA-400-RENDERER-PROBE-MANUAL.md` R400-C019 and R400-E treat secret/credential/environment isolation as a hard prohibition; `DPA-400` §(secret clause) actually frames it as "MUST NOT be exposed unless an accepted future contract explicitly establishes a bounded need." The Probe's stricter stance is safe (a superset prohibition), but the manual should cite the conditional-future clause so an implementer does not read it as an absolute that a later accepted contract would appear to violate. Correction: add the DPA-400 clause reference to C019 with the "absent an accepted bounded-need contract" qualifier. New Lab ref: yes. Rereview: no.

### PPR-m04 — Freeze procedure `same-ref requirement` is `SHOULD`, but cross-Probe adjudication assumes a shared ref
`EXACT_REF_FREEZE_PROCEDURE.md` §5 makes a shared main-repo ref for PROBE-001/002/renderer a `SHOULD`; `PROBE_ADJUDICATION_PROCEDURE.md` §10 builds cross-Probe conclusions on comparing "their exact refs and fixture revisions." The `SHOULD` is defensible, but §10 should state explicitly that divergent refs bound or invalidate cross-Probe conclusions unless the §5 justification is recorded. Correction: one cross-reference sentence in §10. New Lab ref: yes. Rereview: no.

## 7. Editorial findings

- **PPR-e01** — `probes/README.md` status table lists the shared contract as `draft` while the three procedures are `active`; the shared contract is equally load-bearing and `active` in spirit. Align the status label or note why the contract stays `draft` until first execution. No contract effect.
- **PPR-e02** — `reviews/PACKAGE_P_REVIEW_REQUEST.md`, named in the review prompt's bootstrap list (item 39), is absent at the review ref; its content lives in the internal audit's "required next step" and the handoff. Either add the request file or drop it from the bootstrap list to keep the file map exact. Navigation only.
- **PPR-e03** — `PROBE-002-MANUAL.md` §4 lists the 13 lifecycle phases; DPA-300's amended text uses the same names — worth a one-line cross-reference to DPA-300 §7 so the ordering source is unambiguous. No contract effect.

## 8. Cross-artifact consistency assessment

The shared execution/evidence contract is consumed without redefinition by all three manuals, both procedure layers and the fixture manifests: the outcome vocabulary (`PASS`/`FAIL`/`PARTIAL`/`BLOCKED`/`NOT_RUN`) is identical everywhere and `PARTIAL` is consistently called an execution outcome, not a document status. Observation/interpretation/adjudication separation is stated in the shared contract §8, echoed in each manual's observation model, and enforced by the evidence procedure's layered records and the adjudication procedure's primary-class rule. Exact-ref identity, fixture revision, content hashes, changed-path manifests, cleanup, repeatability, and rerun/refreeze on ref movement are mandated consistently across the shared contract §§10–14, the freeze procedure §4, the evidence procedure §§6–9 and the portability plan §8. The seven-class discrepancy taxonomy is identical in the shared contract §8.2, both Probe manuals' adjudication sections and the adjudication procedure §3. The internal audits' `PASS_AFTER_CORRECTION` verdicts are consistent with the corrected artifacts actually present at the ref (spot-verified: the PartitionContract is parent-entry-owned in the PROBE-001 manifest §3.3; PROBE-002 configuration drift is a distinct case C012; renderer plan-invalidation is R400-C009). The only cross-artifact inconsistencies are PPR-M01 (manual vs manifest on C020) and the minor/editorial items above.

## 9. Probe-specific assessment

### PROBE-001
Covers DPA-300 §§4–6 and ADR-017 registry, parent-entry PartitionContract, ownership and validation obligations without inventing serialization (all concrete field names/nesting fenced). Parent-entry ownership, the exactly-one rule, region-reference-without-competing-policy, complete-byte ownership, dangling/duplicate/overlap/unowned-byte rejections, executable-content rejection, and manual-fallback prohibition are all represented with one-mutation negative fixtures. Defects: PPR-M01 (C020 conditional), PPR-M02 (C023 anchor). Otherwise adequate and correctly bounded; the control case (C001) gating harness validity is present.

### PROBE-002
Covers DPA-300 §§7–17 lifecycle ordering, immutable planning, stale-plan rejection, locking and under-lock revalidation, Write–Verify–Record–Release, acceptance state, layered acceptance, gate-set re-acceptance, interruption, recovery, evidence failure and staged enforcement, with ADR-016/021 semantics and DPA-500 inputs. The 58-case matrix maps to fixtures; interruption boundaries are individually identified; conditional base persistence, base-independent evaluation, authorized-owner evolution vs out-of-band mutation, and ambiguous provenance fail-closed are all present (direct evidence that the R5-M01/M03 adjudications propagated into the Probe). Gap: PPR-M03 (staged fail-closed-for-new; gate-set-change→re-acceptance trigger). Otherwise strong.

### DPA-400 renderer Probe
Covers closed static resolution, identifier/interface/semantic/implementation-evidence separation, immutable declared inputs, source-as-data, configuration, deterministic output (same- and fresh-process), one-target scope, payload-only region output, the full prohibited-capability set, secret isolation, semantic bounds vs operational aborts, bounded failure envelope, no-fallback, and lifecycle-only invocation with no renderer-owned authority — 55 cases, each mapped. Only PPR-m03 (secret-clause anchor nuance) applies. This is the most complete of the three packages and aligns cleanly with the amended DPA-400 (§§12–16, ADR-019).

## 10. Freeze, evidence and adjudication assessment

The three procedures form one coherent, crash-safe, non-authoritative chain. Freeze records identity only (§7 prohibitions explicitly bar claiming a run, conformance, acceptance state or silent ref movement) with four progress states that are correctly distinguished from Probe outcomes and repository-fact classes. Evidence capture is layered, ordered, additive-only, with an explicit rule that evidence-persistence failure MUST be recorded as failure and never fabricate success or erase the written/verified/accepted distinction — directly consistent with DPA-300 §14 and DPA-500 §18. Adjudication is Maintainer-owned, single-primary-class, with dispositions that require owner and completion evidence, an architecture-amendment path that routes through ADR-020's governed verification, and a cross-Probe step that preserves each Probe's independent outcome rather than collapsing them. Evidence is consistently barred from becoming runtime/acceptance/lock/registry/workflow authority. Only PPR-m04 (shared-ref `SHOULD` vs cross-Probe assumption) applies.

## 11. CSC, namespace and portability assessment

The CSC/namespace checklist extends existing main-repository authority and explicitly forbids becoming a parallel runtime registry, state store, evidence system, lifecycle or gate (checklist §1, §3). It gates PROBE-001/002 execution behind exact-ref freeze and local isolation, and requires per-entry lifecycle report completeness, Workspace-resolved paths under both profiles, and loud failure on ambiguous authority. The portability slice plan is correctly restrictive: 14 cumulative eligibility rules, an explicit ineligible-surface list that matches the mutation freeze exactly (handoff writer, CURRENT_HANDOFF routing, lifecycle apply, acceptance state, re-acceptance, layered acceptance, projection gates, renderer, registry schema), PRT-C defaulting to ineligible due to proximity to frozen writers, and a Probe-impact rule requiring refreeze+rerun when a slice touches a Probe subject. This cannot silently alter a Probe subject or a frozen surface — the plan makes "Probe-independent" a proof obligation, not an assumption. Only PPR-m01 (stale-head labelling) applies.

## 12. Authority and false-assurance assessment

No artifact creates or implies a second registry, lifecycle, writer, state store, evidence authority, lock authority, gate authority or acceptance authority: the shared contract, both procedure layers, all three manuals and the two internal integration documents each restate the single-authority boundary and the "evidence is not runtime authority" rule. All repository-specific parser/writer/state/renderer/command/lock/evidence/path mappings are fenced `NEEDS_MAIN_REPO_VALIDATION` (verified by search across the probes/ and integration/ trees). No false assurance was found: every artifact carries `not run` / `not materialized`, `PASS_AFTER_CORRECTION` is explicitly scoped to internal synchronization, the Lab-gate green is disclaimed, and no Probe/adoption/conformance claim exists. The internal audits are correctly treated as non-independent (authority order item 7; each audit's own scope statement). Historical Discovery evidence at `6a9da7d…` is consistently marked historical (the one mislabel is PPR-m01).

## 13. Required corrections and sequencing

1. Fix PPR-M01 (C020 unconditional rejection) and PPR-M02 (C023 outcome unconditional, location deferred) in the PROBE-001 manual.
2. Add the two PPR-M03 cases + fixtures to PROBE-002 for staged fail-closed-for-new and the gate-set-change→re-acceptance trigger.
3. Apply minors PPR-m01…m04 (portability head labelling; bidirectional count checks; renderer secret-clause anchor; freeze/cross-Probe cross-reference).
4. Apply editorials PPR-e01…e03.
5. Preserve a new immutable Lab ref for the corrected package.
6. Maintainer adjudication of all findings; then independent rereview limited to PPR-M03 (the only finding that adds test surface).
All corrections are bounded manual/manifest/plan text edits. None changes normative DPA text, ADRs, traceability or diagrams; none requires main-repository evidence; none can be applied by silently selecting a production mechanism.

## 14. Refreeze and rereview obligations

- New Lab ref required: yes (bounded package edits) — `new_lab_ref_required: true`.
- Independent rereview required: yes, but scoped — only PPR-M03's added cases need independent confirmation against DPA-500 §14/§15.6; PPR-M01/M02 and all minors/editorials are Maintainer-checkable mechanical anchor fixes. `independent_rereview_required: true`.
- No main-repository Probe ref is frozen yet, so no executed evidence is invalidated. When execution later begins, the freeze/ref-movement rules already in the package (freeze §4, shared contract §14, portability §8) govern refreeze+rerun.

## 15. Maintainer adjudication readiness

Ready. The package is internally coherent, normatively aligned, and every open item is a bounded, clearly-owned correction with a stated smallest fix and disposition. Adjudication may proceed now; the three MAJOR findings should be dispositioned before the corrected package is frozen for materialization planning.

## 16. Local materialization-planning readiness

After adjudication and the bounded corrections, Package P is complete enough to begin **planning** local executable-fixture materialization (mapping semantic fixtures to serialized forms once the exact-ref parser/lifecycle/renderer surfaces are inspected). Materialization itself remains gated by each manifest's materialization gate and the freeze procedure; **Probe execution remains prohibited** until the current `origin/main` is read, locally confirmed, an exact Probe ref is frozen, fixtures carry immutable revisions/hashes, and safe isolation/observation harnesses are demonstrated. `local_fixture_materialization_planning_may_begin_after_adjudication: true`.

## 17. DPA-600 and DPA-700 disposition

Consistent and intact across STATUS, ROADMAP, `specs/dpa/README.md`, the masterplan annex, the DPA-600 draft header and the handoff: **DPA-600 remains a frozen bounded `draft`** (status `draft`; no review-ready promotion; only sequencing/status/evidence-boundary/defect edits; no expansion into concrete lock/workflow/merge-queue/recovery/rollback mechanics), and **DPA-700 remains `planned` and unstarted** (the file is a three-line status stub). Nothing in Package P releases DPA-600 or begins DPA-700. This review does not release DPA-600 and does not begin or recommend beginning DPA-700. `dpa_600_must_remain_frozen: true`, `dpa_700_must_remain_unstarted: true`.

## 18. Review method and limitations

Method: exact-ref checkout; byte-identity verification of unchanged core specs against the audited main head; full read of the probe/procedure/integration set; re-derivation (not trust) of each internal audit's conclusions against the normative anchors; targeted searches for authority leakage, stale tokens, case-count integrity and false-assurance claims; remote verification of the Lab-gate run bound to the ref. Limitations: (a) no main-repository ref was inspected — every main-repo behavior remains unmeasured and correctly fenced; (b) the review assesses *preparation* only — it cannot and does not establish that any Probe would pass; (c) the prompt file and one bootstrap-listed request file are not at the review ref (PPR-e02) and were read from the working branch / substitutes; (d) internal-audit correctness was assessed against the artifacts at the ref, not against the pre-correction states, which are not present.

## 19. Final machine-readable summary

```yaml
reviewed_repository: vfi64/agentic-project-kit-dpa-lab
reviewed_ref: 18d0fd08b27d97aef1b06b5a75079527290ca8e4
reviewed_branch: review/package-p-20260718
verdict: ACCEPT_WITH_CHANGES
blocker_count: 0
major_count: 3
minor_count: 4
editorial_count: 3
package_p_may_proceed_to_maintainer_adjudication: true
local_fixture_materialization_planning_may_begin_after_adjudication: true
dpa_600_must_remain_frozen: true
dpa_700_must_remain_unstarted: true
new_lab_ref_required: true
independent_rereview_required: true
probe_execution_claimed: false
main_repository_conformance_claimed: false
limitations:
  - No main-repository ref was inspected; all main-repo behavior remains unmeasured and fenced.
  - Review assesses preparation only and establishes no Probe pass or conformance.
  - Review prompt and reviews/PACKAGE_P_REVIEW_REQUEST.md are absent at the review ref (PPR-e02); read from working branch or substitutes.
  - Internal-audit correctness assessed against artifacts at the ref, not pre-correction states.
```

Review bound to exact ref `18d0fd08b27d97aef1b06b5a75079527290ca8e4`.
