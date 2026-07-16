# Status

Status: active
Status-date: 2026-07-16

Superseded-by: n/a

## Current

Phase A is closed on `main`.

Phase B — Core document-management integration is active on branch `spec/dpa-400-renderer-contract`.

The lab remains non-authoritative for main-repository runtime state, contains no production kit code and has not been adopted with the kit.

DPA-200 and DPA-300 are `review-ready`.

## DP1 Discovery

DP1 Discovery is complete for the explicitly inspected scope at:

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

DISC-001 through DISC-010 and DISC-003b are committed.

DISC-003b established:

- `transfer chat-switch-complete` does not write `CURRENT_HANDOFF.md` in the inspected code at that ref;
- `transfer admin-refresh-pr` through `_refresh_operational_handoff_docs()` is an observed writer path;
- global writer-set completeness is not claimed and must be revalidated at Probe time.

No main-repository mutation occurred and no production form was selected.

## DPA-300 closeout

DPA-300 completed:

- primary architecture review;
- secondary technical verification;
- Maintainer adjudication through ADR-016 and ADR-017;
- independent post-adjudication verification;
- bounded synchronization correction;
- diff-scoped re-check with result `PASS`;
- promotion to `review-ready`.

The complete DPA-300 branch was fast-forwarded to `main` at:

`aaa60ef2a596ccfbcd8ce1c49096822a0347c040`

Stability remains blocked on applicable DP1 Probe evidence and later governed revalidation.

## DPA-400 active work

The active renderer-contract branch was created from updated `main`:

`spec/dpa-400-renderer-contract`

The first DPA-400 baseline now contains:

- `specs/dpa/DPA-400-RENDERER-CONTRACT.md`;
- `traceability/DPA-400_TRACEABILITY.md`;
- `diagrams/dpa-400-renderer-boundary.mmd`.

The draft defines:

1. one closed static renderer mapping;
2. declarative renderer identifiers;
3. declared-source and contract-configuration inputs only;
4. text-or-immutable-bytes return values;
5. one invocation for exactly one registered target;
6. payload-only output for registered regions;
7. no writes, locks, subprocesses, network calls, workflow calls, renderer chaining or acceptance assignment;
8. deterministic and reproducible output;
9. renderer-version and fingerprint obligations;
10. explicit failure and resource-bound contracts.

Repository-specific mappings and enforcement mechanisms remain `NEEDS_MAIN_REPO_VALIDATION`.

DPA-400 may progress to `review-ready` before Probe execution, but MUST NOT become `stable` before relevant renderer compatibility and purity evidence exists at an exact main-repository validation ref.

## Probe relationship

PROBE-001 remains governed by DPA-300 and ADR-017. It does not depend on DPA-400.

DPA-400 will require later exact-ref evidence for static renderer mapping, capability restriction, determinism, renderer versioning and lifecycle integration.

PROBE fixtures may be prepared during the no-Mac period but must not be represented as executed.

## Parallel streams

Portability literal fixes in the main repository remain a separate later maintenance stream and may run in parallel with Probe work during the Mac phase.

The `CURRENT_HANDOFF.md` writer remains part of DPA/DP2 architecture and MUST NOT be treated as an isolated portability quick fix.

Independent-context verification remains deferred future scope for DPA-800/DPA-900 and later kit governance; it is not a new active specification slice.

## Next governed step

1. complete the DPA-400 normative contract, traceability and diagrams;
2. run an internal invariant, ADR, failure-mode and cross-artifact audit;
3. produce one immutable DPA-400 primary-review baseline;
4. obtain Claude primary architecture review and secondary technical verification;
5. adjudicate findings before normative changes;
6. promote no further than `review-ready` before applicable Probe evidence;
7. prepare, but do not execute, bounded renderer and PROBE-001/002 fixtures.

## Restrictions

- No production code in the lab.
- No `.agentic/` initialization or simulated adoption.
- No production-form selection from Discovery evidence.
- No Probe execution without its governing reviewable contract and suitable environment.
- No DPA-400 or DPA-500 stability before applicable Probe evidence.
- No review finding becomes normative without adjudication.

Phase B may continue. The active architecture task is DPA-400 completion and review preparation.
