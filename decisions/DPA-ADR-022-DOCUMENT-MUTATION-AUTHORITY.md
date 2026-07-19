# DPA-ADR-022 — Govern document-producing commands by mutation authority

Status: DEFERRED PROPOSAL

Status-date: 2026-07-19

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

## Proposed decision

Every Agentic Kit command mode and internal entry point that creates, rewrites, appends, replaces, moves, archives or deletes document-like artifacts SHALL be classified under a governed document mutation authority.

The architecture SHALL require:

1. one declared primary mutation class per command mode;
2. explicit canonical input authorities;
3. explicit target and output scope;
4. Workspace-resolved paths;
5. lifecycle ownership for governed projection bytes;
6. pure renderer boundaries where rendering is used;
7. appropriate lock and workflow serialization;
8. equality between authorized and actual changed-path scope;
9. post-write verification;
10. explicit trust-state and acceptance effects;
11. bounded findings and evidence;
12. compatibility, migration and deprecation disposition for existing direct writers.

The same semantic fact SHALL NOT be authored independently by multiple commands or files. Multiple projections MAY expose that fact only when they derive it from one declared canonical authority.

Generated artifacts SHALL NOT be normal primary edit surfaces. A durable correction SHALL modify the canonical source, generator contract or governed mutation path and then regenerate or refresh the target.

No second command registry, lifecycle, writer authority, state store, evidence service or gate system may be introduced.

## Mutation classes

The proposed closed primary classes are:

- `CMA-1 canonical-source-mutator`;
- `CMA-2 lifecycle-projection-mutator`;
- `CMA-3 state-transition-mutator`;
- `CMA-4 evidence-report-writer`;
- `CMA-5 derived-reference-generator`;
- `CMA-6 migration-archival-mutator`;
- `CMA-7 cleanup-gc-mutator`;
- `CMA-8 read-only-inspector`.

A command with materially different modes must classify each mode separately.

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

If accepted after review and evidence:

- DPA-200, DPA-300, DPA-400 and DPA-500 require bounded synchronized amendments;
- DPA-600 and DPA-700 require later additions after their current sequencing restrictions permit work;
- PROBE-001, PROBE-002 and renderer Probe planning may require explicit command-integration coverage;
- DP1 must inventory command modes, internal mutators, canonical inputs, actual write sets and semantic-fact overlaps;
- DP2 must adapt or deprecate non-conforming direct writers rather than layering a parallel system over them;
- handoff, status and other generated-document bugs must be corrected at the responsible authority or generation path, not only patched in output files.

## Evidence and review requirements

Before acceptance:

- complete the remote command-to-document inventory for the current exact main-repository ref;
- identify known duplicate or ambiguous semantic writers;
- map proposed classes to real command modes;
- prove that the decision extends existing authorities rather than creating a parallel system;
- obtain bounded independent architecture review;
- record Maintainer adjudication.

Repository-specific command mappings remain `NEEDS_MAIN_REPO_VALIDATION` until locally confirmed against an exact ref.

## Current effect

This is a non-normative deferred proposal. It creates a binding planning obligation through `integration/DOCUMENT_MUTATION_AUTHORITY_AND_COMMAND_INTEGRATION_PLAN.md`, but it does not yet amend normative DPA contracts or authorize main-repository mutation.

DPA-600 remains frozen. DPA-700 remains unstarted. Current writer and lifecycle quick fixes remain prohibited before PROBE-002 execution, adjudication and architecture revalidation.