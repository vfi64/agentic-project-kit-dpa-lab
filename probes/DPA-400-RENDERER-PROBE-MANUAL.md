# DPA-400 Renderer Probe Manual

Status: draft

Status-date: 2026-07-19

Consumes: `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`

Fixture manifest: `probes/DPA-400-RENDERER-FIXTURE-MANIFEST.md`

Governing architecture: DPA-400 and its accepted ADR dependencies

Execution-state: not run

## 1. Purpose

This Probe measures exact-ref renderer resolution, invocation, determinism, purity, output validation, version behavior, failure boundaries and lifecycle separation.

It does not test target writing, acceptance-state persistence, lifecycle locking, gate authority, migration or cross-ref serialization except to prove that the renderer does not own those capabilities.

## 2. Preconditions

Before execution:

1. freeze current main-repository and Lab refs;
2. identify the actual static renderer mapping, lifecycle caller and callable boundary;
3. confirm isolated immutable source and configuration fixtures;
4. establish filesystem, network, subprocess, lock, state, environment-secret and mutation observation hooks;
5. record pre-state hashes and environment identity;
6. define bounded semantic resource limits, operational abort controls, cleanup and rollback;
7. stop when safe isolation or capability observation cannot be demonstrated.

Concrete implementation paths remain `NEEDS_MAIN_REPO_VALIDATION`.

## 3. Case families

### R400-A — Static resolution and identity

- R400-C001: known renderer identifier resolves through one closed static mapping.
- R400-C002: unknown identifier fails loud before invocation and planning.
- R400-C003: duplicate identifier or ambiguous alias fails loud.
- R400-C004: registry-supplied import path, URL, shell command, expression or plugin entry point is rejected.
- R400-C005: identifier, interface version and semantic version are available before invocation.
- R400-C006: incompatible interface version fails before invocation.
- R400-C007: unavailable or unsupported semantic version fails before invocation.
- R400-C008: implementation-evidence-only change does not automatically become semantic-version drift.
- R400-C009: changed renderer semantic version invalidates an existing immutable plan.

### R400-B — Immutable invocation context

- R400-C010: exactly one registered target identity is supplied.
- R400-C011: ordered immutable declared sources equal the fingerprinted source bytes.
- R400-C012: immutable contract-declared configuration is supplied with schema and version.
- R400-C013: missing or invalid required source fails without fallback.
- R400-C014: unknown or malformed configuration fails loud.
- R400-C015: renderer cannot obtain mutable Workspace, registry, lock, Git, writer, subprocess, network, gate or acceptance-state objects.
- R400-C016: ambient repository path reread, traversal, globbing or discovery is prohibited.
- R400-C017: prior target bytes, evidence, historical prose, environment defaults and current time are not substituted as undeclared semantic inputs.
- R400-C018: declared source text is treated as data and cannot become executable instructions.
- R400-C019: absent an accepted future bounded-need contract that preserves determinism and authority boundaries, secrets, credentials and unrelated environment variables are not exposed to the renderer.

### R400-C — Output and target scope

- R400-C020: successful invocation returns one Unicode-text or immutable-bytes payload.
- R400-C021: path, file handle, stream, callback, command, finding or multi-target return is rejected.
- R400-C022: complete-target output does not depend on prior target bytes.
- R400-C023: registered-region output contains payload only and excludes partition markers, separators, preserved-region bytes and parent reconstruction bytes.
- R400-C024: empty output is accepted only when target semantics permit it.
- R400-C025: invalid encoding, normalization or target-semantics output fails before plan capture.
- R400-C026: one invocation cannot update or infer sibling or additional target identities.

### R400-D — Determinism and incidental context

- R400-C027: repeated identical invocation produces byte-equivalent output.
- R400-C028: fresh-process repetition remains byte-equivalent where practical.
- R400-C029: source ordering and configuration ordering are deterministic.
- R400-C030: locale, timezone, working directory, environment, platform, hash randomization, filesystem enumeration and current time do not affect semantic output unless declared and fingerprinted.
- R400-C031: cache loss or reuse does not change output semantics and cache does not become authority.
- R400-C032: mutable global state or prior invocation history does not affect output.

### R400-E — Purity and prohibited capabilities

- R400-C033: renderer creates, modifies or deletes no files.
- R400-C034: renderer performs no network access.
- R400-C035: renderer invokes no subprocess or shell command.
- R400-C036: renderer acquires no lock and starts no nested lifecycle refresh.
- R400-C037: renderer invokes no nested renderer.
- R400-C038: renderer mutates no registry, lifecycle state, evidence, acceptance state, trust state or gate state.
- R400-C039: renderer creates no commit, branch, pull request or repository mutation.
- R400-C040: renderer does not mutate input objects or global registries/caches that affect later output.
- R400-C041: templates, formatting facilities and source-controlled payloads cannot trigger arbitrary code execution, imports, traversal or shell expansion.

### R400-F — Lifecycle and command boundary

- R400-C042: existing commands and workflows request rendering only through the existing lifecycle.
- R400-C043: no command writes renderer output directly, bypasses plan capture or assigns acceptance from renderer success alone.
- R400-C044: renderer output crossing the callable boundary creates no plan, write or acceptance authority by itself.

### R400-G — Failure and resource behavior

- R400-C045: deterministic computation error produces no success payload, plan or mutation authority.
- R400-C046: bounded failure envelope contains only stable code, bounded message and relevant declared-input identity.
- R400-C047: failure envelope does not coexist with success payload, enter fingerprints or become finding/evidence authority.
- R400-C048: semantic resource-bound violation is deterministic, versioned, fingerprint-relevant where applicable and non-accepted.
- R400-C049: operational safety abort is distinct from semantic failure, remains outside semantic fingerprints and produces no semantic output.
- R400-C050: retry after operational abort may reuse the identical plan only after current guards remain valid; retry success is measured independently.
- R400-C051: truncated, malformed or over-bound output is rejected before plan capture and never accepted.
- R400-C052: no fallback renderer is selected automatically after failure.
- R400-C053: prior accepted bytes and state remain unchanged after renderer failure.
- R400-C054: any capability violation terminates the active attempt as `abandoned`.
- R400-C055: additional renderer mapping, caller, capability path or hidden input is recorded without silent scope expansion.

## 4. Observation model

For each case record:

- exact refs and fixture hashes;
- actual mapping, lifecycle caller and callable symbols;
- invocation identity tuple;
- immutable source/configuration hashes;
- return type and output hash;
- repeated-run output comparison;
- filesystem, network, subprocess, lock, state, secret/environment and mutation observations;
- failure envelope and lifecycle translation boundary;
- semantic-bound identity or operational-abort reason;
- plan/target/state deltas, which must be absent at the renderer boundary;
- cleanup and rollback result.

## 5. Outcomes

- `NOT_RUN`: no local execution.
- `BLOCKED`: safe invocation or capability observation cannot be established.
- `FAIL`: dynamic resolution, undeclared input, source-as-code execution, secret exposure, nondeterminism, invalid output acceptance, side effect, prohibited capability, direct command write, plan bypass, nested rendering, fallback behavior or renderer-owned runtime authority occurs.
- `PARTIAL`: only bounded behavior can be measured without proving the full capability boundary.
- `PASS`: all mandatory cases execute with complete evidence and satisfy DPA-400.

## 6. Cleanup

Every case runs in an isolated disposable context. Post-state hashes must prove no repository, target, registry, lock, lifecycle, evidence or acceptance-state mutation. Unexplained residual change blocks reuse.

## 7. Review readiness

This manual is reviewable only when:

- exactly 55 declared cases exist, R400-C001 through R400-C055;
- every declared case maps to at least one fixture;
- every fixture maps to at least one declared case;
- static resolution, immutable inputs, determinism, purity, output scope, lifecycle-only invocation, version distinctions, resource behavior, security boundaries and failure behavior are covered;
- concrete main-repository mappings remain provisional;
- no execution or implementation-conformance claim is present;
- Lab gates pass.
