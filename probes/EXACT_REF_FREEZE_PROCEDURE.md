# Exact-Ref Freeze Procedure

Status: active

Status-date: 2026-07-18

## 1. Purpose

This procedure defines how a main-repository validation ref and the corresponding Lab Probe package are frozen before PROBE-001, PROBE-002 or the DPA-400 renderer Probe is executed.

A freeze records identity. It does not establish conformance, authorize mutation or create runtime authority.

## 2. Required identities

Every freeze record MUST identify:

- main repository: `vfi64/agentic-project-kit`;
- exact remote `origin/main` SHA;
- locally confirmed HEAD SHA;
- remote/local equality result;
- clean or explicitly dispositioned worktree state;
- Probe identifier and case range;
- exact Lab ref containing the manual, fixture manifest and shared execution contract;
- fixture-set ID and revision;
- execution environment identity;
- freeze timestamp as evidence metadata only;
- operator or automation identity;
- known limitations and blocked measurements.

## 3. Freeze sequence

1. Read the current remote `origin/main` SHA without mutation.
2. Record the current Lab branch/ref and all Probe-package file hashes.
3. Synchronize the local main-repository checkout.
4. Verify local HEAD equals the recorded remote SHA.
5. Verify the worktree is clean or record every pre-existing change and exclude the checkout from execution.
6. Revalidate the actual parser, lifecycle, writer, lock, renderer, state, finding and evidence paths needed by the selected Probe.
7. Confirm the isolated fixture workspace, cleanup source and observation hooks.
8. Materialize executable fixtures only after their manifest is updated with concrete paths and hashes.
9. Create one immutable freeze record before the first case runs.
10. Recheck all frozen identities immediately before execution.

## 4. Ref movement

The freeze becomes invalid when any of the following changes:

- main-repository SHA;
- Lab manual, fixture manifest or shared execution contract;
- executable fixture bytes;
- normative expected result affecting the selected cases;
- parser, lifecycle, renderer or command mapping used by the Probe;
- isolation, observation or cleanup mechanism in a way that can affect evidence.

When invalidated:

1. stop execution;
2. preserve completed evidence under the old execution identity;
3. perform impact analysis;
4. create a new freeze identity;
5. rerun every affected case.

Completed evidence MUST NOT be relabeled to the new ref.

## 5. Same-ref requirement

PROBE-001, PROBE-002 and renderer cases SHOULD use the same main-repository validation ref when technically safe and semantically appropriate.

A different ref is permitted only when the freeze record explains:

- why the prior ref cannot be used;
- which code or contracts changed;
- which prior cases are affected;
- which cases require rerun;
- why cross-Probe conclusions remain valid or must be limited.

## 6. Freeze states

A freeze record uses exactly one progress state:

- `pending` — identities are being collected;
- `complete` — all required identities and checks are recorded;
- `blocked` — equality, cleanliness, mapping, isolation or fixture materialization cannot be established;
- `superseded` — a later freeze replaces this one, while the original record remains immutable.

These are progress states, not repository-fact classifications and not Probe outcomes.

## 7. Prohibitions

A freeze record MUST NOT:

- claim that a Probe ran;
- claim implementation conformance;
- authorize writer or lifecycle changes;
- become acceptance state;
- replace Git identities with timestamps or branch names;
- silently move when `main` advances;
- overwrite an earlier execution identity.

## 8. Minimum freeze record template

```text
freeze_id:
probe_id:
case_scope:
main_repository:
remote_main_sha:
local_head_sha:
remote_local_equal:
worktree_state:
lab_repository:
lab_ref:
manual_hash:
fixture_manifest_hash:
shared_contract_hash:
fixture_set_id:
fixture_set_revision:
execution_environment:
isolation_identity:
cleanup_source_hash:
operator:
frozen_at:
limitations:
progress_state:
```
