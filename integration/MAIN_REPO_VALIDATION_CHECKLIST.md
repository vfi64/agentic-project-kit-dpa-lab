# Main Repository Validation Checklist

Status: active

Status-date: 2026-07-18

## 1. Purpose

This is the canonical CSC, namespace-profile and external-habitability validation checklist for the DPA Lab.

It prepares read-only remote inspection and later local execution against `vfi64/agentic-project-kit` and an approved external repository such as `Comm-SCI-Control-private`. It does not record completed validation, adoption or implementation evidence.

The checklist MUST extend existing main-repository authorities and MUST NOT become a parallel runtime registry, state store, evidence system, lifecycle or gate mechanism.

## 2. Validation identity

Before any checked item can support a current claim:

- [ ] Record current remote `origin/main` SHA.
- [ ] Compare it with historical Discovery ref `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`.
- [ ] Record current Lab ref and checklist revision.
- [ ] Confirm the same exact main-repository ref locally before mutation or executed Probe work.
- [ ] Record worktree cleanliness and environment identity.
- [ ] Freeze exact refs according to `probes/EXACT_REF_FREEZE_PROCEDURE.md`.
- [ ] Record every remote-only conclusion as provisional until local confirmation.

## 3. Bootstrap and authority

- [ ] Identify the current bootstrap entry points and source-of-truth files.
- [ ] Verify repository identity and Workspace-root resolution.
- [ ] Verify boot-source classification and boot contract.
- [ ] Verify no Lab file is treated as main-repository runtime authority.
- [ ] Verify no external repository receives an undeclared second registry, lifecycle, state or gate authority.
- [ ] Verify configuration, Direction and rule authority order.
- [ ] Verify failures are loud when bootstrap identity or authority is ambiguous.

## 4. Workspace and namespace resolution

- [ ] Inventory all direct documentation-registry path literals.
- [ ] Inventory all direct `.agentic/`, `docs/`, `tmp/`, transfer, state, lock and handoff path literals relevant to adoption.
- [ ] Verify each path is resolved through the current Workspace or namespace-profile authority where required.
- [ ] Verify legacy-profile behavior remains compatible.
- [ ] Verify namespace-profile behavior changes only declared roots and aliases.
- [ ] Verify no silent fallback to legacy paths when the namespace profile is active.
- [ ] Verify unknown profile, missing root or ambiguous alias fails loud.
- [ ] Verify path normalization does not escape the repository or declared root.
- [ ] Verify symlink, case-sensitivity and relative-path behavior where applicable.
- [ ] Verify protected planning paths remain protected under both profiles.

## 5. Documentation registry

- [ ] Identify the exact registry files, parser, validator, loaders and normalization paths.
- [ ] Verify the current manual-entry format and compatibility behavior.
- [ ] Verify schema/version behavior and unknown-field policy.
- [ ] Verify target identity and registered-region representation.
- [ ] Verify parent-entry `PartitionContract` representability.
- [ ] Verify duplicate, dangling, overlapping and ambiguous entries fail loud.
- [ ] Verify registry resolution uses Workspace/namespace authority rather than fixed repository literals.
- [ ] Verify registry diagnostics are bounded and do not leak unrelated content.
- [ ] Execute PROBE-001 only after exact-ref freeze and local isolation are complete.

## 6. Lifecycle, findings and reports

- [ ] Identify lifecycle entry points and ordered phases actually implemented.
- [ ] Identify all content writers for governed targets, including `CURRENT_HANDOFF.md`.
- [ ] Verify lifecycle remains sole writer for projected payload, partition bytes and acceptance state.
- [ ] Verify lifecycle findings use the existing finding authority.
- [ ] Verify lifecycle reports include per-entry status, target identity, relevant findings and limitations.
- [ ] Verify handoff-context fields are complete and not reconstructed from evidence alone.
- [ ] Verify report paths resolve under both legacy and namespace profiles.
- [ ] Verify report generation is read-only unless an explicit lifecycle mutation is authorized.
- [ ] Verify unavailable mandatory state fails loud rather than disappearing from reports.
- [ ] Execute PROBE-002 only after the writer inventory and isolation method are complete.

## 7. Transfer and handoff

- [ ] Identify transfer command entry points and communication files.
- [ ] Verify local-to-LLM and LLM-to-local ownership and state transitions.
- [ ] Verify transfer paths resolve through Workspace/namespace authority.
- [ ] Verify the current handoff reader/writer graph.
- [ ] Verify no writer bypasses lifecycle ownership for a selected projection target.
- [ ] Verify protected-diff and handoff validation gates remain active.
- [ ] Verify stale, missing or mismatched transfer state fails loud.
- [ ] Verify repeated transfer operations are idempotent or explicitly versioned.
- [ ] Verify no external repository adoption silently imports Lab state or historical transfer artifacts.

## 8. State and locks

- [ ] Inventory state files, acceptance-state candidates and lock locations.
- [ ] Verify state and lock paths resolve correctly under each namespace profile.
- [ ] Verify local lock scope, ownership, release and stale-lock behavior.
- [ ] Verify same-process reentrancy behavior is explicit and bounded.
- [ ] Verify local locks are not represented as cross-ref serialization authority.
- [ ] Verify unresolved recovery or stale ownership blocks unsafe mutation.
- [ ] Verify cleanup leaves no unexplained lock or temporary state.

## 9. Renderer readiness

- [ ] Identify static renderer mapping and lifecycle caller.
- [ ] Verify registry data cannot select arbitrary executable code.
- [ ] Verify immutable source/configuration boundary.
- [ ] Verify prohibited filesystem, network, subprocess, lock, state and nested-renderer capabilities.
- [ ] Verify one invocation produces one target payload.
- [ ] Verify registered-region output excludes partition and preserved bytes.
- [ ] Verify determinism and fresh-process repeatability.
- [ ] Verify semantic-version and implementation-evidence separation.
- [ ] Execute the DPA-400 renderer Probe only after capability observation is safe.

## 10. GUI and command readiness

- [ ] Identify GUI project-selection and active-workspace resolution.
- [ ] Verify GUI commands use the same Workspace and namespace-profile authority as CLI commands.
- [ ] Verify GUI does not cache or invent a second registry, transfer or lifecycle model.
- [ ] Verify active repository identity is visible and unambiguous.
- [ ] Verify unsupported external-repository operations fail loud.
- [ ] Verify protected operations require the same plans, locks and gates as CLI paths.
- [ ] Verify logs and reports remain bounded and linked to exact repository identity.

## 11. Removed-source and legacy-fallback audit

- [ ] Inventory removed, superseded and deprecated source paths relevant to bootstrap, registry, lifecycle and transfer.
- [ ] Search code, docs, tests, workflows and GUI configuration for remaining references.
- [ ] Verify deprecated aliases are explicit, bounded and observable.
- [ ] Verify removed sources cannot silently regain authority.
- [ ] Verify no fallback reads stale copies when the canonical path is missing.
- [ ] Verify error messages identify the missing canonical source rather than silently proceeding.

## 12. External-repository adoption

- [ ] Select an approved disposable or controlled external repository.
- [ ] Record its exact ref and clean pre-adoption state.
- [ ] Apply only the documented namespace profile and approved initialization/adoption steps.
- [ ] Verify bootstrap, registry, lifecycle reports, transfer, handoff, state, locks, GUI and audits.
- [ ] Verify no kit-internal repository-name or path assumption remains.
- [ ] Verify no silent legacy fallback occurs.
- [ ] Verify cleanup or rollback can restore the external repository.
- [ ] Preserve bounded habitability evidence.
- [ ] Repeat with a second independent run or operator where feasible.

## 13. Repeatability and evidence

- [ ] Use `probes/EVIDENCE_CAPTURE_PROCEDURE.md` for every executed validation family.
- [ ] Record exact commands, return codes, relevant hashes and changed-path manifests.
- [ ] Preserve observation, interpretation and adjudication separately.
- [ ] Run a second clean execution for deterministic paths where safe.
- [ ] Explain every variable field between runs.
- [ ] Treat any changed ref or fixture revision as requiring impact analysis and possible refreeze.
- [ ] Do not convert checklist completion into a conformance claim without evidence and adjudication.

## 14. Stop conditions

Stop and record `blocked` when:

- [ ] remote and local refs differ;
- [ ] the worktree is not safely isolatable;
- [ ] registry, lifecycle, writer, renderer, state or lock ownership is ambiguous;
- [ ] cleanup cannot be proven;
- [ ] a protected path would be mutated during preparation;
- [ ] a required observation hook is unavailable;
- [ ] an additional authority or hidden fallback is discovered;
- [ ] a proposed portability change would alter a Probe subject;
- [ ] evidence is insufficient to distinguish absence, incompatibility and unavailable measurement.

## 15. Completion

This checklist is complete only when:

- [ ] every applicable item has evidence-backed `complete`, justified `not-required` or explicit `blocked` status;
- [ ] all exact refs and limitations are recorded;
- [ ] Probe outcomes and adjudications are linked without being collapsed into this checklist;
- [ ] external-habitability conclusions are bounded to the tested repository and profile;
- [ ] no second runtime authority or silent legacy fallback was introduced.
