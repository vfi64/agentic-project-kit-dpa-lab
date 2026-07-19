# PROBE-001 Fixture Manifest

Status: draft

Status-date: 2026-07-19

Manual: `probes/PROBE-001-MANUAL.md`

Execution-state: not run

## 1. Fixture rules

- Every fixture has a stable identifier and revision.
- Serialized syntax is provisional until the exact-ref parser and validator are re-inspected locally.
- Each negative fixture differs from its valid parent by exactly one declared mutation unless a case explicitly tests a relational inconsistency.
- Fixture files MUST NOT contain production secrets or repository-specific absolute paths.
- Every executed fixture MUST have a recorded content hash.
- Parser acceptance, validator acceptance and runtime semantic support are distinct conclusions.
- A multi-region document has exactly one parent-entry `PartitionContract`; projected-region entries reference it and MUST NOT duplicate boundary or write-owner policy.

## 2. Fixture set

Fixture-set-id: `PROBE-001-FIXTURES`

Fixture-set-revision: `draft-2026-07-19-r3`

| Fixture ID | Parent | Purpose | Governing requirement | Cases |
|---|---|---|---|---|
| F001-MANUAL-VALID | none | Current-format compatibility control | exact current manual-entry requirements | P001-C001 |
| F001-PROJECTION-FULL-MIN | none | Minimal full-target ProjectionContract | DPA-300 §5.2 | P001-C002 |
| F001-PARENT-PARTITION-MIN | none | Parent entry with exactly one complete PartitionContract | DPA-300 §5.3; ADR-017 | P001-C003 |
| F001-REGION-PROJECTION-MIN | F001-PARENT-PARTITION-MIN | Projected region referencing parent and partition contract | DPA-300 §5.2; ADR-017 | P001-C004 |
| F001-PROJECTION-MISSING-REQUIRED | F001-PROJECTION-FULL-MIN | Remove one ProjectionContract required field | DPA-300 §§5.2,6 | P001-C005 |
| F001-PARTITION-MISSING-REQUIRED | F001-PARENT-PARTITION-MIN | Remove one PartitionContract required field | DPA-300 §§5.3,6 | P001-C006 |
| F001-UNKNOWN-SCHEMA | F001-PROJECTION-FULL-MIN | Unknown contract schema | DPA-300 §§5.1,6 | P001-C007 |
| F001-UNKNOWN-VERSION | F001-PROJECTION-FULL-MIN | Unsupported schema or compatibility version | DPA-300 §§5.4,6 | P001-C008 |
| F001-UNKNOWN-FIELD | F001-PROJECTION-FULL-MIN | Unknown top-level projection field | ADR-017 consequence; exact parser behavior | P001-C009 |
| F001-DUPLICATE-ID-A | F001-PROJECTION-FULL-MIN | First contract identity | DPA-300 §6 | P001-C010 |
| F001-DUPLICATE-ID-B | F001-PROJECTION-FULL-MIN | Same identity with one semantic conflict | DPA-300 §6 | P001-C010 |
| F001-TARGET-ABSENT | F001-PROJECTION-FULL-MIN | Missing target identity | DPA-300 §§5.2,6 | P001-C011 |
| F001-TARGET-AMBIGUOUS | F001-PROJECTION-FULL-MIN | Conflicting target identity | DPA-300 §6 | P001-C011 |
| F001-REGION-DANGLING-PARENT | F001-REGION-PROJECTION-MIN | Unknown parent document identity | ADR-017 | P001-C012 |
| F001-REGION-DANGLING-PARTITION | F001-REGION-PROJECTION-MIN | Unknown partition-contract identity | ADR-017 | P001-C013 |
| F001-REGION-NOT-IN-PARENT | F001-REGION-PROJECTION-MIN | Region absent from ordered complete region list | DPA-300 §6; ADR-017 | P001-C014 |
| F001-PARENT-DUPLICATE-PARTITION | F001-PARENT-PARTITION-MIN | Second partition contract on same parent | ADR-017 | P001-C015 |
| F001-PARTITION-DUPLICATE-REGION | F001-PARENT-PARTITION-MIN | Duplicate region identity in ordered list | DPA-300 §6; ADR-017 | P001-C016 |
| F001-PARTITION-OVERLAP | F001-PARENT-PARTITION-MIN | Overlapping region or boundary declaration | DPA-300 §6; ADR-017 | P001-C017 |
| F001-PARTITION-UNOWNED-BYTES | F001-PARENT-PARTITION-MIN | Complete-byte ownership does not explain target | DPA-300 §§5.3,6; ADR-017 | P001-C018 |
| F001-PARTITION-ORDER-CONFLICT | F001-PARENT-PARTITION-MIN | Ordering or adjacency contradiction | DPA-300 §5.3; ADR-017 | P001-C019 |
| F001-PARTITION-ENCODING-ABSENT | F001-PARENT-PARTITION-MIN | Encoding/normalization declaration removed with no inferred default | DPA-300 §5.3 | P001-C020 |
| F001-REGION-INDEPENDENT-BOUNDARY | F001-REGION-PROJECTION-MIN | Region entry duplicates boundary representation | DPA-300 §§5.2,6; ADR-017 | P001-C021 |
| F001-REGION-CONFIGURABLE-WRITER | F001-REGION-PROJECTION-MIN | Region entry declares non-lifecycle write owner | DPA-300 §5.2; ADR-017 | P001-C022 |
| F001-RENDERER-ID-UNKNOWN | F001-PROJECTION-FULL-MIN | Unknown static renderer identifier; ultimate fail-loud stage remains to be inventoried | DPA-300 §§5.4,6 | P001-C023 |
| F001-EXECUTABLE-IMPORT | F001-PROJECTION-FULL-MIN | Executable import path or dynamic expression | DPA-300 §§4.1,5.4,6 | P001-C024 |
| F001-SOURCE-ORDER-CHANGED | F001-PROJECTION-FULL-MIN | Same sources in different declared order | DPA-300 §§5.2,5.5 | P001-C025 |
| F001-CONFIG-UNDECLARED | F001-PROJECTION-FULL-MIN | Output-affecting configuration omitted | DPA-300 §§5.2,5.5,6 | P001-C026 |
| F001-POLICY-UNKNOWN | F001-PROJECTION-FULL-MIN | Unknown policy identifier | DPA-300 §§5.2,6 | P001-C027 |

## 3. Required semantic model

### 3.1 ProjectionContract — full target

The candidate MUST represent contract schema version, stable contract identity, one target identity, primary document form, renderer identifier/interface/semantic versions, ordered canonical-source identities, ordered contract-declared configuration, target semantics/version, lifecycle/freshness/evidence policies, fingerprint algorithm/domain version, migration compatibility version and explicit full-target mode.

### 3.2 ProjectionContract — region target

In addition to applicable projection fields, the candidate MUST represent only parent document identity, region identity, parent partition-contract identity and projected payload target semantics. It MUST NOT independently declare boundary ownership or representation, ordering or malformed-boundary behavior, or a configurable write owner.

### 3.3 Parent-entry PartitionContract

The parent registered-document entry MUST carry exactly one candidate contract representing partition identity/schema, parent identity, ordered complete region identities, owner classes, projected-region selection, boundaries, separator ownership, encoding/normalization/line endings, adjacency/malformed behavior, complete-byte ownership, fingerprinting and compatibility.

The exact field names, nesting and allowed values remain `NEEDS_MAIN_REPO_VALIDATION` until current-ref parser inspection.

## 4. Required fixture metadata

Every materialized fixture MUST carry or be accompanied by fixture ID/revision, parent fixture where applicable, declared mutation, governing case and anchors, expected-result class, serialization format, content hash, creation ref and last normative synchronization ref.

## 5. Mutation catalogue

| Mutation ID | Mutation | Isolation rule |
|---|---|---|
| M001 | remove one required field | only syntax repair needed to keep the container parseable |
| M002 | replace schema or compatibility version | all other semantic values unchanged |
| M003 | add one unknown top-level field | valid parent retained |
| M004 | duplicate stable identity with one conflict | conflicting field declared |
| M005 | remove or conflict target identity | no ambient replacement added |
| M006 | break parent or partition reference | one reference changed |
| M007 | remove region from ordered parent list | region projection unchanged |
| M008 | add second parent partition contract | first contract unchanged |
| M009 | duplicate or overlap one region | exact conflicting region declared |
| M010 | create one unexplained byte domain | other ownership declarations unchanged |
| M011 | alter ordering or adjacency | region identities unchanged |
| M012 | remove encoding/normalization field | no default inserted |
| M013 | add forbidden region boundary or writer field | parent contract unchanged |
| M014 | replace renderer or policy identifier | shape unchanged |
| M015 | add executable or dynamic content | one prohibited value added |
| M016 | reorder canonical sources | source set unchanged |
| M017 | remove one output-affecting configuration identity | other contract fields unchanged |

## 6. Execution materialization gate

Executable fixture files MUST NOT be created until the current parser/validator/reader paths, actual serialization and safe loading mechanism are identified; semantic fields are mapped without weakening DPA-300 or ADR-017; the manual control succeeds; exact paths are selected; and concrete hashes are recorded.

Materialization is preparation, not execution.

## 7. Completeness check

Before review, verify:

- exactly 27 declared cases exist, P001-C001 through P001-C027;
- every declared case maps to at least one fixture;
- every fixture maps to at least one declared case;
- each negative fixture names its parent, one mutation and exact normative anchor;
- the parent-entry location and exactly-one rule are tested;
- full ordered region coverage, ownership, boundaries, separators, encoding and complete-byte explanation are tested;
- dangling references, absent regions, duplicates, overlap, unowned bytes and independent region policy are tested;
- executable content and silent manual fallback are tested;
- no fixture implies renderer, lifecycle or gate implementation;
- all concrete parser mappings remain `NEEDS_MAIN_REPO_VALIDATION`.
