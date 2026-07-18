# PROBE-001 Fixture Manifest

Status: draft

Status-date: 2026-07-18

Manual: `probes/PROBE-001-MANUAL.md`

Execution-state: not run

## 1. Fixture rules

- Every fixture has a stable identifier and revision.
- Serialized syntax is provisional until the exact-ref parser and validator are re-inspected locally.
- Each negative fixture differs from its valid parent by exactly one declared mutation unless the case explicitly tests compound ambiguity.
- Fixture files MUST NOT contain production secrets or repository-specific absolute paths.
- Every executed fixture MUST have a recorded content hash.
- Parser acceptance, validator acceptance and runtime semantic support are distinct conclusions.

## 2. Fixture set

Fixture-set-id: `PROBE-001-FIXTURES`

Fixture-set-revision: `draft-2026-07-18`

| Fixture ID | Parent | Purpose | Required semantic fields | Provisional serialization | Cases |
|---|---|---|---|---|---|
| F001-MANUAL-VALID | none | Current-format compatibility control | exact current manual-entry requirements | yes, pending exact-ref inspection | P001-C001 |
| F001-PROJECTION-MIN | none | Minimal proposed ProjectionContract | schema, version, contract identity, source, target, renderer, target semantics, policy/lifecycle references, partition or full-target mode | yes | P001-C002 |
| F001-PARTITION-MIN | none | Minimal proposed PartitionContract | schema, version, partition identity, target identity, region/boundaries, encoding, ownership/policy identity | yes | P001-C003 |
| F001-PROJECTION-MISSING-REQUIRED | F001-PROJECTION-MIN | Missing required projection field | one declared required field removed | yes | P001-C004 |
| F001-PARTITION-MISSING-REQUIRED | F001-PARTITION-MIN | Missing required partition field | one declared required field removed | yes | P001-C005 |
| F001-UNKNOWN-SCHEMA | F001-PROJECTION-MIN | Unknown schema identifier | all valid fields retained except schema identifier | yes | P001-C006 |
| F001-UNKNOWN-VERSION | F001-PROJECTION-MIN | Unsupported schema version | all valid fields retained except version | yes | P001-C007 |
| F001-UNKNOWN-FIELD | F001-PROJECTION-MIN | Unknown top-level field behavior | valid projection plus one unknown field | yes | P001-C008 |
| F001-DUPLICATE-ID-A | F001-PROJECTION-MIN | First duplicate identity entry | valid projection identity | yes | P001-C009 |
| F001-DUPLICATE-ID-B | F001-PROJECTION-MIN | Conflicting duplicate identity entry | same identity, one conflicting semantic field | yes | P001-C009 |
| F001-TARGET-ABSENT | F001-PROJECTION-MIN | Missing target identity | target field removed | yes | P001-C010 |
| F001-TARGET-AMBIGUOUS | F001-PROJECTION-MIN | Ambiguous target identity | two conflicting target representations | yes | P001-C010 |
| F001-REGION-VALID | F001-PARTITION-MIN | Valid registered-region declaration | deterministic region identity and boundaries | yes | P001-C011 |
| F001-REGION-MALFORMED | F001-REGION-VALID | Malformed region | one boundary or identity violation | yes | P001-C012 |
| F001-ENCODING-ABSENT | F001-PARTITION-MIN | Missing partition encoding | encoding removed | yes | P001-C013 |
| F001-RENDERER-ID | F001-PROJECTION-MIN | Renderer identifier preservation | syntactically valid unresolved identifier | yes | P001-C014 |
| F001-POLICY-UNKNOWN | F001-PROJECTION-MIN | Unknown policy identifier behavior | valid shape with unknown policy identifier | yes | P001-C015 |

## 3. Required fixture metadata

Every serialized fixture MUST carry or be accompanied by:

- fixture ID;
- fixture revision;
- parent fixture ID where applicable;
- declared mutation;
- governing case ID;
- intended expected-result class;
- serialization format;
- content hash;
- creation ref;
- last normative synchronization ref.

## 4. Provisional field model

The fixture designer MUST reconcile this provisional field model against the exact DPA-300 and ADR-017 serialization contract before creating executable files.

### ProjectionContract candidate

```text
schema
schema_version
contract_id
source
source_selector
source_semantics
target
target_semantics
renderer_id
lifecycle_policy_id
freshness_policy_id
gate_policy_id
partition_id | full_target
registered_region
```

### PartitionContract candidate

```text
schema
schema_version
partition_id
target
region_id
region_boundaries
encoding
owner_identity
policy_id
```

The exact field names, nesting and allowed values remain `NEEDS_MAIN_REPO_VALIDATION` until current-ref parser inspection and normative serialization reconciliation are complete.

## 5. Mutation catalogue

| Mutation ID | Mutation | Single-change rule |
|---|---|---|
| M001 | remove one required field | no other bytes changed except syntax repair required to keep the container parseable |
| M002 | replace schema identifier | all other semantic values unchanged |
| M003 | replace schema version | all other semantic values unchanged |
| M004 | add one unknown top-level field | valid parent retained |
| M005 | duplicate stable identity with one conflict | conflict field declared |
| M006 | remove target identity | no path-based replacement added |
| M007 | add conflicting target representation | original target retained |
| M008 | corrupt one region boundary or region identity | corruption declared |
| M009 | remove encoding declaration | no default inserted in fixture |
| M010 | replace policy identifier | shape unchanged |

## 6. Execution materialization gate

Executable fixture files MUST NOT be created until:

1. the current main-repository parser and validator paths are identified;
2. the accepted serialization format is recorded;
3. DPA-300 and ADR-017 field requirements are rechecked;
4. safe isolated fixture loading is confirmed;
5. exact fixture filenames and locations are selected;
6. this manifest is updated with concrete file paths and hashes.

Materialization is preparation, not execution.

## 7. Completeness check

Before review, verify:

- every P001-C001 through P001-C015 case maps to at least one fixture;
- every negative fixture names a valid parent and one mutation;
- target identity, registered region, encoding, schema/version, unknown field and duplicate identity are covered;
- no fixture implies renderer, lifecycle or gate implementation;
- all concrete parser mappings remain `NEEDS_MAIN_REPO_VALIDATION`.