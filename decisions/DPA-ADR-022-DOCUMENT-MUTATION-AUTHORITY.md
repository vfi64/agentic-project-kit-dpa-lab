# DPA-ADR-022 — Govern document-producing commands by mutation authority

Status: DEFERRED PROPOSAL

Status-date: 2026-07-20

Maintainer-adjudication: `ACCEPT_FOR_BOUNDED_NORMATIVE_DRAFTING`

Adjudication-record: `reviews/adjudication/PACKAGE_M_MAINTAINER_ADJUDICATION_20260720.md`

Normative-effect: none until the synchronized bounded amendment package is independently verified and accepted

## Context

The DPA already defines registry, renderer, lifecycle, workflow, evidence, freshness, gate and acceptance boundaries. Exact-ref inspection also shows that Agentic Kit contains multiple commands and internal paths that create, refresh, reconcile, finalize, move or otherwise update document-like artifacts.

The motivating handoff and status drift failure class cannot be excluded unless those commands are governed as mutation authorities rather than treated as unrelated CLI utilities.

A pure renderer contract alone is insufficient when a command may:

- write the same semantic fact independently to several files;
- combine source mutation and projection generation;
- update a generated target without proving its canonical inputs;
- write outside its declared output scope;
- bypass Workspace resolution;
- overwrite another command's newer projection;
- treat report or evidence output as state authority;
- return success without post-write verification.

## Adjudicated deferred decision

Every independently invocable, independently schedulable or independently recoverable Agentic Kit command mode that creates, rewrites, appends, replaces, moves, archives or deletes document-like artifacts SHALL be governed by one document mutation contract.

A subordinate internal helper inherits the contract of its owning command or composed step and SHALL NOT broaden that contract's target set, canonical-source authority, changed-path boundary, secondary effects, lock scope, verification obligations or recovery authority.

The architecture SHALL require:

1. one declared primary mutation class per independently governed command mode;
2. explicit canonical input authorities;
3. explicit target and output scope;
4. Workspace-resolved paths;
5. lifecycle ownership for governed projection bytes;
6. pure renderer boundaries where rendering is used;
7. appropriate lock and workflow serialization;
8. plan-bound changed-path conformance over authorized, required, conditional and temporary paths;
9. post-write verification distinct from path-scope verification;
10. explicit target-scoped trust-state and acceptance effects;
11. bounded findings and evidence through existing authorities;
12. compatibility, migration and deprecation disposition for existing direct writers.

The same semantic fact SHALL NOT be authored independently by multiple commands or files. Multiple projections MAY expose that fact only when they derive it from one declared canonical authority.

Generated artifacts SHALL NOT be normal primary edit surfaces. A durable correction SHALL modify the canonical source, generator contract or governed mutation path and then regenerate or refresh the target.

A command mutation contract SHALL extend exactly one existing main-repository runtime authority selected after exact-ref validation. Independently editable duplicate command-contract declarations are prohibited. Derived references MAY expose the contract but SHALL identify their authority source and SHALL NOT become runtime authority.

A synchronized projection set preserves one registered target identity, one renderer invocation and one lifecycle-owned target result per member. Any aggregate attempt result is derived workflow output only and SHALL NOT become a consumer trust state, acceptance-state record, canonical authority, target writer, recovery owner or independent persistent state.

Aggregate recovery SHALL use existing workflow or lifecycle recovery structures and evidence only. It SHALL NOT create a new state store, acceptance store, trust state, canonical history store or target state. Concrete repository representation remains `NEEDS_MAIN_REPO_VALIDATION`.

DPA-300 owns command-plan, mutation-attempt, changed-path, secondary-effect, alias, composed-step and recovery failure semantics. DPA-500 owns only the resulting projection-freshness, trust-evaluation and gate consequences.

No second command registry, lifecycle, writer authority, acceptance authority, state store, recovery store, evidence service, finding system or gate system may be introduced.

## Mutation classes

The proposed closed primary planning classes are:

- `CMA-1 canonical-source-mutator`;
- `CMA-2 lifecycle-projection-mutator`;
- `CMA-3 state-transition-mutator`;
- `CMA-4 evidence-report-writer`;
- `CMA-5 derived-reference-generator`;
- `CMA-6 migration-archival-mutator`;
- `CMA-7 cleanup-gc-mutator`;
- `CMA-8 read-only-inspector`.

A command with materially different modes must classify each independently governed mode separately.

These CMA labels are proposal-local planning vocabulary. They do not create a new runtime registry or serialization authority.

## Alternatives considered

### Continue relying only on renderer and lifecycle boundaries

Rejected as incomplete because existing command orchestration and generated-reference paths can still create duplicate semantic writers or unverified outputs.

### Create a new DPA command registry

Rejected because it would duplicate the existing command manifest, CLI structure and runtime authority.

### Permit each command to document its own ad hoc write behavior

Rejected because local documentation does not provide a closed authority model or detect overlapping semantic ownership.

### Treat generated files as manually maintainable after generation

Rejected because it reintroduces dual authority and makes freshness non-derivational.

## Consequences

Following Maintainer adjudication:

- one synchronized bounded amendment package may be drafted for DPA-200, DPA-300, DPA-400 and DPA-500;
- the package remains non-normative until independently verified and accepted through the normal normative-change process;
- DPA-600 and DPA-700 require only later additions after their current sequencing restrictions permit work;
- PROBE-001, PROBE-002 and renderer Probe planning may require an explicit separately reviewed command-integration amendment;
- DP1 must inventory command modes, internal mutators, canonical inputs, actual write sets and semantic-fact overlaps;
- DP2 must adapt or deprecate non-conforming direct writers rather than layering a parallel system over them;
- handoff, status and other generated-document bugs must be corrected at the responsible authority or generation path, not only patched in output files.

## Evidence and review state

Completed for architecture-direction adjudication:

- bounded remote command-to-document inventory at the recorded exact ref;
- known duplicate or ambiguous semantic-writer analysis;
- provisional class mapping to observed command modes;
- internal consistency audit;
- adversarial pre-review;
- independent architecture review;
- bounded disposition of all review findings;
- Maintainer adjudication.

Still required before repository-specific normative application or implementation:

- complete local exact-ref command and internal-writer inventory;
- installed-CLI comparison;
- identification of the single existing command-contract runtime home;
- disposable-repository changed-path observations;
- Workspace, lifecycle, lock, renderer, verification, finding, gate, recovery and evidence validation;
- explicit Probe-contract adjudication where coverage changes;
- independent verification of the drafted synchronized normative amendments.

Repository-specific command mappings remain `NEEDS_MAIN_REPO_VALIDATION` until locally confirmed against an exact ref.

## Current effect

This remains a non-normative deferred proposal with a positive Maintainer adjudication for bounded normative drafting.

It authorizes preparation of one synchronized DPA-200/300/400/500 amendment package, but it does not yet amend normative DPA contracts, authorize main-repository mutation, establish implementation support, prove adoption or permit Probe execution.

DPA-600 remains frozen. DPA-700 remains unstarted. Current writer and lifecycle quick fixes remain prohibited before applicable Probe execution, adjudication and architecture revalidation.
