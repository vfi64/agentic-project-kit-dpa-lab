# Semantic Authority Efficiency Integration Plan

Status: proposed

Status-date: 2026-07-19

Classification: PROPOSAL

Governing review: `reviews/2026-07-19-SEMANTIC_AUTHORITY_EFFICIENCY_REVIEW.md`

## 1. Purpose

This plan integrates the useful part of the semantic-authority proposal into the active DPA work without adding DPA-150, DPA-160, a semantic-fact registry, a second lifecycle or a parallel dependency system.

The objective is practical improvement:

- make writer and command analysis authority-aware;
- reduce independently maintained representations of the same repository-backed facts;
- enable later impact-scoped regeneration and verification where completeness can be proven;
- reduce review cost without weakening safety or evidence discipline.

## 2. Governing constraints

This plan MUST:

- preserve DPA-000 as the sole invariant owner;
- preserve DPA-100 as the sole foundational vocabulary owner;
- preserve the DPA-000 through DPA-900 sequence;
- reuse the existing documentation registry, lifecycle, Workspace, findings, gates and evidence systems;
- remain non-normative until adjudicated;
- avoid DPA-300 through DPA-500 amendments before Probe evidence establishes a bounded need;
- leave DPA-600 frozen and DPA-700 prohibited under the current work order;
- keep main-repository writer and lifecycle mutation frozen before PROBE-002 adjudication.

## 3. Minimal analytical model

The plan uses one bounded analytical relationship:

```text
canonical source set
        -> governed fact set
        -> authorized mutation operating mode
        -> affected projection target set
        -> lifecycle-owned verification
```

`governed fact set` is an analysis label, not a new runtime object, status namespace, registry entry or authority store.

## 4. Package-M integration

### M-SA-01 — Extend the remote writer and command inventory template

For every discovered document-mutating command operating mode, record:

- command and operating mode;
- target path or registered target identity;
- current writer symbol;
- current writer owner;
- declared or inferred canonical source set;
- governed fact-set description;
- affected projection targets;
- current verification behavior;
- ambiguity or incompleteness;
- evidence ref and source location.

Outcome values for authority analysis:

- single governed authority observed;
- multiple representations, one authority observed;
- competing writer authority suspected;
- competing writer authority confirmed;
- authority not established;
- verification blocked.

This vocabulary is local to the inventory and MUST NOT be reused as document status, progress status, trust state or architecture classification.

### M-SA-02 — Add Probe metadata without changing Probe subjects

PROBE-001 fixture preparation SHOULD annotate:

- which declared sources own the tested fact set;
- which target or registered region represents it;
- whether schema rejection prevents ambiguous authority.

PROBE-002 fixture preparation SHOULD annotate:

- which command operating mode initiates the mutation;
- which fact set is intended to change;
- which projection targets are expected to become stale or be regenerated;
- which lifecycle phase owns post-write verification;
- which ambiguity must fail closed.

The annotations are evidence metadata only. They MUST NOT alter the parser, lifecycle, writer, acceptance or gate baseline under test.

### M-SA-03 — Define the no-parallel-system proof obligation

Every future semantic-impact proposal MUST answer:

1. Which existing registry field or accepted extension owns the relationship?
2. Which existing lifecycle phase consumes it?
3. Which existing finding and gate surfaces report failures?
4. Which existing evidence surface records execution?
5. Why is no additional state store or dependency database required?
6. How is incomplete dependency coverage detected and made fail loud?

A proposal that cannot answer all six questions remains blocked.

### M-SA-04 — Define measurable improvement criteria

A later implementation candidate must establish a baseline and target for at least one metric:

- number of independent writer paths for the same governed fact set;
- number of manual synchronization points across projections;
- number of writer-specific exceptions;
- number of projections regenerated for a bounded source change;
- number of gates executed for a bounded source change;
- review effort required to identify semantic impact;
- count of synchronization defects detected by existing audits.

Selective execution is permitted only when dependency completeness and fallback behavior are proven. Otherwise the full existing regeneration and gate path remains mandatory.

## 5. Later specification mapping

### DPA-300

Potential future bounded clarification only if Probe evidence shows that projection contracts require an explicit authority-scope or dependency identifier. No amendment is authorized by this plan.

### DPA-400

No semantic-authority extension is currently required. Renderers already consume declared sources and must not invent canonical facts.

### DPA-500

Potential future impact-scoped freshness or gate optimization only if complete dependencies can be derived through existing accepted contracts. Unknown or incomplete dependency coverage MUST select the full verification path.

### DPA-800

Primary planned home for implementation mapping:

- complete command operating-mode inventory;
- complete writer inventory;
- canonical source-set mapping;
- authorized mutation path;
- affected projection mapping;
- lifecycle and verification ownership;
- migration of unauthorized direct writers.

### DPA-900

Primary planned home for review-economics evaluation:

- semantic impact summaries;
- risk-based selective verification;
- equivalence proof obligations;
- measurable review-cost reduction;
- mandatory fallback to full verification.

## 6. Stop conditions

Stop and diagnose when:

- a fact-set label would become a second runtime identity system;
- a dependency map would require a parallel registry or maintained mirror;
- selective regeneration or gates are proposed without completeness proof;
- command authority conflicts with the existing rule-registry or command-governance system;
- a new status or lifecycle vocabulary is introduced;
- the work would mutate a frozen writer, lifecycle, acceptance or gate path before PROBE-002 adjudication;
- a normative DPA-300 through DPA-500 amendment is attempted without the established adjudication and independent-verification path.

## 7. Deliverables

The bounded remote-preparation deliverables are:

1. an authority-aware writer and command operating-mode inventory;
2. authority and affected-projection annotations in the prepared Probe fixtures;
3. a no-parallel-system proof for each later implementation proposal;
4. baseline metrics for at least one measurable efficiency improvement;
5. a disposition record after Probe adjudication:
   - no normative change required;
   - bounded clarification required;
   - implementation-only mapping required;
   - proposal rejected because benefit or completeness was not proven.

## 8. Completion criterion

This plan is successful only if it produces a smaller, clearer or mechanically safer implementation and review path.

It is not successful merely because additional concepts, documents or metadata were created.
