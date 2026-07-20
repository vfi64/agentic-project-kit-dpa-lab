# Operational Hardening Register

Status: active
Status-date: 2026-07-20

This register tracks operational improvements discovered during Lab work that are required candidates for `vfi64/agentic-project-kit` but are not normative DPA specifications.

Every entry requires explicit Maintainer disposition during controlled import. The Lab is never imported wholesale, but selective import MUST NOT silently discard registered obligations.

## OHR-001 — Repository access diagnosis and recovery

- Source: `integration/REPOSITORY_ACCESS_DIAGNOSIS_AND_RECOVERY_PROTOCOL.md`
- Trigger: false assertion of lost repository access on 2026-07-20 despite intact connector access, repository reachability, read/write permissions and successful file reads.
- Classification: operational-governance and tooling hardening candidate
- DPA authority: none
- Main-repository implementation: not started
- Required Kit outcome: approved implementation/work-planning slice, equivalent-contract mapping, or explicit rejection with rationale
- Required regression case: an omitted or failed file read MUST NOT be classified as permission loss before repository, ref, path and chunked-read diagnostics are complete
- Current disposition: `PENDING_CONTROLLED_IMPORT`

## Register rule

An entry may be closed only by a durable record identifying:

- the main-repository issue, direction item, work order, PR or governing contract that owns the outcome;
- the exact disposition;
- the approving Maintainer decision;
- any remaining implementation or validation gates.

Lab archival alone cannot close an entry.
