# DPA Lab Execution Contract

Status: active
Status-date: 2026-07-15
Superseded-by: n/a

## 1. Purpose

This contract defines how work in `vfi64/agentic-project-kit-dpa-lab` must be planned, reviewed, committed, consolidated and transferred back to `vfi64/agentic-project-kit`.

The lab is a governed architecture workspace. It is not a scratchpad, prompt archive, production repository or second runtime authority.

## 2. Primary objective

Produce a complete, coherent, reviewable and implementation-ready Document Projection Architecture that extends the existing document-management architecture of `agentic-project-kit`.

The final lab output must include DPA-000 through DPA-900, accepted decisions, assumptions and validation requirements, diagrams, complete traceability, the main-repository validation checklist, controlled import plan and DP1–DP5 implementation contract.

## 3. Non-goals

The lab must not:

- contain production kit code;
- act as a runtime dependency;
- replace or duplicate Direction, registry, lifecycle, freshness, evidence, Workspace, workflow or gate authority;
- fabricate repository facts, test results or gate evidence;
- record model consensus as implementation evidence;
- create live `.agentic/` state before governed lab adoption;
- import private state or secrets;
- execute maintainer-gated main-repository work;
- silently expand DPA into a general plugin framework.

## 4. Language and style

- Chat communication: German, concise, direct and evidence-based.
- Normative specifications, diagrams and machine-readable artifacts: English.
- Normative keywords `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and `MAY` shall be used consistently.
- Ambiguous terms require the qualifications defined in DPA-100.

## 5. Required session bootstrap

Every session must follow `LAB_BOOTSTRAP.md`, complete the mandatory read order and report exact lab ref, phase, task, normative inputs, unresolved decisions, main-repository evidence used and proceed/stop status before work.

Chat memory is never authoritative.

## 6. Vocabulary ownership

DPA-100 is the normative owner of:

- repository-fact and architecture classifications;
- document statuses;
- progress statuses;
- access outcomes;
- authority, document, renderer, lifecycle, workflow, evidence and validation terms.

These dimensions MUST NOT be combined into undeclared compound statuses.

## 7. Architecture invariant ownership

DPA-000 §7 is the sole normative owner of the canonical invariant register `DPA-INV-001` through `DPA-INV-017`.

This contract and all derived artifacts MUST reference those IDs and MUST NOT duplicate, regroup, renumber or redefine them.

Lab decision artifacts are planning authority and evidence of adjudication, not production runtime authority. This is a lab-governance rule, not an additional DPA invariant.

Any normative artifact that contradicts a canonical invariant is invalid until reconciled through an accepted decision.

## 8. Specification order and dependencies

The normative series is developed in this order:

1. `DPA-000-VISION.md`
2. `DPA-100-FOUNDATIONS.md`
3. `DPA-200-DOCUMENT-MODEL.md`
4. `DPA-300-REGISTRY-AND-LIFECYCLE.md`
5. `DPA-400-RENDERER-CONTRACT.md`
6. `DPA-500-FRESHNESS-AND-GATES.md`
7. `DPA-600-CONCURRENCY.md`
8. `DPA-700-MIGRATION.md`
9. `DPA-800-DP1-DP5.md`
10. `DPA-900-FUTURE.md`

A later document may be outlined early but cannot become stable while contradicting or bypassing an earlier contract.

## 9. Phase model

### Phase A — Foundation

Scope:

- DPA-000 and DPA-100;
- canonical invariant register and glossary;
- initial traceability;
- primary architecture review;
- secondary technical verification;
- maintainer adjudication;
- consolidated review record.

Exit criteria:

- DPA-000 and DPA-100 are review-ready or stable;
- terminology and invariant references are internally coherent;
- no hidden parallel subsystem or new runtime authority is implied;
- repository-specific claims use the correct classification and evidence scope;
- initial traceability exists one-to-one for canonical invariants;
- primary architecture review and secondary technical verification are complete;
- maintainer adjudication is complete;
- accepted decisions and normative changes are synchronized;
- no unresolved Phase A blocker remains hidden in prose.

### Phase B — Core document-management integration

Scope: DPA-200 through DPA-500.

Exit criteria include complete document forms, registry extension, renderer boundary, lifecycle/freshness/gate integration, backwards compatibility, fail-loud behavior and exclusive reuse of existing systems.

### Phase C — Operational completion

Scope: DPA-600 through DPA-900.

Exit criteria include complete Git/PR concurrency, migration, rollback, DP1–DP5 implementation contract, future-scope boundary and full traceability.

### Phase D — Lab adoption by the kit

Preconditions:

- DPA-000 through DPA-500 stable;
- bootstrap and governance stable;
- validation against an exact main-repository validation ref;
- reversible adoption without circular runtime authority.

### Phase E — Main-repository validation and implementation

Execute DP1 against a validation ref, correct assumptions, update DPA when evidence requires it, implement DP2–DP5 in the main repository and import only approved artifacts.

## 10. Review governance

Review quality is governed by roles, not named products:

1. Primary architecture review.
2. Secondary technical verification.
3. Maintainer adjudication.
4. Consolidated review record.

A reviewer may be a model or human. A qualifying review must record:

- exact reviewed ref;
- reviewed files;
- reviewer/model and version when known;
- access method and access outcome;
- method and prior exposure relevant to independence;
- findings, strengths, limitations and repository facts requiring validation;
- proposed normative changes.

`access-blocked` is not an architecture verdict and does not satisfy a review role.

Storage directories MAY retain reviewer names, including `reviews/claude/`, `reviews/chatgpt/` and `reviews/gemini/`, but no named product is required when the governed roles are satisfied.

A review is non-normative. No reviewer may change normative meaning directly.

The consolidation sequence is:

1. collect qualifying review and verification inputs;
2. normalize finding identities and evidence;
3. identify agreements, disagreements and main-repository dependencies;
4. obtain maintainer decisions;
5. record accepted, modified and rejected findings;
6. update decisions and normative artifacts;
7. regenerate traceability;
8. reassess phase exit criteria.

## 11. Decision process

Architecture decisions are recorded in `DECISIONS.md` or dedicated ADR files.

Every accepted decision must include identifier, status, context, decision, alternatives, rationale, consequences, validation status, affected DPA documents and affected DP slices.

A decision requiring unavailable main-repository facts remains `PROPOSAL`, `ASSUMPTION` or `NEEDS_MAIN_REPO_VALIDATION` as appropriate.

## 12. Traceability contract

The lab must maintain traceability among motivation, canonical invariant ID, normative requirement, decision, candidate main-repository dependency, DP1–DP5 work, tests, gates, evidence and rollback.

Traceability must distinguish normative requirement, planned implementation, verified implementation, recorded-baseline evidence and future extension.

Each canonical invariant appears exactly once in the invariant table. Traceability is a derived view and never owns normative invariant meaning.

## 13. Commit and branch rules

Before kit adoption, the lab may use ordinary GitHub branches and PRs.

Each coherent change should:

- update only relevant files;
- avoid unrelated edits;
- update `STATUS.md` when phase, task or blockers change;
- update `DECISIONS.md` when a decision changes;
- update `ASSUMPTIONS.md` and `MAIN_REPOSITORY_CONTEXT.md` when fact classification changes;
- record review or adjudication context in the commit message.

## 14. Completion semantics

Document statuses are defined by DPA-100.

A document is not stable merely because prose exists. Stability requires required reviews and adjudication, synchronized decisions and traceability, no known contradiction and no hidden blocker for the document scope.

The lab never upgrades production implementation to verified completion without exact main-repository evidence.

## 15. Main-repository fact handling

When a specification needs a repository fact:

1. add or locate an assumption or fact identifier;
2. identify the required validation ref and evidence;
3. inspect exact sources when access exists;
4. store a minimal static record under `evidence/repo-facts/` when claiming `VERIFIED_AT_RECORDED_BASELINE`;
5. update `ASSUMPTIONS.md`;
6. update `MAIN_REPOSITORY_CONTEXT.md` when subsequent work depends on the result.

A minimal static record must conform to DPA-ADR-011. The lab must not create a parallel evidence database or service. Model agreement is not evidence.

## 16. DP1–DP5 relationship

The lab specifies; the main repository later executes:

- DP1: proof-of-architecture and evidence against an exact validation ref;
- DP2: first production projection and existing-system integration;
- DP3: controlled rollout to additional handoff/bootstrap documents;
- DP4: status-authority discovery and conditional migration;
- DP5: staged strict adoption in the existing lifecycle gate.

DP1 determines document form from evidence. The lab must not predeclare a candidate migration form as verified.

## 17. Required DP1 decision hierarchy

1. Full projection only when complete content is reconstructable from existing canonical sources.
2. Split current projection and historical evidence when historical prose is not canonical.
3. Managed head plus append history only as a justified exception with explicit region ownership and complete workflow serialization.
4. No migration when authority, consumers, readers, writers or rollback cannot be established.

No new canonical history store may be introduced merely to make migration convenient.

## 18. Concurrency contract

The normative DPA must distinguish local mutation locking, base/source/target/contract drift, branch concurrency, pull-request concurrency and workflow serialization.

A production refresh must capture and verify base SHA, target-region or full-target fingerprint, declared source fingerprints, renderer and contract identity and reproducibility against the validation ref.

On drift: block, regenerate from the validation ref, do not auto-merge historical prose and do not treat local locking as cross-PR serialization.

## 19. Stop conditions

Stop and produce a bounded diagnosis when:

- required evidence is unavailable;
- normative documents conflict;
- the work would create a parallel governance or runtime subsystem;
- a new runtime authority is introduced without an accepted decision;
- an implementation claim is requested from lab evidence;
- production code or live `.agentic/` state would enter the lab;
- a review cannot be adjudicated because a maintainer decision is missing;
- the current task depends on an unresolved earlier DPA contract.

## 20. Current work order

After DPA-ADR-009 through DPA-ADR-012 are accepted:

1. synchronize DPA-000, DPA-100 and this contract;
2. create minimal recorded-baseline evidence records;
3. regenerate Phase A traceability one invariant per row;
4. align governance wording, status and planning artifacts;
5. create a consolidated adjudication record;
6. reassess Phase A stability;
7. outline DPA-200 only after no foundational decision remains unresolved.
