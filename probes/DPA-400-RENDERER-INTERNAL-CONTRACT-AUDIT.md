# DPA-400 Renderer Probe Internal Contract Audit

Status: active

Status-date: 2026-07-18

Audit-result: PASS_AFTER_CORRECTION

## 1. Scope

This audit compares:

- `specs/dpa/DPA-400-RENDERER-CONTRACT.md`;
- accepted ADR dependencies named by DPA-400;
- `probes/DPA-400-RENDERER-PROBE-MANUAL.md`;
- `probes/DPA-400-RENDERER-FIXTURE-MANIFEST.md`;
- `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`.

It is a Lab consistency audit, not exact-ref execution evidence and not main-repository conformance.

## 2. Findings corrected

The initial renderer Probe package covered static mapping, version identity, immutable inputs, output type and scope, determinism, purity, resource behavior and failure boundaries. The following normative obligations were not yet explicit enough:

1. renderer semantic-version change invalidates an existing immutable plan;
2. declared source text remains data and cannot become executable instructions;
3. templates and formatting facilities cannot enable imports, arbitrary code, traversal or shell expansion;
4. secrets, credentials and unrelated environment variables remain outside the renderer invocation context;
5. commands and workflows may request rendering only through the existing lifecycle and cannot write output directly or bypass plan capture;
6. renderer output alone creates no plan, write or acceptance authority;
7. operational abort remains outside semantic fingerprints and retry of the same plan requires current guards to remain valid;
8. capability violation terminates the active attempt as `abandoned`;
9. truncated operational output can never become accepted semantic output.

These obligations are now represented by R400-C009, R400-C018, R400-C019 and R400-C041 through R400-C055 and by synchronized fixtures.

## 3. Coverage result

The corrected package contains 55 stable semantic cases covering:

- closed static renderer resolution;
- identifier, interface-version, semantic-version and implementation-evidence separation;
- immutable lifecycle-resolved sources and configuration;
- source-as-data and secret-isolation boundaries;
- one invocation and one target;
- payload-only registered-region output;
- deterministic output across identical and fresh-process contexts;
- all prohibited capability classes;
- lifecycle-only invocation and no direct command write;
- semantic resource bounds and operational aborts;
- bounded failure envelopes;
- no fallback renderer;
- no renderer-owned runtime authority.

Every case maps to at least one fixture. Concrete identifiers, callable signatures, module paths, sandbox mechanisms, lifecycle callers and CI placement remain `NEEDS_MAIN_REPO_VALIDATION`.

## 4. Result

`PASS_AFTER_CORRECTION`

The renderer Probe package is internally consistent with DPA-400 at the semantic preparation level. It remains `draft`, unmaterialized and unexecuted. Exact-ref execution requires remote inventory, local confirmation, safe capability observation and the freeze procedures defined for Package P.
