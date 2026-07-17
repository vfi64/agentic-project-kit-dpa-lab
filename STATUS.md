# Status

Status: active

Status-date: 2026-07-17

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is active on branch `spec/dpa-500-freshness-gates`.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300 and DPA-400 are `review-ready`. DPA-500 remains `draft` pending post-adjudication verification. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence.

## DP1 Discovery

DP1 Discovery is complete for the explicitly inspected scope at:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed. Global writer-set completeness is not claimed and must be revalidated at Probe time.

No main-repository mutation occurred and no production form was selected.

## DPA-300 lineage and bounded amendment

DPA-300 completed primary review, secondary verification, Maintainer adjudication, independent post-adjudication verification and bounded synchronization re-check.

The later review-ready restructure was independently compared against the certified text and received `PASS_WITH_EXPLICIT_RATIFICATION`. The Maintainer ratification record restored the dropped target identity, generic required-field rejection, partition encoding declaration, policy identifiers and normative MUST force; it accepted the enumerated strengthenings and restored Probe and conformance pointers.

DPA-300 remains `review-ready`. ADR-021 now adds a bounded synchronized amendment for conditional accepted-base persistence and layered post-acceptance comparison of registered-region projections. This amendment must be included in the DPA-500 post-adjudication verification before DPA-500 promotion. DPA-300 stability remains blocked on applicable DP1 Probe evidence and later governed revalidation.

## DPA-400 closeout

DPA-400 completed primary review, adjudication, governed amendment, independent post-adjudication verification and status-only promotion.

Independent verification at exact ref `6050d0664d9c1ac8bd1a2eb9d6409593046ede9c` returned `PASS` with zero blocking findings. DPA-400 is `review-ready` and was merged through PR #2 at merge commit `7de43fff8debe5c0b9b0c8276a21723d5bc12da6`.

Repository-specific renderer mappings and enforcement mechanisms remain `NEEDS_MAIN_REPO_VALIDATION`; no production implementation, Probe success or main-repository conformance is claimed.

## DPA-500 review and adjudication

The immutable primary-review baseline was:

`60d6457f0473365789ece4f885a48ea5320b01ff`

Claude's primary architecture review returned `ACCEPT_WITH_CHANGES` with three majors, four minors and three editorial findings.

All findings were accepted. The Maintainer selected:

- operation-scoped base context with conditional accepted-base persistence;
- lifecycle-owned gate-set re-evaluation and re-acceptance without renderer invocation or target mutation;
- layered acceptance for registered-region projections.

ADR-021 records these decisions. The governed amendment batch synchronizes:

- `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`;
- `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`;
- `traceability/DPA-500_TRACEABILITY.md`;
- `diagrams/dpa-500-freshness-gates.mmd`;
- `decisions/DPA-ADR-021-FRESHNESS-REACCEPTANCE-AND-LAYERED-ACCEPTANCE.md`.

The amended DPA-500 contract now defines:

- multidimensional derivational freshness with time excluded as sole failure authority;
- clean separation of freshness classification, consumer trust state, drift class, finding subreason, gate decision and enforcement stage;
- operation-scoped base-context evaluation;
- conditional accepted-base persistence only for declared base dependence;
- mutation-free gate-set re-acceptance through the existing lifecycle and gate authority;
- layered post-acceptance freshness for registered-region projections;
- complete-target and preserved-region fingerprints retained as plan, write, verification and recovery guards;
- authorized declared non-lifecycle-owner evolution distinguished from out-of-band lifecycle-byte mutation;
- fail-closed behavior for ambiguous ownership, unavailable evaluation and persistence failure;
- identity-critical gate evidence fields as mandatory;
- expanded conformance and invalid-state catalogs.

DPA-500 remains `draft`. No review-ready, implementation, Probe-success or main-repository-conformance claim is made.

## Probe relationship

PROBE-001 remains governed by DPA-300 and ADR-017. It does not depend on DPA-400 or DPA-500 runtime completion.

DPA-400 requires later exact-ref evidence for static renderer mapping, capability restriction, determinism, renderer versioning and lifecycle integration before `stable`.

DPA-500 requires later exact-ref evidence for findings, severities, conditional base persistence, re-acceptance, ownership provenance, layered freshness, gate integration, recovery and staged strict adoption before `stable`.

Probe fixtures may be prepared during the no-Mac period but must not be represented as executed.

## Next governed step

1. run the durable Lab gates on the complete amendment head;
2. perform an internal post-adjudication consistency audit across DPA-100, DPA-300, DPA-400, DPA-500, ADR-021, traceability and diagram;
3. freeze an immutable DPA-500 amendment ref;
4. obtain independent post-adjudication verification against that exact ref;
5. disposition any verification findings;
6. only after a zero-blocker verification result, promote DPA-500 through a separate status-only commit.

## Restrictions

- No production code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without adjudication.
- A promotion commit changes status surfaces only and MUST NOT change normative text.

Phase B may continue. The active gate is DPA-500 post-adjudication consistency and independent verification readiness.
