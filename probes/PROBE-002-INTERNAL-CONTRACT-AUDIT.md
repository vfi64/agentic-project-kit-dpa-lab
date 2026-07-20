# PROBE-002 Internal Contract Audit

Status: complete

Status-date: 2026-07-18

Audit result: `PASS_AFTER_CORRECTION`

## Scope

Compared:

- `probes/PROBE-002-MANUAL.md`;
- `probes/PROBE-002-FIXTURE-MANIFEST.md`;
- DPA-300 lifecycle, plan, acceptance, evidence and recovery requirements;
- DPA-500 freshness, findings, gate, re-acceptance, layered-acceptance and conformance requirements;
- accepted ADR-016 and ADR-021 semantics as incorporated into DPA-300 and DPA-500.

## Findings corrected

1. configuration drift was not independently represented;
2. renderer identifier, interface version, semantic version and implementation evidence were not sufficiently separated;
3. missing, malformed, scope-mismatched and internally inconsistent acceptance states were under-specified;
4. unavailable evaluation machinery lacked its own explicit case;
5. re-acceptance warning and failure behavior was missing;
6. successful re-acceptance state-write scope was not explicit;
7. recovery exact-match and bytes-only prohibitions were not separately tested;
8. evidence failure after Write or re-acceptance was missing;
9. read-only audit behavior was missing;
10. freshness classification, drift class, trust state, gate decision and enforcement stage were not explicitly tested as separate dimensions;
11. observe, warn, block-new and strict stages were missing;
12. unknown safety-relevant findings were not explicitly required to fail closed.

## Result

The corrected package contains cases P002-C001 through P002-C058 with fixture coverage. It remains a remote preparation artifact only. Concrete main-repository entry points, schemas, paths, commands, persistence ordering and enforcement mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

No Probe execution, implementation completion or main-repository conformance is claimed.