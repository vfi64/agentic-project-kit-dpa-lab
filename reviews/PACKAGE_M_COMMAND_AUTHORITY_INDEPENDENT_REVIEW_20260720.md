# Package M Command Authority — Independent Architecture Review

Status: complete

Status-date: 2026-07-20

Review role: independent architecture verification

## 1. Review metadata

- Review target repository: `vfi64/agentic-project-kit-dpa-lab`.
- Review candidate: Package M — document mutation authority and command integration.
- Driving request: `reviews/PACKAGE_M_COMMAND_AUTHORITY_REVIEW_REQUEST_V3.md`.
- Immutable review branch: `review/package-m-command-authority-v3-20260720`.
- Exact reviewed commit: `3527a181fa602957ee2ff20b047fa50ce98f00e6`.
- Working branch for this deliverable: `spec/dpa-600-concurrency`.
- No main-repository source was inspected; repository-specific statements remain `NEEDS_MAIN_REPO_VALIDATION`.

## 2. Method

The reviewer read the mandatory Lab bootstrap, DPA-000 and DPA-100, DPA-200 through DPA-500, the Package M proposal, ADR-022, both correction addenda, the evidence inventories and matrices, the internal reviews, Probe contracts and sequencing state.

Conflict precedence applied:

1. `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_V2_20260720.md`;
2. `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`;
3. `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`.

Internal reviews were treated only as draft-history evidence. Every prior finding was re-evaluated against the controlling text.

## 3. Limitations

- No exact-ref inspection of `vfi64/agentic-project-kit` was performed.
- This review is not Probe evidence, implementation validation, adoption, maintainer adjudication or main-repository conformance.
- The original reviewer had no push credential. The locally reported gate result and local commit were not remote evidence and are not adopted as such by this repository copy.

## 4. Verdict

Verdict: `ACCEPT_WITH_CHANGES`.

No blocker exists.

The proposal and both controlling addenda extend existing DPA authority families rather than creating a second command registry, lifecycle, writer authority, acceptance authority, trust-state taxonomy, finding system, gate runner, evidence authority or state store.

All seven prior findings are independently confirmed resolved:

- `PMA-M01`;
- `PMA-M02`;
- `PMA-M03`;
- `PMA-m01`;
- `PMA2-M01`;
- `PMA2-M02`;
- `PMA2-m01`.

## 5. Finding summary

| ID | Severity | Subject | Refreeze | Rereview |
|---|---|---|---|---|
| `IRM-01` | MINOR | Evidence-base tokens such as `REMOTE_VERIFIED`, `REMOTE_PARTIAL` and `VERIFICATION_BLOCKED` are not members of the closed DPA-100 classification vocabulary | no | no |
| `IRE-01` | EDITORIAL | Frozen V3 candidate contains freeze/readiness wrappers that still describe the prior V2 review ref | no | no |
| `IRE-02` | EDITORIAL | `aggregate recovery identity` needs an explicit statement that it uses existing workflow/lifecycle recovery state and creates no new persistence surface | no | no |

Totals: blockers 0, majors 0, minors 1, editorials 2.

## 6. Findings

### IRM-01 — Evidence classification hygiene

Affected planning evidence uses analysis tokens that are not part of the closed DPA-100 repository-fact classification set. This does not alter the normative candidate, which correctly leaves repository-specific mappings `NEEDS_MAIN_REPO_VALIDATION`.

Smallest safe correction: declare the tokens as a separate analysis-only namespace and provide an explicit DPA-100 mapping, or replace them with the applicable DPA-100 classification. Do not edit the frozen review branch.

### IRE-01 — Stale frozen navigation wrappers

`integration/PACKAGE_M_REVIEW_FREEZE_RECORD_20260720.md` and `integration/PACKAGE_M_REVIEW_READINESS_CHECKPOINT_20260720.md` remain historically accurate for V2 but are stale as navigation wrappers inside V3. The V3 review request and candidate composition control. Do not refreeze solely for this editorial defect.

### IRE-02 — Recovery identity wording

The bounded orchestration recovery identity must be carried by already-existing workflow/lifecycle recovery state or evidence. It must not authorize a new store, new canonical history or independent persistent aggregate state. Concrete representation remains `NEEDS_MAIN_REPO_VALIDATION`.

## 7. Prior-finding resolution

- `PMA-M01`: resolved by making aggregate outcome derived workflow output only and excluding trust, acceptance, write and persistence authority.
- `PMA-M02`: resolved by binding the command mutation contract to exactly one existing main-repository authority selected after exact-ref validation.
- `PMA-M03`: resolved by keeping proposed finding strings as abstract proposal-local labels.
- `PMA-m01`: resolved by reserving acceptance terminology for lifecycle-owned target results.
- `PMA2-M01`: resolved by requiring subordinate helpers to inherit the owning command contract without broadening authority.
- `PMA2-M02`: resolved by assigning general command/mutation failures to DPA-300 and only projection freshness/gate consequences to DPA-500.
- `PMA2-m01`: resolved by replacing strict changed-path equality with plan-bound conformance over authorized, required, conditional and temporary paths.

## 8. Parallel-system assessment

| Subject | Classification | Existing authority or boundary |
|---|---|---|
| command mutation contract | `EXISTING_AUTHORITY_EXTENSION` | exactly one existing main-repository command authority, selected after exact-ref validation |
| CMA primary classes | `PROPOSAL_LOCAL_VOCABULARY_ONLY` | planning taxonomy only |
| synchronized projection set | `EXISTING_AUTHORITY_EXTENSION` | existing workflow orchestration over independent lifecycle targets |
| derived aggregate attempt result | `EXISTING_AUTHORITY_EXTENSION` | workflow result reporting only |
| aggregate recovery identity | `EXISTING_AUTHORITY_EXTENSION` | existing workflow/lifecycle recovery; see `IRE-02` |
| changed-path verifier | `EXISTING_AUTHORITY_EXTENSION` | DPA-300 plan and post-write verification |
| proposal-local finding labels | `PROPOSAL_LOCAL_VOCABULARY_ONLY` | existing main-repository finding system retains production authority |
| proposal-local DMA identifiers | `PROPOSAL_LOCAL_VOCABULARY_ONLY` | traceability labels only; DPA-000 invariants remain authoritative |
| internal helper inheritance | `EXISTING_AUTHORITY_EXTENSION` | owning command contract and lifecycle boundary |
| command-contract runtime home | `EXISTING_AUTHORITY_EXTENSION` | one existing runtime authority; concrete home remains `NEEDS_MAIN_REPO_VALIDATION` |
| target-scoped acceptance | `EXISTING_AUTHORITY_EXTENSION` | DPA-300/DPA-500 lifecycle acceptance |
| command-plan invalidation | `EXISTING_AUTHORITY_EXTENSION` | DPA-300 immutable plan and stale-plan rules |
| command-related DPA-500 consequences | `EXISTING_AUTHORITY_EXTENSION` | DPA-500 freshness and gate consequences only |

No subject is `AMBIGUOUS_REQUIRES_CORRECTION` or `PARALLEL_SYSTEM_RISK` after application of both addenda.

## 9. Specification ownership

- DPA-200 owns semantic-fact authority, command-mutation versus write ownership and generated-surface invalid states.
- DPA-300 owns command/lifecycle integration, plan fields, changed-path conformance, verification, failure semantics and recovery.
- DPA-400 owns renderer purity, determinism and one invocation per registered target.
- DPA-500 owns only projection freshness, trust-state and gate consequences.

No reviewed clause is materially mis-homed.

## 10. Probe and sequencing assessment

No Probe identity, fixture, PASS condition or executed evidence is changed. Package M planning labels are not Probe case identifiers. Any future Probe amendment requires adjudication and a new immutable identity where applicable.

DPA-600 remains frozen with status `draft`.

DPA-700 remains unstarted with status `planned`.

## 11. Mandatory closing answers

- Blocker: no.
- All seven prior findings resolved: yes.
- ADR-022 may proceed as a `DEFERRED PROPOSAL` to maintainer adjudication: yes.
- Bounded DPA-200/300/400/500 amendment package adjudication-ready but not normatively applicable: yes, after disposition of the non-normative findings.
- Additional remote inventory before adjudication: no.
- Local exact-ref main-repository validation before repository-specific acceptance: yes.
- DPA-600 must remain frozen: yes.
- DPA-700 must remain unstarted: yes.
- New refreeze required for these findings: no.
- Immediate further independent rereview required: no.

## 12. Final recommendation

Proceed to maintainer adjudication of ADR-022 and the bounded amendment package after closing `IRM-01` on the working branch and recording the editorial dispositions. Keep the package non-normative and non-applicable until exact-ref main-repository validation and applicable Probe evidence exist.

This review document does not amend the frozen candidate, any DPA specification, ADR-022, either correction addendum, a Probe manual, a fixture or the main repository.