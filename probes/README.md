# Probe Preparation

Status: active

Status-date: 2026-07-18

The files in this directory prepare exact-ref main-repository Probes. They do not record executed Probe evidence.

## Authority

- Normative DPA specifications and accepted ADRs define the behavior to test.
- `PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md` defines the shared case, evidence, outcome, cleanup and adjudication structure.
- Probe-specific manuals define bounded test scope and aggregation rules.
- `EXACT_REF_FREEZE_PROCEDURE.md`, `EVIDENCE_CAPTURE_PROCEDURE.md` and `PROBE_ADJUDICATION_PROCEDURE.md` govern later execution identity, evidence and disposition.
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
| `PROBE-002-INTERNAL-CONTRACT-AUDIT.md` | active | audit complete after correction |
| `DPA-400-RENDERER-PROBE-MANUAL.md` | draft | not run |
| `DPA-400-RENDERER-FIXTURE-MANIFEST.md` | draft | not materialized or run |
| `DPA-400-RENDERER-INTERNAL-CONTRACT-AUDIT.md` | active | audit complete after correction |
| `EXACT_REF_FREEZE_PROCEDURE.md` | active | procedure prepared; no ref frozen |
| `EVIDENCE_CAPTURE_PROCEDURE.md` | active | procedure prepared; no execution evidence |
| `PROBE_ADJUDICATION_PROCEDURE.md` | active | procedure prepared; no adjudication performed |

## Current sequence

1. Keep the shared execution/evidence contract and all three corrected Probe packages synchronized.
2. Preserve all executable serialization and concrete mappings as blocked pending exact-ref remote inventory and local confirmation.
3. Prepare the CSC and namespace-profile checklist.
4. Prepare Probe-independent portability slice specifications with explicit proof that they do not alter Probe subjects.
5. Synchronize project-control surfaces and prepare the closed Package P review set.

## Rules

- Preparation MUST NOT be described as execution.
- Concrete parser, lifecycle, renderer, command and path mappings remain `NEEDS_MAIN_REPO_VALIDATION` until current-ref inspection and local confirmation.
- Every execution requires an exact frozen main-repository ref and immutable fixture revision.
- Observation, interpretation and Maintainer adjudication remain separate.
- Evidence is not runtime authority.
- Probe preparation does not release the main-repository mutation freeze.
- DPA-600 remains frozen and DPA-700 remains unstarted while Package P is active.
