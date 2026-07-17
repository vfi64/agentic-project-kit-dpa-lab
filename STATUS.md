# Status

Status: active
Status-date: 2026-07-17

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is active on branch `spec/dpa-500-freshness-gates`.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300 and DPA-400 are `review-ready`. DPA-500 is `draft`. DPA-400 and DPA-500 remain blocked from `stable` pending applicable exact-ref Probe evidence.

## DP1 Discovery

DP1 Discovery is complete for the explicitly inspected scope at:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed. Global writer-set completeness is not claimed and must be revalidated at Probe time.

No main-repository mutation occurred and no production form was selected.

## DPA-300 lineage closeout

DPA-300 completed primary review, secondary verification, Maintainer adjudication, independent post-adjudication verification and bounded synchronization re-check.

The later review-ready restructure was independently compared against the certified text and received `PASS_WITH_EXPLICIT_RATIFICATION`. The Maintainer ratification record restored the dropped target identity, generic required-field rejection, partition encoding declaration, policy identifiers and normative MUST force; it accepted the enumerated strengthenings and restored Probe and conformance pointers.

DPA-300 remains `review-ready`. Stability remains blocked on applicable DP1 Probe evidence and later governed revalidation.

## DPA-400 closeout

DPA-400 completed primary review, adjudication, governed amendment, independent post-adjudication verification and status-only promotion.

Independent verification at exact ref `6050d0664d9c1ac8bd1a2eb9d6409593046ede9c` returned `PASS` with zero blocking findings. DPA-400 is `review-ready` and was merged through PR #2 at merge commit `7de43fff8debe5c0b9b0c8276a21723d5bc12da6`.

Repository-specific renderer mappings and enforcement mechanisms remain `NEEDS_MAIN_REPO_VALIDATION`; no production implementation, Probe success or main-repository conformance is claimed.

## DPA-500 draft

The first normative DPA-500 draft now defines:

- multidimensional projection freshness rather than time-only freshness;
- acceptance-state validity and trust-state consequences;
- independent contract, source, configuration, renderer, target, partition, gate-set and base-context drift classes;
- structured finding semantics;
- `pass`, `warn`, `block` and fail-closed `error` gate outcomes;
- mandatory mutation and acceptance blockers;
- observe, warn, block-new and strict staged enforcement;
- renderer failure, nondeterminism, side-effect and operational-abort handling;
- complete-target and registered-region freshness behavior;
- interrupted `written-unverified` recovery;
- bounded non-authoritative evidence;
- conformance-test and invalid-state catalogs.

Traceability is recorded in `traceability/DPA-500_TRACEABILITY.md` and the primary flow in `diagrams/dpa-500-freshness-gates.mmd`.

Concrete finding identifiers, severities, acceptance-state schema, strict-adoption switches, gate-set representation and command integration remain `NEEDS_MAIN_REPO_VALIDATION`.

## Probe relationship

PROBE-001 remains governed by DPA-300 and ADR-017. It does not depend on DPA-400 or DPA-500 runtime completion.

DPA-400 requires later exact-ref evidence for static renderer mapping, capability restriction, determinism, renderer versioning and lifecycle integration before `stable`.

DPA-500 requires later exact-ref evidence for findings, severities, acceptance-state persistence, freshness checks, gate integration, recovery and staged strict adoption before `stable`.

Probe fixtures may be prepared during the no-Mac period but must not be represented as executed.

## Next governed step

1. run the durable Lab gates on the DPA-500 draft head;
2. perform an internal cross-artifact audit of DPA-100 through DPA-500;
3. freeze an immutable DPA-500 primary-review baseline;
4. obtain a primary architecture review against that exact ref;
5. adjudicate findings before any promotion beyond `draft`;
6. continue bounded PROBE-001/002 and renderer/freshness fixture preparation without claiming execution.

## Restrictions

- No production code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without adjudication.
- A promotion commit changes status surfaces only and MUST NOT change normative text.

Phase B may continue. The active gate is DPA-500 internal consistency and primary-review readiness.
