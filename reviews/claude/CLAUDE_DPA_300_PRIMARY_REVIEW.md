# Claude Primary Architecture Review — DPA-300 Registry and Lifecycle Integration

Reviewed repository: `vfi64/agentic-project-kit-dpa-lab`

Reviewed ref: `6682485e3809d42bb17a90b62582b15e4d8fd467`

Reviewer: Claude Fable 5

Review status: COMPLETE

Overall verdict: **ACCEPT_WITH_CHANGES**

DPA-300 may advance to `review-ready` after adjudication. No blocker, hidden parallel subsystem, new runtime authority, false implementation claim or production-form preselection was found.

This committed review record preserves the complete set of findings, decisions requested, audit conclusions and final verdict supplied by the reviewer. It is non-normative until maintainer adjudication.

## 1. Executive assessment

The evidence-first sequence materially improved DPA-300. The draft is grounded in exact-ref Discovery evidence for the document-wide registry, dry-run lifecycle without a content writer, reentrant PID-based workspace lock and the observed `admin-refresh-pr` append writer that bypasses the existing bounded-replacement primitive. The registry-extension model, twelve-phase lifecycle, mutation-plan contract, stale-plan guards, sole-writer rule, trust-state boundary and existing-command adaptation are sound.

Four major changes are required before `review-ready`.

## 2. Blocking findings

None.

## 3. Major findings

### R3-M01 — Direct-write detection storage and drift classification

DPA-300 requires accepted fingerprints but defines no INV-010-compliant storage locus. Evidence records cannot be the runtime source. Recomputation alone cannot distinguish source drift from target drift.

Required disposition:

- define a persisted lifecycle-owned acceptance-state record, distinct from evidence;
- persist accepted contract, renderer, source, target/partition and output fingerprints;
- classify source and target drift independently, allowing both findings;
- retain recomputation as a secondary integrity check;
- leave the concrete main-repository storage mapping `NEEDS_MAIN_REPO_VALIDATION`.

### R3-M02 — Crash and interrupted-mutation recovery missing

DPA-200 delegated crash recovery to DPA-300, but the draft covers only failures while the process remains alive. It does not govern process loss after lock acquisition or after writing but before verification/evidence/release.

Required disposition:

- detect stale locks, plans without completed verification and planned-but-unverified output;
- mark the interrupted refresh instance `abandoned` before a new mutation;
- never silently accept bytes from an interrupted instance;
- re-verify against a recovered still-valid plan or regenerate;
- record stale-lock takeover and disposition;
- preserve the atomic old-or-new complete-file guarantee.

### R3-M03 — Partition-contract registry representation undefined

DPA-300 validates and fingerprints a partition contract but never defines its registry representation. Boundary fields are duplicated on region targets, conflicting with DPA-200 and ADR-013 ownership.

Required disposition:

- define the partition contract on the parent document registry entry;
- include ordered region identities and owner classes, boundary representation, normalization, ordering/adjacency and malformed/missing/duplicate behavior;
- reduce a region target to parent identity, region identity, partition-contract identity and its own target semantics;
- reject missing, dangling or inconsistent partition references;
- keep serialized-schema compatibility for PROBE-001.

### R3-M04 — Discovery completeness overstated

The DISC-003 correction record remains `ASSUMPTION` with factual verification steps. `STATUS.md` nevertheless declares Discovery complete and several artifacts say “the active writer path”, implying completeness that the evidence does not support.

Required disposition:

- execute bounded read-only DISC-003b at the recorded validation ref, or explicitly record an owned open Discovery gap;
- until closed, use “an observed writer path” rather than “the active writer path”;
- update A-002, STATUS, MAIN_REPOSITORY_CONTEXT, DPA-300 and traceability consistently;
- keep the normative rule generic and plural for every existing candidate writer.

## 4. Minor findings

### R3-m01 — Residual DPA-300 stub

Remove or demote `specs/dpa/DPA-300-REGISTRY-AND-LIFECYCLE.md` and add a DPA number-to-filename map to `specs/dpa/README.md`.

### R3-m02 — `written-unverified` entry condition

The state begins immediately after the governed write. Verification success does not create the state; verification failure transitions the instance to `abandoned` with a finding.

### R3-m03 — Drift vocabulary ownership

Unify `boundary drift` and `partition drift` as `partition drift`. Register the extended drift family under one owner. If DPA-100 is touched, fold the consumer-trust-state amendment into DPA-100 in the same governed change.

### R3-m04 — Region plan fingerprints

For region targets capture the payload fingerprint, preserved-region fingerprint and expected complete-target fingerprint.

### R3-m05 — Reentrancy rule

Replace the untestable “complete call graph” condition. A projection refresh must not initiate another projection mutation. Existing same-process reentrancy may wrap exactly one refresh under outer orchestration.

### R3-m06 — Traceability and validation gaps

Add anchors for DPA-INV-008, DPA-INV-014 and DPA-INV-016; add Workspace path-resolution traceability; reject unknown fingerprint algorithms/input-domain versions; normalize Discovery record headers.

### R3-m07 — Diagram synchronization

Separate or clearly distinguish refresh execution states from byte trust states. Add Preflight to the command-flow diagram.

## 5. Editorial findings

- Clarify that warnings do not authorize mutation; only explicit plan-bound execution does.
- Make identity-critical evidence fields mandatory.
- Tighten the wording around fields that alter evidence or gate interpretation.
- Clarify the scoped VERIFIED heading in MAIN_REPOSITORY_CONTEXT.

## 6. Registry-contract audit

PASS except for the missing partition representation and unknown fingerprint-algorithm rejection. Manual entries remain backwards compatible; malformed projection metadata fails loud; no executable plugin path or silent fallback is permitted.

## 7. Lifecycle-phase audit

The order Resolve → Inspect → Validate → Render → Plan → Preflight → Lock → Revalidate → Write → Verify → Record → Release is sound. Render remains a named pure phase before Plan. In-process failures are governed; process-loss recovery is missing under R3-M02.

## 8. Mutation-plan and stale-plan audit

The immutable plan and exact-plan-bound execution are sound. Every semantics-affecting input invalidates the plan. Region plans require the additional payload and complete-target fingerprint distinction. Time remains evidence only.

## 9. Locking and atomic-write audit

Local workspace locking and complete-file atomic replacement are correct boundaries. Cross-PR serialization remains delegated. Reentrancy must be made testable, and stale-lock takeover must dispose of interrupted refresh state explicitly.

## 10. Direct-write and evidence audit

The sole-writer rule is complete. Evidence remains non-authoritative. Direct-write detection needs the lifecycle-owned acceptance state required by R3-M01.

## 11. Trust-state audit

The closed token set remains valid. `accepted` remains DPA-500-owned. `written-unverified` starts at Write. Crashed attempts require governed transition to `abandoned` by a later detecting lifecycle run.

## 12. Existing-command integration audit

The draft correctly adapts existing candidate writers instead of creating a DPA-only parallel command. The observed `admin-refresh-pr` flow is correctly conditional on later target registration and form selection. Writer-set completeness remains open under R3-M04.

## 13. Invariant audit

All DPA-INV-001 through DPA-INV-017 pass or are correctly delegated. R3-M01 is a caveat for INV-010; missing traceability anchors are minor. No invariant contradiction exists.

## 14. Decision audit

ADRs 001–015 are substantively respected. Required corrections concern ADR-013 partition representation, ADR-014 write-state timing, ADR-015 Discovery-completion discipline and registration of the expanded drift vocabulary.

## 15. Traceability audit

RL-001 through RL-020 have the required fields. New rows are required for acceptance state/direct-write classification, interrupted recovery, partition representation and Workspace path resolution. PROBE-002 must include the DISC-003 correction/follow-up evidence.

## 16. Failure-mode audit

Most required failure modes are covered. Missing or partial cases are interrupted process recovery, stale-lock disposition, nested projection mutation, partition representation, correct drift classification and the unresolved writer-set inventory.

## 17. Main-repository validation audit

The Discovery records are exact-ref bounded and suitable as architecture inputs. Concrete serialized schema, state location, lifecycle integration, finding IDs, gate mappings, atomic-write mechanism and candidate form remain `NEEDS_MAIN_REPO_VALIDATION` or Probe-owned.

## 18. Answers to pre-review questions

1. Keep Render as a distinct pure phase before Plan; no second render occurs under lock when all captured fingerprints still match.
2. Payload plus deterministic reconstruction inputs is the default; complete bytes may be stored. Region plans require payload, preserved-region and expected complete-target fingerprints.
3. Prohibit nested projection mutations, while allowing outer orchestration reentrancy around exactly one refresh.
4. Do not add a sixth trust state for evidence-write failure; remain `written-unverified` with a blocking finding for DPA-500.
5. Persist a lifecycle-owned acceptance-state record; recomputation is secondary.
6. Preserve governed command behavior, not permanent CLI naming. Normal command-deprecation governance may rename an entry point.
7. Keep partition fingerprints separate from the complete-target fingerprint to preserve drift classification.

## 19. Accepted findings

Accept R3-M01 through R3-M04, R3-m01 through R3-m07 and the editorial batch for adjudication. Internal pre-audits correctly verify invariant and ADR alignment but have repeatedly missed cross-artifact and evidence-discipline defects; they do not replace external review.

## 20. Rejected alternatives

Rejected:

- reading acceptance fingerprints from evidence;
- mandatory OS file watchers or Git hooks;
- banning all lock reentrancy;
- adding a sixth trust token;
- requiring complete target bytes in every plan;
- folding partition fingerprints into only the complete-target fingerprint;
- defining DPA-500 finding IDs/severities in DPA-300;
- creating a DPA-specific refresh command;
- rewriting architecture from the unverified DISC-003 correction;
- delaying the architecture review until the DISC-003b follow-up.

## 21. Unresolved maintainer decisions

1. Acceptance-state placement class.
2. Recovery policy for bytes written by a crashed instance.
3. Partition-contract placement in the registry.
4. DISC-003b now versus an owned open gap.
5. Ownership of the extended drift vocabulary.

## 22. Recommended adjudication order

1. Record this review and obtain secondary verification against `6682485e…`.
2. Adjudicate acceptance state and crash recovery together.
3. Adjudicate partition representation.
4. Close DISC-003b or explicitly own the gap.
5. Apply normative major changes and the seven pre-review clarifications.
6. Apply minor/editorial changes, remove the stub and fold the DPA-100 amendment when DPA-100 is touched.
7. Regenerate traceability and diagrams.
8. Run independent post-adjudication verification.
9. Promote DPA-300 only after all exit criteria pass.

## 23. Review-ready assessment

DPA-300 is not yet review-ready because direct-write detection, crash recovery and partition representation are incomplete. Traceability, diagrams and exact-ref wording require bounded corrections. No structural redesign is required.

## 24. Final verdict

**ACCEPT_WITH_CHANGES**

DPA-300 may advance to `review-ready` after adjudication of R3-M01 through R3-M04 and application of the resulting amendments. The persisted acceptance-state decision and crash-recovery section are prerequisites for DPA-500; partition representation is a prerequisite for PROBE-001.

Review bound to `6682485e3809d42bb17a90b62582b15e4d8fd467`.
