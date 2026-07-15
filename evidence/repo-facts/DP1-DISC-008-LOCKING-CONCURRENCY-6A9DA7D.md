# DP1 Discovery Record — DISC-008 Locking and Concurrency

Status: active
Classification: VERIFIED
Inspection date: 2026-07-15
Fact family: DISC-008
Repository: `vfi64/agentic-project-kit`
Validation ref: `6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

## Factual question

Which local mutation-lock and branch/pull-request serialization mechanisms exist at the validation ref?

## Inspected paths and symbols

- `src/agentic_project_kit/workspace_lock.py`
  - `acquire_workspace_lock`
  - `workspace_mutation_lock`
  - `WorkspaceLockBusy`
- `src/agentic_project_kit/transfer_repo_actions.py`
  - mutation-lock wrappers around repository actions
  - branch guards and remote mutation preflight
  - full-SHA guards
  - PR creation, wait, merge and administrative refresh paths
  - successor-package freshness ancestry checks
- `src/agentic_project_kit/transfer_operation_monitor.py`
- observed administrative refresh flow for handoff artifacts

## Observed result

1. The local workspace lock is a filesystem lock file created with exclusive creation under the configured `.agentic` temporary area.
2. Lock payload contains PID, command and acquisition timestamp.
3. A live foreign holder raises `WorkspaceLockBusy`; a dead or unreadable stale holder can be removed and replaced with a warning.
4. The lock is reentrant inside the same process through a per-path depth counter.
5. Outermost release removes the lock file; nested release only decrements the depth.
6. `workspace_mutation_lock` is a semantic alias over the same acquire/release lifecycle.
7. Multiple repository mutation actions in `transfer_repo_actions.py`, including pull, push, branch deletion, PR merge and administrative refresh, are wrapped in the local mutation lock.
8. Branch guards distinguish allowed feature/admin mutation from prohibited direct main mutation for relevant operations.
9. Guarded PR actions require or resolve full 40-character head SHAs; short SHAs are refused.
10. Push paths verify that the remote branch head matches local HEAD after mutation.
11. PR merge paths combine branch-state monitoring, expected-head guards, remote mutation preflight and post-merge follow-up.
12. Successor-package freshness checks compare generated head with current head and allow only a bounded refresh-only descendant path.
13. Administrative handoff refresh is serialized as a dedicated branch/PR workflow and rejects or recovers several duplicate/stale branch states.
14. No repository-global cross-PR projection-target lease, target-hash reservation or merge-queue-specific DPA mechanism was observed.

## Limitations and unresolved questions

- This record does not prove complete mutation-lock coverage across every command.
- GitHub branch-protection and required-check settings are external configuration and were not inferred from source code.
- It does not judge whether the observed guards satisfy DPA-600 or the future projection refresh workflow.
- No projection plan fingerprint or target-content stale-plan check exists in the inspected vocabulary.

## Related assumptions

- A-005 — refresh workflow and stale-plan enforcement.

## Later Probe or Assessment obligation

After DPA-300 and DPA-600 define plan identity and serialization, exercise local reentrancy, stale plan rejection, competing refresh PRs and exact-head enforcement without introducing a second lock or workflow subsystem.

## No-generalization note

`VERIFIED` applies only to the inspected local lock and transfer-workflow behavior at the exact validation ref. This record is evidence, not a concurrency sufficiency judgment.
