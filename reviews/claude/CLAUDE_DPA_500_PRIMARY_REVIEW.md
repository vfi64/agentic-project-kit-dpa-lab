# Claude Primary Architecture Review — DPA-500 Freshness and Gates

## 2. Metadata

- Repository: `vfi64/agentic-project-kit-dpa-lab`
- Exact review ref: `60d6457f0473365789ece4f885a48ea5320b01ff` (`Close DPA-500 pre-review vocabulary audit`)
- Branch at prompt creation: `spec/dpa-500-freshness-gates` (used for navigation only; all content evaluated at the exact ref)
- Reviewer/model: Claude Fable 5 — Primary Architecture Reviewer under DPA-ADR-012
- Review date: 2026-07-17
- Access method: HTTPS fetch; `git checkout` of the exact ref; unchanged bootstrap files verified byte-identical to previously fully-read states via `git diff`; targeted repository-wide searches; durable-gate run page read via public web UI. No repository writes; no main-repository inspection; no claims about any newer main-repository state.
- Durable Lab gate evidence at the ref: workflow `DPA lab gates`, run `29582601216`, result `success`, verified on the run page as bound to `60d6457…`. Per the prompt and `DPA-500` invalid state 23, this is repository-integrity evidence only — not architecture approval, Probe evidence, implementation evidence or main-repository conformance.
- Prompt provenance note: `reviews/claude/CLAUDE_DPA_500_PRIMARY_REVIEW_PROMPT.md` is not present at the review ref itself; it exists one commit later (`ee3e6b3`, "Add DPA-500 primary review prompt") on the same branch and binds explicitly and exclusively to `60d6457…`. The discrepancy is benign (prompt committed after freezing its baseline) and is recorded here; all reviewed content was taken solely from the ref.

## 3. Independence disclosure

1. This context did **not** author or apply any DPA-500 normative text. 2. It did **not** author or apply the pre-review corrections. 3. It did **not** participate in the pre-review audit or its closeout. 4. It **has** prior exposure: it produced the Phase A, DPA-200, DPA-300 and DPA-400 primary reviews, the DPA-300 equivalence verification and the DPA-300/DPA-400 post-adjudication verifications, and therefore knows the upstream contracts in depth. Authorship of reviewed changes: none. → Not `INDEPENDENCE_BLOCKED`; a meaningfully independent review is possible and provided.

## 4. Bootstrap completion statement

All 23 bootstrap items were read completely, in the prescribed order, at the exact ref, before any evaluation. Items verified byte-identical to previously fully-read states (0-line diffs at the ref): README, LAB_BOOTSTRAP, MAIN_REPOSITORY_CONTEXT, LAB_EXECUTION_CONTRACT, GOVERNANCE, DECISIONS, ASSUMPTIONS, DPA-000, DPA-100, DPA-200, DPA-300, checklist, import plan, and ADR-013/014/016/017/019/020. Read in full at the ref: STATUS, ROADMAP, `specs/dpa/README.md` (changed by the DPA-400 status-only promotion), DPA-400 (header-only status change verified as exactly that), DPA-500, its traceability, its diagram, the pre-review audit and the closeout. The audit and closeout were verified against the normative text rather than trusted (§ audits below; divergences in §22).

## 5. Method

Clause-level architecture review against the prompt's thirteen fields: dimensional-vocabulary sweep (including collision greps for every token named in field A); per-dimension freshness-model evaluation with evaluability analysis (can each dimension actually be computed from the defined records at each operation?); acceptance-record sufficiency check against every comparison the model requires; drift/finding mapping audit against the DPA-100 closed classes; gate/stage interaction analysis; renderer-consequence table verification against DPA-400; hybrid/region scenario walk-throughs (including the governed-manual-edit case); recovery-path analysis; parallel-system sweep; traceability anchor re-derivation against the canonical invariant register; diagram-to-text comparison; the nine mandated targeted searches; independent verification of every audit/closeout closure claim.

## 6. Reviewed files

The 23 bootstrap items; `reviews/claude/CLAUDE_DPA_500_PRIMARY_REVIEW_PROMPT.md` (from `ee3e6b3`, instructions only); the GitHub run page for 29582601216. Nothing else informed any conclusion.

## 7. Exact review ref

`60d6457f0473365789ece4f885a48ea5320b01ff`

## 8. Overall verdict

**`ACCEPT_WITH_CHANGES`**

## 9. Executive summary

DPA-500 is architecturally coherent and close to adjudication-ready. The pre-review audit's three vocabulary corrections (A5-M01…M03) are genuinely and completely applied: the five status dimensions are cleanly separated, the DPA-100 trust, drift and gate vocabularies are used without extension, `warn` (stage) vs `warning` (gate) is explicitly disambiguated, staged enforcement is fail-closed for mutation and acceptance in every stage, time never acts alone, renderers hold no freshness/finding/gate/acceptance authority, and no parallel engine, taxonomy, runner or database is created anywhere. The main-repository fence is complete and no implementation or Probe success is claimed.

Three majors remain, all in the evaluability/operational layer the vocabulary audit did not reach: (1) the mandatory base-context freshness dimension is defined against "the accepted plan" while the acceptance-state record carries no base identity and plans are attempt-scoped — the dimension is unevaluable after acceptance as specified; (2) the model provides no governed re-acceptance operation for policy-only changes, so a gate-set change makes accepted projections permanently `stale` unless they are fully regenerated, which staged adoption (DP5) will trigger constantly; (3) authorized manual-region evolution in hybrid documents — the normal life of the primary candidate document class — is classified as `target drift` and projection staleness, because the drift comparator is the accepted complete-target fingerprint with no authorized-owner carve-out; §17's payload-protection sentence acknowledges the tension without resolving the classification. Four minors and three editorials complete the set. All corrections are bounded; none requires redesign.

## 10. Major findings

### R5-M01 — Base-context freshness (dimension 9) is unevaluable after acceptance

- Severity: MAJOR | Files/sections: `DPA-500` §5.9 ("any base, repository or workflow identity **required by the accepted plan** remains current for the operation being authorized"); §8 record field list (no base/ref field); §7 evaluation inputs ("base or ref context where the requested operation requires it"); pre-review audit A5-m01 (question posed, unanswered by the text).
- Analysis: dimension 9 is mandatory, but its comparator is "the accepted plan". Plans are attempt-scoped lifecycle artifacts subject to bounded cleanup (DPA-300 §13); the persistent acceptance-state record (§8) contains no base or ref identity. After Release, an audit or integration evaluation of dimension 9 has no defined accepted-side operand: the dimension cannot be computed as specified, and §7's fail-closed rule would then force every post-acceptance evaluation toward `indeterminate` — or implementations will silently skip the dimension, which invalid state 21's spirit prohibits.
- Consequence: a mandatory dimension that cannot be evaluated makes the freshness contract unimplementable as written and pushes the ambiguity into DP2.
- Smallest bounded correction: rescope §5.9 to "required by the **governing plan or the requested operation**" and state the persistence rule explicitly: base/ref identity is operation-scoped (plans, integration context — DPA-600's input) and is persisted in acceptance state **only** when the accepted contract declares base-dependence, in which case §8 gains the conditional field "accepted base identity, when the contract declares base-dependence". Add one conformance test (post-acceptance audit evaluates dimension 9 without a live plan).
- Fresh main-repo validation: NO. Maintainer decision: YES (persist-when-declared vs never-persist).

### R5-M02 — No governed re-acceptance operation for policy-only changes (gate-set freshness dead end)

- Severity: MAJOR | Files/sections: `DPA-500` §5.7, §6 (`stale` definition), §15 (operations: audit, dry-run, mutation, post-Write, integration — nothing else), §21 (no re-acceptance test); pre-review audit A5-m02 (question posed for this review).
- Analysis: gate-set freshness makes a projection `stale` the moment the contract's required gate set changes — correct as a signal. But the only defined path back to `fresh` is the full mutation cycle (§15.2–15.4): re-render, re-write, re-verify, re-accept — although the bytes are proven identical and nothing semantic changed. During staged adoption (observe→warn→block-new→strict is itself a sequence of gate-policy changes), every stage transition or gate-set revision would mark the entire accepted estate stale and demand mass regeneration, or leave permanent noise. The architecture is missing the operation the model itself implies: re-evaluating the current required gate set against unchanged accepted bytes and updating the acceptance record.
- Consequence: DP5 staged rollout becomes operationally absurd (regenerate-everything-per-policy-change) or permanently noisy; "stale" loses its consumer meaning.
- Smallest bounded correction: add §15.6 **Gate-set re-evaluation (re-acceptance without mutation)**: a lifecycle-owned operation, valid only when every dimension except gate-set freshness is `fresh`, that runs the complete current required gate set against the existing accepted bytes, performs no render and no target write, and on full `pass` updates the acceptance record's gate-set identity and outcome (a governed acceptance-state write under the existing sole-writer rule). On any failure it emits findings and leaves state unchanged. Add the matching conformance test and an FG row.
- Fresh main-repo validation: NO for the contract; the persistence mechanics fold into the existing PROBE-002 acceptance-state items. Maintainer decision: YES (accept the operation, or explicitly ratify regenerate-on-policy-change as intended — the second option should then be written down as a stated cost).

### R5-M03 — Authorized manual-region evolution is misclassified as target drift and staleness

- Severity: MAJOR | Files/sections: `DPA-500` §5.5 (target freshness), §10 ("complete-target, payload **or preserved-region byte mismatch** under `target drift`"), §17 (payload-protection sentence), §8 (record includes complete-target fingerprint); root shared with `DPA-300` §12.2 ("changed actual target bytes against the accepted complete-target fingerprint produce target drift"); `DPA-200`/ADR-013 ownership model (manual regions are legitimately written by their governed owner).
- Analysis: hybrid documents exist so that a governed manual/historical region evolves while a projected region stays machine-owned — the observed `CURRENT_HANDOFF.md`, the primary DP2 candidate, appends history routinely. Under the current model, every authorized manual edit changes the preserved-region and complete-target fingerprints relative to the acceptance record, which §10 classifies as `target drift` and §6 as projection `stale`. The model thereby cannot distinguish the two events it most needs to separate: an **unauthorized out-of-band write to lifecycle-owned bytes** (the attack/defect case drift exists for) and the **normal authorized life of the document** (not a defect at all). §17's sentence ("preserved-region target drift … MUST NOT automatically classify the renderer-owned payload itself as semantically stale") shows the authors saw the tension, but it only protects the payload's reputation — the projection still reports drift + stale, findings fire on every append, and in `block-new`/`strict` staging this noise sits directly on the acceptance path. Consumers asking DPA-000's founding question ("is the generated content current?") get "stale" although the generated content is byte-perfect.
- Consequence: permanent false-positive drift on exactly the document class the whole architecture was built for; finding fatigue; wrong remediation signals (regeneration cannot "fix" an authorized manual edit).
- Smallest bounded correction (two coherent models — maintainer decision): **(a) layered acceptance (recommended):** target freshness for region projections compares lifecycle-owned bytes only (payload + partition fingerprints); preserved-region and complete-target fingerprints remain plan-time write guards (DPA-300 §8/§10.4, unchanged) and acceptance-integrity checks at Write/Verify, but post-acceptance change in bytes owned by a governed non-lifecycle owner, performed consistently with the partition contract, is **not** drift and **not** staleness — it produces at most a bounded informational finding ("complete-target superseded by owned-region evolution"); out-of-band change to lifecycle-owned bytes or partition bytes remains target/partition drift exactly as today. Requires a synchronized one-clause amendment to DPA-300 §12.2 (governed, per ADR-020 — not silent) scoping the complete-target comparator to complete-target projections and adding the owned-bytes comparator for region projections. **(b) strict acceptance, explicitly ratified:** keep complete-target acceptance semantics, but then DPA-500 must state the consequence honestly (every authorized manual edit supersedes acceptance and requires a refresh cycle) and must downgrade the classification wording so authorized-owner changes are distinguishable from out-of-band drift in findings. Add conformance tests for the authorized-edit and out-of-band cases under either model.
- Fresh main-repo validation: NO. Maintainer decision: YES.

## 11. Minor findings

### R5-m01 — Attempt-scoped vs projection-scoped freshness classification in §16
`DPA-500` §16 assigns freshness `invalid` for renderer nondeterminism and side-effect/capability violations. These are properties of an **attempt**, not of the previously accepted projection; as written, a failed attempt could appear to reclassify accepted bytes. Consequence: ambiguity about what object carries the classification. Correction: one sentence in §6 or §16 — freshness classification attaches to the evaluated projection context of the operation; a failed attempt's `invalid`/`abandoned` outcome does not reclassify previously accepted bytes, whose classification continues to derive from the §5 comparisons. Maintainer decision: NO.

### R5-m02 — Configuration and target-semantics drift mapping left disjunctive
`DPA-500` §10 maps configuration change to "`source drift` **or** `contract drift` according to the accepted contract model" (and test 8/16 mirror the disjunction). Since configuration is contract-declared by DPA-300 §5.2 / DPA-400 §7.2 and covered by the contract fingerprint, the deterministic mapping is **contract drift**; the pre-review closeout itself mapped it so. An open disjunction lets two evaluators classify the same event differently, violating §6's determinism sentence in spirit. Correction: fix the mapping to contract drift (and partition drift for partition-owned semantics elements), delete the source-drift alternative or define its precondition exactly (configuration explicitly declared as a canonical source by an accepted contract). Maintainer decision: NO.

### R5-m03 — Traceability invariant anchors are systematically inaccurate
`traceability/DPA-500_TRACEABILITY.md`: FG-001 ("time alone is not authority") omits DPA-INV-013 — the time invariant — while citing INV-011; FG-002 (state ≠ evidence) cites INV-013 instead of INV-010; FG-006 (stages not time-triggered) cites INV-005/INV-014, not INV-013; FG-004's INV-003/006/009 set does not match its content; FG-012 similarly loose. The columns read as decorative rather than derived — after ADR-010, anchors are load-bearing audit trails. Consequence: false confidence and broken invariant-to-requirement tracing. Correction: re-derive every FG row's invariant set from the canonical register; add rows/tests for R5-M01 (post-acceptance dimension-9 evaluation), R5-M02 (re-acceptance) and R5-M03 (authorized-edit vs out-of-band). Maintainer decision: NO.

### R5-m04 — Gate-evidence field list is uniformly SHOULD
`DPA-500` §19 lists all evidence fields as SHOULD, while DPA-300 §14 (after the ratified amendment) distinguishes identity-critical MUST fields from contextual SHOULD fields. For gate evidence, the identity-critical subset (evaluated ref/tree, target identity, classification, drift classes/subreasons, gate decision, stage) should be MUST for the same reproducibility reasons. Correction: mirror the DPA-300 MUST/SHOULD split. Maintainer decision: NO.

## 12. Editorial findings

- R5-e01 — §8 uses "invalid" as an adjective for acceptance-state records adjacent to the `invalid` freshness token; "malformed or unusable" avoids token adjacency (the dimensions are formally distinct, so this is wording only).
- R5-e02 — Diagram: `PASS --> ACCEPT` is unconditional, but §15.1's read-only audit `pass` records nothing; label the edge "pass (acceptance-bearing operation)" and let audit terminate at findings. `WARNING --> PRESERVE` is correct but could note "per staged policy".
- R5-e03 — §5.5's phrase "current target **or renderer-owned region** bytes" is the ambiguity R5-M03 resolves; whatever model is adjudicated, restate dimension 5 with explicit complete-target vs region comparators.

## 13. Vocabulary and dimensional-separation audit (field A)

PASS with the findings above. The eight dimensions are individually named, separately defined and never composed: freshness (`fresh/stale/invalid/indeterminate`, §6), trust state (five DPA-100 tokens applied verbatim, §9), drift (seven DPA-100 classes, §10), finding subreason (§10–11), lifecycle attempt outcome (§9, via DPA-300), gate decision (`pass/warning/failure`, §12), enforcement stage (`observe/warn/block-new/strict`, §14 with the explicit `warn`≠`warning` prohibition), severity/user wording (delegated to the main-repository system, §11). Collision greps: no trust-state use of `stale`/`invalid`/`unknown`; no gate outcome `warn`/`block`/`error`; `abandoned` only as trust token; `block` only inside `block-new`. Invalid states 6–8 encode the separations as negatives; test 34 tests them. The closeout's closure claims for A5-M01/M02/M03 are independently confirmed accurate.

## 14. Freshness and acceptance-state audit (fields B, C)

The nine dimensions are the right set and mutually coherent, with two evaluability defects: dimension 9 (R5-M01) and dimension 5's region semantics (R5-M03); dimension 7's operational dead end is R5-M02. No duplicated dimension; ownership per dimension is unambiguous otherwise; time is correctly excluded (§5 tail; §14; invalid state 22). Acceptance state: lifecycle state not evidence (§8, FG-002); single-target scoping enforced with scope-mismatch invalidity; the field set is sufficient for all §5 comparisons **except** base context (R5-M01); timestamps are metadata only; malformed/missing state fails safely to `indeterminate`/`invalid` + finding + fail-closed gate (§7, §12, test 3–5); silent reconstruction from bytes or evidence prohibited twice (§8, §18); rendering alone can never create `accepted` (§9, test proof obligation, invalid state 19).

## 15. Drift/finding and gate audit (fields D, E)

Drift: only the seven closed classes appear; every non-drift failure (acceptance-state defects, gate-set mismatch, nondeterminism, aborts, diagnostics, persistence failures, unavailable machinery) is explicitly listed as finding cause or lifecycle failure (§10) — the A5-M03 correction is complete. Mapping ambiguity remains only for configuration/target-semantics (R5-m02). Distinguishability: §10's last rule and §11's multi-failure reporting keep independent failures separate; the one indistinguishability defect is authorized-edit vs out-of-band (R5-M03). Gates: mandatory evaluation failure fails closed for mutation/acceptance/integration/strict (§12–13); `warning` cannot authorize acceptance past a failed mandatory check (§12; invalid state 10); read-only audit may return `failure` without mutation (§12; §15.1; test 33); gate decisions do not overwrite classification or trust state (§12; invalid states 7–8); no lab workflow is production gate authority (§4; §14 last line; invalid state 23).

## 16. Staged-enforcement audit (field F)

PASS. Transitions explicit, reviewable, reversible, Direction/configuration-controlled, never time-activated (§14; FG-006; test 29; invalid state 22); legacy compatibility cannot weaken new-mutation/acceptance safety (§13 last paragraph; §14 block-new definition); unknown findings fail closed where mutation safety, contract interpretation, target identity or acceptance is affected, with the remainder correctly left as main-repository policy (§14); `warn` vs `warning` explicitly separated; no lab statement activates production strict mode (§14 last line). Residual note: stage transitions are themselves gate-set/policy changes — their interaction with accepted-state staleness is exactly R5-M02.

## 17. Renderer integration audit (field G)

PASS against DPA-400: identifier drift (with the correct "where comparable" nuance), interface incompatibility, semantic-version drift with plan invalidation, implementation evidence remaining evidence-only (including the raw-commit rule restated), nondeterminism, side effects/capabilities, semantic bounds, operational aborts (non-drift, non-semantic, `abandoned`, never accepted output — §16, test 23, invalid state 11) and bounded diagnostics (lifecycle-translated only) are each mapped consistently with DPA-400 §§12–16 and ADR-019. Aborts are not misclassified as renderer drift. One scoping ambiguity: R5-m01.

## 18. Region/partition audit (field H)

Payload, preserved-region, partition-contract, partition-boundary and complete-target evaluations are independently required (§17); manual/historical bytes are never regenerated to clear staleness (§17; invalid state 18); byte ownership governs remediation. The classification of authorized preserved-region evolution is the R5-M03 defect; the write-guard layer (DPA-300) is unaffected and correct.

## 19. Recovery/crash-safety audit (field I)

PASS. §18 distinguishes verified bytes, acceptance-state persistence, evidence persistence and interrupted attempt state; completion of recording is permitted only on proven exact-byte and identity match against the governed plan and current contract; otherwise evidence preservation + findings + regeneration or Maintainer remediation; reconstruction from target bytes alone prohibited; `written-unverified` never accepted (invalid state 19; test 28); acceptance-state write failure after Write is a mandatory gate failure (§13) and evidence failure cannot fabricate success or erase the bytes-vs-state distinction (§19). No path promotes interrupted bytes to `accepted`.

## 20. Authority and parallel-system audit (field J)

PASS on all seven prohibitions: no second findings taxonomy (subreasons live under DPA-100 classes; concrete codes fenced), no second gate runner (existing gate architecture is sole production authority, §4), no second freshness engine (lifecycle-owned evaluation extending the existing stack, §1/§4), no second acceptance database (one lifecycle-state record class per DPA-300/ADR-016), no new runtime authority, no lab-controlled production strict switch (§14; switches fenced in §20), no renderer-owned finding/trust/gate authority (§4's seven-item prohibition; diagram NOTE3).

## 21. Main-repository validation boundary (field K)

PASS. §20's ten-item fence covers finding identifiers/severities, gate-set representation and configuration authority, acceptance-state schema/path, strict switches, command integration, unknown-finding policy, persistence ordering, CI placement, non-projection compatibility and performance bounds; §1 restates the fence; §23 blocks `stable` before Probe evidence; "No claim in this document states that the current main repository already conforms" is present and true — no unsupported `VERIFIED`, implementation or Probe claim was found in any DPA-500 artifact, STATUS or ROADMAP (both state `draft` and the review-ready ceiling).

## 22. Traceability and diagram audit (field L)

Traceability: structurally sound (12 FG rows with tests, later work, evidence/rollback; Probe obligations; explicit non-normativity clause) but with systematically inaccurate invariant anchors (R5-m03) and three missing scenario rows/tests tied to the majors. Diagram: faithful on authority boundaries, dimension inputs, classification/finding separation and the three NOTE guards; two simplifications (R5-e02). Neither artifact creates competing normative meaning. Pre-review audit and closeout: their three closure claims are accurate (independently confirmed); consistent with the four-cycle pattern, the audit did not surface the evaluability-layer defects (R5-M01…M03 — two of which it had itself flagged as open questions A5-m01/A5-m02 for this review, correctly) nor the anchor inaccuracies outside its vocabulary scope.

## 23. Targeted-search results

| Search | Result | Classification |
|---|---|---|
| trust-state uses of `stale`/`invalid`/`unknown` | none | closed (A5-M01) |
| gate outcomes `warn`/`block`/`error` | none | closed (A5-M02) |
| drift tokens outside the DPA-100 list | none in current normative text | clean |
| `boundary drift` | DPA-100 retirement rule; DPA-200 amendments-pointer provenance note; ADR-013/ADR-017 decision prose | current normative rule + sanctioned historical prose; no defect |
| `implementation version` | none | clean |
| `renderer contract version` | ADR-019 context/consequence only | valid historical decision prose |
| time-only freshness or strict activation | prohibitions only (§5, §14, invalid state 22) | current normative text, correct polarity |
| Lab-CI-proves-architecture claims | none; the opposite is stated (invalid state 23; STATUS) | clean |
| DPA-500 `review-ready`/`stable`/implemented/adopted claims | none; `draft` everywhere; review-ready only as future ceiling | clean |

## 24. Remaining `NEEDS_MAIN_REPO_VALIDATION` obligations

Exactly the §20 list plus the traceability Probe obligations (finding/severity mapping; gate representation, gate-set identity, strict controls, command integration; acceptance-state schema, Workspace path, crash-safe persistence order; non-projection compatibility; staged-policy demonstration). R5-M02's re-acceptance persistence and R5-M01's conditional base field fold into the existing acceptance-state Probe items; no new Probe class is needed.

## 25. Limitations and `ACCESS_BLOCKED` items

None blocked. The gate run page was publicly readable and bound to the ref; PR #3 prose was not needed for any conclusion. The prompt-file provenance discrepancy is recorded in §2. No main-repository state was inspected.

## 26. Smallest bounded correction set

1. R5-M01: rescope §5.9 to plan/operation; add the conditional base field rule to §8; one test.
2. R5-M02: add §15.6 gate-set re-evaluation (or ratify regenerate-on-policy-change explicitly); one FG row; one test.
3. R5-M03: adjudicate layered vs strict acceptance for region projections; amend §5.5/§10/§17 accordingly; synchronized one-clause governed amendment to DPA-300 §12.2; two tests (authorized edit; out-of-band write).
4. R5-m01/m02: two clarifying sentences (§6 or §16; §10 mapping fix).
5. R5-m03/m04: regenerate traceability anchors + add three rows; apply the MUST/SHOULD evidence split in §19.
6. Editorial batch R5-e01…e03; regenerate the diagram after 1–3.

All items are bounded text changes; per ADR-020 they belong in a governed amendment batch, never in a promotion commit, followed by the required verification path.

## 27. Promotion recommendation

> DPA-500 may proceed to Maintainer adjudication after all required review findings are dispositioned. Any later promotion to `review-ready` must be a separate status-only commit and does not establish production implementation, Probe success or main-repository conformance.

Review bound to exact ref `60d6457f0473365789ece4f885a48ea5320b01ff`.
