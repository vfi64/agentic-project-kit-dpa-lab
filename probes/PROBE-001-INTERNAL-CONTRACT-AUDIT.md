# PROBE-001 Internal Contract Audit

Status: active

Status-date: 2026-07-18

Audited artifacts:

- `probes/PROBE-001-MANUAL.md`
- `probes/PROBE-001-FIXTURE-MANIFEST.md`

Normative comparison set:

- `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md` §§4–6
- `decisions/DPA-ADR-017-PARENT-ENTRY-PARTITION-CONTRACT.md`

Execution-state: not run

## Verdict

`PASS_AFTER_CORRECTION`

The initial Probe package had a material representation defect: it modeled the PartitionContract as a region-oriented object with one region and target rather than exactly one complete contract stored on the parent registered-document entry. It also omitted several DPA-300 required ProjectionContract fields and mandatory relational rejection cases.

The package was corrected before fixture materialization or execution.

## Accepted corrections

1. The PartitionContract fixture is now parent-entry-owned.
2. The contract now covers the ordered complete region list, owner classes, projected-region selection, boundary and separator ownership, normalization, encoding, line endings, adjacency, malformed cases, complete-byte ownership, fingerprinting and compatibility.
3. Region projection entries now carry only parent identity, region identity, parent partition-contract identity and payload target semantics in addition to applicable projection fields.
4. Region entries are explicitly forbidden from declaring competing boundary policy or write ownership.
5. ProjectionContract coverage now includes document form, renderer interface and semantic versions, ordered sources and configuration, policy identifiers, fingerprint domain and migration compatibility.
6. Negative cases now cover dangling parent and partition references, missing region membership, multiple parent contracts, duplicate and overlapping regions, unexplained bytes, ordering conflicts, missing encoding, forbidden region-local boundary/writer declarations, executable content, source ordering and undeclared configuration.
7. Unknown renderer and policy identifiers are interpreted without claiming runtime support from parser acceptance.
8. Unsupported-schema rejection is separated from field-level semantic validation.

## Remaining intentional uncertainties

The following remain `NEEDS_MAIN_REPO_VALIDATION`:

- actual registry serialization;
- exact parser and validator symbols;
- whether parsing and semantic validation are separable;
- safe fixture-loading command or API path;
- normalization representation;
- current unknown-field behavior;
- current renderer and policy identifier validation location;
- all additional registry readers and loaders.

These uncertainties block executable fixture materialization but do not block the remote semantic manual.

## Scope conclusion

The corrected PROBE-001 package now tests the normative registry representation without selecting a concrete main-repository implementation shape. It introduces no parallel registry, lifecycle, renderer, state, gate or evidence authority and makes no execution claim.

## Follow-up

- Run Lab gates on the corrected package.
- Preserve the package at an exact Lab ref before external review or execution.
- Materialize executable fixtures only after current-ref and local parser/validator inspection.
- Begin PROBE-002 preparation independently; do not infer lifecycle behavior from PROBE-001 parser outcomes.