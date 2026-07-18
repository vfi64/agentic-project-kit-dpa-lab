# DPA-600 — Concurrency and Workflow Serialization

Status: draft
Status-date: 2026-07-18
Superseded-by: n/a

## 1. Purpose

This specification defines the concurrency domains, guard ownership and workflow-serialization contract for document projections.

DPA-600 extends the existing document lifecycle, Workspace lock and workflow orchestration of `vfi64/agentic-project-kit`. It does not create a second lock service, workflow engine, state authority, writer path, renderer authority, evidence system or gate architecture.

Concrete main-repository lock APIs, workflow commands, branch-protection settings, merge-queue behavior, lease formats, persistence paths and CI placement remain `NEEDS_MAIN_REPO_VALIDATION` until verified against an exact main-repository validation ref.

## 2. Normative dependencies

DPA-600 depends on:

- DPA-000 for canonical invariants and concurrency principles;
- DPA-100 for authority, validation-ref, drift, fingerprint, mutation-plan, lock and workflow vocabulary;
- DPA-200 for target identity, ownership and document-form constraints;
- DPA-300 for lifecycle phases, immutable plans, local locking, under-lock revalidation, acceptance state and recovery;
- DPA-400 for renderer identity, immutable inputs and renderer-derived payloads;
- DPA-500 for freshness, findings, gate decisions, re-acceptance and integration consequences;
- DPA-ADR-003, DPA-ADR-006, DPA-ADR-007, DPA-ADR-016, DPA-ADR-019 and DPA-ADR-021.

Historical Discovery observations inform validation obligations but do not establish present implementation conformance.

## 3. Scope

DPA-600 owns:

1. concurrency-domain separation;
2. local Workspace-lock semantics at the architecture boundary;
3. same-process reentrancy limits;
4. cross-ref guard ownership;
5. branch and pull-request concurrency semantics;
6. integration-time stale-plan rejection;
7. regeneration after drift;
8. coordination of renderer-derived plans without transferring renderer authority;
9. concurrency interaction with acceptance state and recovery;
10. fail-loud behavior, evidence and rollback obligations for concurrency failures.

DPA-600 does not own registry serialization, renderer computation semantics, lifecycle target writes, acceptance-state schema, finding identifiers or severities, gate authority, migration-form selection or concrete Git-hosting configuration.

## 4. Concurrency domains

The DPA distinguishes four non-interchangeable concurrency domains.

### 4.1 Renderer computation domain

A renderer computes one immutable payload for one registered target from lifecycle-resolved immutable inputs.

The renderer MUST NOT acquire locks, inspect branch or pull-request state, write targets or lifecycle state, serialize workflows, decide whether a plan is current or regenerate after integration drift on its own authority.

Renderer output becomes mutation-relevant only after the lifecycle captures it in an immutable plan.

### 4.2 Lifecycle mutation domain

The existing document lifecycle owns mutation of one governed target within one local Workspace boundary.

It owns preflight validation, immutable plan capture, acquisition and release of the existing Workspace mutation lock, under-lock guard revalidation, atomic target replacement, post-Write verification, acceptance-state and recovery handling, lifecycle findings and bounded evidence.

The lifecycle lock serializes local mutation only. It MUST NOT be represented as cross-branch, cross-ref or cross-PR serialization.

### 4.3 Workflow integration domain

Workflow orchestration owns coordination across repository refs, branches and pull requests.

It owns selection of the exact integration validation ref, verification that a plan or produced tree is based on the required ref, cross-branch and cross-PR sequencing, integration-time revalidation of plan and acceptance assumptions, rejection of stale or unverifiable results and triggering regeneration through the lifecycle from current authoritative inputs.

Workflow orchestration MUST NOT render payloads directly, write projection targets, modify acceptance state or define projection semantics.

### 4.4 Repository integration domain

Repository integration is the point at which a branch or pull request may enter the protected target ref.

Integration MUST occur only when all required workflow guards are current and reproducible against the selected exact validation ref. A locally successful mutation, green historical workflow run or existing evidence record is insufficient by itself.

## 5. Local Workspace lock contract

Every projection mutation MUST use the existing Workspace mutation lock through the lifecycle.

The lock scope MUST cover every local lifecycle-owned mutation required for one exact plan, including as applicable target replacement, partition-byte replacement, acceptance-state mutation, recovery-state mutation and required crash-safe lifecycle bookkeeping.

The lock MUST be acquired only after dry-run planning and preflight checks and before under-lock revalidation.

Lock acquisition failure, scope mismatch or inability to establish exclusive local mutation MUST fail loud before Write.

A lock holder MUST release the lock deterministically on success, rejection, exception or recovery disposition. Concrete lock mechanics remain `NEEDS_MAIN_REPO_VALIDATION`.

## 6. Same-process reentrancy

Same-process reentrancy MAY exist only as a property of the existing Workspace lock when required by an already-governed outer orchestration path.

Reentrancy is valid only when one process owns both acquisitions, both govern the same Workspace mutation boundary, the inner path belongs to the same exact projection refresh instance, no second renderer invocation or target refresh occurs, release accounting is balanced and recovery remains observable.

Same-process reentrancy MUST NOT authorize nested projection refreshes, lock ordering across multiple targets, cross-workspace mutation, cross-process overlap, cross-ref serialization or hidden extension of lock lifetime across workflow boundaries.

If identity or balanced release cannot be proven, reentrant acquisition MUST fail loud.

## 7. Guard domains

Every mutation plan and integration decision MUST treat the following guard domains independently:

1. base guard;
2. ordered declared-source guards;
3. pre-mutation target and lifecycle-owned payload guards;
4. projection, partition, target-semantics and output-affecting configuration guards;
5. renderer identifier, interface-compatibility and semantic-version guards;
6. partition and boundary guards;
7. ownership guards;
8. gate-set guard where acceptance or integration depends on it;
9. target-scoped acceptance-state guard where required by the operation.

The closed DPA-100 drift classes remain authoritative. DPA-600 does not add a new drift class for branch or pull-request concurrency. Cross-ref mismatch is reported through affected guard classes and workflow context.

Multiple guard failures MAY coexist and MUST remain separately visible.

## 8. Plan lifecycle across refs

An immutable mutation plan is valid only for its captured identities and fingerprints.

A plan produced on one ref MUST NOT be applied or integrated as though it were produced on another ref merely because the textual diff appears mergeable.

Before local Write, the lifecycle MUST revalidate every mutation-relevant guard under the local lock without invoking the renderer a second time for the same plan.

Before protected integration, workflow orchestration MUST revalidate the required base, declared sources, lifecycle-owned target bytes, contracts, renderer identity, partition, ownership, required gate-set and acceptance context and reproducibility against the selected integration ref.

If any required guard differs or cannot be evaluated, the plan or integration result MUST be rejected.

## 9. Branch concurrency

Two branches MAY independently create internally valid plans from different refs. Their independent validity does not make both integrable.

When one branch changes any guarded input, every competing branch whose plan or produced target depends on the earlier value MUST be revalidated against the new integration ref.

Rebase, merge or conflict resolution MUST NOT preserve a projection plan by textual convenience alone. The workflow MUST prove every guard still matches or require regeneration.

A branch changing only declared non-lifecycle-owned bytes MAY avoid projection regeneration only when ownership, partition and target semantics prove no projection guard changed. Ambiguous ownership MUST fail closed.

## 10. Pull-request concurrency

Competing pull requests affecting the same target, declared sources, renderer contract, partition contract, ownership contract, acceptance requirements or integration base MUST be serialized at the workflow/integration boundary.

Serialization MUST ensure that at most one competing result is accepted against an obsolete assumption set, later candidates are revalidated after earlier integration, a previously green check does not authorize integration after guard context changes, integration order is explicit and regeneration uses the exact post-integration authoritative ref.

The concrete mechanism MAY be a governed refresh workflow, protected integration job, merge queue or equivalent proven mechanism. No implementation is selected here.

## 11. Stale-plan rejection

A stale or unverifiable plan MUST NOT be written, committed as current projection output, accepted, re-accepted or integrated.

The system MUST fail loud for base, source, lifecycle-owned target, contract, renderer, partition, ownership, required gate-set or acceptance-state mismatch; unknown guard versions; missing workflow context; or an ambiguous plan ref.

Elapsed wall-clock time alone does not stale a plan.

## 12. Regeneration after drift

After drift or guard uncertainty, the only valid forward path is a new lifecycle plan from current authoritative inputs at a new explicit validation ref.

Regeneration MUST resolve active contracts and sources, invoke the renderer once, create a new immutable plan, perform normal preflight, lock, revalidation, Write, Verify and gate processing and record bounded evidence linking rejected and regenerated attempts.

Regeneration MUST NOT textually merge generated payloads, auto-merge historical prose, reuse target bytes as semantic input, transplant acceptance state or modify non-lifecycle-owned bytes outside active ownership and partition contracts.

## 13. Renderer-derived plans

Renderer output MUST remain bound to the exact immutable inputs captured by the lifecycle.

A workflow MAY carry plan and renderer identities but MUST NOT reinterpret or patch renderer output.

A plan becomes invalid when renderer identifier, interface compatibility, semantic version, declared inputs, output-affecting configuration or target semantics differ.

A renderer implementation-evidence change alone does not invalidate a plan when semantic version and proven behavior remain unchanged. Evidence of unversioned semantic change returns the renderer contract and affected plans to adjudication and regeneration.

## 14. Acceptance state and re-acceptance

Acceptance state is lifecycle state scoped to an accepted target and contract context. It is not a cross-ref serialization token.

Workflow integration MUST NOT infer current acceptability solely from an acceptance record created on another ref.

Where accepted state is required, the workflow MUST verify active contract, renderer, sources, lifecycle-owned bytes, ownership, partition, gate-set and required base context.

Gate-set-only re-acceptance remains lifecycle-owned under DPA-500. Workflow orchestration MAY require or sequence it but MUST NOT update acceptance state directly.

A re-acceptance result produced before a competing ref changes any required guard MUST be revalidated and, where necessary, repeated through the lifecycle.

## 15. Recovery interaction

Local interrupted-refresh recovery remains owned by DPA-300 and DPA-500.

Workflow orchestration MUST treat unresolved recovery state, `written-unverified` bytes, abandoned attempts or incomplete acceptance-state recording as non-integrable.

A workflow MAY resume only after explicit lifecycle recovery disposition. It MUST NOT infer recovery from target bytes, clear stale locks directly, fabricate acceptance state or integrate interrupted output because its text appears correct.

Cross-ref integration still requires fresh workflow revalidation after local recovery.

## 16. Fail-loud behavior

Concurrency uncertainty MUST fail closed for mutation, acceptance, re-acceptance and protected integration.

Explicit failures are required for lock or ownership failure, invalid reentrancy, unknown guard versions, ambiguous refs, stale local plans, stale integration results, obsolete competing-PR assumptions, unavailable workflow context, unresolved recovery state, evidence or acceptance state used as serialization authority and any attempted generated- or historical-prose auto-merge.

A warning-only result MUST NOT authorize mutation or integration when a mandatory concurrency guard failed.

## 17. Evidence obligations

Concurrency evidence MUST remain bounded and non-authoritative.

It MUST record as applicable repository and exact ref, branch and PR context, target and plan identity, guard results, local lock scope, reentrancy and balanced release, preflight and under-lock revalidation, integration-time revalidation, rejection, regeneration or recovery disposition, gate and trust-state consequences, limitations and unavailable checks.

Evidence MUST NOT become a lease, lock, acceptance record, canonical source or authorization for later integration.

## 18. Rollback obligations

Concurrency failure before Write MUST leave target bytes and acceptance state unchanged. Failure after Write remains governed by DPA-300 and DPA-500 recovery and leaves the result non-accepted until recovery completes.

A rejected integration MUST leave the protected target ref unchanged.

If an incorrectly integrated projection is later detected, rollback MUST use governed repository rollback and lifecycle recovery from a known exact ref. It MUST NOT reconstruct authority by merging historical prose or accepting generated target bytes as canonical input.

DPA-700 owns complete rollback policy. DPA-600 requires enough exact-ref, plan and guard evidence to make rollback decidable.

## 19. Main-repository validation boundary

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- Workspace-lock implementation and exact reentrancy behavior;
- lock scope, timeout, stale-lock and release mechanics;
- branch, SHA and remote-head guards;
- pull-request and administrative refresh serialization;
- merge-queue, protected-branch and required-check behavior;
- integration workflow entry points;
- plan persistence across workflow boundaries;
- acceptance-state and recovery persistence ordering;
- finding identifiers, severities, tests and CI placement.

Historical observations at `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` do not establish current conformance.

## 20. Conformance tests

A conforming implementation MUST test local exclusion, bounded same-process reentrancy, rejection across targets or workspaces, balanced release, stale-lock recovery, stale plans before and under lock, independent and simultaneous guard failures, obsolete branch and PR results, changed-source and changed-contract concurrency, invalid historical green evidence, exact-ref regeneration, no generated or historical textual merge, workflow and renderer authority boundaries, acceptance state not acting as serialization, re-acceptance after ref change, unresolved recovery blocking integration, rejection leaving protected refs unchanged and exact-ref rollback inputs.

## 21. Invalid states

Invalid states include local lock represented as cross-ref serialization, workflow target writes, renderer lock or PR access, nested projection refresh, ambiguous multi-target lock scope, stale-plan application based on textual mergeability, historical green results treated as current authority, integration without exact-ref revalidation, generated or historical auto-merge, acceptance state used as a lock, evidence used as authorization, workflow clearing lifecycle recovery state, unknown guards treated as matches, missing context treated as current, time-only invalidation, unevidenced implementation claims and any parallel concurrency, lock, workflow, state or gate subsystem.

## 22. Draft exit criteria

DPA-600 may proceed to formal review preparation when concurrency domains, local locking, reentrancy limits, guard domains, branch and PR serialization, stale-plan rejection, regeneration, acceptance and recovery interactions, evidence and rollback traceability and exact-ref validation boundaries are complete; diagrams and traceability are synchronized; and an internal DPA-000 through DPA-500 audit finds no contradiction or parallel subsystem.

`draft` does not establish implementation, Probe success, main-repository conformance or readiness for promotion.
