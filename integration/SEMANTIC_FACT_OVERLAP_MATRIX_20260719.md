# Semantic Fact Overlap Matrix — Remote Partial

Status: remote-partial

Status-date: 2026-07-19

Main-repository exact ref: `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Lab branch: `spec/dpa-600-concurrency`

## Purpose

This document records confirmed and suspected semantic-fact overlap among document-like artifacts and command surfaces inspected remotely for Package M.

It is an evidence-bound planning artifact. It is not a complete writer inventory, does not amend DPA specifications, does not authorize main-repository changes and does not establish actual runtime behavior beyond the inspected source.

## Classification

- `CONFIRMED_OVERLAP`: the same semantic fact is read from or projected into more than one identified artifact or command path.
- `CONFIRMED_PROJECTION_SET`: one identified generator owns a declared multi-artifact projection set.
- `SUSPECTED_DUPLICATE_WRITER`: more than one possible writer surface exists, but complete call-path and changed-path proof is absent.
- `REMOTE_PARTIAL`: evidence is concrete but global completeness is not established.
- `LOCAL_VERIFICATION_REQUIRED`: installed CLI, indirect calls, dynamic paths or actual changed paths must be checked locally.

## Matrix

| Fact family | Candidate canonical input or authority | Confirmed projections / consumers | Confirmed or suspected writer surfaces | Classification | Required follow-up |
|---|---|---|---|---|---|
| repository identity and local path | Git remote plus repository-identity resolution | successor context; successor prompt; bootstrap prompts | successor handoff package generator | `CONFIRMED_PROJECTION_SET` | verify local remote resolution and all generated changed paths |
| current HEAD, origin/main equality, branch and cleanliness | Git repository state at generation time | successor context; validation report; successor prompt; bootstrap prompts | successor handoff package generator; post-merge refresh flow | `CONFIRMED_OVERLAP` | prove one accepted snapshot per generation transaction and detect mixed-generation output |
| current safe handoff state | `.agentic/handoff_state.yaml` | handoff summaries; successor handoff package; prompt projections | `handoff refresh --write`; administrative refresh flows | `CONFIRMED_OVERLAP` and `SUSPECTED_DUPLICATE_WRITER` | enumerate every direct and indirect handoff-state writer and compare declared versus actual scope |
| operational handoff state | `.agentic/operational_handoff_state.yaml` | successor package long-term sources; administrative refresh set | transfer/post-merge administrative flows suspected | `REMOTE_PARTIAL` | identify exact writer functions and lock/verify behavior |
| current project direction and open tasks | project-direction document resolved through Workspace | successor context open-task projection; successor prompt | project-direction writer commands; successor package generator as consumer/projector | `CONFIRMED_OVERLAP` | prove prompts never become an independent planning authority |
| current project status | Workspace status path, presently `STATUS.md` | successor package long-term sources; administrative refresh target set | status maintenance commands and administrative refresh flows suspected | `SUSPECTED_DUPLICATE_WRITER` | complete status-writer inventory and semantic field map |
| documentation registry membership and class | documentation registry | handoff registry summary; successor package; lifecycle and registry commands | `doc-registry register`; lifecycle sweep actions that may alter registry metadata | `CONFIRMED_OVERLAP` | distinguish registry membership authority from lifecycle metadata authority |
| documentation lifecycle metadata | document headers plus registry lifecycle fields | lifecycle plan, sweep, apply and evidence report | lifecycle bootstrap/sweep/apply; registry registration for new entries | `CONFIRMED_OVERLAP` | map field-level ownership and prohibit two commands from independently owning one field |
| command reference and startup commands | machine-readable command reference plus chat-entrypoint contract | successor prompt; bootstrap prompts; execution contract | command-reference generator; successor handoff generator | `CONFIRMED_OVERLAP` | verify reference regeneration order before prompt generation |
| generated handoff policy rules | general source authorities and execution-contract rule construction | execution contract; successor prompt; bootstrap prompts | successor handoff package generator | `CONFIRMED_PROJECTION_SET` | verify all projections share one source snapshot and validation result |
| successor package freshness | generated HEAD, source manifest and validation rules | validation report; handoff freshness checks; post-merge status | successor package generator; post-merge checker | `CONFIRMED_OVERLAP` | define accepted-base semantics and refresh-only descendant policy in the governed plan |
| transfer session state | Git state, rule acknowledgement, transfer inbox and typed-work-order queue | normalize-session result; optional transfer outbox | `transfer normalize-session --write-outbox`; transfer uplink/report writers | `CONFIRMED_OVERLAP` | classify outbox/report ownership and retention separately from authoritative repository facts |
| transfer result evidence | command result and transfer runner state | canonical outbox; remote reports; logs | multiple transfer helper paths | `SUSPECTED_DUPLICATE_WRITER` | inventory report writers, naming policy, latest-pointer behavior and cleanup authority |
| local garbage-collection result | local runtime scan | garbage-collector report; transfer command preflight side effect | shared transfer preflight | `CONFIRMED_OVERLAP` | make secondary writer effects explicit in command mutation declarations |
| documentation lifecycle evidence | lifecycle scan and plan result | default evidence JSON under docs architecture evidence | `docs lifecycle report --execute` | `CONFIRMED_PROJECTION_SET` | verify collision policy, lock coverage and direct-edit prohibition |
| generated handoff prompts | handoff state, project direction, registry, command reference and repository state | `NEXT_CHAT_BOOTSTRAP.md`; `START_NEW_CHAT_PROMPT.md`; `CLOSEOUT_BEFORE_CHAT_SWITCH_PROMPT.md`; `successor_prompt.md` | `transfer chat-switch-complete`; deprecated `prepare-successor-handoff` alias | `CONFIRMED_OVERLAP` | treat alias as the same authority class and prohibit divergent generation semantics |

## Confirmed cross-family risk patterns

### Mixed snapshot risk

The successor package combines repository state, handoff state, operational state, project direction, registry information and command-reference material. Remote source inspection confirms a broad source set and a multi-artifact output set, but does not prove that every source is reread under one immutable accepted snapshot or that partial writes are recovered atomically.

### Projection becoming authority

Generated prompts repeat current state, next work and command guidance. They must remain deterministic projections. Direct maintenance of a generated prompt would create an unauthorized semantic writer unless an explicit exception contract exists.

### Alias divergence risk

`transfer prepare-successor-handoff` is a compatibility alias for `transfer chat-switch-complete`. Both must be represented as command modes under one mutation authority. A deprecated alias is not semantically harmless while it remains executable and mutating.

### Hidden secondary-writer risk

The common transfer preflight invokes local garbage collection with report writing enabled. Therefore a command whose primary result is diagnostic may still mutate document-like evidence. Primary command classification alone is insufficient.

### Registry/lifecycle field collision risk

The registry registration command owns insertion of reviewed document entries. Lifecycle commands can stamp headers and update lifecycle-related metadata. Field-level authority must be established so registry membership, classification, review dates, deferrals and document headers cannot drift through independent writers.

## Provisional architecture consequences

The bounded ADR-022 proposal should require each command mode to declare:

1. canonical semantic inputs;
2. primary and secondary semantic facts consumed;
3. authoritative targets and generated projections;
4. primary and secondary changed-path scopes;
5. composed-command ordering;
6. lock and lifecycle owner;
7. verification and evidence outputs;
8. alias or compatibility relationship;
9. direct-edit policy for generated outputs;
10. recovery behavior for partial multi-target writes.

These are proposed requirements only. They are not yet normative DPA clauses.

## Completeness boundary

Not yet proven:

- all CLI command modes;
- internal non-CLI mutators;
- dynamically constructed output paths;
- actual changed-path equality;
- status-writer completeness;
- operational-handoff writer completeness;
- transfer report and latest-pointer ownership;
- field-level registry/lifecycle ownership;
- lock, atomicity and post-write verification coverage.

Global completeness remains blocked until local exact-ref discovery and disposable-repository observation are complete.
