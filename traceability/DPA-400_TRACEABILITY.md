# DPA-400 Traceability

Status: draft
Status-date: 2026-07-16

## 1. Requirement matrix

| ID | Requirement | Invariants / decisions | DPA-300 dependency | Planned tests / Probe | DPA-500 gate obligation | Evidence obligation | Rollback consequence |
|---|---|---|---|---|---|---|---|
| RC-001 | Renderer identifiers resolve through one closed static mapping. | DPA-INV-006, DPA-INV-007; ADR-005 | validated renderer identifier and version | known/unknown/duplicate identifier tests; renderer-map Probe | unknown or ambiguous renderer blocks plan | resolved canonical identifier and map version | restore prior mapping/contract version |
| RC-002 | Registry data cannot select executable code or dynamic imports. | DPA-INV-006, DPA-INV-007; ADR-005 | fail-loud registry validation | import-path, URL, shell and expression negatives | executable metadata blocks use | rejected field and validator result | remove invalid metadata |
| RC-003 | Renderer receives only declared sources and contract-declared configuration. | DPA-INV-001, DPA-INV-010; ADR-003, ADR-004 | lifecycle resolves and fingerprints inputs before invocation | undeclared-input and ambient-discovery negatives | undeclared input blocks acceptance | ordered source/config identities and fingerprints | regenerate from declared authorities |
| RC-004 | Renderer returns text or immutable bytes only. | DPA-INV-002, DPA-INV-003; ADR-003 | lifecycle owns planning and writing | return-type positives and negatives | invalid return blocks plan | return type and output fingerprint | no target mutation |
| RC-005 | One invocation computes exactly one registered target. | DPA-INV-008 | one target identity per contract and plan | multi-target and inferred-target negatives | multi-target output blocks plan | target identity and invocation transcript | split into independent contracts/plans |
| RC-006 | Renderer never invokes another renderer. | DPA-INV-009 | lifecycle/workflow owns orchestration | call-graph and nested-invocation negatives | chaining blocks use | invocation boundary record | independent governed refreshes |
| RC-007 | Renderer performs no target, state, evidence or acceptance-state writes. | DPA-INV-002, DPA-INV-004, DPA-INV-010; ADR-003, ADR-016 | lifecycle sole-writer and state owner | filesystem/state mutation negatives | side effect blocks acceptance and strict integration | capability violation record | restore prior target/state; abandon attempt |
| RC-008 | Renderer acquires no locks and starts no mutation workflow. | DPA-INV-004, DPA-INV-005; ADR-003, ADR-006 | DPA-300 owns local mutation lock | lock/subprocess/workflow negatives | violation blocks plan | attempted capability and failure result | abandon attempt |
| RC-009 | Identical governed inputs yield byte-equivalent output. | ADR-004 | source/contract/renderer fingerprints anchor the plan | repeated and fresh-process determinism tests | nondeterminism blocks acceptance | input fingerprint set and repeated outputs | retain prior accepted version; revert renderer |
| RC-010 | Ambient time, randomness, environment, platform and enumeration order cannot affect output unless declared. | ADR-004 | contract fingerprint covers declared representation context | perturbation matrix tests | unexplained output variance blocks acceptance | environment matrix and output hashes | declare/version input or remove dependency |
| RC-011 | Region renderers return payload bytes only and never partition bytes. | DPA-INV-003, DPA-INV-008; ADR-013, ADR-017 | parent-entry PartitionContract reconstructs parent | marker/boundary injection negatives | partition-byte output blocks plan | payload and partition fingerprints | reject payload; preserve prior target |
| RC-012 | Complete-target renderers do not use prior target bytes as semantic input. | DPA-INV-001, DPA-INV-010; ADR-004 | DPA-300 direct-write and drift model | prior-target perturbation test | target-derived output blocks acceptance | source/input audit | regenerate solely from canonical sources |
| RC-013 | Renderer version is stable and fingerprinted. | ADR-004, ADR-005 | plans and acceptance state capture renderer identity/version | version-change invalidates-plan tests | stale renderer version blocks write/acceptance | implementation version and plan fingerprint | restore prior renderer or regenerate plan |
| RC-014 | Invalid or empty output fails before plan capture when disallowed. | DPA-INV-004, DPA-INV-015 | Render precedes immutable Plan | invalid-type, encoding, normalization and empty-output tests | invalid output blocks plan | validation result | no mutation |
| RC-015 | Renderer failure never selects a fallback renderer automatically. | DPA-INV-007; ADR-005 | failed attempt becomes abandoned | fallback-chain negative | fallback attempt blocks use | requested/resolved identifier and failure | explicit reviewed contract change only |
| RC-016 | Renderer success never assigns accepted state. | DPA-INV-004; ADR-014 | DPA-300 produces at most computed/plan-captured/written-unverified | privilege-boundary test | DPA-500 alone accepts | trust-transition record | remain non-accepted |
| RC-017 | Existing command paths invoke renderers only through the lifecycle. | DPA-INV-011, DPA-INV-012; ADR-001, ADR-003 | command adaptation contract in DPA-300 | observed-writer integration Probe | bypass blocks strict integration | command→lifecycle→renderer trace | revert adapter without parallel writer |
| RC-018 | Resource-bound failure never emits truncated accepted output. | ADR-004 | lifecycle validates output before plan | size/time/memory bound tests | resource failure blocks plan | resource policy and failure result | keep prior accepted target |
| RC-019 | Repository-specific mapping and enforcement claims remain exact-ref fenced. | DPA-INV-017; ADR-011, ADR-015 | Probe stage supplies compatibility evidence | classification audit | unsupported claim blocks promotion/stability | exact-ref Probe record | return claim to NEEDS_MAIN_REPO_VALIDATION |

## 2. Invalid-state test catalog

A conforming implementation MUST reject:

1. unknown, duplicate or ambiguous renderer identifiers;
2. executable import paths, URLs, commands or expressions in registry data;
3. dynamic plugin discovery or environment-dependent resolution;
4. renderer invocation before registry and input validation;
5. undeclared source access or repository traversal;
6. use of prior target, evidence, history or acceptance state as semantic fallback;
7. output depending on undeclared time, randomness, locale, environment or platform;
8. mutable global state changing semantic output;
9. file, registry, lifecycle-state, evidence or acceptance-state writes;
10. lock acquisition, subprocess execution or network access;
11. nested renderer invocation;
12. multi-target output;
13. partition bytes in region payload;
14. bytes owned by manual or historical regions in renderer output;
15. invalid return type or encoding;
16. disallowed empty output;
17. silent fallback renderer selection;
18. renderer-version drift ignored by plan validation;
19. renderer success represented directly as accepted;
20. truncated output accepted after a resource-limit failure.

## 3. Probe boundary

DPA-400 is reviewable without executing a main-repository Probe.

Before `stable`, exact-ref evidence MUST establish:

- a feasible static renderer mapping in the real repository;
- a bounded callable/capability surface;
- deterministic output for selected renderer fixtures;
- enforcement or reliable detection of prohibited side effects;
- renderer-version integration with DPA-300 plans and acceptance state;
- integration through existing lifecycle and command paths without a parallel renderer subsystem.

PROBE-001 remains owned by DPA-300 and ADR-017; it does not depend on DPA-400 beyond using a syntactically plausible renderer identifier in registry fixtures.

## 4. Later ownership

- DPA-500 owns concrete findings, severity, staged gates and acceptance consequences.
- DPA-600 owns cross-ref serialization around renderer-derived plans.
- DPA-700 owns rollback when renderer versions change or disappear.
- DPA-800 owns exact DP2 implementation and Probe recipes.

No item in this artifact claims current implementation conformance.
