# Source Assumptions

Every item must be revalidated against the then-current `origin/main` before implementation. `VERIFIED` below is limited to the exact validation ref and cited record; suitability and compatibility remain Probe questions unless stated otherwise.

Validation ref for the current Discovery set: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

| ID | Status | Evidence-backed statement | Remaining validation |
|---|---|---|---|
| A-001 | NEEDS_MAIN_REPO_VALIDATION | The observed registry is document-wide and schema-bounded; no region identity or projection block was observed. See `evidence/repo-facts/DP1-DISC-001-REGISTRY-6A9DA7D.md`. | DP1 Probe must test whether the real parser and validator accept a proposed optional projection contract compatibly. |
| A-002 | VERIFIED | `docs/handoff/CURRENT_HANDOFF.md` mixes a bounded generated current-state block with accumulated historical prose; full-document readers and the active admin-refresh writer path were identified. See DISC-002, DISC-003 and DISC-010 records. | The production document form and ownership of preserved non-projected bytes remain Assessment decisions. |
| A-003 | PARTIAL | `.agentic/operational_handoff_state.yaml` and existing render helpers provide observed inputs for the current generated block, but they do not encode all historical/manual bytes. See DISC-003, DISC-004 and DISC-010 records. | Probe must determine whether declared canonical inputs are sufficient for the proposed projection scope without new runtime authority. |
| A-004 | PARTIAL | The existing lifecycle provides structured findings, WARN/FAIL/BLOCK result semantics, strict-code staging, dry-run triage and plans. See DISC-005, DISC-006 and DISC-009 records. | Probe and DPA-500 must determine whether these structures can represent projection drift and required gate consequences without a parallel audit. |
| A-005 | PARTIAL | Existing transfer workflows provide local reentrant locking, branch guards, full-SHA PR guards, remote-head checks and administrative refresh serialization. See DISC-008 and DISC-009 records. | Probe and DPA-600 must determine whether plan fingerprints, stale-target rejection and competing projection refreshes can be enforced with these mechanisms. |

No row above selects a production document form, establishes compatibility or creates normative architecture.
