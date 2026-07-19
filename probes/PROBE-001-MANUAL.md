# PROBE-001 Manual — Registry Parser and Validator Compatibility

Status: draft

Status-date: 2026-07-19

Consumes: `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`

Fixture manifest: `probes/PROBE-001-FIXTURE-MANIFEST.md`

Governing architecture: DPA-300 §§4–6 and DPA-ADR-017

Execution-state: not run

## 1. Purpose

PROBE-001 measures how the exact-ref main-repository documentation-registry parser and validator handle proposed DPA projection and partition metadata.

It distinguishes:

- parser acceptance;
- semantic-validator acceptance;
- normalization behavior;
- unsupported representation;
- missing implementation;
- implementation behavior that conflicts with a DPA requirement or assumption;
- defective fixture or harness behavior.

It does not test renderer execution, lifecycle mutation, acceptance state, recovery, freshness gates, workflow serialization, migration or adoption.

## 2. Evidence boundary

The historical Discovery ref

`vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

may inform preparation only. Execution claims require a current remote-main identity, local confirmation, an exact frozen Probe ref, immutable Lab manual and fixture refs, recorded commands and bounded outputs.

Until execution, all concrete parser, validator, schema, command and path mappings remain `NEEDS_MAIN_REPO_VALIDATION`.

## 3. Normative requirements under test

### 3.1 Existing-registry compatibility

- The existing documentation registry remains the sole declarative authority.
- A registry entry without projection metadata remains manual.
- Unknown or malformed projection metadata fails loud and never silently downgrades to manual behavior.
- Contracts are data, not executable behavior.

### 3.2 ProjectionContract

A candidate must represent all DPA-300 §5.2 fields, including target identity, document form, renderer identity and versions, ordered sources and configuration, target semantics and version, lifecycle/freshness/evidence policies, fingerprint algorithm and domain version, and migration compatibility version.

For a region target it must additionally represent parent document identity, region identity, parent partition-contract identity and payload target semantics. Region entries must not independently configure partition boundaries, malformed-boundary behavior or write ownership.

### 3.3 Parent-entry PartitionContract

A multi-region document must declare exactly one partition contract on its parent registry entry. The contract must explain the complete ordered region set, every region owner class, projected-region selection, boundaries, separator ownership, normalization, encoding, line endings, adjacency, malformed cases, complete-byte ownership, fingerprinting and compatibility.

Projected-region entries reference this parent contract. They do not carry competing boundary or writer authority.

### 3.4 Validation

The Probe covers the DPA-300 §6 rejection classes that are representable at parser/validator scope, including unknown versions, ambiguous identities, dangling references, absent or overlapping regions, unowned bytes, forbidden executable content, unsupported renderer identifiers, incomplete target semantics and silent fallback.

Parser acceptance never proves runtime semantic implementation.

## 4. Execution preconditions

Before execution:

1. record the current remote `origin/main` SHA;
2. synchronize a clean local checkout to that exact ref;
3. identify every relevant registry reader, parser, validator and normalization path;
4. record current manual-entry shape and supported schema/version behavior;
5. select a safe isolated fixture-loading path;
6. freeze the Lab manual and fixture revisions;
7. materialize fixtures only after semantic-to-serialized-field reconciliation;
8. record cleanup and rollback actions;
9. confirm that no production registry or protected planning path can be changed.

If a safe isolated path cannot be established, all cases requiring loading are `BLOCKED`.

## 5. Case matrix

### Control

| Case | Purpose | Required interpretation |
|---|---|---|
| P001-C001 | Current-format manual entry | Must pass before DPA cases support conclusions; failure blocks the harness |

### Valid candidates

| Case | Purpose | Required interpretation |
|---|---|---|
| P001-C002 | Minimal full-target ProjectionContract | Compatibility observation only |
| P001-C003 | Parent entry with one complete PartitionContract | Tests parent location, exactly-one rule and complete contract shape |
| P001-C004 | Region ProjectionContract referencing parent and partition | Tests reference and inheritance representation without duplicated boundary policy |

### Required fields, schema and identity

| Case | Purpose | Expected behavior when schema support is claimed |
|---|---|---|
| P001-C005 | Projection field missing | Reject before rendering or planning |
| P001-C006 | Partition field missing | Reject before rendering or planning |
| P001-C007 | Unknown schema | Fail loud; no manual fallback or partial registration |
| P001-C008 | Unknown schema/compatibility version | Fail loud; no downgrade |
| P001-C009 | Unknown top-level field | Record strict rejection, warning, explicit ignore or silent acceptance separately |
| P001-C010 | Duplicate contract identity | Reject ambiguity; no invented last-writer-wins rule |
| P001-C011 | Missing or ambiguous target identity | Reject; no inference from path or ambient state |

### Parent and partition relationships

| Case | Purpose | Expected behavior |
|---|---|---|
| P001-C012 | Dangling parent identity | Reject |
| P001-C013 | Dangling partition-contract reference | Reject |
| P001-C014 | Region absent from parent ordered list | Reject |
| P001-C015 | More than one partition contract on parent | Reject |
| P001-C016 | Duplicate region identity | Reject |
| P001-C017 | Overlapping region/boundary declaration | Reject |
| P001-C018 | Partition metadata leaves unexplained bytes | Reject |
| P001-C019 | Ordering or adjacency contradiction | Reject |
| P001-C020 | Encoding/normalization declaration missing | Reject: DPA-300 §5.3 requires encoding, normalization and line-ending behavior; no default may be inferred |
| P001-C021 | Region independently declares boundary representation | Reject |
| P001-C022 | Region declares configurable non-lifecycle writer | Reject |

### Static and complete declarative form

| Case | Purpose | Expected behavior |
|---|---|---|
| P001-C023 | Unknown renderer identifier | MUST fail loud in resolution, validation or planning. The owning stage remains `NEEDS_MAIN_REPO_VALIDATION`; if the registry path does not prove the ultimate rejection, record `PARTIAL`, never `PASS` or support |
| P001-C024 | Executable import path or dynamic expression | Reject |
| P001-C025 | Ordered source list changed | Preserve order and expose semantic difference where normalized representation is available |
| P001-C026 | Output-affecting configuration omitted | Reject or expose missing required declaration; never infer ambient configuration silently |
| P001-C027 | Unknown policy identifier | Record reject/defer/ignore behavior without inferring policy implementation |

### Discovery extension

If any case reveals an additional registry reader, parser, validator, loader or normalization path:

- record exact symbol and path;
- do not expand scope silently;
- classify whether the current case must be repeated through that path;
- amend the inventory and rerun obligations before a Probe-level conclusion.

## 6. Observation record

For every case, record separately:

- parser result;
- validator result;
- normalized representation or hash;
- diagnostic class and bounded diagnostic;
- return code or API result;
- changed-path manifest;
- partial-state creation, if any;
- cleanup result;
- exact main-repository, manual and fixture refs.

The report must distinguish unsupported schema rejection from field-level semantic validation.

## 7. Always-significant failures

The following are prohibited:

- unknown DPA metadata silently treated as a manual entry;
- partial registration after rejection;
- identity inferred contrary to fixture data;
- malformed region treated as full-target ownership;
- unknown version silently treated as current;
- destructive normalization that loses required identity or order;
- executable or dynamic registry content accepted as behavior;
- region metadata creating competing boundary or writer authority;
- diagnostics leaking unrelated repository content.

## 8. Evidence set

Execution must produce:

- execution manifest and environment identity;
- exact main-repository ref;
- exact Lab manual and fixture refs;
- parser/validator/reader inventory;
- command or API invocation records;
- per-case input hashes;
- parse, validation and normalized-output observations;
- bounded diagnostics;
- changed-path and cleanup records;
- interpretation report;
- Maintainer adjudication record after review.

Evidence records behavior; it does not become registry, lifecycle or acceptance authority.

## 9. Outcome aggregation

- `NOT_RUN`: no local execution.
- `BLOCKED`: exact ref, safe harness, parser/validator path or required tooling cannot be established.
- `FAIL`: prohibited fallback, partial registration, identity/order loss, executable-content acceptance or a mandatory negative rejection failure occurs.
- `PARTIAL`: bounded compatibility is measured, but the proposed representation is unsupported in part or parser and validator stages cannot be distinguished.
- `PASS`: the control succeeds, every mandatory case executes, mandatory rejection behavior is observed and required evidence is complete.

A Probe-level `PASS` is parser/validator compatibility evidence only. It is not full DPA-300 runtime conformance.

## 10. Cleanup and repeatability

Each case runs against isolated fixture state. Cleanup must remove fixture registrations and temporary generated files, preserve only declared evidence, and verify that production registry and protected planning paths are unchanged.

Required repetitions:

- one clean manual control;
- one complete fixture-set run;
- a second run after cleanup where safe;
- explicit comparison of stable and variable fields.

Any main-repository ref, fixture revision or normative-expectation change requires impact analysis and a new exact execution identity.

## 11. Adjudication

For every discrepancy, the Maintainer must classify whether:

1. current implementation supports the proposed representation;
2. required support is missing;
3. implementation conflicts with the DPA proposal;
4. a DPA assumption is falsified or incomplete;
5. the fixture or harness is defective;
6. another registry path was discovered;
7. evidence is insufficient.

The record must state whether architecture, implementation, fixture or evidence changes are required and whether PROBE-001 must be rerun.

## 12. Review readiness

This package is reviewable only when:

- exactly 27 declared cases exist, P001-C001 through P001-C027;
- every declared case maps to at least one fixture;
- every fixture maps to at least one declared case;
- DPA-300 §§4–6 and ADR-017 anchors are synchronized;
- provisional serialized mappings are clearly marked;
- no execution or conformance claim is present;
- the Lab gates pass.
