# Probe Preparation

Status: active

Status-date: 2026-07-18

The files in this directory prepare exact-ref main-repository Probes. They do not record executed Probe evidence.

## Authority

- Normative DPA specifications and accepted ADRs define the behavior to test.
- `PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md` defines the shared case, evidence, outcome, cleanup and adjudication structure.
- Probe-specific manuals define bounded test scope and aggregation rules.
- Exact-ref execution evidence will outrank preparation assumptions.

## Current package

| Artifact | Status | Execution state |
|---|---|---|
| `PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md` | draft | not applicable |
| `PROBE-001-MANUAL.md` | draft | not run |
| `PROBE-001-FIXTURE-MANIFEST.md` | draft | not materialized or run |
| `PROBE-001-INTERNAL-CONTRACT-AUDIT.md` | active | audit complete after correction |
| `PROBE-002-MANUAL.md` | draft | not run |
| `PROBE-002-FIXTURE-MANIFEST.md` | draft | not materialized or run |
| `DPA-400-RENDERER-PROBE-MANUAL.md` | planned | not run |
| `DPA-400-RENDERER-FIXTURE-MANIFEST.md` | planned | not materialized or run |

## Current sequence

1. Keep the shared execution/evidence contract synchronized.
2. Preserve the corrected PROBE-001 semantic package; executable serialization remains blocked on exact-ref parser inspection.
3. Audit PROBE-002 against DPA-300, DPA-500, ADR-016 and ADR-021.
4. Prepare the DPA-400 renderer Probe package.
5. Prepare exact-ref freeze, evidence capture and adjudication procedures.

## Rules

- Preparation MUST NOT be described as execution.
- Concrete parser, lifecycle, renderer, command and path mappings remain `NEEDS_MAIN_REPO_VALIDATION` until current-ref inspection and local confirmation.
- Every execution requires an exact frozen main-repository ref and immutable fixture revision.
- Observation, interpretation and Maintainer adjudication remain separate.
- Evidence is not runtime authority.
- Probe preparation does not release the main-repository mutation freeze.
- DPA-600 remains frozen and DPA-700 remains unstarted while Package P is active.