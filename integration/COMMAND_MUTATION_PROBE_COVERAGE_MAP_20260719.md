# Command Mutation Authority to Probe Coverage Map — Remote Partial

Status: remote-partial

Status-date: 2026-07-19

Main-repository exact ref: `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Lab branch: `spec/dpa-600-concurrency`

## Purpose

This document maps Package-M command mutation authority requirements to the existing Probe packages without silently changing any reviewed Probe case.

It identifies:

- existing direct coverage;
- existing partial coverage;
- precondition or observation-model coverage;
- bounded amendments that may be required after ADR-022 review and Maintainer adjudication;
- requirements that remain inventory-only until a safe local harness exists.

No Probe has run. This document does not modify case semantics and does not authorize fixture materialization or execution.

## Coverage labels

- `DIRECT`: an existing case already tests the requirement materially.
- `PARTIAL`: an existing case covers part of the requirement but not the command-authority dimension completely.
- `PRECONDITION`: the requirement is already demanded before execution but is not itself a case outcome.
- `OBSERVATION`: the evidence model records the datum but does not define pass/fail behavior for it.
- `GAP`: no sufficient existing case exists.
- `NOT_APPLICABLE`: the Probe is intentionally outside the requirement's scope.

## Cross-Probe matrix

| Package-M requirement | PROBE-001 | PROBE-002 | Renderer Probe | Current assessment | Proposed disposition |
|---|---|---|---|---|---|
| complete command and internal-mutator inventory | discovery-extension requirement for registry paths | P002-C058 plus execution precondition 3 | internal-contract audit discovery extension expected | `PARTIAL` | keep as global precondition; require inventory completeness disposition before Probe-level conclusion |
| canonical input identity | registry fixture and normalized representation | P002-C007, C010–C014, C029 | renderer immutable-input and source-as-data cases | `DIRECT` across packages | no case change needed; add cross-Probe terminology only after review |
| declared target identity | P001-C011 and contract fields | P002-C002, C007, C029, C035 | renderer target/output-scope cases | `DIRECT` | no new case needed |
| command mode and alias identity | no direct coverage | entry point recorded, but alias equivalence is not a dedicated case | likely no direct alias case | `GAP` | bounded PROBE-002 amendment candidate: executable aliases must map to one mutation authority and identical declared semantics |
| primary changed-path scope | changed-path manifest recorded | pre/post hashes and target mutation recorded | output-scope cases | `PARTIAL` | strengthen execution contract/observation schema before adding a case; compare declared versus actual scope |
| secondary writer effects | changed-path manifest can reveal them | C058 can discover extra writer paths | prohibited-capability/resource evidence may reveal them | `PARTIAL` | bounded PROBE-002 amendment candidate or C058 clarification after review; no silent reinterpretation |
| declared-versus-actual changed-path equality | recorded but no explicit equality outcome | target/state changes observed, no dedicated equality case | output-scope likely partial | `GAP` | add one synchronized case only after ADR-022 adjudication, or define as mandatory cross-case assertion |
| generated-artifact ownership | P001-C022 rejects competing writer declaration | C004, C014, C024, C029, C041–C043 | lifecycle-only invocation and bounded output ownership | `DIRECT/PARTIAL` | retain current cases; add generated-artifact matrix as required input |
| direct-edit prohibition for generated output | not directly tested | C027 detects out-of-band lifecycle-byte mutation; C042 distinguishes authorized preserved-byte evolution | renderer output/lifecycle ownership cases | `PARTIAL` | proposed clarification: generated projection repair outside generator authority is unauthorized unless recovery contract permits it |
| composed-command ordering | not applicable | lifecycle order C001 and observed phases; no explicit nested command graph | renderer invocation boundary only | `PARTIAL` | bounded PROBE-002 amendment candidate for composed commands and helper side effects |
| one accepted source snapshot for multi-target generation | not applicable | immutable plan and drift cases cover one target/context | deterministic renderer inputs cover render scope | `GAP` | new Package-M-specific case family or synchronized extension required after review |
| atomic multi-target replacement | not applicable | C022 tests complete target atomic replacement, not multi-target package atomicity | output-scope only | `GAP` | bounded new case required for registered projection sets if implementation claims transactional group generation |
| partial multi-target failure and recovery | not applicable | C026 and C044–C050 cover lifecycle target recovery, but not synchronized artifact groups explicitly | failure semantics partial | `PARTIAL/GAP` | extend recovery fixtures only after safe interruption harness and ADR-022 acceptance |
| lock ownership and reentrancy | not applicable | C017–C021 | renderer must not own lifecycle lock | `DIRECT` for lifecycle path | require command-authority inventory to prove every mutator enters this path or classify exceptions |
| post-write verification before success | changed-path and cleanup only | C024, C028, C032, C053 | renderer failure semantics do not replace lifecycle verify | `DIRECT` | no new principle needed; command mapping must prove coverage |
| source/result freshness and stale projection rejection | registry ref freeze only | C009–C016, C033–C040, C059 | deterministic versions/input identities | `DIRECT` | no new case needed |
| evidence remains non-authoritative | explicit PROBE-001 evidence boundary | C052–C055 | renderer evidence cannot authorize write | `DIRECT` | no change needed |
| registry membership versus lifecycle-field ownership | parser/validator coverage and P001-C022 | C004, C014, C043 | not applicable | `PARTIAL` | add field-level authority map as execution precondition; new case only if overlapping writers exist |
| deprecated mutating alias behavior | no direct coverage | no dedicated case | not applicable | `GAP` | bounded alias-equivalence case after review |
| read-only command with hidden report write | changed-path manifest may reveal | C054 expects read-only audit without target/acceptance mutation but bounded evidence is permitted | not applicable | `PARTIAL` | define evidence-output exception separately from target mutation and require declared secondary scope |
| Workspace-resolved output containment | fixture isolation and protected-path checks | C002 plus cleanup requirements | output scope and secret boundaries | `DIRECT/PARTIAL` | strengthen exact declared path-set assertion in execution contract |
| symlink and path-escape behavior | not explicit in current manual | not explicit in listed C001–C060 | renderer secret/output boundary may be relevant | `GAP` | harness-level safety test required before any mutation Probe; architecture case only if DPA contract claims behavior |
| generator version and command-reference synchronization | schema/version coverage | contract and renderer drift cases | renderer version cases | `PARTIAL` | add source ordering requirement: command-reference regeneration must precede successor prompt projection where applicable |

## Existing PROBE-001 coverage relevant to Package M

PROBE-001 already provides strong registry authority evidence for:

- sole declarative registry authority;
- loud rejection of malformed or unknown projection metadata;
- rejection of competing region writer authority in P001-C022;
- changed-path manifests and partial-state observation;
- discovery and rerun obligations for additional readers, parsers, validators, loaders or normalization paths.

PROBE-001 intentionally does not test lifecycle mutation, generated handoff sets, aliases, composed commands or recovery. Those subjects must not be inserted into PROBE-001 merely because registry metadata names an owner.

## Existing PROBE-002 coverage relevant to Package M

PROBE-002 already covers most underlying lifecycle safety principles:

- ambiguous ownership rejection;
- immutable plans and exact context binding;
- target/source/contract/configuration/renderer/partition/ownership drift;
- lock exclusion, reentrancy, under-lock revalidation and release;
- atomic complete-target replacement;
- post-write verification;
- acceptance only after verify and gates;
- layered ownership and ambiguous-provenance rejection;
- interruption and recovery states;
- independent findings, evidence boundaries and staged enforcement;
- discovery of additional writer, reader, lock, state, gate, evidence or recovery paths through P002-C058.

However, current cases mostly model one governed lifecycle target. Package M introduces command-level and multi-artifact questions that are not automatically equivalent to those cases.

## Bounded amendment candidates

The following are candidates for a later synchronized Probe amendment. They MUST NOT be inserted before ADR-022 and the associated DPA-200/300/400/500 clauses are independently reviewed and adjudicated.

### Candidate M-P002-01 — Alias authority equivalence

An executable mutating alias and its canonical command must resolve to one registered mutation authority, equivalent declared primary and secondary scopes, equivalent ordering and equivalent verification behavior. Deprecation alone is not a pass condition.

### Candidate M-P002-02 — Declared versus actual changed-path equality

For each command mode, the governed declared changed-path set must equal the actual changed-path set, apart from separately declared volatile evidence outputs. Unexpected targets fail closed and block conformance conclusions.

### Candidate M-P002-03 — Secondary writer declaration

Helpers, preflights, garbage collectors, report writers and nested commands that create document-like output must appear in the command's secondary mutation declaration and evidence manifest.

### Candidate M-P002-04 — Multi-artifact accepted snapshot

A registered projection set must be rendered from one accepted source snapshot. Source drift between member writes must prevent the set from being represented as current.

### Candidate M-P002-05 — Partial projection-set failure

Interruption or failure during a multi-artifact generation must leave an explicit incomplete/recovery state. A subset must not be accepted or advertised as the current synchronized set.

### Candidate M-P002-06 — Direct generated-output repair

A direct edit to a generated projection must be rejected as a durable repair unless the registered ownership contract explicitly permits bounded source regions or recovery-only editing followed by complete regeneration and verification.

These identifiers are planning labels, not Probe case numbers.

## Cases that should not be changed

Current evidence does not justify changing the semantics of:

- P001-C001 through P001-C027;
- P002-C001 through P002-C060;
- renderer cases governing static resolution, determinism, prohibited capabilities and lifecycle-only invocation.

Any later amendment must preserve historical identifiers, document the exact changed contract and require review of fixture manifests, internal audits, evidence procedures and adjudication rules together.

## Required pre-execution additions without case-number change

Before execution, the common execution contract should require the local package to include:

1. complete public CLI mode inventory;
2. internal mutator inventory;
3. alias map;
4. primary and secondary changed-path declarations;
5. generated-artifact ownership matrix;
6. semantic-fact overlap matrix;
7. composed-command graph;
8. local observed changed-path manifest;
9. explicit classification of inventory gaps;
10. confirmation that no protected repository state can be reached by the fixture harness.

This is a proposed Package-M requirement and remains non-normative pending review.

## Outcome boundary

A Probe result cannot establish command-authority completeness when:

- the command or internal writer inventory is incomplete;
- aliases are untested;
- secondary writer effects are omitted;
- declared-versus-actual scope is not compared;
- a generated projection set is tested only as independent files despite synchronized-current claims;
- partial-failure recovery cannot be safely exercised.

Such conditions require `BLOCKED`, `PARTIAL` or an explicit inventory limitation, not inferred conformance.
