# Status

Status: active
Status-date: 2026-07-15
Superseded-by: n/a

## Current

Phase A — Foundation is closed on `main` at commit `a1b81beaf8f8a065d8a869d15bbf39d0e6459aae`.

Phase B — Core document-management integration is active on branch `spec/dpa-200-document-model`.

The lab remains non-authoritative for the runtime state of `vfi64/agentic-project-kit`, contains no production kit code and has not been adopted with the kit.

## DPA-200 review baseline

Primary and secondary review baseline:

`44a87127fca7f482bc2991f0c258af0a386a7048`

- Claude primary architecture review: `ACCEPT_WITH_CHANGES`; no blockers.
- ChatGPT secondary technical verification: `ACCEPT_WITH_CHANGES`; all four Major findings verified.
- Maintainer adjudication: complete.

## Accepted DPA-200 decisions

- DPA-ADR-013 — document-form partition and lifecycle-owned boundary partition.
- DPA-ADR-014 — closed consumer trust-state model.

Accepted corrections include:

1. Split projection is a multi-target arrangement only.
2. A single document with projected and non-projected regions is hybrid.
3. Managed-head is an exceptional hybrid subtype.
4. Lifecycle-owned partition contracts own boundary bytes.
5. Renderers emit payload bytes only.
6. Trust states are `computed`, `plan-captured`, `written-unverified`, `accepted`, `abandoned`.
7. Drift starts a new refresh attempt without silently rewriting prior accepted-byte state.
8. DPA-200 owns one invalid-state catalog.
9. DM-011 validates target-semantics completeness.
10. `no migration` is the fourth migration outcome when evidence is insufficient.

## Accepted sequencing decision

DPA-ADR-015 — Permit early read-only DP1 discovery — is accepted.

DP1 remains one formal slice with internal stages:

1. Discovery
2. Probe
3. Assessment

Only Discovery may execute in Phase B before DPA-300 and before lab adoption.

The governed Discovery contract is:

`integration/DP1_DISCOVERY_CONTRACT.md`

Discovery is strictly read-only. It records observed facts at one exact validation ref and may verify or falsify assumptions. It performs no mutation, migration, adoption, conformance judgment, production-form selection or architecture decision.

## Governance synchronization

Completed:

- dedicated accepted ADR-015;
- `LAB_EXECUTION_CONTRACT.md` updated with the Phase-B Discovery exception and DP1 internal stages;
- `ROADMAP.md` updated to evidence-first sequencing;
- `integration/DP1_DISCOVERY_CONTRACT.md` created;
- factual Discovery questions separated from later sufficiency and compatibility Probes.

## Remaining DPA-200 work

1. Consolidate the adjudicated amendments into `DPA-200-DOCUMENT-MODEL.md`.
2. Synchronize `DPA-200-DOCUMENT-FORM-MATRIX.md`.
3. Regenerate region-ownership and trust-state diagrams.
4. Add DM-011 and re-key taxonomy, invalid-state and trust-transition traceability.
5. Run bounded post-adjudication verification.
6. Promote DPA-200 and its matrix to `review-ready` only after verification passes.

## Next governed step

Finish DPA-200 post-adjudication consolidation first.

After DPA-200 becomes `review-ready`, execute DP1 Discovery against a newly fetched exact `origin/main` validation ref of `vfi64/agentic-project-kit`.

Use Discovery evidence to update assumptions and write DPA-300. Defer DP1 Probe and Assessment until a reviewable contract exists.

## Main-repository validation boundary

Concrete region support, marker syntax, candidate readers and writers, lifecycle hooks, finding suitability, gate mapping, concurrency mechanisms and rollback implementation remain `NEEDS_MAIN_REPO_VALIDATION` until the appropriate Discovery, Probe or Assessment evidence exists.

No production candidate has been assigned a form.

## Phase B restrictions

- No production kit code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No registry-field or module-name claims without exact evidence.
- No production-form selection before DP1 evidence.
- No DPA-300 detail may bypass DPA-200 authority, ownership or trust-state rules.
- No Discovery conclusion may make an architecture decision.
- No review finding becomes normative without adjudication.

Phase B may continue. DPA-200 remains `draft` until accepted amendments are consolidated and verified.
