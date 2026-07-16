# DPA-400 Review Adjudication Record

Status: active
Date: 2026-07-16
Primary review ref: `8c9b6892540895e58be53038c6064648d49a2b57`
Primary verdict: `ACCEPT_WITH_CHANGES`

## Maintainer dispositions

### R4-M01 — ACCEPTED

Renderers consume only lifecycle-resolved immutable source values or immutable content-addressed snapshots. They do not open or re-resolve mutable repository paths. A path-like handle is conforming only when it identifies the same immutable bytes that the lifecycle fingerprinted and cannot expose adjacent repository content.

Owned by DPA-ADR-019.

### R4-M02 — ACCEPTED

Resource policy is split into deterministic semantic bounds and host-dependent operational safety aborts. Operational aborts end the attempt as `abandoned`, never become semantic output or fingerprint input and never authorize truncated output.

Owned by DPA-ADR-019.

### R4-M03 — ACCEPTED

The renderer vocabulary has four concepts: renderer identifier, renderer interface version, renderer semantic version and renderer implementation evidence. Only renderer semantic version is output-identity and fingerprint relevant. DPA-100, DPA-300 and DPA-400 must be synchronized.

Owned by DPA-ADR-019.

### R4-M04 — ACCEPTED

Promotion commits are status-only. A normative body changed after verification requires a new qualifying review or an independent exact-ref diff-scoped equivalence verification.

The DPA-300 restructuring in `e3f8b85c5eb76b8c6cae76dde317fd33f236ce88` requires an independent equivalence verification against the last independently certified text. This adjudication does not certify that equivalence.

Owned by DPA-ADR-020.

## Minor and editorial batch

Accepted for synchronized incorporation:

- bounded failure-only diagnostic envelope;
- capability restriction by construction plus deterministic negative-test evidence, with optional Probe-assessed hard isolation;
- explicit invocation identity tuple;
- template/injection-safety requirement and tests;
- ADR-018 indexing and one decision-status vocabulary;
- removal of the open-ended representation-context slot;
- diagram correction for gate/state inputs;
- traceability anchor cleanup;
- fully materialized immutable success output.

## Required change sets

### Change set A — DPA-300 lineage verification

Independent verifier compares the certified pre-promotion DPA-300 text at `a86aa49851c96c39380a8eb4afad17763263fe00` with the promotion restructure at `e3f8b85c5eb76b8c6cae76dde317fd33f236ce88` and reports per-rule equivalence or exact semantic changes.

This change set is verification-only. It must not edit DPA-300.

### Change set B — vocabulary and contract synchronization

After the lineage verification result is recorded:

- DPA-100 registers the renderer identity/version terms and decision-status vocabulary;
- DPA-300 replaces the ambiguous renderer-version field with renderer interface version and renderer semantic version as applicable;
- DPA-400 applies the input, resource, version, failure-envelope and capability rules;
- traceability and diagram are regenerated;
- DECISIONS, STATUS and ROADMAP are synchronized.

### Change set C — post-adjudication verification

A context that did not apply Change set B verifies the exact adjudicated ref. DPA-400 remains `draft` until that verification passes.

## Stability boundary

DPA-400 may be promoted at most to `review-ready` after adjudication verification. It cannot become `stable` before exact-ref renderer-map, input-snapshot, determinism, purity, versioning and lifecycle-integration Probe evidence exists.

## Prohibitions

- No production code in the lab.
- No Probe execution is represented as complete.
- No DPA-300 equivalence is assumed from author intent or incidental sampling.
- No promotion commit may rewrite normative content.