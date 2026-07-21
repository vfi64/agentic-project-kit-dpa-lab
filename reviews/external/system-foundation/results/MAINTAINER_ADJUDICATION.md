# Maintainer Adjudication — Federated System Foundation Review

Status: maintainer-directed adjudication
Status-date: 2026-07-21
Reviewed external review: `CLAUDE_FALSIFYING_ARCHITECTURE_REVIEW.md`
Reviewed review commit: `2468995e288db4ccee5091ec06e9c2f8718f0987`
Reviewed package commit: `ea84c80e4531d3a3e5ba3f3e2ed51ab2969ebc97`

## Authority and scope

This document adjudicates the non-authoritative external review for the purpose of preparing bounded follow-up changes. It does not itself amend AGF, DPA, Kit or ROS authority. Each repository must apply the accepted decisions through its own governed workflow.

The adjudication vocabulary is:

- `ACCEPT`
- `ACCEPT_WITH_ADAPTATION`
- `DEFER_TO_PILOT`
- `REJECT`

## Overall adjudication

The external verdict `MAJOR_REVISION` is accepted as a verdict on the current system-foundation drafts. The underlying layered and federated direction is retained, but the present documents must not be treated as an implementation-ready baseline.

The target architecture after adjudication is:

1. AGF owns governance and reasoning method plus only the minimal cross-repository meta-vocabulary required for interchange.
2. DPA owns representation, document lifecycle and context-projection architecture.
3. The Agentic Project Kit is the sole executable repository runtime, validation, evidence and gate implementation authority.
4. ROS remains a separate operating-model research/specification concern for now, but it may define only declarative operating profiles and requirements. It must not implement a second runtime. Whether ROS remains a separate repository or becomes a Kit profile is decided by pilot evidence.
5. Each repository owns its local canonical graph or structured state. Cross-repository relations are exchanged as validated, versioned records. Any system-wide graph is a derived materialized view, never a shared live authority.
6. Cross-repository coordination is explicitly non-authoritative and cannot replace repository-local plans.

## Finding adjudications

### P1 — Manifest copy-rule contradiction

Decision: `ACCEPT`

Rationale:

The package is internally valid, but `byte-identical copies` conflicts with the declared removal of a trailing newline. Future review-package contracts must distinguish raw-source identity from normalized-content identity.

Required action:

- Do not rewrite the frozen package commit.
- Future package manifests must say `content-identical after the declared normalization`.
- A later package-version note may record the defect without changing the reviewed snapshot.

### F1 — Incomplete Kit non-change evidence

Decision: `ACCEPT_WITH_ADAPTATION`

Rationale:

The evidence failed to disclose relevant pre-existing Kit work, especially PR #1867. A retroactive breach of the later hold is not established. PR #1865 is related research input, not equivalent to runtime adoption.

Required disposition:

- Classify Kit PR #1867 as `PRE_EXISTING_UNADJUDICATED_KIT_WORK`.
- Disclose Kit PR #1865 as related pre-existing non-normative research work.
- Keep both unmerged pending the repository-authoritative local Mac workflow.
- Do not continue PR #1867 or count it as adoption before that adjudication.
- Correct the Kit non-change narrative only through the Kit's native governed workflow when Mac access is available.

### F2 — AGF overscope

Decision: `ACCEPT_WITH_ADAPTATION`

Rationale:

AGF is overscoped where it claims domain vocabularies belonging to DPA, Kit and ROS and where its masterplan can be read as downstream planning authority. However, AGF may legitimately define a minimal meta-vocabulary and host a clearly non-authoritative coordination view.

Binding boundary:

AGF may own:

- governance and reasoning method;
- evidence, review, adjudication, adoption, falsification, simplification and retirement concepts;
- minimal interchange metadata such as source, authority scope, version, adoption state and evidence reference.

AGF must not own:

- DPA representation or projection schemas;
- Kit runtime or execution schemas;
- ROS operating-state schemas;
- downstream repository priorities, task states or release plans.

The current `SYSTEM_FOUNDATION_MASTERPLAN.md` must be reframed or relocated as a `NON_AUTHORITATIVE_COORDINATION_PLAN` with a named coordinator and explicit repository-local adoption gates.

### F3 — Competing graph models

Decision: `ACCEPT`

Rationale:

The current drafts leave an unacceptable ambiguity between a shared cross-repository graph and loose record-based federation.

Binding architecture decision:

- Canonical graphs/state are repository-local.
- Repositories exchange validated, versioned interchange records.
- Cross-repository edges are references with exact source refs and adoption state, not jointly mutable authoritative edges.
- A system-wide graph may be materialized for search or analysis, but it is a derived projection with no independent authority.
- No shared live transactional graph is part of the foundation baseline.

### F4 — ROS risks becoming a second Kit

Decision: `ACCEPT_WITH_ADAPTATION`

Rationale:

The overlap risk is real, but it does not yet prove that ROS must be dissolved into the Kit. The distinction must be structural and testable.

Binding ROS boundary:

ROS may specify:

- roles and authority contexts;
- declarative operating profiles;
- work-package semantic requirements;
- session-entry, escalation and closeout requirements;
- multi-repository coordination rules.

ROS may not implement or independently persist:

- workspaces or registries;
- lifecycle state stores;
- validators, gates or evidence collectors;
- handoff engines;
- GitHub mutation tooling;
- a second `.agentic/` runtime namespace.

Every ROS concept that requires execution must map to an existing or proposed Kit capability. An unmapped executable ROS feature is a blocker. The pilot will decide whether ROS remains a separate specification repository or is reduced to a Kit operating profile.

### F5 — Alleged bootstrap circular dependency

Decision: `ACCEPT_WITH_ADAPTATION`

Rationale:

The review correctly identifies a bootstrap risk, but the dependency is not inherently circular. AGF does not need prior Kit adoption to be tested. A non-adopted experimental pilot can exercise candidate contracts before any repository accepts them normatively.

Binding bootstrap rule:

- `proposal` and `experimental pilot` are distinct from `adoption`.
- A pilot may use temporary adapters or fixtures without establishing Kit adoption.
- The Kit may adopt only after pilot evidence and repository-local adjudication.
- Pilot artifacts must be explicitly non-authoritative, isolated and reversible.
- No pilot may mutate governed Kit planning or runtime state before the Mac/native-command gate.

Thus the claimed unavoidable cycle is rejected, while the need for an explicit bootstrap protocol is accepted.

### F6 — AGF/DPA governance overlap

Decision: `ACCEPT`

Rationale:

The boundary must be explicit.

Binding split:

- AGF defines generic governance method and evidence/adjudication semantics.
- DPA defines how those semantics apply to documents, projections, freshness, provenance, acceptance and lifecycle within DPA scope.
- DPA-local status vocabularies and gates remain under DPA authority unless explicitly mapped and adopted.
- AGF cannot directly change a DPA artifact's state.

### F7 — Missing interchange and conflict owner

Decision: `ACCEPT_WITH_ADAPTATION`

Rationale:

There must not be a central owner with downstream authority. Ownership is divided:

- AGF owns only the minimal interchange envelope semantics.
- Each producing repository owns its payload schema and version.
- Each consuming repository owns adoption, compatibility and migration decisions.
- Cross-repository incompatibilities are coordinated by a named, non-authoritative system coordinator and resolved by the affected repository maintainers.

No global decider may override repository-local authority.

### F8 — Projection-type proliferation

Decision: `ACCEPT_WITH_ADAPTATION`

Rationale:

The warning is valid, but DPA must decide the representation model. The baseline should begin with one parameterized context-projection contract rather than separate independent projection architectures.

Initial parameters should include:

- purpose or role;
- target repository and exact ref;
- authority scope;
- included object classes;
- freshness policy;
- unresolved-conflict policy;
- token or size budget;
- prioritization and eviction policy.

Specialized named projections may be introduced only when the pilot demonstrates materially different invariants.

### F9 — Pre-existing capture work outside the governed sequence

Decision: `ACCEPT_WITH_ADAPTATION`

Rationale:

No temporal violation is established. The work nevertheless cannot become de facto adoption.

Required action:

- Freeze PR #1867 as pre-existing unadjudicated work.
- At Mac access, inspect it through the Kit's native planning, documentation, registry, gate and handoff workflow.
- Then explicitly adopt, rewrite, split or close it.
- Do not import its state into AGF, DPA or ROS as accepted evidence before that decision.

## Adjudication of simplification proposals

- S1 loose federation: `ACCEPT`.
- S2 trim AGF: `ACCEPT_WITH_ADAPTATION`; retain minimal interchange meta-vocabulary and non-authoritative coordination capability.
- S3 ROS as thin profile: `DEFER_TO_PILOT`; immediately impose the no-runtime boundary.
- S4 separate non-authoritative coordination plan: `ACCEPT`.
- S5 parameterized projection contract: `ACCEPT_WITH_ADAPTATION` under DPA authority.
- S6 manifest wording: `ACCEPT` for future packages; frozen package remains immutable.

## Repository-specific follow-up package

### AGF

Required before AGF PR #2 can be accepted:

1. Narrow AGF scope to governance/reasoning method and minimal interchange metadata.
2. Replace the ambiguous federated-graph language with repository-local canonical graphs plus validated interchange records and a derived materialized view.
3. Reclassify the system masterplan as non-authoritative coordination or move it into a dedicated coordination area.
4. Remove any implication that AGF owns downstream domain schemas, priorities or adoption state.
5. Define measurable pilot success and failure criteria.

### DPA Lab

Required before DPA PR #7 can be accepted:

1. Update the adoption analysis to reflect loose federation rather than a shared live graph.
2. Define the AGF/DPA governance-method versus projection-governance boundary.
3. Start from one parameterized context-projection contract.
4. Preserve all existing exact-ref, Probe, review and adjudication gates.
5. Do not amend stable or review-ready DPA specifications until the governed DPA plan authorizes it.

### ROS

Required before ROS PR #2 can be accepted:

1. Recast ROS as declarative operating-model requirements and profiles.
2. Add explicit prohibited-runtime criteria and a mandatory Kit capability map.
3. Remove or qualify any lifecycle or gate language that implies an independently persisted ROS runtime.
4. State that repository independence versus Kit-profile status is pilot-decidable.
5. Keep application profiles deferred until after pilot adjudication.

### Agentic Project Kit

No remote implementation action is authorized now.

At Mac access:

1. Re-bootstrap from current remote main and validated handoff evidence.
2. Inspect PR #1867 and PR #1865 through native Kit commands.
3. Correct the non-change/hold disclosure through the Kit's governed documentation and planning workflow.
4. Decide whether PR #1867 is closed, rewritten, split or adopted into a new bounded plan item.
5. Do not disturb the current authoritative Kit masterplan without the correct native planning operation.

## Pilot requirements

The first pilot must compare the adjudicated architecture against a simpler baseline. At minimum it must measure:

- successor-task completion without chat memory;
- provenance survival and exact-source recovery;
- authority-conflict rate;
- projection size and relevance versus direct repository retrieval;
- maintenance operations per source change;
- stale or broken cross-repository references;
- duplicate-state incidence;
- time and intervention required for handoff and continuation.

The pilot must use repository-local canonical state, validated interchange records and a derived view. A shared live graph is outside scope.

## Final disposition

The external review is substantially accepted, but not verbatim.

- Accepted core corrections: AGF scope reduction, loose federation, structural ROS/Kit boundary, explicit AGF/DPA split, named distributed schema ownership and measurable pilot criteria.
- Adapted correction: the bootstrap issue is a risk requiring an experimental protocol, not an unavoidable circular dependency.
- Deferred decision: whether ROS remains a separate specification repository or becomes a Kit profile.
- Kit remains blocked from further adoption work until Mac access and native Agentic-Kit commands are available.

No reviewed PR is approved or merged by this adjudication document. Each must be revised and re-reviewed at an exact new ref.