# PROBE-001 Manual — Registry Parser and Validator Compatibility

Status: draft

Status-date: 2026-07-18

Consumes: `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`

Governing architecture: DPA-300 and accepted ADRs, including ADR-017

Execution-state: not run

## 1. Purpose

PROBE-001 measures how the exact-ref main-repository registry parser and validator handle the proposed DPA projection-contract and partition-contract representations.

It is designed to distinguish:

- syntax accepted by the current parser;
- semantic validation performed by the current validator;
- required DPA fields or constraints not represented by the current implementation;
- implementation behavior that conflicts with or falsifies a DPA assumption;
- defects in the Probe fixtures or expectations.

PROBE-001 does not test renderer execution, lifecycle mutation, acceptance state, recovery, freshness gates or production adoption.

## 2. Evidence boundary

The historical Discovery ref

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

may inform fixture design only. It does not establish current parser or validator behavior.

All execution claims require:

- current remote-main identification;
- local confirmation;
- exact Probe-ref freeze;
- immutable fixture revision;
- recorded commands and bounded outputs.

Until execution, every concrete main-repository parser, schema and command mapping remains `NEEDS_MAIN_REPO_VALIDATION`.

## 3. In scope

PROBE-001 covers:

- manual registry compatibility controls;
- proposed `ProjectionContract` representation;
- proposed `PartitionContract` representation;
- schema and schema-version handling;
- required-field validation;
- unknown-field behavior;
- target identity representation;
- registered-region representation;
- partition encoding declaration;
- policy and renderer identifiers as data fields;
- duplicate identity and conflicting-entry behavior where the current registry supports such validation;
- bounded parser and validator diagnostics.

## 4. Out of scope

The Probe MUST NOT claim conclusions about:

- renderer resolution or execution;
- target writing;
- lifecycle planning or locking;
- acceptance-state persistence;
- recovery;
- findings or gate integration;
- branch or pull-request serialization;
- migration or rollback;
- strict adoption.

A parser accepting a field does not prove that any runtime consumer implements its semantics.

## 5. Required execution preconditions

Before execution:

1. record current remote `origin/main` SHA;
2. synchronize a local checkout to that exact ref;
3. record worktree cleanliness and environment identity;
4. identify the actual registry parser, validator and supported invocation path;
5. record the current manual-registry format and schema/version behavior;
6. freeze this manual and the fixture manifest at exact Lab refs;
7. create an isolated fixture or test workspace that cannot alter production registry state;
8. confirm cleanup and rollback actions;
9. record any permissions or tool limitations.

Failure to establish a safe isolated execution path makes mutating or import cases `BLOCKED`.

## 6. Fixture families

The exact serialized syntax remains provisional until current-ref parser inspection. The semantic fixture families are fixed.

### F001-MANUAL

A current-format manual registry entry used as a compatibility control.

Purpose:

- confirm the invocation and evidence path;
- establish expected current-format acceptance;
- detect Probe harness defects before DPA-specific cases.

### F001-PROJECTION

A proposed projection-contract entry containing at least:

- schema identifier;
- schema version;
- stable contract identity;
- source identity or source selector;
- target identity;
- renderer identifier;
- target semantics;
- lifecycle and policy identifiers where required by DPA-300;
- partition reference or full-target declaration;
- registered-region declaration where applicable.

### F001-PARTITION

A proposed partition-contract entry containing at least:

- schema identifier;
- schema version;
- stable partition identity;
- target identity;
- registered-region or partition boundaries;
- encoding declaration;
- ownership or policy identity where required;
- deterministic region identity.

### F001-INVALID

Negative variants derived from valid fixtures by one bounded change.

## 7. Case matrix

### P001-C001 — Manual registry compatibility control

Expected:

- current-format control parses and validates as documented by the exact-ref implementation;
- no DPA-specific conclusion is drawn.

Failure consequence:

- Probe harness or invocation is defective or current behavior changed;
- DPA-specific cases are `BLOCKED` until resolved.

### P001-C002 — Minimal valid ProjectionContract candidate

Expected-result class:

- informational compatibility observation.

Possible valid outcomes:

- accepted by parser and validator;
- parsed but rejected by semantic validator;
- rejected as unknown schema or shape;
- execution blocked because no safe generic fixture path exists.

No outcome alone establishes architecture conformance.

### P001-C003 — Minimal valid PartitionContract candidate

Same outcome interpretation as P001-C002, with special attention to partition encoding, region identity and target binding.

### P001-C004 — ProjectionContract missing required field

Fixture mutation:

- remove exactly one DPA-required field.

Expected:

- if the current validator claims the proposed schema, it MUST reject the fixture;
- if the schema is unsupported, rejection reason MUST be recorded without treating it as field-level validation.

### P001-C005 — PartitionContract missing required field

Equivalent to P001-C004 for a partition-required field.

### P001-C006 — Unknown schema identifier

Expected:

- fail loud;
- no silent fallback to manual-entry semantics;
- no partial registration.

### P001-C007 — Unknown schema version

Expected:

- fail loud;
- no silent downgrade or reinterpretation;
- bounded diagnostic identifies unsupported version or equivalent reason.

### P001-C008 — Unknown top-level field

Expected:

- exact behavior recorded;
- classify strict rejection, explicit ignore, warning or silent acceptance;
- DPA compatibility assessed only after the architecture's unknown-field rule is compared with observed behavior.

### P001-C009 — Duplicate contract identity

Expected:

- duplicate or conflicting identity is rejected, or current implementation limitation is recorded;
- no last-writer-wins assumption may be invented.

### P001-C010 — Target identity absent or ambiguous

Expected:

- reject when the tested schema claims DPA contract support;
- no target inferred from path, filename or ambient workspace state unless that behavior is explicitly normative.

### P001-C011 — Registered-region declaration valid

Expected:

- parser preserves the declared region identity and boundaries if the representation is supported;
- no runtime ownership or lifecycle conclusion is drawn.

### P001-C012 — Registered-region declaration malformed

Expected:

- fail loud;
- no silent conversion to full-target ownership;
- no loss of target identity.

### P001-C013 — Partition encoding declaration absent

Expected:

- reject when required by the claimed schema;
- unsupported-schema rejection must not be misreported as successful field validation.

### P001-C014 — Renderer identifier syntactically present

Expected:

- parser preserves the identifier as data if the schema is accepted;
- renderer resolution and interface compatibility remain out of scope.

### P001-C015 — Policy identifier unknown

Expected:

- record whether validation rejects, defers or ignores the identifier;
- do not infer policy implementation from parser acceptance.

### P001-C016 — Additional related path discovery

Triggered when execution reveals another registry reader, parser, validator, loader or normalization path.

Expected:

- record exact symbol/path and relation to the case;
- do not expand execution scope silently;
- classify whether a new bounded case or a later Probe amendment is required.

## 8. Expected observation categories

For each case record separately:

- parse result;
- validation result;
- normalized representation, if any;
- diagnostics;
- return code or API result;
- changed paths;
- whether any partial registry state was created;
- cleanup result.

Parser acceptance and validator acceptance MUST be reported as separate observations when the implementation exposes both stages.

## 9. Prohibited observations

The following are always significant:

- silent fallback from unknown DPA schema to manual-entry semantics;
- partial registry mutation after rejection;
- target identity inferred contrary to fixture data;
- malformed registered region treated as full-target ownership;
- unknown schema version silently treated as current;
- destructive normalization that loses required identity;
- unbounded diagnostics containing unrelated repository content.

## 10. Evidence set

Execution MUST produce:

- execution manifest;
- exact main-repository ref;
- exact Lab manual and fixture refs;
- parser and validator symbol/path inventory;
- command or API invocation record;
- per-case input hash;
- per-case parse and validation results;
- bounded diagnostics;
- normalized-output hash and bounded representation where available;
- changed-path manifest;
- cleanup record;
- interpretation report;
- Maintainer adjudication record after review.

## 11. Outcome aggregation

Mandatory control:

- P001-C001 MUST be `PASS` before DPA-specific cases can support conclusions.

Probe-level outcome:

- `PASS` only if all mandatory negative cases behave as required and all required evidence is complete;
- `FAIL` if a prohibited fallback, partial registration, identity loss or required negative rejection failure occurs;
- `PARTIAL` if valid execution establishes only bounded compatibility because the proposed schema is not fully supported or parser and validator stages cannot be separated;
- `BLOCKED` if the exact-ref implementation, safe invocation path, fixture isolation or required tooling cannot be established;
- `NOT_RUN` before local execution.

A `PARTIAL` result may still falsify or confirm individual assumptions, but it MUST NOT be summarized as full DPA-300 conformance.

## 12. Cleanup and rollback

Each case MUST run against isolated fixture state.

Cleanup MUST:

- remove temporary fixture registrations and generated files;
- preserve evidence artifacts only in the declared evidence location;
- verify no production registry or protected planning path changed;
- compare pre-state and post-cleanup hashes for governed paths.

Any unexplained residual change blocks reuse of the worktree.

## 13. Repeatability

The manual requires:

- one clean control run;
- one complete DPA fixture run;
- a second run after cleanup for deterministic parser/validator results where safe;
- a new execution identity for every run;
- explicit comparison of stable and variable fields.

A changed main-repository ref, fixture revision or normative expectation requires impact analysis and ref freeze before rerun.

## 14. Adjudication questions

After execution, the Maintainer must decide for each discrepancy:

- does the current parser already support the proposed representation;
- is support missing but architecture unchanged;
- does implementation behavior require a bounded DPA-300 amendment;
- is the fixture or expected result defective;
- was an additional registry path discovered;
- must PROBE-001 be amended and rerun;
- which exact evidence may constrain DP2 planning.

## 15. Review readiness

This manual is reviewable only when:

- the fixture manifest exists;
- actual current-ref parser/validator invocation placeholders are clearly marked provisional;
- every mandatory case has a fixture mapping;
- DPA-300 and ADR anchors are synchronized;
- no execution claim is present;
- Lab gates pass.