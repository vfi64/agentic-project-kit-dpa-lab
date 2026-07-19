# Package M Command Authority Correction Addendum

Status: review-candidate

Status-date: 2026-07-20

Authority: non-normative bounded correction to `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`

Resolves:

- `PMA-M01`;
- `PMA-M02`;
- `PMA-M03`;
- `PMA-m01`.

## 1. Boundary

This addendum corrects ambiguity in the Package M clause proposal before independent review.

It does not amend DPA-200 through DPA-500, accept ADR-022, create runtime state, execute a Probe or authorize main-repository changes.

Where this addendum conflicts with the earlier proposal, this addendum controls the Package M review candidate.

## 2. Corrected synchronized projection-set definition

Replace the proposal's synchronized projection-set definition with:

> A **synchronized projection set** is two or more generated targets whose contracts require derivation from one immutable, plan-bound source-snapshot identity and whose orchestration requires one bounded aggregate attempt result.
>
> Each member retains exactly one registered target identity, one renderer invocation and one lifecycle-owned target result. The aggregate attempt result is workflow-orchestration output only. It MUST NOT create a consumer trust state, acceptance-state record, canonical authority, target write owner or independent persistent state.
>
> Aggregate success may be reported only when every required member has completed its own lifecycle-owned verification, required gates and target-scoped acceptance, and every declared secondary effect and cleanup obligation has verified success.
>
> Aggregate failure preserves every member's actual lifecycle and trust-state outcome and creates one bounded orchestration recovery identity. It MUST NOT downgrade, promote or replace a target's lifecycle-owned acceptance state.

Consequential interpretation:

- `aggregate completion decision` means a derived orchestration result, not acceptance authority;
- the existing workflow layer may coordinate ordering and summarize results but MUST NOT write targets or acceptance state;
- no aggregate acceptance database, trust state or DPA state store is permitted;
- a later diagram must label the edge `workflow orchestration -> derived aggregate attempt result` rather than `aggregate coordinator -> synchronized projection-set completion decision`.

## 3. Corrected command mutation-contract authority

Add to the proposal's command mutation-contract definition:

> A command mutation contract MUST be represented through a reviewed extension of exactly one existing main-repository authority selected after exact-ref validation. Candidate existing homes may include the existing command manifest, existing command metadata or a statically reviewed code mapping. The Lab proposal defines required semantics only and authorizes no new persistence surface.
>
> The same command-mode contract MUST NOT be duplicated in independently editable stores. Derived references MAY project the contract but MUST identify their source and MUST NOT become runtime authority.

Consequential interpretation:

- the contract is not a DPA-owned command registry;
- concrete storage, schema and mapping remain `NEEDS_MAIN_REPO_VALIDATION`;
- the existing registry, lifecycle, command manifest and code authorities retain their current ownership until an accepted bounded amendment assigns integration responsibilities;
- unknown runtime home or conflicting duplicate declarations fail closed for mutation.

## 4. Corrected DPA-500 finding language

Replace `DPA-500 should define distinct findings for` with:

> DPA-500 should require distinct abstract finding semantics for the following proposal-local subreason labels:

The listed labels remain:

- `unclassified-command-mutator`;
- `unauthorized-direct-writer`;
- `unexpected-changed-path`;
- `missing-expected-output`;
- `undeclared-secondary-writer`;
- `alias-authority-divergence`;
- `direct-generated-surface-edit`;
- `mixed-source-snapshot`;
- `partial-synchronized-projection-set`;
- `stale-generated-reference`.

Add:

> These strings are proposal-local labels, not accepted production finding identifiers. Concrete identifiers, severity mappings, serialization and UX wording remain owned by the existing main-repository finding system and remain `NEEDS_MAIN_REPO_VALIDATION`.

## 5. Corrected acceptance and freshness interpretation

The command or orchestration identity is relevant to target freshness only when the accepted target contract declares that identity or its semantics as output-affecting or acceptance-affecting input.

Alias choice alone MUST NOT make byte-equivalent accepted output stale when the alias is proven contract-equivalent and the target acceptance contract does not distinguish it.

A changed command contract that broadens authority, target set, source set, secondary effects, ordering or verification obligations invalidates the active mutation plan even when output bytes might remain equal.

This keeps:

- plan validity;
- target freshness;
- consumer trust state;
- command conformance;
- aggregate attempt outcome

as distinct dimensions.

## 6. Corrected recovery interpretation

For a synchronized projection set:

- target recovery remains lifecycle-owned per registered target;
- orchestration recovery records which member results and secondary effects remain unresolved;
- a new aggregate attempt requires a new plan-bound source-snapshot identity and current per-target plans;
- already accepted target results may be reused only when their current contracts explicitly permit reuse and all required freshness and aggregate-snapshot conditions are revalidated;
- orchestration MUST NOT fabricate all-or-nothing rollback where a target-specific contract does not provide it;
- partial success MUST remain visible and MUST NOT be mislabeled aggregate success.

## 7. Review obligations added

The independent reviewer must determine whether these corrections:

1. fully exclude an aggregate acceptance authority or aggregate trust state;
2. preserve target-scoped lifecycle acceptance;
3. bind the command mutation contract to an existing runtime authority rather than a new store;
4. prevent duplicate editable command-contract declarations;
5. preserve the existing finding taxonomy and repository-specific mapping boundary;
6. correctly distinguish plan invalidation from target freshness;
7. preserve DPA-600 and DPA-700 sequencing restrictions.

## 8. Effect on prior proposal

The prior proposal remains the primary clause draft except where this addendum explicitly replaces or narrows its text.

The pair must be reviewed together. Neither document is normative.
