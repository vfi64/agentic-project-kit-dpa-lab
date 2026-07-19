# Main-Repository Current-Ref Evidence — 2026-07-19

Status: verified-remote

Status-date: 2026-07-19

Repository: `vfi64/agentic-project-kit`

Remote branch: `main`

Freshly read remote ref:

`6a9da7d363ae3f97f347b79a2679f6f848d8cdf3`

Commit subject:

`Refresh handoff state after PR1863 (#1864)`

## Evidence method

The ref was read again from the remote GitHub repository after final Package-P closure. It was not copied forward solely from the historical Discovery record.

The freshly observed ref equals the recorded DP1 Discovery baseline. Equality does not convert the old observation into current evidence by itself; this record is the new remote-read evidence.

## Scope of verification

Verified remotely:

- repository identity;
- default branch identity;
- current remote `main` commit SHA;
- commit subject;
- selected source files and symbols needed for local materialization planning.

Not verified by this record:

- local checkout equality;
- local worktree cleanliness;
- local Python environment or dependency identity;
- executable command behavior;
- test or gate outcomes in the main repository;
- complete reader, writer, renderer, acceptance-state, recovery, gate or evidence path inventories;
- Probe execution or DPA conformance.

## Required local confirmation

Before executable fixture materialization or Probe execution, the Mac phase MUST record:

1. `git ls-remote origin refs/heads/main`;
2. local `git rev-parse HEAD`;
3. local `git status --short`;
4. equality of local HEAD and the then-current remote `main` SHA;
5. environment identity;
6. any difference from this recorded remote ref.

If remote `main` moves before local confirmation, this record remains historical evidence and a new current-ref record is required.

## Authority boundary

This file is repository-fact evidence only. It is not runtime authority, acceptance state, Probe evidence, implementation authorization or a release of any frozen DPA-critical surface.
