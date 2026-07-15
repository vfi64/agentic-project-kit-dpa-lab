# DPA-200 Traceability

Status: active
Status-date: 2026-07-15
Scope: DPA-200 document-model planning only; no production implementation is claimed.

## 1. Requirement traceability

| ID | Requirement | Invariants / decisions | Later owner | Planned validation | Evidence obligation | Rollback obligation |
|---|---|---|---|---|---|---|
| DM-001 | Every projected target resolves to one complete document or one registered region. | DPA-INV-008; ADR-003 | DPA-300, DPA-400 | target-resolution and multi-target rejection tests | registry and resolver evidence at validation ref | remove projection contract and restore prior target |
| DM-002 | Every byte range has exactly one write owner. | DPA-INV-002, 004, 012 | DPA-300, DPA-700 | overlap, gap and duplicate-owner negative tests | region ownership map | revert to prior manual ownership model |
| DM-003 | Projected output derives only from declared canonical sources and contract-declared configuration. | DPA-INV-001, 010; ADR-002, 004 | DPA-400 | undeclared-input and evidence-as-input rejection tests | source authority graph and fingerprint domain | disable projection where authority cannot be proven |
| DM-004 | Full projection is allowed only when every target byte is reproducible. | ADR-004, ADR-007 | DPA-500, DPA-700 | full reconstruction test | byte-complete authority map | restore prior manual document |
| DM-005 | Split and hybrid forms require non-overlapping ownership domains. | DPA-INV-004, 012 | DPA-300, DPA-700 | boundary overlap and normalization-conflict tests | registered-region boundary record | remove region contracts and restore prior target |
| DM-006 | Managed-head projection is exceptional and never auto-merges historical prose. | DPA-INV-005, 014; ADR-006, 007 | DPA-600, DPA-700 | competing-PR, drift and historical-conflict scenarios | concurrency and rollback evidence | abandon migration and restore tracked pre-migration form |
| DM-007 | Only output that crosses the consumer trust boundary is accepted state. | DPA-INV-004; ADR-003 | DPA-300, DPA-500 | computed/planned/written-unverified/accepted transition tests | lifecycle and gate result record | discard unaccepted bytes and retain last accepted target |
| DM-008 | Manual documents retain existing behavior when no projection contract exists. | DPA-INV-011, 012; ADR-001 | DPA-300 | manual-document regression tests | registry compatibility evidence | remove optional projection metadata |
| DM-009 | Malformed projection metadata fails loudly and never silently falls back to manual mutation. | DPA-INV-006, 007; ADR-005 | DPA-300, DPA-400 | malformed-contract and unknown-semantics tests | validator result | restore valid registry entry |
| DM-010 | Form selection requires exact-ref authority, reader, writer, compatibility and rollback evidence. | DPA-INV-017; ADR-009, 011 | DPA-800 / DP1 | evidence-completeness audit | DP1 fact records | select no migration when evidence is incomplete |

## 2. Document-form decision coverage

| Form | Primary requirements | Planned tests | Gate obligations | Rollback evidence |
|---|---|---|---|---|
| Manual | DM-008, DM-009 | compatibility and no-projection path | existing gates unchanged | prior registry and target remain authoritative |
| Full projection | DM-001, DM-003, DM-004, DM-007 | complete reconstruction, determinism, acceptance transition | reproducibility and lifecycle gates | restore complete prior target |
| Split projection | DM-001, DM-002, DM-003, DM-005, DM-007 | region partition, reader distinction, boundary integrity | projected component acceptance only | preserve and restore both components |
| Managed head | DM-002, DM-003, DM-005, DM-006, DM-007 | stale-plan, competing-PR and history conflict tests | cross-ref serialization plus trust-state gates | recover head and history from tracked authority |
| Hybrid | DM-001, DM-002, DM-003, DM-005, DM-007 | multi-region ownership, manual-boundary and normalization tests | per-region acceptance and document-level consistency | restore region map and pre-migration document |

## 3. Invalid-state tests

The later specifications MUST plan negative tests for:

1. missing canonical authority;
2. ambiguous target identity;
3. overlapping registered regions;
4. unowned byte ranges;
5. duplicate write ownership;
6. renderer mutation;
7. undeclared semantic input;
8. evidence or history used as runtime authority;
9. acceptance asserted before gates complete;
10. automatic historical-prose merge;
11. unavailable rollback source;
12. silent malformed-contract fallback;
13. one invocation producing multiple registered targets;
14. shared manual/projected boundary ownership;
15. append behavior that moves a historical boundary.

## 4. Main-repository validation boundary

The following remain `NEEDS_MAIN_REPO_VALIDATION` and MUST NOT be inferred from this traceability artifact:

- registry support for region-level target identity;
- actual boundary markers or structural addressing;
- actual lifecycle writer and direct-write paths;
- actual candidate readers and read order;
- actual gate placement and severity mapping;
- actual atomic-write behavior;
- actual rollback sources available at a validation ref.

## 5. Review readiness

DPA-200 traceability is sufficient for a first review baseline when:

- each matrix entry maps to at least one requirement ID;
- each requirement has a later-spec owner;
- every permitted projected form has test, gate, evidence and rollback obligations;
- every prohibited combination has a negative-test obligation;
- no row claims current implementation behavior without exact main-repository evidence.
