# DPA-300 Secondary Technical Verification

Status: complete

Reviewed repository: `vfi64/agentic-project-kit-dpa-lab`

Reviewed ref: `6682485e3809d42bb17a90b62582b15e4d8fd467`

Role: Secondary technical verification under DPA-ADR-012

Primary review verified: `reviews/claude/CLAUDE_DPA_300_PRIMARY_REVIEW.md`

## 1. Result

Overall result: **ACCEPT_WITH_CHANGES**

The secondary verification independently confirms that DPA-300 contains no blocker, parallel registry or lifecycle, new runtime authority, production-form preselection or false implementation claim.

The four Claude Major findings are accepted as technically valid:

- R3-M01 — ACCEPT
- R3-M02 — ACCEPT
- R3-M03 — ACCEPT
- R3-M04 — ACCEPT

The seven Minor findings and editorial batch are also accepted, subject to the maintainer dispositions recorded below.

## 2. Independent verification of R3-M01

DPA-300 §12 requires accepted contract, source, target and output fingerprints to be recorded but does not define an authoritative lifecycle-state location. DPA-300 §13 correctly prohibits evidence from becoming runtime authority. Therefore evidence cannot satisfy §12 without violating DPA-INV-010.

The classification rule is also incomplete. A mismatch between recomputed output and target bytes cannot by itself distinguish changed canonical sources from an out-of-band target edit.

Disposition verified:

- introduce one lifecycle-owned persisted acceptance-state record;
- keep it distinct from evidence;
- classify source, target and partition drift by independent accepted fingerprints;
- allow simultaneous drift findings;
- use recomputation only as a secondary integrity check.

## 3. Independent verification of R3-M02

The lifecycle model defines failure before and after Write only while the process can continue executing. It does not govern process termination, orphaned plans, stale-lock takeover, written-but-unverified bytes or the transition of a crashed instance to `abandoned`.

DPA-200 explicitly delegated crash recovery to DPA-300. The omission is therefore real and in scope.

Disposition verified:

- detect interrupted prior refreshes before planning or mutation;
- mark the interrupted instance `abandoned` with a finding;
- permit re-verification only when the exact recovered plan and every guard remain valid;
- otherwise regenerate from declared sources;
- never accept orphaned bytes silently;
- record stale-lock takeover and recovery disposition.

## 4. Independent verification of R3-M03

DPA-300 references a partition-contract identity, partition fingerprint and validation requirement but defines no registry representation for the partition contract. At the same time it duplicates boundary representation and malformed-boundary behavior on region targets, conflicting with DPA-200 and DPA-ADR-013 document-level partition ownership.

Disposition verified:

- place the partition contract on the parent document registry entry;
- define ordered regions, ownership classes, boundaries, normalization, ordering and malformed behavior there;
- make region projection entries reference the parent partition contract;
- remove configurable boundary ownership from projected-region entries;
- leave exact serialized shape to PROBE-001.

## 5. Independent verification of R3-M04

The DISC-003 correction record remains an `ASSUMPTION` and lists factual verification work. Discovery completion therefore cannot be stated without qualification unless the item is assigned and explicitly deferred.

Disposition verified:

- execute bounded DISC-003b now at validation ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`, which remains current at verification time;
- until its result is committed, replace singular completeness language with `an observed writer path`;
- update DISC-003, its correction record, A-002, STATUS, MAIN_REPOSITORY_CONTEXT, DPA-300, traceability and PROBE-002 consistently.

## 6. Maintainer dispositions

### Acceptance-state placement

Accepted placement class: **Workspace-resolved lifecycle state under `.agentic/`**.

This is not evidence, not canonical source state, not registry authority and not target metadata. The exact main-repository path and serialized schema remain `NEEDS_MAIN_REPO_VALIDATION` and must be covered by PROBE-002.

### Crash-written bytes

Accepted policy: **verify against the recovered plan only when the exact plan, output and every captured guard remain valid; otherwise regenerate**.

No interrupted output may become accepted merely because bytes match a previous write attempt.

### Partition-contract placement

Accepted placement: **the parent registered-document entry**.

A separate registry object is rejected because it would add unnecessary identity and ownership complexity.

### DISC-003 correction

Accepted action: **execute DISC-003b now** rather than leave an ownerless open gap.

### Drift vocabulary ownership

Accepted ownership: DPA-100 owns the closed drift-class vocabulary. The canonical terms are:

- base drift;
- source drift;
- target drift;
- contract drift;
- renderer drift;
- partition drift;
- ownership drift.

`boundary drift` is retired in favor of `partition drift`.

Because DPA-100 is being revised, the temporary consumer trust-state amendment must be folded into DPA-100 proper and then retired as a normative source.

## 7. Minor and editorial dispositions

Accepted:

- remove the residual DPA-300 stub and add a number-to-file map;
- enter `written-unverified` immediately after Write;
- capture payload, preserved-region and complete-target fingerprints for region plans;
- prohibit nested projection mutations while preserving outer orchestration reentrancy around one refresh;
- add missing invariant/Workspace/recovery/partition traceability;
- reject unknown fingerprint algorithms and input-domain versions;
- separate execution and trust-state meaning in diagrams and add Preflight;
- make identity-critical evidence fields mandatory;
- clarify warning semantics and command-deprecation freedom;
- normalize evidence-record headers when DISC-003b is applied.

## 8. Conclusion

Claude's review is technically sound. The required changes are bounded adjudication and completion work, not structural redesign.

DPA-300 must not be promoted to `review-ready` until:

1. ADR-016 and ADR-017 are accepted;
2. DISC-003b is closed;
3. DPA-100 is consolidated;
4. DPA-300, traceability and diagrams are synchronized;
5. an independent post-adjudication verification passes.
