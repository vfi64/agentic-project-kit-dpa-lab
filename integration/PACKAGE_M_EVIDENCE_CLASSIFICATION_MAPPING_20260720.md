# Package M Evidence Classification Mapping

Status: active

Status-date: 2026-07-20

Authority: non-normative analysis-vocabulary mapping for Package M evidence artifacts

Resolves: `IRM-01`

## 1. Purpose

Package M inventory and matrix artifacts use compact analysis tokens to describe how far remote inspection progressed. Those tokens are not repository-fact classifications and MUST NOT be interpreted as additions to, aliases for or replacements of the closed DPA-100 classification vocabulary.

Every repository or architecture claim remains subject to exactly one DPA-100 classification. Access method, inspection completeness and execution availability are separate analytical dimensions.

## 2. Analysis-only namespace

The following tokens are analysis-only progress labels:

- `REMOTE_VERIFIED` — the stated observation was directly supported by reading identified material at the recorded remote exact ref, but this label alone does not establish implementation conformance, local behavior, completeness or Probe success;
- `REMOTE_PARTIAL` — some directly relevant remote material was read, while one or more required call chains, modes, files or behaviors remain uninspected;
- `VERIFICATION_BLOCKED` — the required verification action could not be completed through the available remote surface;
- `CONFIRMED_OVERLAP`, `SUSPECTED_DUPLICATE_WRITER` and similar matrix terms — analysis findings within the named matrix only, not DPA-100 classifications, trust states, gate states or runtime findings.

These tokens MUST NOT be serialized as runtime states or used as normative acceptance evidence.

## 3. Mandatory DPA-100 mapping

For Package M evidence artifacts:

| Analysis condition | Required DPA-100 repository-fact classification |
|---|---|
| direct exact-ref remote observation, reproducibly cited and limited to the inspected statement | `VERIFIED`, explicitly scoped to the recorded ref and remote-inspection method |
| repository-specific behavior still requiring local, installed-CLI, complete-source, mutation or Probe confirmation | `NEEDS_MAIN_REPO_VALIDATION` |
| proposed architecture semantics not yet adjudicated | `PROPOSED` |
| blocked access or unavailable execution surface | retain the applicable fact classification and record `access-blocked` or `execution-blocked` only as a separate progress/access dimension |

A compound label such as `REMOTE_VERIFIED` MUST NOT replace the required DPA-100 classification in any future normative, adjudication or acceptance artifact.

## 4. Interpretation of existing Package M artifacts

Existing rows in:

- `integration/REMOTE_COMMAND_MUTATION_INVENTORY_20260719.md`;
- `integration/REMOTE_HANDOFF_AND_TRANSFER_MUTATION_MAP_20260719.md`;
- `integration/SEMANTIC_FACT_OVERLAP_MATRIX_20260719.md`;
- `integration/GENERATED_ARTIFACT_OWNERSHIP_MATRIX_20260719.md`;
- `STATUS.md`

must be read using this mapping.

In particular:

- an observed remote call or path may be `VERIFIED` only for that bounded exact-ref observation;
- command completeness, full call-chain behavior, changed-path behavior, lock coverage, runtime authority placement and conformance remain `NEEDS_MAIN_REPO_VALIDATION` unless separately proven;
- no analysis token changes the Package M proposal's repository-specific validation boundary.

## 5. Forward rule

Future Package M planning artifacts SHOULD use separate fields for:

1. DPA-100 classification;
2. evidence method;
3. inspection completeness;
4. access or execution status.

They MUST NOT combine those dimensions into an undeclared classification token.

## 6. Effect

This mapping closes `IRM-01` without changing the frozen Package M review candidate, its normative meaning, any DPA specification, ADR-022, a Probe identity or a main-repository claim.

No refreeze and no immediate independent rereview are required.