# Remote Handoff and Transfer Mutation Map — 2026-07-19

Status: active

Status-date: 2026-07-19

Main-repository exact ref:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Classification: exact-ref remote map, incomplete pending full call-chain and local confirmation

Related inventory:

`integration/REMOTE_COMMAND_MUTATION_INVENTORY_20260719.md`

## 1. Purpose

This map isolates the handoff and transfer command family because it contains composed command paths that read, write, repair, restore, generate, validate and publish multiple document-like and state artifacts.

It is not a normative authority model, completeness claim, Probe result or implementation authorization.

## 2. Public command map

| ID | Public command | Mode | Primary provisional class | Secondary effects | Observed targets | Notes |
|---|---|---|---|---|---|---|
| HTM-001 | `agentic-kit handoff show` | read-only | CMA-8 | registry-summary read | stdout | direct handoff path input |
| HTM-002 | `agentic-kit handoff check` | read-only | CMA-8 | registry-summary read | stdout | validates handoff state and optional registry summary |
| HTM-003 | `agentic-kit handoff prompt` | read-only | CMA-8 | renders freshness guard and prompt | stdout | does not persist the rendered prompt |
| HTM-004 | `agentic-kit handoff refresh` | dry-run default | CMA-8 | reads Git HEAD and computes proposed safe state | stdout | validates proposed state before output |
| HTM-005 | `agentic-kit handoff refresh --write` | execute | CMA-3 | complete YAML serialization | selected handoff-state YAML | no lock or post-write reread observed in direct caller |
| HTM-006 | `agentic-kit transfer normalize-session` | diagnostic default | CMA-8 primary | mandatory GC-report write may occur in preflight | local runtime report surface | command documentation understates total write surface when preflight report writing is counted |
| HTM-007 | `agentic-kit transfer normalize-session --write-outbox` | execute | CMA-3 or CMA-4, unresolved authority | GC-report write; optional volatile restoration when separately requested | canonical transfer outbox plus local GC report | outbox carries normalized session state but must not become handoff or acceptance authority |
| HTM-008 | `agentic-kit transfer normalize-session --repair-known-volatile` | repair | CMA-7 or CMA-6 depending restoration semantics | GC-report write; Git restoration of known volatile paths | configured known volatile transfer outputs | actual restored path set and authority require local changed-path observation |
| HTM-009 | `agentic-kit transfer chat-switch-complete` | execute | CMA-5 derived-reference-generator | package validation and optional canonical prompt updates | successor package directory; by default NEXT_CHAT_BOOTSTRAP, START_NEW_CHAT_PROMPT and CLOSEOUT_BEFORE_CHAT_SWITCH_PROMPT | public output directory is configurable; canonical prompt updates default true |
| HTM-010 | `agentic-kit transfer chat-switch-complete --no-update-canonical-prompts` | execute | CMA-5 | package-only write | selected successor package directory | still mutates package artifacts |
| HTM-011 | `agentic-kit transfer prepare-successor-handoff` | deprecated execute alias | CMA-5 | same package and canonical-prompt writes as chat-switch-complete | fixed latest package directory plus canonical prompts | deprecated alias remains a live writer path and must remain in writer inventory until removed or fail-loud blocked |
| HTM-012 | administrative refresh PR command, public binding to `admin_refresh_pr()` | composed execute | mixed composed authority | handoff state, operational state, status, current handoff, prompts, package, Git branch/commit/push/PR effects | at least eleven fixed Workspace targets plus package-prefix and post-PR handoff artifacts | exact public decorator and full call chain pending inspection |

## 3. Internal writer and orchestration map

### HWI-001 — `save_handoff_state()`

Inputs:

- current or proposed handoff mapping;
- direct path argument;
- preservation-anchor constants.

Writes:

- complete YAML file through `Path.write_text()`.

Observed safeguards:

- callers validate the proposed mapping before write;
- required preservation anchors are appended when absent.

Not observed:

- Workspace containment at the writer boundary;
- mutation lock;
- atomic replace;
- post-write reread;
- content-hash verification;
- changed-path-scope assertion;
- rollback record.

Provisional disposition:

Suspected implementation defect or architecture gap pending complete writer-set and intended authority evidence. Do not modify before PROBE-002 adjudication.

### HWI-002 — `write_transfer_outbox()`

Caller:

`transfer normalize-session --write-outbox`

Semantic role observed:

- persists one normalized session result to the canonical transfer outbox.

Open questions:

- whether the outbox is state, evidence or transport output;
- whether other commands independently write the same semantic result;
- retention and cleanup ownership;
- Workspace resolution and containment;
- atomicity and verification;
- whether downstream consumers can accidentally treat it as authorization.

Provisional disposition:

CMA-3 versus CMA-4 unresolved. Must be classified by consumer graph, not filename.

### HWI-003 — `write_successor_handoff_package()`

Callers observed:

- `transfer chat-switch-complete`;
- deprecated alias `transfer prepare-successor-handoff`.

Inputs observed at caller boundary:

- repository root;
- configurable or fixed package output directory;
- Boolean canonical-prompt update policy.

Outputs exposed by the result:

- `successor_context.yaml`;
- `source_manifest.json`;
- `validation_report.json`;
- `successor_prompt.md`;
- canonical prompt projections when enabled;
- generated HEAD identities and validation findings.

Authority finding:

The deprecated alias is not read-only compatibility. It remains an independent public route into the same writer. Therefore public command aliases must be inventoried as mutation operating modes even when they delegate to one implementation.

### HWI-004 — transfer preflight garbage collector

Observed call:

`run_local_garbage_collector(Path("."), write_report=True, run_id=command_stack_id)`

Finding:

The shared transfer preflight is not purely read-only. It writes a report before command-specific behavior. Consequently every transfer command using this preflight has at least one secondary document/report write unless the implementation short-circuits before it.

Architecture consequence:

Mutation classification requires primary and constrained secondary effects. A command advertised as diagnostic may still need declared write scope, cleanup, retention and evidence classification.

## 4. Administrative refresh target set

The inspected `_admin_refresh_paths(Workspace)` returns the following fixed target classes:

1. handoff state;
2. operational handoff state;
3. status document;
4. `CURRENT_HANDOFF.md`;
5. `NEXT_CHAT_BOOTSTRAP.md`;
6. `START_NEW_CHAT_PROMPT.md`;
7. successor `execution_contract.json`;
8. successor `source_manifest.json`;
9. successor `successor_context.yaml`;
10. successor `successor_prompt.md`;
11. successor `validation_report.json`.

The refresh-only ancestry check additionally admits:

- `CLOSEOUT_BEFORE_CHAT_SWITCH_PROMPT.md`;
- all paths below the latest successor-package directory;
- paths matching the Workspace post-PR successor-handoff prefix.

This is a broader allowed changed-path set than the eleven fixed targets. The distinction between fixed writer targets, package-prefix outputs and post-PR artifacts must remain explicit.

## 5. Semantic-fact overlap hypotheses

| ID | Semantic fact | Representations | Risk classification | Evidence still required |
|---|---|---|---|---|
| HOF-001 | repository HEAD and generated HEAD | handoff safe state, administrative evidence state, successor context, source manifest, validation report, rendered prompts | one fact with multiple generated representations; competing writer not yet proven | writer and consumer graph; generation ordering; mismatch behavior |
| HOF-002 | next allowed work / first instruction | handoff state, current handoff, next-chat bootstrap, start prompt, successor prompt | conflicting authority suspected | canonical input owner; every writer; direct-edit policy; stale detection |
| HOF-003 | current project status | status document, current handoff, successor context and prompt | composition-dependent writer suspected | status source and update ordering; partial-failure behavior |
| HOF-004 | transfer session result | transfer outbox, transfer report/uplink, command stdout | state-versus-evidence ambiguity | consumer graph and authorization behavior |
| HOF-005 | package validity | validation report, command return status, freshness checker findings | legitimate evidence projections possible | prove validation report cannot become runtime authorization without current guard checks |

## 6. Confirmed architecture-planning findings

### HTF-001 — Aliases are mutation authorities

Classification: confirmed planning requirement.

A deprecated public alias can still invoke a writer. Mutation inventory must classify command modes and aliases, not only unique internal functions.

### HTF-002 — Diagnostic commands can have secondary writers

Classification: confirmed planning requirement.

The transfer preflight writes a garbage-collector report. Primary CMA classification alone is insufficient; constrained secondary effects must be recorded and verified.

### HTF-003 — Configurable output directories widen the authorized path problem

Classification: suspected architecture gap requiring evidence.

`chat-switch-complete` accepts an arbitrary output directory at the CLI boundary. The exact package writer must be inspected for Workspace containment, root escape, symlink handling and protected-path collision.

### HTF-004 — Administrative refresh is a multi-artifact transaction without proven transaction semantics

Classification: suspected architecture gap requiring evidence.

The target family is known, but remote evidence has not yet established:

- one immutable mutation plan;
- under-lock revalidation of every input;
- atomic multi-artifact commit semantics;
- partial-failure recovery;
- post-write cross-artifact semantic verification;
- equality of authorized and actual changed paths.

No implementation defect is claimed until the full call chain is inspected and locally observed.

## 7. Required Probe and validation mapping

Potential bounded additions or explicit mappings, not yet amendments:

- PROBE-002: composed-command partial failure and recovery;
- PROBE-002: declared versus actual changed-path set;
- PROBE-002: state, evidence and generated-prompt authority separation;
- PROBE-002: direct path and configurable output-root containment;
- PROBE-002: alias and primary command equivalence;
- renderer Probe boundary: package renderer/generator distinction where pure rendering is identifiable;
- CSC/namespace checklist: successor package and canonical prompt paths under both profiles;
- local materialization plan: preflight secondary report writes included in before/after manifests.

No existing Probe case is changed by this map.

## 8. Next remote inspection

1. read `successor_handoff_package.py` completely;
2. read the transfer safety-context outbox writer;
3. read the local garbage-collector report writer and retention policy;
4. locate the public `admin-refresh-pr` decorator and full call chain;
5. inspect `_refresh_operational_handoff_docs()` and all delegated writers;
6. map status, current-handoff and canonical-prompt source ownership;
7. classify partial failure and retry behavior;
8. update the main mutation inventory with exact writer symbols and targets.

## 9. Current boundary

This map authorizes no writer changes, no direct generated-output patches and no Probe execution.

ADR-022 remains a deferred proposal. DPA-200 through DPA-500 remain unchanged. DPA-600 remains frozen. DPA-700 remains unstarted.
