# DPA-300 Traceability

Status: draft

Status-date: 2026-07-15

## 1. Requirement matrix

| ID | Requirement | Invariants / decisions | Discovery evidence | Later owner | Planned tests / probes | Gate obligation | Evidence obligation | Rollback consequence |
|---|---|---|---|---|---|---|---|---|
| RL-001 | Projection contracts extend the existing registry and do not create a second registry. | DPA-INV-006, DPA-INV-011, DPA-INV-012; ADR-001, ADR-005 | DISC-001 | DPA-300 | PROBE-001; existing-entry regression; unknown-field negatives | malformed or unknown projection metadata blocks use | exact parser/validator output at validation ref | remove optional extension and retain valid manual entry |
| RL-002 | Manual documents remain valid when no projection contract exists. | ADR-001; DPA-200 manual form | DISC-001 | DPA-300 | registry regression over all existing entries | no new failure for projection-absent entries | entry-count and parser regression record | registry extension can be reverted without document rewrite |
| RL-003 | Projection metadata is declarative and renderer resolution is static. | DPA-INV-006, DPA-INV-007; ADR-005 | DISC-001 | DPA-300 / DPA-400 | executable-field rejection; unknown-renderer negative | unknown renderer blocks plan | resolved identifier and contract fingerprint | remove rejected entry or restore prior registry version |
| RL-004 | Registry validation is side-effect free and precedes rendering and planning. | DPA-INV-004, DPA-INV-015 | DISC-001, DISC-006 | DPA-300 | mutation-free validation tests | validation failure blocks render/write | validation result record | target remains unchanged |
| RL-005 | A projection refresh follows Resolve→Inspect→Validate→Render→Plan→Preflight→Lock→Revalidate→Write→Verify→Record→Release. | DPA-INV-002–005, DPA-INV-015 | DISC-006, DISC-008 | DPA-300 | state-machine tests; phase-order negative tests | phase bypass blocks mutation | lifecycle transcript and phase results | failure before write is no-op; later failure requires governed recovery |
| RL-006 | Planning is dry-run by default and execution is bound to an exact plan. | DPA-INV-015 | DISC-006 | DPA-300 | no-execute default; wrong-plan-id rejection | unbound execute blocks | immutable plan record | no target change |
| RL-007 | Plans capture base, contract, renderer, sources, target, partition and output fingerprints. | ADR-004, ADR-006 | DISC-001, DISC-008 | DPA-300 | fingerprint-domain completeness; field-omission negatives | incomplete plan blocks | complete plan payload | regenerate plan from current authorities |
| RL-008 | Any captured drift invalidates the plan. | ADR-004, ADR-006, DPA-INV-005 | DISC-008 | DPA-300 / DPA-600 | base/source/target/contract/renderer/partition/owner drift tests | stale plan blocks write | invalidation finding and compared fingerprints | regenerate; never merge target prose |
| RL-009 | Every projection mutation uses the existing workspace mutation lock. | DPA-INV-004, ADR-003, ADR-006 | DISC-008 | DPA-300 | lock-acquisition, busy, stale-lock and reentrancy tests | lock failure blocks write | lock acquire/release evidence | target unchanged |
| RL-010 | Lifecycle is the sole writer of projected and partition bytes. | DPA-INV-002–004; ADR-003, ADR-013 | DISC-003, DISC-006 | DPA-300 | writer-call-graph negatives; renderer-side-effect tests | direct write produces drift finding | writer identity and plan evidence | restore from Git-backed prior target or regenerate |
| RL-011 | Region mutation constructs and atomically replaces the complete parent document. | ADR-013; DPA-200 byte ownership | DISC-003, DISC-006 | DPA-300 | crash/interruption tests; complete-file replacement | inability to prove atomicity blocks | pre/post file fingerprints | restore prior complete target from recoverable history |
| RL-012 | Bytes outside a projected region are preserved byte-identically. | ADR-013, ADR-007 | DISC-002, DISC-003, DISC-010 | DPA-300 / DPA-700 | outside-region preservation tests; concurrent-edit negative | changed preserved bytes invalidate plan | preserved-region fingerprints | restore prior target; no historical merge |
| RL-013 | Post-write verification precedes any gate acceptance. | ADR-014; DPA-INV-004 | DISC-005, DISC-006, DISC-009 | DPA-300 / DPA-500 | reread/fingerprint/boundary/normalization tests | verification failure blocks acceptance | verification record | governed recovery or prior-target restore |
| RL-014 | Lifecycle never assigns `accepted`. | ADR-014 | DISC-005, DISC-009 | DPA-300 / DPA-500 | privilege-boundary negative tests | only DPA-500 gate set may accept | trust transition evidence | abandon refresh instance |
| RL-015 | Direct writes are detected as target or partition drift without requiring a file watcher. | DPA-INV-004, ADR-004 | DISC-003, DISC-005, DISC-009 | DPA-300 / DPA-500 | modify-target-outside-lifecycle tests | drift finding blocks strict integration when adopted | expected vs observed target record | regenerate or restore; no silent normalization |
| RL-016 | Evidence is bounded and never runtime authority. | DPA-INV-010; ADR-002, ADR-011 | DISC-005, DISC-006 | DPA-300 | evidence-input prohibition tests | evidence cannot satisfy source validation | mutation/verification evidence record | evidence deletion does not change semantic output |
| RL-017 | Existing mutating command paths are adapted, not replaced by a parallel DPA command. | DPA-INV-011, DPA-INV-012; ADR-001 | DISC-003, DISC-004 | DPA-300 / DPA-800 | PROBE-002 command-path test | old append/direct path prohibited after adoption | command-to-lifecycle trace | revert adapter while preserving original command contract |
| RL-018 | `admin-refresh-pr` replaces a governed region rather than appending when the candidate is later approved. | ADR-007, ADR-013 | DISC-003 | DPA-300–700 | PROBE-002 | append behavior fails proposed conformance | before/after target and command transcript | restore prior target; no form preselection |
| RL-019 | Time is evidence only and cannot invalidate a plan or cause a hard failure by itself. | DPA-INV-013; ADR-008 | DISC-005, DISC-009 | DPA-300 / DPA-500 | old-plan-with-unchanged-inputs test | no time-only blocker | timestamp plus unchanged fingerprints | none |
| RL-020 | Repository-specific mapping remains exact-ref bounded until Probe. | DPA-INV-017; ADR-011, ADR-015 | DISC-001–010 | DPA-300 / DPA-800 | review classification audit | unsupported claim blocks review-ready | cited evidence records | return claim to NEEDS_MAIN_REPO_VALIDATION |

## 2. Trust-state mapping

| Lifecycle event | Permitted resulting state | Prohibited result |
|---|---|---|
| renderer returns valid payload | `computed` | `accepted` |
| immutable plan captured | `plan-captured` | target write without execution guard |
| plan invalidated or validation rejected | `abandoned` | automatic merge or silent retry |
| atomic write and byte verification succeed | `written-unverified` | direct `accepted` |
| DPA-500 gate set succeeds | `accepted` | lifecycle-local acceptance shortcut |

## 3. DPA-300 invalid-state tests

The planned implementation test suite MUST reject:

1. projection metadata accepted through a second registry;
2. unknown contract schema version;
3. unknown renderer identifier;
4. executable renderer import path;
5. ambiguous or duplicate target identity;
6. overlapping regions;
7. unowned boundary bytes;
8. multiple owners for one byte range;
9. renderer invocation before registry validation;
10. mutation without a captured plan;
11. execution with a nonmatching plan identity;
12. mutation without the workspace lock;
13. source, target, base, contract, renderer, partition or owner drift after planning;
14. renderer or workflow code writing target bytes;
15. in-place partial region write;
16. modified outside-region bytes silently preserved into a stale plan;
17. post-write verification omitted;
18. lifecycle assignment of `accepted`;
19. evidence used as a semantic input;
20. a new DPA-only command bypassing the observed existing command path;
21. append-based current-state accumulation after governed bounded replacement is adopted;
22. hard failure caused only by elapsed time.

## 4. Probe mapping

| Probe | DPA-300 questions |
|---|---|
| PROBE-001 | Can the actual registry parser and validator represent the optional contract without breaking existing entries or allowing silent fallback? |
| PROBE-002 | Can the existing `admin-refresh-pr` writer path be routed through a plan-bound, locked, atomic, verified bounded replacement while preserving bytes outside the region? |
| PROBE-003 | Can existing finding structures carry DPA lifecycle and direct-write findings without a parallel finding system? |
| PROBE-005 | Can the existing local lock and transfer orchestration implement the DPA-300 local contract and provide the inputs DPA-600 needs? |

## 5. Repository-specific evidence boundary

The following facts are `VERIFIED` only at `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`:

- the existing documentation registry is document-wide and does not expose the proposed projection schema;
- the observed document lifecycle has dry-run triage and plan paths but no projection target writer;
- the Workspace and workspace mutation lock exist;
- `admin-refresh-pr` and `_refresh_operational_handoff_docs()` are the observed active mutation path for the handoff refresh family;
- a bounded generated-block replacement primitive exists but is not used by that active `CURRENT_HANDOFF.md` append path;
- CI executes Ruff, the complete pytest suite and CLI smoke;
- Git contains recoverable prior document states.

No item above proves compatibility with this specification.