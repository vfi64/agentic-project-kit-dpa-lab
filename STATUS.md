# Status

Status: active
Status-date: 2026-07-17

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is active on branch `spec/dpa-400-renderer-contract`.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200, DPA-300 and DPA-400 are `review-ready`. DPA-400 remains blocked from `stable` pending applicable exact-ref Probe evidence.

## DP1 Discovery

DP1 Discovery is complete for the explicitly inspected scope at:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed. Global writer-set completeness is not claimed and must be revalidated at Probe time.

No main-repository mutation occurred and no production form was selected.

## DPA-300 lineage closeout

DPA-300 completed primary review, secondary verification, Maintainer adjudication, independent post-adjudication verification and bounded synchronization re-check.

The later review-ready restructure was independently compared against the certified text and received `PASS_WITH_EXPLICIT_RATIFICATION`. The Maintainer ratification record restored the dropped target identity, generic required-field rejection, partition encoding declaration, policy identifiers and normative MUST force; it accepted the enumerated strengthenings and restored Probe and conformance pointers.

DPA-300 remains `review-ready`. Stability remains blocked on applicable DP1 Probe evidence and later governed revalidation.

## DPA-400 review and adjudication

The immutable primary-review baseline was:

`8c9b6892540895e58be53038c6064648d49a2b57`

Claude's primary review returned `ACCEPT_WITH_CHANGES` with four majors:

1. immutable lifecycle-resolved renderer inputs;
2. semantic resource bounds separated from operational safety aborts;
3. renderer identifier/interface-version/semantic-version/implementation-evidence separation;
4. DPA-300 restructure lineage verification.

All four were accepted. DPA-ADR-019 and DPA-ADR-020 are committed. The DPA-300 equivalence verification returned `PASS_WITH_EXPLICIT_RATIFICATION`, and its complete difference set was dispositioned.

The governed amendment batch synchronized:

- `specs/dpa/DPA-100-FOUNDATIONS.md`;
- `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`;
- `specs/dpa/DPA-400-RENDERER-CONTRACT.md`;
- `traceability/DPA-400_TRACEABILITY.md`;
- `diagrams/dpa-400-renderer-boundary.mmd`;
- `DECISIONS.md`.

DPA-400 defines immutable content-addressed inputs, the four-part renderer identity/version model, bounded failure diagnostics, deterministic semantic bounds, non-semantic operational aborts and mandatory capability-boundary plus negative-test evidence.

Independent post-adjudication verification at exact ref `6050d0664d9c1ac8bd1a2eb9d6409593046ede9c` returned `PASS` with zero blocking findings. The report is committed as `reviews/claude/CLAUDE_DPA_400_POST_ADJUDICATION_VERIFICATION.md`.

DPA-400 is promoted to `review-ready`. Repository-specific mappings and enforcement mechanisms remain `NEEDS_MAIN_REPO_VALIDATION`; no production implementation, Probe success or main-repository conformance is claimed.

## Probe relationship

PROBE-001 remains governed by DPA-300 and ADR-017. It does not depend on DPA-400.

DPA-400 requires later exact-ref evidence for static renderer mapping, capability restriction, determinism, renderer versioning and lifecycle integration before `stable`.

Probe fixtures may be prepared during the no-Mac period but must not be represented as executed.

## Next governed step

1. keep the durable Lab gates green on the promoted branch head;
2. begin DPA-500 drafting;
3. prepare PROBE-001 and the DPA-300-owned subset of PROBE-002 as bounded fixtures and expected-result contracts;
4. prepare renderer-map, determinism, immutable-input and purity fixtures for later DPA-400 Probe work;
5. execute Probes only when a suitable main-repository environment is available.

## Restrictions

- No production code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without adjudication.
- A promotion commit changes status surfaces only and MUST NOT change normative text.

Phase B may continue. The active specification step is DPA-500 drafting with bounded Probe-fixture preparation.
