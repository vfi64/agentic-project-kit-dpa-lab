# Claude Primary Architecture Review — DPA-400 Renderer Contract

Status: complete
Reviewed ref: `8c9b6892540895e58be53038c6064648d49a2b57`
Reviewer role: Primary Architecture Reviewer under DPA-ADR-012
Verdict: `ACCEPT_WITH_CHANGES`

## Executive assessment

DPA-400 may advance to `review-ready` after adjudication. It MUST NOT become `stable` before applicable exact-ref renderer Probe evidence exists. No blocker, parallel subsystem, new runtime authority, false implementation claim or production-form preselection was found.

## Major findings

### R4-M01 — Renderer input model is ambiguous

DPA-400 permits reading declared canonical sources while also requiring an immutable invocation context sufficient without ambient repository reads. Direct path reopening would create a race between lifecycle fingerprinting and renderer consumption.

Disposition proposed by the reviewer: renderers consume lifecycle-resolved immutable values or content-addressed immutable snapshots. A renderer MUST NOT open, re-read or re-resolve mutable repository paths.

### R4-M02 — Semantic resource bounds and operational aborts are conflated

The draft requires deterministic resource limits while listing wall-clock duration. Wall-clock timeout and host memory pressure are operational, not deterministic semantic inputs.

Disposition proposed by the reviewer: split deterministic contract-declared semantic bounds from operational safety aborts. Operational aborts transition the attempt to `abandoned`, never enter fingerprint domains and never authorize truncated output.

### R4-M03 — Renderer version vocabulary is not closed

DPA-300 uses `renderer contract version`; DPA-400 uses `renderer-version identity`; implementation commit SHA is evidence-only. Their relationship is undefined.

Disposition proposed by the reviewer: define four distinct concepts — renderer identifier, renderer interface version, renderer semantic version and implementation evidence. Only renderer semantic version is output/fingerprint relevant. Synchronize DPA-300 and DPA-100.

### R4-M04 — DPA-300 normative body changed during promotion after verification

The DPA-300 promotion commit restructured and reworded the normative body after the review, adjudication and diff-recheck chain. Sampling found no semantic regression, but the resulting `review-ready` text was not itself independently certified.

Disposition proposed by the reviewer: perform an exact-ref, independent, diff-scoped equivalence verification of the DPA-300 restructuring. Adopt a standing rule that promotion commits change status surfaces only, never normative bodies.

## Minor findings

- R4-m01: define a bounded failure-only diagnostic envelope; success remains payload-only.
- R4-m02: state capability-enforcement tiers: restricted context by construction, deterministic negative tests, optional Probe-assessed hard isolation.
- R4-m03: define the invocation identity/fingerprint tuple rather than use an undefined token.
- R4-m04: add traceability and negative tests for template/injection safety.
- R4-m05: index deferred ADR-018 and register decision statuses.
- R4-m06: remove the open-ended `representation-only context` extension slot.

## Editorial findings

- Regenerate the renderer-boundary diagram with lifecycle state and correct gate inputs.
- Remove the loose DPA-INV-015 anchor from output validation.
- Clarify that success output is fully materialized immutable text/bytes, not a stream.

## Contract audits

- DPA-000 consistency: PASS.
- DPA-100 consistency: PASS with version-vocabulary gaps.
- DPA-200 consistency: PASS.
- DPA-300 substantive consistency: PASS, with R4-M04 lineage debt and R4-M03 token mismatch.
- ADR-003/004/005/013/014/016/017 consistency: PASS subject to the findings above.
- Canonical invariants DPA-INV-001 through DPA-INV-017: no violation found.
- Traceability: structurally complete; add rows for operational aborts, failure diagnostics and template safety.
- Diagram: load-bearing architecture is synchronized; editorial corrections remain.

## Answers to architecture questions

1. Renderer inputs: immutable lifecycle-resolved values or immutable content-addressed snapshots only.
2. Resource policy: semantic deterministic bounds and operational aborts are separate classes.
3. Diagnostics: payload-only on success; bounded non-authoritative diagnostic envelope on failure.
4. Capability isolation: restricted context by construction plus deterministic negative-test evidence; hard isolation is Probe-assessed, not assumed.
5. Version model: identifier, interface version, semantic version and implementation evidence are distinct; only semantic version enters output-related fingerprint domains.

## Internal-audit assessment

The internal audit correctly verified invariant and ADR conformance and correctly identified the input, resource-bound and version tensions. It did not identify the DPA-300 post-verification restructuring, ADR-018 indexing, invocation-identity vocabulary or template-safety traceability gap.

## Required adjudication

1. Accept a renderer input-snapshot rule.
2. Split semantic bounds from operational aborts.
3. Accept and register the four-part renderer identity/version model.
4. Require independent equivalence verification of the DPA-300 promotion restructuring.
5. Apply the minor/editorial batch and regenerate traceability and diagram.
6. Perform post-adjudication verification before promotion.

## Final verdict

`ACCEPT_WITH_CHANGES`

DPA-400 may become `review-ready` after governed adjudication and verification. It MUST NOT become `stable` before exact-ref renderer-map, determinism, purity and lifecycle-integration Probe evidence exists.

This review is non-normative until Maintainer adjudication.