# Generated Artifact Ownership Matrix — Remote Partial

Status: remote-partial

Status-date: 2026-07-19

Main-repository exact ref: `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Lab branch: `spec/dpa-600-concurrency`

## Purpose

This matrix records remotely confirmed generated-artifact ownership relationships needed by Package M. It distinguishes source authority, generator authority, direct-edit policy, regeneration trigger and verification needs.

It is non-normative and incomplete. It does not authorize direct edits, implementation changes or Probe execution.

## Ownership terms

- `source authority`: artifact or runtime state from which semantic content must be derived.
- `generator authority`: command or internal writer permitted to materialize the generated target.
- `direct-edit policy`: whether durable manual editing is allowed.
- `regeneration trigger`: event that requires the target to be rebuilt.
- `verification owner`: component or command that must prove the written target is valid and synchronized.

## Matrix

| Generated artifact or family | Source authority | Generator authority | Direct-edit policy | Regeneration trigger | Verification requirement | Remote status |
|---|---|---|---|---|---|---|
| `docs/handoff/NEXT_CHAT_BOOTSTRAP.md` | handoff state, operational state, repository state, project direction, registry and command-reference sources | successor handoff package generator reached through `transfer chat-switch-complete`; compatibility alias reaches same path | durable direct edits prohibited unless explicitly declared as source-owned content | governed chat switch; accepted administrative refresh | deterministic regeneration, source-manifest coverage, freshness validation and changed-path verification | confirmed generator and target; full transaction semantics unverified |
| `docs/handoff/START_NEW_CHAT_PROMPT.md` | same successor-package source set | same successor package generator | generated projection; durable direct edit prohibited | governed chat switch or accepted refresh | content validation, command-reference contract and stale-marker checks | confirmed |
| `docs/handoff/CLOSEOUT_BEFORE_CHAT_SWITCH_PROMPT.md` | same successor-package source set | same successor package generator | generated projection; durable direct edit prohibited | governed chat switch | deterministic projection and source-manifest inclusion | confirmed |
| `docs/reports/handoff-packages/latest/successor_context.yaml` | repository, handoff, operational, direction, registry and command-reference state | successor handoff package generator | no direct durable edits | every package generation | schema validation and consistency with generated HEAD | confirmed |
| `docs/reports/handoff-packages/latest/source_manifest.json` | enumerated long-term source set plus generated context inputs | successor handoff package generator | no direct durable edits | every package generation | every consumed authoritative input represented or explicitly excluded | confirmed target; completeness locally unverified |
| `docs/reports/handoff-packages/latest/validation_report.json` | generated package plus validation rules | successor handoff package generator/validator | no direct durable edits | every package generation | status must be PASS and generated-head/freshness policy must hold | confirmed |
| `docs/reports/handoff-packages/latest/execution_contract.json` | general source authorities and contract rule construction | successor handoff package generator | no direct durable edits | every package generation or source-contract change | required rule IDs and semantic consistency checks | confirmed |
| `docs/reports/handoff-packages/latest/successor_prompt.md` | successor context plus execution contract and chat-entrypoint contract | successor handoff package generator | no direct durable edits | every package generation | deterministic output, required bootstrap markers, no stale markers or literal newline artifacts | confirmed |
| latest transfer handoff report JSON/log | transfer result and handoff flow | transfer handoff/report writer paths | direct edit prohibited; reports are evidence projections | transfer/handoff completion | report pair consistency, retention and latest-pointer policy | target set confirmed; exact writers and collision behavior incomplete |
| canonical transfer outbox result | normalize-session or transfer result payload | `transfer normalize-session --write-outbox` and possibly other transfer writer paths | direct edit should be prohibited except controlled recovery | explicit outbox-writing mode or transfer operation | payload schema, command identity and overwrite/latest policy | primary writer confirmed; complete writer set unverified |
| local garbage-collector report | local runtime garbage-collection scan | shared transfer preflight through `run_local_garbage_collector(..., write_report=True)` | evidence artifact; no durable manual correction | commands using shared transfer preflight | secondary-write declaration, cleanup/retention validation and scope check | confirmed secondary writer |
| documentation lifecycle evidence report, default `docs/architecture/evidence/doc-lifecycle-report.json` | lifecycle scan and plan payload | `docs lifecycle report --execute` | no manual durable edit; regenerate from lifecycle state | explicit execute mode or required lifecycle evidence refresh | output containment, JSON validity, post-write reread/hash and collision policy | generator and default target confirmed; post-write mechanics incomplete |
| documentation lifecycle headers | document content plus lifecycle classification policy | `docs lifecycle bootstrap --execute`, selected `docs lifecycle sweep --execute`, and bounded lifecycle apply modes | direct edit policy must be field-specific; manual edits cannot impersonate generated lifecycle state | approved lifecycle action | preserve semantic content, verify exact selected scope and field ownership | writer modes confirmed; field-level ownership incomplete |
| documentation registry entry | reviewed document classification decision | `doc-registry register` | registry is authoritative source, not generated projection; direct edits outside governed writer should be prohibited | explicit reviewed registration | schema validation, duplicate prevention, lock and post-write verification | writer confirmed; implementation mechanics incomplete |
| refreshed `.agentic/handoff_state.yaml` | existing handoff state plus current Git safe state | `handoff refresh --write` and administrative refresh path(s) | authoritative state; direct edits require governed authority, not projection repair | accepted safe-state refresh | validation before write and required post-write reread/hash/transaction proof | direct writer confirmed; complete authority set and atomicity unverified |

## Confirmed generator grouping

The successor handoff generator declares a ten-path generated projection family:

1. three canonical handoff prompts;
2. four package data/contract artifacts;
3. the successor prompt;
4. two latest transfer handoff report artifacts.

This grouping is architecture-significant. It implies that the durable unit is not one prompt file but a synchronized projection set. A repair to one member alone is not a sufficient durable correction unless the ownership contract explicitly permits independent regeneration.

## Direct-edit policy proposal

For each registered generated artifact, later normative clauses should select exactly one policy:

- `PROHIBITED`: only the registered generator may create or replace the target;
- `SOURCE_SECTION_ONLY`: bounded human-owned regions may be edited and must be preserved by regeneration;
- `RECOVERY_ONLY`: direct repair is permitted only under an explicit recovery procedure followed by complete regeneration;
- `AUTHORITATIVE_NOT_GENERATED`: target is a source authority and is updated by a governed state writer rather than a renderer.

The current remote evidence supports `PROHIBITED` for successor-package projections and evidence reports, while `.agentic/handoff_state.yaml` and the documentation registry are authoritative state rather than generated projections.

## Required ownership invariants proposed for review

1. Every generated target has one registered generator authority.
2. Aliases map to the same generator identity and cannot define divergent output semantics.
3. A command declares secondary generated artifacts produced by helpers or preflights.
4. Multi-target generation uses one accepted source snapshot.
5. The declared target set equals the actual changed-path set, except separately declared volatile evidence.
6. Partial failure cannot leave a subset represented as current.
7. Verification occurs after write and before success is returned.
8. Generated artifacts cannot become independent semantic authorities.
9. Direct edits are either prohibited or governed by an explicit bounded-region/recovery contract.
10. Retention and garbage collection do not silently redefine generation authority.

These are proposed architecture clauses only.

## Local verification obligations

The Mac phase must establish:

- exact installed command and alias set;
- all generated target paths after Workspace resolution;
- actual changed paths for each command mode;
- overwrite, append, move and delete behavior;
- symlink and containment handling;
- lock coverage and reentrancy;
- temporary-file and atomic-replace strategy;
- post-write reread/hash verification;
- partial-failure cleanup and recovery;
- latest-pointer and report-pair consistency;
- whether any test, script or internal entry point writes the same targets outside the listed generators.

Until that work is complete, this matrix remains `REMOTE_PARTIAL`.
