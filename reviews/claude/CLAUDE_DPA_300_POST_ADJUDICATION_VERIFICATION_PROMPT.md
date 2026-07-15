# Claude Prompt — DPA-300 Independent Post-Adjudication Verification

Repository: `vfi64/agentic-project-kit-dpa-lab`

Exact verification ref: `6d7ae431ee411063b15f7c80025897a3584e9dd9`

Role: independent post-adjudication verifier under DPA-ADR-012

## Independence requirement

Do not use the session that applied the DPA-300 adjudication changes. Clone the repository, fetch and check out the exact ref above. Make no repository writes.

## Mandatory bootstrap order

Read fully, in order:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `DECISIONS.md`
9. `ASSUMPTIONS.md`
10. `specs/dpa/README.md`
11. `specs/dpa/DPA-000-VISION.md`
12. `specs/dpa/DPA-100-FOUNDATIONS.md`
13. `specs/dpa/DPA-100-CONSUMER-TRUST-STATE-AMENDMENT.md`
14. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
15. `specs/dpa/DPA-200-DOCUMENT-FORM-MATRIX.md`
16. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
17. `decisions/DPA-ADR-013-DOCUMENT-FORM-AND-PARTITION-OWNERSHIP.md` or the exact ADR-013 file present in the tree
18. `decisions/DPA-ADR-014-CONSUMER-TRUST-STATE.md` or the exact ADR-014 file present in the tree
19. `decisions/DPA-ADR-015-EARLY-DP1-DISCOVERY.md`
20. `decisions/DPA-ADR-016-ACCEPTANCE-STATE-AND-INTERRUPTED-RECOVERY.md`
21. `decisions/DPA-ADR-017-PARENT-ENTRY-PARTITION-CONTRACT.md`
22. all `DP1-*` records under `evidence/repo-facts/`, including DISC-003b
23. `integration/DP1_DISCOVERY_CONTRACT.md`
24. `integration/DP1_PROBE_BACKLOG.md`
25. `traceability/DPA-300_TRACEABILITY.md`
26. all `dpa-300-*.mmd` diagrams
27. `reviews/claude/CLAUDE_DPA_300_PRIMARY_REVIEW.md`
28. `reviews/consolidated/DPA-300_SECONDARY_TECHNICAL_VERIFICATION.md`
29. `reviews/consolidated/DPA-300_ADJUDICATION_RECORD.md`

Resolve any filename variation by inspecting the tree; do not omit the underlying artifact.

## Verification questions

Verify independently:

1. DPA-100 is again the single normative vocabulary owner.
2. The former trust-state amendment is only a historical pointer.
3. Consumer trust-state timing matches ADR-014: Write enters `written-unverified`; only DPA-500 may produce `accepted`.
4. The acceptance-state record is lifecycle state, not evidence, canonical state, registry authority or renderer input.
5. Drift classification distinguishes base, source, target, contract, renderer, partition and ownership drift and permits simultaneous findings.
6. Recomputation is secondary and evidence is never used as runtime state.
7. Interrupted-refresh detection covers stale locks, orphaned plans and crashed-after-Write bytes.
8. Re-verification is allowed only for an exactly recovered still-valid plan; otherwise regeneration is mandatory.
9. The parent registry entry owns exactly one complete partition contract.
10. Projected-region entries do not duplicate boundary ownership or malformed-boundary policy.
11. Region plans carry payload, preserved-region, partition and expected complete-target fingerprints.
12. Nested projection mutations are prohibited while bounded outer orchestration reentrancy remains possible.
13. DISC-003b correctly resolves the earlier correction claim and all dependent language says `an observed writer path`, not global completeness.
14. The inspected `chat-switch-complete` path is not represented as a writer of `CURRENT_HANDOFF.md` at the Discovery ref.
15. Traceability contains requirements and negative tests for acceptance state, recovery, Workspace paths and partition representation.
16. Diagrams match the amended lifecycle, including Recover and Preflight, and do not conflate execution states with trust tokens.
17. The duplicate DPA-300 stub is absent and the canonical file map has one DPA-300 owner.
18. No parallel registry, lifecycle, state, evidence, command or gate subsystem is implied.
19. No production document form or implementation success is claimed.
20. Repository-specific claims remain exact-ref scoped.

## Required output

Produce a commit-ready English verification with:

1. metadata and exact ref;
2. method and reviewed files;
3. PASS or FAIL;
4. blocking findings;
5. major findings;
6. minor/editorial findings;
7. primary-finding closure table for R3-M01 through R3-M04;
8. ADR-016 and ADR-017 consistency audit;
9. DPA-100 single-home vocabulary audit;
10. DPA-300 lifecycle/recovery audit;
11. partition-contract audit;
12. evidence and DISC-003b propagation audit;
13. traceability and diagram audit;
14. remaining main-repository validation obligations;
15. final recommendation: promote to `review-ready` or return to adjudication.

Do not propose production code. Do not inspect a different main-repository ref. Do not treat reviewer agreement as implementation evidence.
