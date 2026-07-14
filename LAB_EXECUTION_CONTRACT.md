# DPA Lab Execution Contract

Status: active
Status-date: 2026-07-14
Superseded-by: n/a

## 1. Purpose

This contract defines how work in `vfi64/agentic-project-kit-dpa-lab` must be planned, reviewed, committed, consolidated and transferred back to `vfi64/agentic-project-kit`.

The lab is a governed architecture workspace. It is not a scratchpad, not a prompt archive and not a second implementation repository.

## 2. Primary objective

Produce a complete, coherent, reviewable and implementation-ready Document Projection Architecture that extends the existing document-management architecture of `agentic-project-kit`.

The final lab output must include:

- normative DPA specifications DPA-000 through DPA-900,
- accepted architecture decisions,
- explicit assumptions and validation requirements,
- diagrams,
- traceability from goals to contracts, DP1–DP5, tests and gates,
- a main-repository validation checklist,
- a controlled import plan,
- a final implementation contract for DP1–DP5.

## 3. Non-goals

The lab must not:

- contain production kit code,
- act as a runtime dependency,
- replace the main repository's Direction, registry, lifecycle or evidence,
- fabricate repository facts,
- record model consensus as implementation evidence,
- create live `.agentic/` state before the agreed adoption phase,
- import private repository state or secrets,
- execute P5c or other maintainer-gated work,
- silently expand DPA into a general template or plugin framework.

## 4. Language and style

- Chat communication: German, concise, direct and evidence-based.
- Normative specifications: English.
- Machine-readable artifacts: English.
- Diagram labels: English unless a compelling review reason exists.
- Normative words `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and `MAY` shall be used consistently.
- Avoid vague terms such as `current`, `latest`, `safe` or `substantive` unless their authority and derivation are defined.

## 5. Required session bootstrap

Every new session must follow `LAB_BOOTSTRAP.md` and read all mandatory files before work.

After reading, the session must state:

- exact lab repository/ref,
- active phase,
- current task,
- normative inputs,
- unresolved decisions,
- main-repository evidence used,
- whether work is unblocked.

No session may start from chat memory alone.

## 6. Status vocabulary

Use the following meanings:

### VERIFIED

Supported by an exact repository ref and reproducible evidence.

### ASSUMPTION

A working belief not yet validated against the relevant authoritative source.

### NORMATIVE

A rule or requirement adopted by the lab governance.

### PROPOSAL

A candidate design not yet accepted.

### REJECTED

A considered alternative that has been explicitly declined, with rationale.

### NEEDS_MAIN_REPO_VALIDATION

A repository-specific claim or decision that cannot become normative implementation guidance until checked against a fresh main repository.

## 7. Architecture invariants

The following constraints are binding across the complete DPA series:

1. Canonical state never owns rendering logic.
2. Renderers never own write logic.
3. Renderers return text or bytes only.
4. The document lifecycle validates projection contracts, plans changes, acquires the mutation lock and performs writes.
5. Workflow orchestration serializes across branches and pull requests.
6. The documentation registry describes contracts; it does not name arbitrary executable imports.
7. Renderer identifiers resolve through static, reviewed code.
8. A renderer reads declared canonical sources and computes exactly one registered target.
9. A renderer never triggers another renderer.
10. Evidence is never runtime authority.
11. Lab decision artifacts are planning evidence, not production truth.
12. The final runtime projection contract belongs only in the main repository's existing registry/lifecycle system.
13. No parallel registry, lifecycle, freshness, evidence, workspace or gate subsystem may be introduced.
14. Time-based findings never become hard failures merely because wall-clock time elapsed.
15. Append-only historical prose is never automatically merged during drift recovery.
16. Dry-run is the default for mutations.
17. All production paths must eventually resolve through the main repository's Workspace abstraction.

Any normative document that contradicts an invariant is invalid until reconciled.

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

A later document may be drafted early, but it cannot become stable while contradicting or bypassing an earlier contract.

## 9. Phase model

### Phase A — Foundation

Scope:

- DPA-000,
- DPA-100,
- glossary,
- architectural invariants,
- initial traceability,
- first review baseline.

Exit criteria:

- terminology is internally coherent,
- no hidden parallel system is implied,
- main-repository claims are classified,
- Claude, ChatGPT and Gemini review prompts exist or are planned,
- accepted decisions are recorded.

### Phase B — Core document-management integration

Scope:

- DPA-200,
- DPA-300,
- DPA-400,
- DPA-500.

Exit criteria:

- document types and authority are defined,
- optional registry extension is specified,
- renderer boundary is specified,
- lifecycle/freshness/gate integration is specified,
- backwards compatibility and fail-loud behavior are defined,
- no second registry or audit is required.

### Phase C — Operational completion

Scope:

- DPA-600,
- DPA-700,
- DPA-800,
- DPA-900.

Exit criteria:

- Git/PR concurrency contract is complete,
- migration and rollback are complete,
- DP1–DP5 is implementation-ready,
- future work is clearly out of scope,
- traceability is complete.

### Phase D — Lab adoption by the kit

Preconditions:

- DPA-000 through DPA-500 are stable,
- governance and bootstrap are stable,
- adoption will not contaminate the main repository or create circular authority,
- current kit behavior has been freshly inspected.

The lab may then be adopted as an external repository test. Adoption must remain reversible and must not make lab state authoritative for the main repository.

### Phase E — Main-repository validation and implementation

Scope:

- execute DP1 against fresh main,
- correct assumptions,
- update DPA when evidence requires it,
- implement DP2–DP5 in the main repository,
- import only approved normative artifacts.

## 10. Review workflow

Reviews are stored separately under:

- `reviews/chatgpt/`
- `reviews/claude/`
- `reviews/gemini/`
- `reviews/consolidated/`

Each model review must record:

- reviewed commit/ref,
- reviewed files,
- model/version when known,
- accepted findings,
- rejected findings,
- unresolved findings,
- repository facts requiring validation,
- proposed normative changes.

A review is not normative.

The consolidation process is:

1. collect review,
2. classify each finding,
3. verify internal consistency,
4. identify main-repository dependencies,
5. record accepted/rejected decisions,
6. update normative documents,
7. update traceability,
8. commit with a summary of incorporated findings.

No model may write directly into normative meaning without adjudication.

## 11. Decision process

Architecture decisions are recorded in `DECISIONS.md` or later dedicated ADR files.

Every accepted decision must include:

- identifier,
- status,
- context,
- decision,
- alternatives considered,
- rationale,
- consequences,
- validation status,
- affected DPA documents,
- affected future DP slices.

Decisions requiring main-repository facts remain provisional or `NEEDS_MAIN_REPO_VALIDATION` until evidence exists.

## 12. Traceability contract

The lab must maintain traceability among:

- motivation/problem statements,
- architecture invariants,
- normative requirements,
- decisions,
- candidate main-repository modules,
- DP1–DP5 work items,
- required tests,
- required gates,
- evidence and rollback requirements.

Traceability must distinguish:

- normative requirement,
- planned implementation,
- verified implementation,
- future extension.

No table may label planned implementation as completed.

## 13. Commit and branch rules

Before kit adoption, the lab may use simple GitHub branches and PRs.

Recommended branch families:

- `spec/dpa-000-vision`
- `spec/dpa-100-foundations`
- `spec/dpa-registry-lifecycle`
- `spec/dpa-concurrency`
- `review/claude-*`
- `review/chatgpt-*`
- `review/gemini-*`
- `consolidation/dpa-*`

Each coherent change should:

- update only relevant files,
- avoid mixed unrelated edits,
- update `STATUS.md` when the active phase or next action changes,
- update `DECISIONS.md` when a decision changes,
- update `ASSUMPTIONS.md` when a repository claim changes classification,
- include review context in the commit or PR description.

A commit message must describe the architectural change, not merely say `update docs`.

## 14. Completion semantics

A document is not complete merely because prose exists.

### Draft

- structure exists,
- major concepts identified,
- unresolved issues visible.

### Review-ready

- terminology consistent,
- alternatives recorded,
- traceability started,
- repository assumptions classified.

### Stable

- required reviews adjudicated,
- no known contradiction with earlier stable DPA contracts,
- decisions recorded,
- traceability complete for its scope,
- no unresolved blocker hidden in prose.

### Adopted

- validated against a fresh main repository,
- accepted into the main repository through governed PRs,
- runtime contracts live only in the main repository.

The lab itself never upgrades an implementation to `verified complete` without main-repository evidence.

## 15. Main-repository fact handling

When a specification needs a repository fact:

1. add or locate an assumption ID,
2. identify the exact required evidence,
3. fetch/inspect an exact ref when possible,
4. store a concise evidence record under `evidence/repo-facts/`,
5. update `ASSUMPTIONS.md`,
6. update `MAIN_REPOSITORY_CONTEXT.md` if the fact changes subsequent work.

Model agreement is not evidence.

## 16. DP1–DP5 relationship

The lab prepares the normative specification. The main repository later executes:

- DP1: proof-of-architecture and evidence against fresh main,
- DP2: first production projection and existing-system integration,
- DP3: controlled rollout to additional handoff/bootstrap documents,
- DP4: status authority discovery and conditional migration,
- DP5: staged strict adoption in the existing lifecycle gate.

DP1 must decide document form from evidence. The lab must not predeclare Fall A, B or C as a verified outcome.

## 17. Required DP1 decision hierarchy

The implementation plan shall preserve this preference:

1. Full projection only when complete content is already reconstructable from existing canonical sources.
2. Split current projection and historical evidence when historical prose is not canonical.
3. Managed head plus append history only as a justified exception with complete workflow serialization.

No new canonical history database or log may be introduced merely to make a migration convenient.

## 18. Concurrency contract

The normative DPA must distinguish:

- local mutation locking,
- repository/branch drift,
- pull-request concurrency,
- workflow serialization.

A production refresh must eventually capture and verify:

- base SHA,
- target-region hash or full-target hash,
- declared source hashes,
- reproducibility against fresh `origin/main`.

On drift:

- block,
- regenerate from fresh main,
- do not auto-merge historical prose,
- do not treat local locking as cross-PR serialization.

## 19. Stop conditions

Stop and produce a bounded diagnosis when:

- required evidence is unavailable,
- normative documents conflict,
- the work would create a parallel governance subsystem,
- a new runtime truth source is being introduced without accepted authority,
- an implementation claim is requested in the lab,
- production code would be added to the lab,
- a review cannot be adjudicated because a maintainer decision is required,
- the current task depends on an unresolved earlier DPA contract.

## 20. Current work order

The next session shall:

1. complete bootstrap reading,
2. inspect the current lab structure,
3. expand DPA-000 into a complete vision and principle contract,
4. create DPA-100 with normative terminology,
5. create initial traceability artifacts,
6. create a Claude Fable 5 review prompt,
7. commit work in coherent reviewable units,
8. update `STATUS.md` and decisions as appropriate.

Continue without routine questions. Ask only when a genuine maintainer decision or stop condition applies.
