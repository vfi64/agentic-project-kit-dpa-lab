# DPA-400 Pre-Review Architecture Audit

Status: complete
Status-date: 2026-07-16
Audited branch: `spec/dpa-400-renderer-contract`
Result: `PASS_WITH_REVIEW_QUESTIONS`

## 1. Scope

This audit checks:

- `specs/dpa/DPA-400-RENDERER-CONTRACT.md`;
- `traceability/DPA-400_TRACEABILITY.md`;
- `diagrams/dpa-400-renderer-boundary.mmd`;
- consistency with DPA-000 through DPA-300 and accepted ADRs;
- invariant, authority, failure-mode, traceability and later-owner boundaries.

The audit is internal and non-normative. It does not replace primary review.

## 2. Executive result

No foundational contradiction was found.

The draft:

- extends the existing registry/lifecycle architecture rather than creating a renderer subsystem;
- preserves the renderer/lifecycle/workflow boundary;
- keeps renderers side-effect-free and payload-only;
- uses static, fail-loud resolution;
- preserves one invocation / one registered target;
- does not assign acceptance or gate authority to renderers;
- does not claim current main-repository conformance;
- correctly limits pre-Probe maturity to `review-ready`.

Two cross-section tensions and five bounded review questions remain. They do not block primary review.

## 3. Authority-owner audit

| Concern | Normative owner | DPA-400 result |
|---|---|---|
| renderer identity and static resolution | DPA-400 | PASS |
| renderer inputs and configuration | DPA-400 | PASS WITH Q1 |
| payload return contract | DPA-400 | PASS |
| registry serialization | DPA-300 | correctly delegated |
| plan, lock, write and recovery | DPA-300 | correctly delegated |
| findings, severity, gates and acceptance | DPA-500 | correctly delegated |
| cross-ref serialization | DPA-600 | correctly delegated |
| migration and rollback | DPA-700 | correctly delegated |

No competing authority owner was found.

## 4. Canonical-invariant audit

| Invariant | Result | Basis |
|---|---|---|
| DPA-INV-001 | PASS | canonical state does not contain renderer logic; inputs are declared |
| DPA-INV-002 | PASS | renderers cannot write |
| DPA-INV-003 | PASS | renderer boundary returns text or immutable bytes |
| DPA-INV-004 | PASS / delegated | lifecycle remains sole writer |
| DPA-INV-005 | PASS / delegated | renderer has no serialization authority |
| DPA-INV-006 | PASS | registry contains declarative identifiers only |
| DPA-INV-007 | PASS | identifiers resolve through closed reviewed code |
| DPA-INV-008 | PASS | exactly one target per invocation |
| DPA-INV-009 | PASS | no renderer chaining |
| DPA-INV-010 | PASS | evidence and prior targets are not semantic inputs |
| DPA-INV-011 | PASS | runtime contracts remain in existing registry/lifecycle |
| DPA-INV-012 | PASS | no parallel renderer command or subsystem |
| DPA-INV-013 | PASS / delegated | no time-based gate rule introduced |
| DPA-INV-014 | PASS | no historical merge or target fallback |
| DPA-INV-015 | PASS / delegated | plan capture remains DPA-300-owned |
| DPA-INV-016 | PASS / delegated | concrete paths remain Probe-fenced |
| DPA-INV-017 | PASS | implementation claims remain `NEEDS_MAIN_REPO_VALIDATION` |

## 5. Decision audit

The draft is consistent with:

- ADR-003: renderer/lifecycle/workflow separation;
- ADR-004: derivational reproducibility;
- ADR-005: static fail-loud resolution;
- ADR-013 and ADR-017: lifecycle ownership of partition bytes and parent-entry partition contract;
- ADR-014: renderer success does not assign acceptance;
- ADR-016: acceptance state remains lifecycle state and is not a renderer input.

No decision change is proposed by the draft.

## 6. Cross-artifact tensions

### Q1 — Resolved values versus renderer-owned source reads

DPA-400 §4 says a renderer `MAY read declared canonical sources`, while §6 requires an invocation context sufficient to compute output without ambient repository reads and §7 says the lifecycle resolves and fingerprints sources before invocation.

These statements can be reconciled only if "read" means "consume immutable source values or bounded source handles already resolved by the lifecycle". If it means opening repository paths directly, the capability boundary is weaker and source identity may race between lifecycle fingerprinting and renderer access.

Recommended disposition: make the renderer consume lifecycle-resolved immutable values or content-addressed snapshots. If bounded paths remain permitted, define who opens them and how post-resolution mutation is excluded.

### Q2 — Deterministic limits versus operational timeouts

DPA-400 §15 says every resource limit is deterministic while listing execution duration. Size, recursion and memory-policy inputs can be deterministic; wall-clock timeout firing can vary by host load.

Recommended disposition: separate semantic deterministic bounds from operational safety timeouts. A timeout may abort an attempt and produce no accepted output, but timeout occurrence must not become a semantic renderer result or reproducibility input.

## 7. Failure-mode audit

Covered and fail-loud:

1. unknown or ambiguous renderer identifier;
2. executable or dynamic renderer reference;
3. undeclared semantic input;
4. ambient repository discovery;
5. invalid source or configuration;
6. invalid output type or encoding;
7. disallowed empty output;
8. partition bytes in a region payload;
9. manual or historical bytes in output;
10. target/evidence/history fallback;
11. nondeterministic output;
12. filesystem, state or registry mutation;
13. lock, subprocess, network or workflow access;
14. renderer chaining;
15. multi-target output;
16. renderer-version mismatch;
17. fallback renderer selection;
18. resource-bound failure;
19. renderer success represented as acceptance.

Open review questions:

### Q3 — Diagnostics channel

The renderer returns exactly one payload and must not emit evidence or findings. The contract does not say whether structured non-authoritative diagnostics may accompany a failure or whether only an exception/result envelope is allowed. A diagnostics channel must not become a second semantic output, target or evidence authority.

### Q4 — Side-effect enforcement level

The contract requires prevention or detection of file, network, subprocess and lock side effects but leaves the mechanism Probe-fenced. Review should assess whether architecture conformance requires capability restriction by construction, post-hoc detection, or either with equivalent negative evidence.

### Q5 — Renderer-version identity

The renderer version must change for output-affecting implementation changes, while a raw HEAD is insufficient. Review should assess whether the contract needs an explicit relation among canonical identifier, semantic version, implementation fingerprint and source commit evidence, or whether DPA-300 fingerprints plus Probe evidence are enough.

## 8. Traceability audit

RC-001 through RC-019 contain:

- invariant and ADR anchors;
- DPA-300 dependency;
- tests or Probe obligations;
- DPA-500 gate ownership;
- evidence obligation;
- rollback consequence.

The invalid-state catalog covers twenty renderer defects.

Potential additions after review:

- a requirement for immutable/content-addressed resolved source values, depending on Q1;
- an explicit operational-timeout test distinct from deterministic semantic bounds, depending on Q2;
- a diagnostics-envelope requirement, depending on Q3.

No false implementation claim was found.

## 9. Diagram audit

The diagram correctly shows:

- existing registry and lifecycle;
- closed renderer map;
- lifecycle-resolved sources and configuration;
- one renderer invocation;
- one payload;
- lifecycle-owned plan and target mutation;
- parent partition ownership;
- DPA-500 gate ownership.

The negative edges correctly prohibit writes, partition bytes, locks/workflow orchestration, evidence/acceptance-state access and renderer chaining.

Review should check whether the edge from declared sources to lifecycle plus lifecycle to renderer sufficiently communicates the Q1 snapshot boundary.

## 10. Review-baseline recommendation

Result: `PASS_WITH_REVIEW_QUESTIONS`.

The draft is suitable for an immutable primary architecture review baseline. Claude should independently verify rather than trust this audit, with special attention to Q1 through Q5 and to cross-artifact vocabulary/ownership residue.

DPA-400 remains `draft`. It may not become `stable` before exact-ref renderer-map, purity, determinism and lifecycle-integration Probe evidence exists.