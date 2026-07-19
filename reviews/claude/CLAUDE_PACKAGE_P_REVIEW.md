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

The mandatory bootstrap was completed in full at the review ref before assessment. Read and verified: the governance/authority chain (README, LAB_BOOTSTRAP, MAIN_REPOSITORY_CONTEXT, LAB_EXECUTION_CONTRACT, GOVERNANCE, STATUS, ROADMAP, MASTERPLAN, MASTERPLAN_REMOTE_PREPARATION, DECISIONS, ASSUMPTIONS); the normative specs DPA-000, 100, 200, 300, 400, 500 and the frozen DPA-600 draft, verified byte-identical to the last independently verified/audited states (0-line diffs against the audited main head `8ac3b1b` for all six review-ready/stable specs); the accepted ADRs relevant to partition, lifecycle, acceptance, recovery, renderer, freshness, promotion and evidence boundaries (013, 014, 016, 017, 019, 020, 021); the full `probes/` set (README, shared execution/evidence contract, all three manuals, all three fixture manifests, all three internal audits, freeze, evidence-capture and adjudication procedures); `integration/MAIN_REPO_VALIDATION_CHECKLIST.md` and `integration/PORTABILITY_SLICE_PLAN.md`; `reviews/PACKAGE_P_INTERNAL_CONSISTENCY_AUDIT.md`; and the successor handoff. `reviews/PACKAGE_P_REVIEW_REQUEST.md` is not present at this ref (its content is carried by the internal consistency audit's "required next step" section and the handoff); this absence is recorded as editorial finding PPR-e02. Internal audits were read as non-independent evidence and their conclusions were re-derived, not trusted.

## 3. Executive verdict

**`ACCEPT_WITH_CHANGES`**

Package P is internally coherent, normatively aligned with DPA-300/400/500 and ADR-016/017/019/021, cleanly bounded, and safe: preparation is consistently distinguished from execution, the outcome vocabulary is closed and shared, observation/interpretation/adjudication are separated, every concrete main-repository mapping is fenced as `NEEDS_MAIN_REPO_VALIDATION`, no parallel authority is created, and no Probe execution, fixture materialization, adoption or conformance is claimed anywhere. The three internal Probe audits and the package audit are accurate as internal synchronization evidence and are correctly labelled as non-independent. The package is complete enough to proceed to Maintainer adjudication and, after adjudication, to begin local fixture-materialization planning, with Probe execution still barred until exact-ref and safety preconditions are met.

The verdict is `ACCEPT_WITH_CHANGES` rather than `ACCEPT` because of two MAJOR normative-anchor defects where a Probe case would, as written, under-test a mandatory DPA-300 rule (PPR-M01, PPR-M02) and one MAJOR coverage gap against the DPA-500 conformance surface (PPR-M03). None is a blocker: each is a bounded manual/manifest correction that changes no architecture and invalidates no executed evidence (nothing has executed). Minor and editorial findings follow.

## 4. Blockers

None. Package P may proceed to Maintainer adjudication. `blocker_count: 0`.

## 5. Major findings

### PPR-M01 — PROBE-001 C020 makes a mandatory partition field conditional

- File/section: `probes/PROBE-001-MANUAL.md` §5, case P001-C020; fixture `F001-PARTITION-ENCODING-ABSENT`.
- Governing anchor: `DPA-300` §5.3; ADR-017; manifest §3.3.
- Observed defect: the case expectation is conditional ("when required by the claimed schema"), contradicting the unconditional DPA-300 §5.3 obligation and the manifest's required model.
- Consequence: execution could record false compatibility for an implementation that silently tolerates a missing encoding declaration.
- Smallest safe correction: make rejection unconditional and prohibit inferred defaults.
- New Lab ref required: yes. Independent rereview: no. Executed evidence invalidated: none.

### PPR-M02 — PROBE-001 C023 renderer-identifier rejection is anchored to an uncertainty

- File/section: `probes/PROBE-001-MANUAL.md` §5, P001-C023; manifest `F001-RENDERER-ID-UNKNOWN`.
- Governing anchor: `DPA-300` §6 and `DPA-400` §5.
- Observed defect: uncertainty about which component performs the check is folded into the outcome expectation.
- Consequence: an unknown renderer identifier accepted with no fail-loud owner could be masked as acceptable deferral.
- Smallest safe correction: location remains `NEEDS_MAIN_REPO_VALIDATION`, but the ultimate failure expectation is unconditional; absent stage proof yields `PARTIAL`, never `PASS`.
- New Lab ref required: yes. Independent rereview: no. Executed evidence invalidated: none.

### PPR-M03 — PROBE-002 misses two DPA-500 behaviors

- File/section: `probes/PROBE-002-MANUAL.md` §5 families P002-H and P002-F.
- Governing anchor: `DPA-500` §14 and §15.6 with ADR-021.
- Observed defect: no explicit case for `block-new`/`strict` failing closed for a new projection while legacy accepted content remains readable; no explicit case that a gate-set change triggers re-acceptance on unchanged bytes.
- Consequence: a later PASS could overstate staged-enforcement and re-acceptance conformance.
- Smallest safe correction: add two bounded cases and matching fixtures.
- New Lab ref required: yes. Independent rereview: yes, limited to the added cases. Executed evidence invalidated: none.

## 6. Minor findings

### PPR-m01 — Portability plan mislabels the historical Discovery SHA as current remote head

Correction: state it as the last recorded Discovery baseline and require a fresh current remote read at Phase A/B start.

### PPR-m02 — Completeness checks are not bidirectional

Correction: each Probe package must assert both every case maps to at least one fixture and every fixture maps to at least one declared case, with explicit total case counts.

### PPR-m03 — Renderer secret-isolation anchor needs the future bounded-need qualifier

Correction: state that secrets are unavailable absent an accepted future bounded-need contract preserving determinism and authority boundaries.

### PPR-m04 — Cross-Probe adjudication must bound conclusions when refs diverge

Correction: add an explicit cross-reference that divergent refs narrow or invalidate combined conclusions unless the freeze-procedure justification is recorded and accepted.

## 7. Editorial findings

- **PPR-e01** — Align or explain the shared contract's `draft` status relative to active procedures.
- **PPR-e02** — Add `reviews/PACKAGE_P_REVIEW_REQUEST.md` to the corrected review ref or remove it from bootstrap references.
- **PPR-e03** — Add a DPA-300 §7 cross-reference to the PROBE-002 lifecycle sequence.

## 8. Cross-artifact consistency assessment

The shared execution/evidence contract is consumed without redefinition by all three manuals, procedures and fixture manifests. The outcome vocabulary is identical, observation/interpretation/adjudication separation is preserved, exact-ref and evidence obligations are synchronized, and the discrepancy taxonomy is consistent. The only material cross-artifact inconsistencies are PPR-M01 and the listed minor/editorial items.

## 9. Probe-specific assessment

### PROBE-001

Covers DPA-300 §§4–6 and ADR-017 without inventing serialization. Defects: PPR-M01 and PPR-M02. Otherwise adequate and bounded.

### PROBE-002

Covers DPA-300 §§7–17 lifecycle ordering, immutable planning, stale-plan rejection, locking, Write–Verify–Record–Release, acceptance, recovery, freshness, gates and staged enforcement. Gap: PPR-M03. Otherwise strong.

### DPA-400 renderer Probe

Covers closed static resolution, immutable inputs, source-as-data, deterministic output, one-target scope, prohibited capabilities, secret isolation, bounds, aborts, failure envelopes, no fallback and lifecycle-only invocation. Only PPR-m03 applies.

## 10. Freeze, evidence and adjudication assessment

The procedures form one coherent, crash-safe, non-authoritative chain. Freeze records identity only; evidence is layered and additive; adjudication is Maintainer-owned and preserves independent Probe outcomes. Only PPR-m04 applies.

## 11. CSC, namespace and portability assessment

The checklist extends existing authority and forbids parallel systems. The portability plan is appropriately restrictive and makes Probe independence a proof obligation. Only PPR-m01 applies.

## 12. Authority and false-assurance assessment

No artifact creates a second registry, lifecycle, writer, state, evidence, lock, gate or acceptance authority. No false assurance was found. All repository-specific mappings remain fenced `NEEDS_MAIN_REPO_VALIDATION`.

## 13. Required corrections and sequencing

1. Fix PPR-M01 and PPR-M02 in PROBE-001.
2. Add the two PPR-M03 cases and fixtures to PROBE-002.
3. Apply PPR-m01 through PPR-m04.
4. Apply PPR-e01 through PPR-e03.
5. Preserve a new immutable Lab ref.
6. Perform Maintainer adjudication and limited independent rereview of PPR-M03.

## 14. Refreeze and rereview obligations

- New Lab ref required: yes.
- Independent rereview required: yes, limited to PPR-M03.
- No executed evidence exists and none is invalidated.

## 15. Maintainer adjudication readiness

Ready. All findings are bounded and have smallest-safe corrections.

## 16. Local materialization-planning readiness

After adjudication and corrections, Package P is complete enough to begin planning local executable-fixture materialization. Probe execution remains prohibited until current remote main is read, locally confirmed, an exact Probe ref is frozen, immutable fixture revisions/hashes exist and safe isolation is demonstrated.

## 17. DPA-600 and DPA-700 disposition

DPA-600 remains a frozen bounded draft. DPA-700 remains planned and unstarted. This review releases neither.

## 18. Review method and limitations

Method: exact-ref checkout, byte-identity verification, full package read, independent re-derivation, targeted searches and remote gate verification. Limitations: no main-repository implementation inspection; preparation only; prompt/request provenance outside the review ref; internal audits assessed against corrected artifacts.

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
```

Review bound to exact ref `18d0fd08b27d97aef1b06b5a75079527290ca8e4`.
