# DPA Lab Execution Contract

Status: active
Status-date: 2026-07-15
Superseded-by: n/a

## 1. Purpose

This contract defines how work in `vfi64/agentic-project-kit-dpa-lab` is planned, reviewed, committed, validated and transferred to `vfi64/agentic-project-kit`.

The lab is a governed architecture workspace. It is not a production repository, runtime dependency, prompt archive or second runtime authority.

## 2. Primary objective

Produce a coherent, reviewable and implementation-ready Document Projection Architecture consisting of DPA-000 through DPA-900, accepted decisions, classified assumptions, diagrams, traceability, main-repository evidence obligations, controlled import planning and the DP1–DP5 implementation contract.

## 3. Non-goals

The lab MUST NOT:

- contain production kit code;
- replace or duplicate Direction, registry, lifecycle, freshness, evidence, Workspace, workflow or gate authority;
- fabricate repository facts, tests or gate evidence;
- treat model agreement as implementation evidence;
- create live `.agentic/` state before governed adoption;
- import secrets or private runtime state;
- execute mutation or migration work in the main repository except through later governed implementation;
- become a general executable plugin framework.

## 4. Language and style

- Chat communication: German, concise, direct and evidence-based.
- Normative specifications, diagrams and machine-readable artifacts: English.
- Normative keywords MUST be used consistently.
- Ambiguous terms MUST be qualified using DPA-100.

## 5. Required session bootstrap

Every session MUST follow `LAB_BOOTSTRAP.md`, complete its read order and report exact lab ref, phase, task, normative inputs, unresolved decisions, main-repository evidence and proceed/stop status.

Chat memory is never authoritative.

## 6. Vocabulary ownership

DPA-100 owns repository classifications, document status, progress status, access outcomes, consumer trust-state vocabulary and all foundational authority and component terms.

Vocabulary dimensions MUST NOT be combined into undeclared compound statuses.

## 7. Architecture invariant ownership

DPA-000 §7 solely owns `DPA-INV-001` through `DPA-INV-017`.

Derived artifacts MUST reference but MUST NOT duplicate, regroup, renumber or redefine those invariants.

Lab decisions are planning authority and adjudication evidence, not production runtime authority.

## 8. Specification sequence

1. DPA-000 — Vision and architectural principles.
2. DPA-100 — Foundations and terminology.
3. DPA-200 — Document model.
4. DPA-300 — Registry and lifecycle integration.
5. DPA-400 — Renderer contract.
6. DPA-500 — Freshness and gates.
7. DPA-600 — Concurrency and workflow serialization.
8. DPA-700 — Migration and rollback.
9. DPA-800 — DP1–DP5 implementation specification.
10. DPA-900 — Future evolution.

A later document MAY be outlined early but MUST NOT become stable while contradicting an earlier stable contract.

DPA-ADR-015 creates one bounded sequencing exception: the read-only Discovery stage of DP1 MAY execute after DPA-200 is review-ready and before DPA-300. This exception does not reorder the normative specification series.

## 9. Phase model

### Phase A — Foundation

Scope: DPA-000, DPA-100, canonical invariants, initial traceability, primary review, secondary verification, maintainer adjudication and consolidation.

Exit requires coherent terminology and invariants, correct evidence classification, no hidden parallel system, completed review roles, synchronized decisions and no unresolved Phase A blocker.

### Phase B — Core document-management integration

Scope: DPA-200 through DPA-500.

Exit requires complete document forms, registry and lifecycle integration, renderer boundary, freshness and gate contracts, backwards compatibility, fail-loud behavior and exclusive reuse of existing systems.

After DPA-200 becomes review-ready, Phase B MAY include the early DP1 Discovery stage governed by DPA-ADR-015 and `integration/DP1_DISCOVERY_CONTRACT.md`.

Early Discovery is factual inventory only. It MUST NOT perform Probe, Assessment, migration, mutation, adoption, conformance judgment or architecture adjudication.

### Phase C — Operational completion

Scope: DPA-600 through DPA-900.

Exit requires complete concurrency, migration, rollback, DP1–DP5 implementation contract, future-scope boundary and full traceability.

### Phase D — Lab adoption by the kit

Preconditions:

- DPA-000 through DPA-500 stable;
- bootstrap and governance stable;
- exact-ref validation evidence available for adoption assumptions;
- reversible adoption without circular runtime authority.

### Phase E — Main-repository validation and implementation

Phase E executes the DP1 Probe and Assessment stages against exact validation refs, corrects assumptions and specifications when evidence requires it, implements DP2–DP5 in the main repository and imports only approved artifacts.

The early Discovery exception does not authorize Phase-E implementation work.

## 10. Review governance

Review quality is governed by roles:

1. Primary architecture review.
2. Secondary technical verification.
3. Maintainer adjudication.
4. Consolidated review record.

A qualifying review records exact ref, files, reviewer, access method and outcome, method and prior exposure, findings, limitations, repository-validation needs and proposed normative changes.

`access-blocked` is not an architecture verdict. Reviews are non-normative until adjudicated.

## 11. Decision process

Accepted decisions MUST record identifier, status, context, decision, alternatives, rationale, consequences, validation status, affected artifacts and affected DP slices.

Decisions MAY be stored in `DECISIONS.md` or dedicated files under `decisions/`.

A decision requiring unavailable main-repository facts remains `PROPOSAL`, `ASSUMPTION` or `NEEDS_MAIN_REPO_VALIDATION`.

## 12. Traceability contract

The lab MUST maintain traceability among motivation, invariant, requirement, decision, main-repository dependency, DP work, tests, gates, evidence and rollback.

Traceability distinguishes planned, verified, baseline-recorded and future work and never owns normative meaning.

## 13. Commit and branch rules

Before adoption the lab MAY use ordinary branches and pull requests.

Each coherent change SHOULD update only relevant files, synchronize STATUS and decisions, update assumptions when facts change and record review or adjudication context in the commit message.

## 14. Completion semantics

Document status is defined by DPA-100.

Stability requires completed reviews and adjudication, synchronized decisions and traceability, no known contradiction and no hidden blocker for the document scope.

The lab never marks production implementation verified without exact main-repository evidence.

## 15. Main-repository fact handling

When a specification needs a repository fact:

1. identify the assumption or fact ID;
2. record the exact validation ref;
3. inspect exact sources using a governed method;
4. create bounded records under `evidence/repo-facts/`;
5. update `ASSUMPTIONS.md`;
6. update `MAIN_REPOSITORY_CONTEXT.md` only where later work depends on the result.

Records MUST follow DPA-ADR-011. The lab MUST NOT create a parallel evidence database, generator, maintained mirror or runtime evidence service.

### Early Discovery evidence

Early DP1 Discovery MUST follow `integration/DP1_DISCOVERY_CONTRACT.md`.

Discovery MAY verify or falsify assumptions for the exact validation ref. It MUST NOT:

- decide contract sufficiency;
- infer conformance;
- select a production form;
- create or reject architecture decisions;
- mutate either repository.

Questions about whether observed mechanisms satisfy a proposed DPA contract belong to Probe or Assessment.

## 16. DP1–DP5 relationship

The lab specifies and the main repository later implements:

- DP1 — proof of architecture and exact-ref evidence;
- DP2 — first production projection and existing-system integration;
- DP3 — controlled rollout;
- DP4 — status-authority discovery and conditional migration;
- DP5 — staged strict lifecycle-gate adoption.

DP1 remains one slice with three internal stages:

1. **Discovery** — read-only factual inventory. It MAY occur in Phase B after DPA-200 is review-ready.
2. **Probe** — bounded compatibility and contract tests. It requires a reviewable DPA-300 or relevant later contract and remains Phase E validation work.
3. **Assessment** — proof-of-architecture conclusion from Discovery and Probe evidence. It remains Phase E work.

DP1 determines document form from evidence. The lab MUST NOT predeclare a production form as verified.

## 17. Required DP1 decision hierarchy

1. Full projection only when complete reconstruction from existing canonical sources is demonstrated.
2. Split projection when current representation and non-canonical history use separate target identities.
3. Managed-head hybrid only as a justified exception with complete partition ownership and workflow serialization.
4. No migration when authority, readers, writers, consumers, compatibility or rollback cannot be established.

No new canonical history source may be introduced for migration convenience.

## 18. Concurrency contract

The DPA MUST distinguish local locking, base/source/target/contract drift, branch concurrency, pull-request concurrency and workflow serialization.

A production refresh captures base SHA, target fingerprint, declared-source fingerprints, renderer and contract identity and reproducibility against the validation ref.

On drift: block new integration, regenerate from the validation ref, never auto-merge historical prose and never treat local locking as cross-PR serialization.

## 19. Stop conditions

Stop and diagnose when:

- required evidence is unavailable;
- normative contracts conflict;
- work would create a parallel governance or runtime subsystem;
- a new runtime authority lacks an accepted decision;
- implementation is claimed from lab evidence;
- production code, mutation or live `.agentic/` state would enter the lab;
- a required maintainer decision is missing;
- work depends on an unresolved earlier contract;
- early Discovery crosses into Probe, Assessment or mutation.

## 20. Current work order

1. Consolidate accepted DPA-200 review amendments.
2. Verify and promote DPA-200 to review-ready when its exit criteria pass.
3. Execute the bounded DP1 Discovery stage under DPA-ADR-015.
4. Synchronize assumptions and exact-ref evidence.
5. Draft DPA-300 from the resulting evidence.
6. Defer DP1 Probe and Assessment until reviewable contracts exist.
