# Operational Hardening Register

Status: active
Status-date: 2026-07-20

This register tracks operational improvements discovered during Lab work that are required candidates for `vfi64/agentic-project-kit` but are not normative DPA specifications.

Every entry requires explicit Maintainer disposition during controlled import. The Lab is never imported wholesale, but selective import MUST NOT silently discard registered obligations.

## OHR-001 — Repository capability diagnosis and recovery

- Source: `integration/REPOSITORY_ACCESS_DIAGNOSIS_AND_RECOVERY_PROTOCOL.md`
- Trigger RC-READ-001: false assertion of lost read access despite intact connector access, repository reachability, ref resolution and successful file reads.
- Trigger RC-PUBLISH-001: exact-ref read, checkout and review succeeded, while authenticated push and remote-workflow triggering were unavailable because no usable write credential was present.
- Classification: operational-governance and tooling hardening candidate
- DPA authority: none
- Main-repository implementation: not started
- Required Kit outcome: approved implementation/work-planning slice, equivalent-contract mapping, or explicit rejection with rationale
- Required regression coverage:
  - an omitted or failed file read MUST NOT be classified as read-permission loss before repository, ref, path and chunked-read diagnostics are complete;
  - a confirmed missing write credential MUST terminate as a write/publish capability blocker and MUST NOT be converted into an endless or irrelevant read-diagnosis loop;
  - local review completion MUST NOT be represented as successful remote push, publication or CI triggering.
- Current disposition: `PENDING_CONTROLLED_IMPORT`

## Register rule

An entry may be closed only by a durable record identifying:

- the main-repository issue, direction item, work order, PR or governing contract that owns the outcome;
- the exact disposition;
- the approving Maintainer decision;
- any remaining implementation or validation gates.

Lab archival alone cannot close an entry.
