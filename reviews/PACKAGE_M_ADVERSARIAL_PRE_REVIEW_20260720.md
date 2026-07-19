# Package M Adversarial Pre-Review

Status: complete

Status-date: 2026-07-20

Review role: adversarial Maintainer/self-review; not independent verification

Exact review target: `d7d0bf5729d935579280f6acba96771ac8a54b44`

Review instruction ref: `402ade550d246047ff8da989fe01fe93b3633b6a`

Verdict: `ACCEPT_WITH_CHANGES`

## 1. Scope and limitation

This review evaluates the Package M command-mutation-authority proposal together with its correction addendum against the current Lab authority, lifecycle, renderer, freshness, gate and Probe boundaries.

It is an adversarial pre-review performed in the same working context that prepared Package M. It is not independent verification and cannot satisfy the independent-review requirement in `reviews/PACKAGE_M_COMMAND_AUTHORITY_REVIEW_REQUEST_V2.md`.

No normative DPA specification, ADR status, Probe manual, Probe result or main-repository implementation is changed or accepted by this review.

## 2. Material reviewed

The review considered:

- `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`;
- `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`;
- `reviews/PACKAGE_M_INTERNAL_CONSISTENCY_AUDIT_20260720.md`;
- DPA-200, DPA-300, DPA-400 and DPA-500 authority boundaries;
- ADR-022 as a deferred proposal;
- the Package M inventory, overlap, ownership and Probe-coverage planning artifacts;
- the V2 review questions and prohibitions.

The addendum controls wherever it narrows or conflicts with the original clause proposal.

## 3. Executive assessment

Package M does not presently require rejection. The correction addendum successfully removes the previously identified risks of:

- aggregate acceptance authority;
- aggregate consumer trust state;
- a DPA-owned command registry or persistence surface;
- independently editable duplicate command-contract stores;
- proposal-local labels becoming concrete production finding identifiers;
- alias identity automatically becoming target freshness input.

The proposal also preserves:

- one renderer invocation per registered target;
- lifecycle-owned target writes and target-scoped acceptance;
- separation of plan validity, target freshness, trust state, command conformance and aggregate attempt outcome;
- provisional status for repository-specific mappings;
- the freeze on DPA-600 and the prohibition on beginning DPA-700.

Three additional defects should be corrected before Maintainer adjudication of the bounded amendment package. None is a blocker, but two are material authority-boundary defects.

## 4. Finding summary

| ID | Severity | Subject | Refreeze required | Independent rereview required |
|---|---|---|---|---|
| `PMA2-M01` | MAJOR | contract granularity for internal entry points | yes | yes |
| `PMA2-M02` | MAJOR | DPA-500 ownership over command failures | yes | yes |
| `PMA2-m01` | MINOR | conditional changed-path conformance | yes | yes |

No blocker was found.

## 5. Findings

### PMA2-M01 — Internal helper functions are over-classified as independent command-contract subjects

Severity: `MAJOR`

Exact surface:

- `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`, proposed DPA-300 §4.6;
- sentence beginning: “Every command mode and internal entry point that may create, rewrite, append, replace, move, archive or delete...”

Governing anchors:

- DPA-300 responsibility boundary and immutable-plan authority;
- the addendum requirement that one command-mode contract be represented through exactly one existing runtime authority;
- the prohibition on independently editable duplicate declarations;
- the existing lifecycle remaining the sole writer for projected targets.

Observed defect:

The phrase “every ... internal entry point” is too broad. A low-level helper, lifecycle method, adapter or child function may physically perform bytes or state mutation while remaining entirely subordinate to one already-classified top-level command mode or composed mutation step. Requiring a separate reviewed command mutation contract for every such function would duplicate authority declarations, confuse call-graph implementation detail with runtime mutation authority and potentially create the parallel contract inventory that the addendum is intended to prohibit.

Consequence:

- contract identity could fragment across implementation layers;
- refactoring a helper could appear to change runtime authority unnecessarily;
- duplicate or inconsistent declarations could emerge;
- lifecycle-owned internal operations could be misrepresented as independent command authorities;
- Probe scope could expand from observable mutation modes to every implementation function.

Smallest safe correction:

Replace the rule with a boundary-based requirement:

> Every externally invocable command mode, compatibility alias with materially distinct behavior, and independently schedulable or recoverable composed mutation step that can authorize document-like mutation MUST resolve through one reviewed command mutation contract before mutation. Internal helpers that cannot independently broaden authority, select targets, persist state, be invoked outside the owning operation or produce an independently recoverable result inherit the owning contract and MUST NOT define a competing contract.

The normative amendment should additionally require static review or testing that internal delegated paths cannot bypass or broaden the owning contract.

Refreeze required: yes.

Independent rereview required: yes.

### PMA2-M02 — DPA-500 is at risk of becoming the general command-mutation finding owner

Severity: `MAJOR`

Exact surfaces:

- `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`, candidate DPA-500 §§6.1–6.3;
- `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`, §§4–5.

Governing anchors:

- DPA-500 scope: projection freshness, projection-specific finding semantics, consumer-trust consequences and gate behavior;
- DPA-500 exclusion of concrete finding codes, command UX and production implementation;
- DPA-300 ownership of lifecycle ordering, mutation plans, verification, recovery and attempt outcomes;
- the existing main-repository finding system remaining the production finding authority.

Observed defect:

The addendum correctly makes the proposed labels abstract and proposal-local, but it does not fully resolve which specification owns their semantics. Several labels concern command-plan or mutation-attempt conformance rather than projection freshness:

- `unclassified-command-mutator`;
- `unauthorized-direct-writer`;
- `unexpected-changed-path`;
- `missing-expected-output`;
- `undeclared-secondary-writer`;
- `alias-authority-divergence`.

Making DPA-500 define all of these as its distinct abstract finding semantics would broaden DPA-500 into a general command-mutation failure model. The addendum’s freshness correction narrows when command identity affects target freshness, but the ownership split remains implicit.

Consequence:

- DPA-300 and DPA-500 could both appear to own command verification failures;
- non-projection document mutations could be pulled into projection freshness architecture;
- command conformance could be incorrectly represented as target staleness;
- gate consequences and lifecycle failure causes could be conflated;
- future implementation might introduce a DPA-500-specific command finding layer.

Smallest safe correction:

Split ownership explicitly:

1. DPA-300 defines command-plan, mutation-attempt, changed-path, secondary-effect, alias-equivalence and recovery failure semantics.
2. DPA-500 defines only:
   - the projection-freshness consequence when an accepted target contract declares command semantics output- or acceptance-affecting;
   - projection-specific gate consequences;
   - `mixed-source-snapshot`, `partial-synchronized-projection-set`, `direct-generated-surface-edit` and `stale-generated-reference` only to the extent that they affect registered projection evaluation.
3. All production identifiers, severity mappings and serialization remain mappings into the existing main-repository finding authority.
4. A DPA-300 failure must not automatically classify an otherwise independently evaluable accepted target as stale.

Refreeze required: yes.

Independent rereview required: yes.

### PMA2-m01 — Exact changed-path equality does not yet model contract-declared conditional outputs precisely

Severity: `MINOR`

Exact surface:

- `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`, proposed DPA-300 §10.5.

Governing anchors:

- immutable mutation-plan target and scope binding;
- fail-closed treatment of unexpected mutations;
- post-write semantic and ownership verification;
- bounded no-op behavior.

Observed defect:

The current text speaks of equality between the actual changed-path set and the plan-authorized set, and treats a missing expected path as failure unless an explicit no-op is permitted. This is adequate for a fixed exact output set but under-specified for commands whose contract authorizes a bounded conditional result, for example:

- create only when missing;
- rewrite only when semantic content differs;
- remove zero or more obsolete members selected by a plan-bound inventory;
- emit an optional report only when a declared finding exists;
- perform cleanup only when a declared temporary artifact was created.

In these cases the authorized set is a maximum permission boundary, while the expected set is a conditionally resolved obligation. Strict equality against the maximum authorized set would produce false failures; equality against an under-specified expected set could hide omissions.

Consequence:

The rule may either over-fail legitimate conditional mutations or encourage broad authorization sets that weaken omission detection.

Smallest safe correction:

Define three plan-bound sets or predicates:

- `authorized_changed_paths`: the maximum fail-closed mutation boundary;
- `required_changed_paths`: paths that must change after preconditions are resolved;
- `permitted_conditional_paths`: paths whose change or non-change is governed by explicit, verified conditions.

Require:

- actual changed paths are a subset of `authorized_changed_paths`;
- every `required_changed_path` is present;
- every conditional path outcome satisfies its plan-bound predicate;
- unexpected changes always fail;
- missing required changes fail;
- verified no-op is one conditional outcome, not a blanket exception;
- semantic, content, ownership and acceptance verification remain separate.

Equivalent relational wording is acceptable; these exact field names need not become normative.

Refreeze required: yes.

Independent rereview required: yes.

## 6. Resolution status of prior findings

### PMA-M01 — aggregate completion authority ambiguity

Status: `FULLY_RESOLVED_FOR_REVIEW_CANDIDATE`

Reason:

The addendum makes the aggregate result derived workflow-orchestration output only and expressly prohibits it from becoming a trust state, acceptance-state record, canonical authority, target writer or independent persistent state.

### PMA-M02 — command mutation contract could become a new runtime registry

Status: `FULLY_RESOLVED_FOR_REVIEW_CANDIDATE`

Reason:

The addendum requires representation through exactly one existing main-repository authority selected after exact-ref validation, prohibits an independently editable duplicate store and leaves concrete storage `NEEDS_MAIN_REPO_VALIDATION`.

PMA2-M01 does not reopen the new-registry defect; it narrows which invocation boundaries require a contract.

### PMA-M03 — proposal labels could become a second finding taxonomy

Status: `FULLY_RESOLVED_FOR_IDENTIFIER_AND_STORAGE_BOUNDARY`

Reason:

The labels are explicitly proposal-local and concrete production mappings remain with the existing finding system.

PMA2-M02 identifies a remaining specification-ownership issue, not a renewed concrete-code or persistence-taxonomy defect.

### PMA-m01 — source-snapshot and acceptance terminology

Status: `FULLY_RESOLVED_FOR_REVIEW_CANDIDATE`

Reason:

The addendum binds synchronization to immutable plan-bound source-snapshot identity without assigning acceptance or trust state to the snapshot itself.

## 7. Required parallel-system assessment

| Subject | Classification | Controlling authority / explanation |
|---|---|---|
| command mutation contract | `EXISTING_AUTHORITY_EXTENSION` | Must extend exactly one existing command manifest, command metadata or statically reviewed code authority selected after exact-ref validation; no new DPA store is allowed. |
| CMA primary classes | `PROPOSAL_LOCAL_VOCABULARY_ONLY` | Planning classification used to reason about command effects; it has no accepted runtime serialization or independent authority. |
| synchronized projection set | `EXISTING_AUTHORITY_EXTENSION` | Existing workflow orchestration coordinates multiple target-scoped lifecycle results; each target remains governed by DPA-300 lifecycle and acceptance. |
| derived aggregate attempt result | `EXISTING_AUTHORITY_EXTENSION` | Existing workflow/result reporting may derive a bounded summary; it has no independent trust, acceptance, write or persistence authority. |
| aggregate recovery identity | `EXISTING_AUTHORITY_EXTENSION` | Existing workflow/lifecycle recovery evidence may correlate member outcomes while target recovery remains lifecycle-owned. Concrete persistence remains subject to exact-ref validation. |
| changed-path verifier | `EXISTING_AUTHORITY_EXTENSION` | DPA-300 post-write verification and immutable-plan scope checking; it is a verification responsibility, not a new writer or gate system. PMA2-m01 requires more precise relational semantics. |
| proposal-local finding subreason labels | `PROPOSAL_LOCAL_VOCABULARY_ONLY` | They are review vocabulary only. Production identifiers and severities remain with the existing finding authority. Their DPA-300/DPA-500 ownership split requires PMA2-M02 correction. |
| proposal-local DMA traceability identifiers | `PROPOSAL_LOCAL_VOCABULARY_ONLY` | They organize proposed requirement groups and expressly do not create a second invariant namespace. |

No reviewed subject presently requires classification as `PARALLEL_SYSTEM_RISK` after application of the correction addendum, provided PMA2-M01 and PMA2-M02 are corrected before normative application.

## 8. Review-question disposition

1. Existing authority extension rather than parallel subsystem: `PASS_WITH_FINDINGS`.
2. One semantic fact, one canonical authority: `PASS`.
3. Write ownership distinct from orchestration: `PASS`.
4. Lifecycle sole writer and target acceptance owner: `PASS`.
5. Contract bound to one existing runtime authority: `PASS`, exact home remains `NEEDS_MAIN_REPO_VALIDATION`.
6. Duplicate editable declarations prohibited: `PASS`.
7. Modes, aliases and secondary effects precise: `PASS_WITH_FINDING_PMA2-M01`.
8. Changed-path comparison testable and separate from semantic verification: `PASS_WITH_FINDING_PMA2-m01`.
9. One renderer invocation per target: `PASS`.
10. Aggregate completion remains derived only: `PASS`.
11. Per-target acceptance distinct from aggregate outcome: `PASS`.
12. Partial success visible and recoverable: `PASS`.
13. Generator orchestration preserves renderer purity: `PASS`.
14. Plan invalidation distinguished from target freshness: `PASS`.
15. Labels remain abstract, not production codes: `PASS_WITH_FINDING_PMA2-M02` for specification ownership only.
16. DMA identifiers do not create invariant namespace: `PASS`.
17. Repository mappings remain provisional: `PASS`.
18. Probe impact remains bounded: `PASS`; adjudication of proposed cases is still required before any Probe change.
19. DPA-600 frozen and DPA-700 unstarted: `PASS`.
20. Additional amendment surfaces: DPA-300/DPA-500 ownership split and internal-entry-point granularity require correction.

## 9. Probe consequences

No Probe may be executed or retrospectively broadened as a consequence of this review.

Before later Probe adjudication, Package M should ensure that cases distinguish:

- top-level or independently recoverable mutation authority boundaries from subordinate internal helpers;
- unauthorized actual paths from permitted conditional paths and missing required paths;
- command-attempt conformance failures from projection-freshness consequences;
- per-target lifecycle results from derived aggregate attempt results.

These are candidate coverage refinements only. They do not modify an existing Probe identity or PASS condition.

## 10. Verdict and progression decision

Verdict: `ACCEPT_WITH_CHANGES`

Blocker exists: no.

PMA-M01, PMA-M02, PMA-M03 and PMA-m01 fully resolved: yes, for the corrected review candidate and with the qualification stated for PMA-M03 that PMA2-M02 concerns specification ownership rather than production-taxonomy authority.

ADR-022 may proceed to Maintainer adjudication as a deferred proposal: not yet. First apply the three bounded review corrections and refreeze the candidate. No new remote inventory is required for those corrections.

Bounded DPA-200/300/400/500 amendment package ready for adjudication but not normative application: not yet. It becomes ready for Maintainer adjudication after PMA2-M01, PMA2-M02 and PMA2-m01 are resolved and the corrected candidate receives independent review.

Additional remote inventory required before adjudication: no.

Local exact-ref validation required before repository-specific acceptance: yes.

DPA-600 must remain frozen: yes.

DPA-700 may begin: no.

## 11. Required next sequence

1. prepare one bounded Package M correction addendum V2 resolving PMA2-M01, PMA2-M02 and PMA2-m01;
2. do not edit the existing immutable review branch;
3. freeze a new immutable review ref;
4. update the independent review request to point to that ref and state that the original proposal plus both controlling addenda form the review candidate;
5. run Lab gates and record exact evidence;
6. obtain independent review;
7. only after an acceptable independent verdict, present ADR-022 and the bounded amendment package for Maintainer adjudication;
8. keep DPA-600 frozen and DPA-700 unstarted throughout.
