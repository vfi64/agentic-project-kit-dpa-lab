# Governance

Status: active
Status-date: 2026-07-20

## Authority

This laboratory is authoritative only for its own planning history, accepted decisions and pre-import normative specifications. It is not authoritative for runtime facts, Direction state, release state or implementation status of `vfi64/agentic-project-kit`.

The main repository remains the sole runtime authority.

The private repository `vfi64/agentic-governance-framework` is authoritative only for its accepted reusable governance method. It does not automatically govern this Lab or the Kit. Lab and Kit adoption require explicit, exact-ref evaluation and adjudication.

## Normative change process

1. Primary architecture reviews and secondary technical verification audits are recorded under `reviews/` against exact refs.
2. Maintainer adjudication records accepted, modified and rejected findings.
3. Accepted architecture decisions are documented in `DECISIONS.md`.
4. Normative specifications under `specs/dpa/` change only after consolidated adjudication.
5. Repository-specific statements carry an explicit DPA-100 classification.
6. Document status, progress status, access outcome and review verdict remain separate namespaces.
7. No implementation claim is `VERIFIED` without exact main-repository evidence.

## Meta-governance gate

Before further substantive DPA development, the Lab MUST complete Package G under:

`integration/PACKAGE_G_META_GOVERNANCE_VALIDATION_AND_ADOPTION_PLAN.md`

Package G audits the Lab's active working and development instructions for correctness, efficiency, effectiveness, redundancy freedom, consistency, completeness, testability, usability, maintainability and complexity proportionality.

Governance is not self-justifying. Every retained control MUST identify the protected problem and a credible mechanism by which it improves correctness, useful yield, safety, selectivity, maintainability, reproducibility or evidence quality. Safety-critical false negatives remain non-tradeable.

Until Package G closes through independent review and Maintainer adjudication:

- no substantive new DPA normative package may begin;
- DPA-600 remains frozen;
- DPA-700 remains unstarted;
- only Package-G work, evidence preservation, verified false-claim correction and non-semantic synchronization may proceed.

## Review roles

Required review roles are:

- primary architecture review,
- secondary technical verification,
- maintainer adjudication,
- consolidated review record.

No named model or vendor is mandatory. A reviewer must have sufficient access to inspect the exact ref. `ACCESS_BLOCKED` is an access outcome, not an architecture verdict.

## Evidence boundary

Minimal static repository-fact records MAY exist under `evidence/repo-facts/` when required by accepted decisions. They support reproducibility and classification but MUST NOT become runtime authority, a live mirror of the main repository or a parallel evidence system.

## Prohibitions

- No production kit code.
- No copied secrets.
- No live `.agentic/` state from private repositories.
- No fabricated test or gate evidence.
- No second runtime authority.
- No vendor-bound review requirement.
- No review finding becomes normative without adjudication.
- No governance addition without an explicit purpose, cost and later simplification or retirement path.
- No silent or memory-based adoption of the Agentic Governance Framework.
