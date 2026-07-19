# Package M Internal Consistency Audit

Status: complete

Status-date: 2026-07-20

Audit target: `review/package-m-command-authority-20260720`

Exact audited ref: `eab8b3aefb04f0c557f41f0c06d4b7ec00eb261c`

Audit role: internal pre-review consistency check; not independent verification

## 1. Scope

This audit checks the non-normative Package M clause proposal against DPA-200, DPA-300, DPA-400 and DPA-500 for:

- authority duplication;
- ownership drift;
- acceptance-state duplication;
- finding-taxonomy duplication;
- repository-specific overclaim;
- DPA-600 and DPA-700 sequencing violations.

It does not validate main-repository behavior, execute Probes or adjudicate ADR-022.

## 2. Result

Verdict: `CORRECTION_REQUIRED_BEFORE_INDEPENDENT_REVIEW`

Findings:

- blockers: 0;
- majors: 3;
- minors: 1;
- editorials: 0.

The proposal is directionally consistent and does not require a new subsystem. Four bounded clarifications are required so that an independent reviewer is not asked to infer safety-critical boundaries.

## 3. Findings

### PMA-M01 — Aggregate completion risks a second acceptance authority

Severity: MAJOR

Affected proposal:

- synchronized projection-set definition;
- DPA-300 aggregate verification and recovery clauses;
- candidate diagram edge `aggregate coordinator -> synchronized projection-set completion decision`.

Governing anchors:

- DPA-300 §4.3: the existing lifecycle owns acceptance state;
- DPA-300 §4.4: workflow orchestration owns sequencing and MUST NOT become target writer;
- DPA-500 §8: acceptance state is scoped to exactly one registered target identity;
- DPA-500 §9: only complete lifecycle verification, gates and persistence produce `accepted`.

Observed defect:

The phrase `one higher-level completion decision` can be read as a new aggregate acceptance authority or aggregate trust state spanning several targets.

Consequence:

That interpretation would create a second acceptance layer outside the existing lifecycle and target-scoped acceptance-state contract.

Smallest safe correction:

Define aggregate completion as an orchestration result only. It MUST NOT create a consumer trust state, acceptance-state record, target authority or independent persistent state. Aggregate success is derivable only when every required target has its own lifecycle-owned accepted result and every declared secondary effect and cleanup obligation has verified success. Failure preserves per-target outcomes and creates one bounded orchestration recovery identity.

Refreeze required: yes.

### PMA-M02 — Runtime home of the command mutation contract is ambiguous

Severity: MAJOR

Affected proposal:

- command mutation contract definition;
- DPA-300 command-integration clauses;
- candidate diagram edge `CLI command mode -> command mutation contract`.

Governing anchors:

- DPA-200 §3.10;
- DPA-300 §§1 and 4;
- ADR-022 prohibition on a second command registry or writer authority.

Observed defect:

The proposal correctly says the contract is not a second registry, but it does not state where its runtime authority must live. A future implementation could therefore introduce a DPA-owned command-contract store while claiming textual conformance.

Consequence:

The proposal would insufficiently exclude the parallel-system failure it is intended to prevent.

Smallest safe correction:

State that the contract MUST be represented by a reviewed extension of one existing main-repository authority selected after exact-ref validation, such as the existing command manifest, existing command metadata or statically reviewed code mapping. The Lab proposal defines required semantics only and authorizes no new persistence surface. Duplicate declarations that can diverge are prohibited.

Refreeze required: yes.

### PMA-M03 — Proposed finding names can be mistaken for concrete runtime codes

Severity: MAJOR

Affected proposal:

- candidate DPA-500 §6.2 findings.

Governing anchors:

- DPA-500 §§1, 3 and 11: concrete finding identifiers and severity mappings remain `NEEDS_MAIN_REPO_VALIDATION` and are owned by the existing finding system.

Observed defect:

The proposal lists hyphenated identifiers under `DPA-500 should define distinct findings`. This can be read as creating concrete production finding codes before exact-ref validation.

Consequence:

It risks a second taxonomy or a repository-specific normative claim unsupported by evidence.

Smallest safe correction:

Classify the listed strings as proposal-local abstract subreason labels only. DPA-500 may require distinct semantics, but concrete identifiers and mappings must be adapted into the existing main-repository finding system after validation.

Refreeze required: yes.

### PMA-m01 — `accepted source snapshot` is imprecise

Severity: MINOR

Affected proposal:

- synchronized projection-set definition.

Observed defect:

A source snapshot is captured and fingerprinted as a plan input; it is not itself assigned the DPA consumer trust state `accepted`.

Smallest safe correction:

Use `one immutable, plan-bound source snapshot identity` and reserve `accepted` for lifecycle-governed target output.

Refreeze required: yes.

## 4. Confirmed non-findings

The audit found no defect in these boundaries:

- one renderer invocation still returns one target payload;
- renderers remain pure and are not writers;
- the existing lifecycle remains the sole projected-target writer;
- changed-path equality supplements rather than replaces semantic and content verification;
- aliases with materially different effects require separate classification;
- direct generated-surface repair cannot silently become accepted state;
- current Probe manuals remain unchanged;
- ADR-022 remains a deferred proposal;
- DPA-600 remains frozen and DPA-700 remains unstarted.

## 5. Required disposition

Before independent review:

1. add a bounded correction addendum resolving PMA-M01 through PMA-m01;
2. freeze a new immutable review ref including the addendum and this audit;
3. update the review request to the new exact ref and require reviewers to assess the corrections;
4. do not mutate the original immutable review branch.
