# Package M Command Authority Correction Addendum V2

Status: review-candidate

Status-date: 2026-07-20

Authority: non-normative bounded correction to the Package M clause proposal and first correction addendum

Resolves:

- `PMA2-M01`;
- `PMA2-M02`;
- `PMA2-m01`.

## 1. Boundary and precedence

This addendum corrects the three findings in `reviews/PACKAGE_M_ADVERSARIAL_PRE_REVIEW_20260720.md`.

It does not amend DPA-200 through DPA-500, accept ADR-022, create runtime state, execute a Probe or authorize main-repository changes.

The Package M review candidate consists of:

1. `integration/PROPOSED_COMMAND_MUTATION_AUTHORITY_CLAUSES_20260720.md`;
2. `integration/PACKAGE_M_COMMAND_AUTHORITY_CORRECTION_ADDENDUM_20260720.md`;
3. this addendum.

Where this addendum conflicts with or narrows either earlier document, this addendum controls.

## 2. Corrected contract granularity

Replace the first paragraph proposed for DPA-300 §4.6 with:

> Every externally invocable command mode, compatibility alias with materially distinct behavior, and independently schedulable or independently recoverable composed mutation step that can authorize document-like mutation MUST resolve through one reviewed command mutation contract before mutation.
>
> An internal helper, lifecycle method, adapter or delegated function that cannot independently broaden authority, select additional targets, persist independent authoritative state, be invoked outside the owning operation or produce an independently recoverable result inherits the owning command mutation contract and MUST NOT define a competing command mutation contract.
>
> Delegation MUST remain statically reviewable. An inherited internal path MUST NOT broaden the owning contract's target set, changed-path boundary, source authority, secondary effects, lock scope, verification obligations or recovery authority.

Consequential interpretation:

- contract identity follows an observable or independently recoverable mutation-authority boundary, not every implementation function;
- helper refactoring alone does not create a new command mode or contract identity;
- a child step requires independent classification only when it has independently schedulable, authority-bearing or recoverable semantics;
- no internal path may bypass the owning contract merely because it is not independently declared;
- Probe coverage targets authority-bearing modes and bounded child steps, while static and focused tests cover subordinate delegation integrity.

## 3. Corrected DPA-300 and DPA-500 ownership split

Replace the earlier interpretation that DPA-500 should define all listed command-mutation finding semantics with the following ownership split.

### 3.1 DPA-300-owned failure semantics

DPA-300 should define abstract lifecycle and mutation-attempt failure semantics for:

- unclassified mutation-authority boundary;
- unauthorized direct writing;
- unexpected changed path;
- missing required output;
- violated conditional-path predicate;
- undeclared or failed secondary writer effect;
- alias or delegated-path authority divergence;
- command-contract mismatch or invalidation;
- composed-step ordering or recovery failure.

These are command-plan, mutation-attempt, verification or recovery failures. They MUST NOT automatically classify previously accepted target bytes as stale.

### 3.2 DPA-500-owned projection consequences

DPA-500 should define only the projection-freshness and gate consequences that arise when:

- an accepted target contract declares command semantics output-affecting or acceptance-affecting;
- a registered projection has a mixed source snapshot;
- a synchronized projection attempt is only partially complete;
- a generated surface was edited directly in a way relevant to registered target evaluation;
- a generated reference is stale under the registered projection contract;
- a DPA-300 failure prevents safe projection evaluation, mutation or acceptance.

DPA-500 MUST preserve the distinction between:

- DPA-300 mutation-attempt failure;
- target freshness classification;
- consumer trust state;
- gate decision;
- enforcement stage.

A DPA-300 command failure may produce a DPA-500 gate failure for the active projection operation without making independently verifiable, previously accepted bytes stale.

### 3.3 Existing finding authority

All labels in the Package M documents remain proposal-local abstract language.

Concrete identifiers, severity mappings, serialization, suppression rules and user-facing wording remain owned by the existing main-repository finding authority and remain `NEEDS_MAIN_REPO_VALIDATION`.

No DPA-300-specific or DPA-500-specific production finding store, taxonomy or service is authorized.

## 4. Corrected changed-path conformance relation

Replace the proposed strict changed-path equality rule with:

> Every mutating command MUST bind a plan-scoped changed-path conformance relation before mutation.
>
> The plan MUST distinguish, directly or through equivalent predicates:
>
> - the maximum authorized changed-path boundary;
> - paths or path classes required to change after plan-bound preconditions are resolved;
> - conditionally permitted paths whose change or non-change is governed by explicit plan-bound predicates;
> - declared temporary paths and their required cleanup or retention outcome.
>
> The actual changed-path set MUST be a subset of the maximum authorized boundary. Every required change MUST occur. Every conditional path outcome MUST satisfy its bound predicate. Every temporary path MUST satisfy its cleanup or retention contract.
>
> Any unauthorized changed path, missing required change, violated conditional predicate or unexplained residual temporary path is mutation failure.
>
> A verified no-op is one explicitly declared conditional outcome. It is not a blanket exception and MUST NOT broaden authority or suppress missing required work.
>
> Changed-path conformance does not replace content, semantic, ownership, lifecycle, acceptance or recovery verification.

Consequential interpretation:

- fixed-output commands may use exact set equality as a special case;
- conditional commands must not authorize broad path sets merely to avoid omission failures;
- condition resolution must be plan-bound and reproducible rather than inferred after mutation;
- create-if-missing, rewrite-if-different, bounded cleanup and conditional report emission remain testable without weakening fail-closed mutation scope.

## 5. Traceability effect

The later normative amendment should preserve the proposal-local requirement groups while refining:

- `DMA-004` to apply to every materially distinct authority-bearing command mode or independently recoverable composed step, not subordinate helpers;
- `DMA-007` from literal set equality to plan-bound changed-path conformance;
- `DMA-012` so DPA-500 owns projection freshness and gate consequences while DPA-300 owns command-plan and mutation-attempt failure semantics.

These identifiers remain proposal-local and do not create a second invariant namespace.

## 6. Probe consequences

No Probe manual or identity is changed by this addendum.

Future Probe adjudication should distinguish:

- authority-bearing command modes from subordinate inherited helpers;
- maximum authorized paths, required changes and conditionally permitted outcomes;
- command-attempt failure from target freshness consequence;
- per-target lifecycle outcome from derived aggregate attempt result.

Static review and focused implementation tests may be required for delegated helper non-bypass properties. That does not by itself require a separate externally executed Probe case for every helper.

## 7. Resolution claims

### PMA2-M01

Resolved by binding contracts to externally invocable or independently authority-bearing/recoverable mutation boundaries while requiring subordinate helpers to inherit and not broaden the owning contract.

### PMA2-M02

Resolved by assigning command-plan, mutation-attempt, verification and recovery failure semantics to DPA-300, and limiting DPA-500 to projection freshness and gate consequences under the existing finding authority.

### PMA2-m01

Resolved by replacing unqualified changed-path equality with a fail-closed conformance relation over authorized, required, conditional and temporary path outcomes.

## 8. Remaining limitations

- The concrete existing runtime home for command mutation contracts remains `NEEDS_MAIN_REPO_VALIDATION`.
- Concrete command modes, helpers, aliases, changed-path capture mechanics and finding mappings require local exact-ref validation.
- ADR-022 remains a deferred proposal.
- DPA-200 through DPA-500 remain unchanged.
- DPA-600 remains frozen.
- DPA-700 remains unstarted.
- No Probe has been executed or amended.
