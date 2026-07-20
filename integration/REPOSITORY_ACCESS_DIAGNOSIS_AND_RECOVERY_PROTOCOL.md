# Repository Access Diagnosis and Recovery Protocol

Status: active planning contract
Status-date: 2026-07-20
Authority: non-normative Lab operational-hardening candidate
Target repository: `vfi64/agentic-project-kit`

## 1. Purpose

This protocol prevents an LLM or automation from falsely claiming loss of repository access when repository, ref and file access have not been diagnosed completely.

It records a concrete regression case observed on 2026-07-20: repository access and permissions remained intact, but the agent asserted that the required specification files were inaccessible without completing repository, ref, path and chunked-read diagnostics.

This protocol is not a DPA normative contract, creates no runtime authority and authorizes no production implementation. It is a mandatory Kit hardening candidate that MUST be carried into controlled-import planning and MUST NOT be dropped as incidental Lab process commentary.

## 2. Failure model

A failed or absent tool call does not prove loss of access. The diagnostic process MUST distinguish:

- connector unavailable;
- authentication or permission denial;
- repository not found;
- ref not found;
- path not found;
- target file too large for one response;
- transient tool failure;
- incomplete agent diagnosis;
- confirmed access.

## 3. Closed classification

Every access assessment MUST resolve to exactly one current classification:

- `ACCESS_CONFIRMED`
- `ACCESS_PARTIAL`
- `CONNECTOR_UNAVAILABLE`
- `PERMISSION_DENIED`
- `REPOSITORY_NOT_FOUND`
- `REF_NOT_FOUND`
- `PATH_NOT_FOUND`
- `TRANSIENT_TOOL_FAILURE`
- `DIAGNOSTIC_INCOMPLETE`

`PERMISSION_DENIED` MUST NOT be asserted without explicit permission evidence or an unambiguous remote denial.

An agent that has not completed the ladder in §4 MUST use `DIAGNOSTIC_INCOMPLETE`, not a stronger failure claim.

## 4. Mandatory diagnostic ladder

Before stating that repository content cannot be accessed, the agent or tool MUST perform, where capabilities permit:

1. **Connector check** — confirm the repository connector/tool is available.
2. **Identity and permission check** — resolve authenticated identity, repository metadata and reported read permission.
3. **Known-good default-ref read** — read a small known file such as `README.md` on the default branch.
4. **Target-ref read** — read the same known file on the requested branch, tag or exact commit.
5. **Canonical path discovery** — consult the repository's file map, index, manifest, PR changed-file list or repository search before declaring the target path absent.
6. **Target-file read** — read the requested file at the exact ref.
7. **Chunked continuation** — when output is truncated, continue with explicit line ranges until the complete file is read.
8. **Bounded retry** — retry a transient failed operation after rechecking repository and ref state.
9. **Evidence record** — record the resulting classification and the successful and failed steps.

A single failed file operation MUST NOT terminate the ladder unless it returns an unambiguous terminal classification.

## 5. Recovery rules

- If the repository metadata and known-good read succeed, permission loss is disproven for the tested scope.
- If the default-ref read succeeds but the target-ref read fails, classify the problem as ref-specific until disproven.
- If the target ref succeeds but one path fails, discover the canonical path before using `PATH_NOT_FOUND`.
- If a response is truncated, continue reading by line range; truncation is not access failure.
- If a tool call is not attempted, the result is `DIAGNOSTIC_INCOMPLETE`.
- If one call fails transiently while later calls succeed, the final classification is based on the completed ladder, and the transient failure remains contextual evidence only.

## 6. Minimum evidence schema

```yaml
repository: owner/name
connector: github
authenticated_identity: <login-or-unknown>
default_ref: main
target_ref: <branch-tag-or-sha>
repository_reachable: true|false
read_permission_reported: true|false|unknown
known_good_read:
  path: README.md
  ref: <ref>
  result: success|failure|not_run
target_read:
  path: <path>
  ref: <ref>
  result: success|failure|partial|not_run
chunk_ranges: []
classification: ACCESS_CONFIRMED
observed_errors: []
```

Evidence labels in this protocol are operational diagnosis vocabulary. They MUST NOT be added to DPA-100 document status, lifecycle state or consumer trust-state vocabulary.

## 7. Bootstrap and handoff requirements

A future Kit implementation SHOULD add a bounded repository-access self-check to bootstrap when repository work is required.

A handoff that depends on remote repository access SHOULD record:

- connector and authenticated identity;
- repository and exact ref;
- last confirmed head;
- last successful known-good read;
- last successful target-file read;
- current access classification;
- unresolved tool errors.

A successor MUST revalidate rather than treating historical access evidence as permanent authorization.

## 8. Planned Kit integration surfaces

Controlled Kit adoption MUST evaluate integration into existing authorities rather than creating a parallel subsystem:

- bootstrap/session-entry validation;
- repository and connector operations;
- diagnostic finding/report vocabulary;
- handoff package context;
- bounded evidence output;
- CLI and, where applicable, GUI diagnostics.

A candidate command may be exposed through an existing diagnostics or environment command family. The exact command name and implementation location remain `NEEDS_MAIN_REPO_VALIDATION`.

## 9. Acceptance criteria for the future Kit slice

The future Kit slice is incomplete until it demonstrates at least:

1. a single failed or omitted read cannot produce a false permission-loss claim;
2. repository, ref and path failures are distinguished;
3. large files are read through deterministic continuation;
4. evidence records the diagnostic ladder and terminal classification;
5. bootstrap and handoff consumers can reuse the result without treating it as permanent authority;
6. no second repository registry, evidence system or state authority is introduced;
7. regression coverage includes the 2026-07-20 false-access-loss case.

## 10. Import obligation

This artifact is a durable Kit hardening obligation.

During controlled import, the Maintainer MUST explicitly disposition it as one of:

- imported into an approved Kit work slice;
- superseded by a demonstrably equivalent existing Kit contract;
- rejected by a recorded Maintainer decision with rationale.

Silence, omission or Lab archival MUST NOT count as disposition.
