# Probe-Independent Portability Slice Plan

Status: active

Status-date: 2026-07-18

## 1. Purpose

This document defines the only portability changes that may be planned in parallel with DPA Probe work.

A portability slice is eligible only when it replaces a confirmed direct path or namespace bypass with an existing Workspace or resolver authority and does not alter any Probe subject, runtime ownership boundary or DPA semantic contract.

This plan does not authorize implementation.

## 2. Current evidence boundary

The current remote `vfi64/agentic-project-kit` `main` head observed during this preparation is:

`6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

This equals the recorded Discovery baseline. That equality does not replace local confirmation before mutation.

Remote connector code search did not provide a complete path-literal inventory during this session. Therefore no concrete file or symbol is classified here as a current verified defect. Candidate entries remain `verification-blocked` until exact source inspection succeeds remotely or locally.

## 3. Eligibility rules

A proposed slice MUST satisfy all of the following:

1. the current exact-ref source path and symbol are identified;
2. the direct literal or namespace bypass is reproduced;
3. an existing Workspace or resolver authority already owns the replacement behavior;
4. the smallest change is a mechanical resolver substitution or equivalent bounded adaptation;
5. legacy-profile behavior is preserved;
6. namespace-profile behavior is tested negatively and positively;
7. registry schema and parser behavior are unchanged;
8. lifecycle phase ordering and mutation semantics are unchanged;
9. writer identity and ownership are unchanged;
10. acceptance-state schema, persistence and recovery are unchanged;
11. findings, gate authority and enforcement behavior are unchanged;
12. Probe fixtures, expected results and observation paths are unchanged, or the affected Probe is explicitly refrozen and rerun;
13. no silent fallback is introduced;
14. rollback is a bounded code revert without data migration.

Failure of any item makes the candidate DPA-critical or out of scope for parallel portability work.

## 4. Ineligible surfaces before PROBE-002 adjudication

The following are not portability slices even when they contain direct paths:

- handoff-writer behavior;
- `CURRENT_HANDOFF.md` writer routing;
- Doc Lifecycle Apply content-writing behavior;
- governed writer semantics;
- mutation-plan execution semantics;
- lock ownership or reentrancy semantics;
- acceptance-state schema or persistence;
- recovery completion;
- gate-set re-acceptance;
- layered acceptance;
- projection freshness and gate integration;
- renderer authority or callable semantics;
- registry schema or unknown-field policy.

These surfaces remain frozen.

## 5. Candidate families

The following families MAY yield eligible slices after exact-ref source inspection:

### PRT-A — Documentation-registry path resolution

Potential shape:

- replace a direct registry root literal with the existing Workspace registry resolver;
- preserve parser, schema, validator and registry contents unchanged.

Required proof:

- same resolved path under legacy profile;
- declared alternate path under namespace profile;
- missing or unknown profile fails loud;
- no parser or lifecycle behavior changes.

### PRT-B — Report and audit output paths

Potential shape:

- route report destination through an existing Workspace output resolver;
- preserve report content, finding semantics and command behavior.

Required proof:

- identical content and exit code under legacy profile;
- correct namespace destination;
- no protected-path escape;
- no lifecycle or evidence-authority change.

### PRT-C — Transfer and handoff transport paths

Potential shape:

- replace a transport-location literal only where the existing transfer authority already defines the path;
- do not change writer routing, handoff contents or state transitions.

Required proof:

- same transfer protocol and ownership;
- no writer or lifecycle change;
- no stale-state fallback;
- no impact on PROBE-002 subjects.

Because transfer and handoff paths are close to frozen writer surfaces, every PRT-C candidate defaults to ineligible until proven otherwise.

### PRT-D — Temporary and cache paths

Potential shape:

- replace kit-internal temporary-root assumptions with the existing Workspace temporary resolver.

Required proof:

- temporary data remains non-authoritative;
- cleanup semantics remain identical;
- cache loss does not change semantic results;
- no evidence, state or acceptance path moves.

### PRT-E — GUI project and workspace selection

Potential shape:

- route project-root selection through the same existing Workspace authority used by CLI paths.

Required proof:

- no second GUI registry or project-state model;
- exact repository identity remains visible;
- protected commands retain existing plans and gates;
- unsupported external repositories fail loud.

GUI behavior requires local or suitable interactive validation and is not established remotely.

## 6. Slice record

Every candidate MUST use this record before implementation:

```text
slice_id:
status:
exact_main_ref:
source_file:
source_symbol:
historical_finding:
current_revalidation_result:
direct_literal_or_bypass:
existing_resolver_authority:
smallest_change:
legacy_profile_tests:
namespace_profile_tests:
negative_tests:
expected_no_change_areas:
probe_impact:
probe_refreeze_required:
frozen_surface_check:
rollback:
limitations:
maintainer_decision:
```

Allowed candidate progress states are:

- `pending`;
- `verification-blocked`;
- `eligible`;
- `ineligible`;
- `implemented` only after later main-repository evidence;
- `superseded`.

These are planning progress states, not implementation or conformance classifications.

## 7. Required tests for every eligible slice

At minimum:

- focused legacy-profile regression test;
- namespace-profile positive test;
- namespace-profile unknown/missing-root negative test;
- repository-root escape negative test where path input is involved;
- no-silent-fallback assertion;
- unaffected registry/lifecycle/writer/acceptance/gate behavior assertion;
- changed-path and cleanup evidence;
- full relevant gate suite required by the main repository.

## 8. Probe-impact rule

A portability merge requires Probe impact analysis.

If the changed code is observed by a Probe, supplies a fixture path, changes an invocation path or changes evidence capture, the affected Probe MUST receive:

- a new exact validation ref;
- updated materialized fixture metadata;
- rerun of affected cases;
- preserved prior evidence.

A claim that a slice is Probe-independent MUST be proven, not assumed.

## 9. Next local action

At the Mac phase:

1. confirm local HEAD equals the recorded remote SHA;
2. run a complete literal and Workspace-bypass inventory;
3. populate candidate records with exact files and symbols;
4. classify each candidate `eligible` or `ineligible`;
5. implement only eligible slices in separate bounded PRs;
6. execute focused and namespace negative tests;
7. record Probe impact and refreeze obligations.
