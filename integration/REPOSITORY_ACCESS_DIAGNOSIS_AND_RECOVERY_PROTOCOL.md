# Repository Capability Diagnosis and Recovery Protocol

Status: active planning contract
Status-date: 2026-07-20
Authority: non-normative Lab operational-hardening candidate
Target repository: `vfi64/agentic-project-kit`

## 1. Purpose

This protocol prevents an LLM or automation from falsely claiming loss of repository capability when the failed capability has not been diagnosed completely. It also prevents a confirmed write or publish blocker from being misrepresented as an incomplete read diagnosis.

Two distinct regression cases were observed on 2026-07-20:

1. **RC-READ-001 — false read-access loss**: connector access, repository reachability, ref resolution and file reads were available, but an agent asserted that required specification files could not be accessed before completing repository, ref, path and chunked-read diagnostics.
2. **RC-PUBLISH-001 — correctly diagnosed publish blocker**: read/fetch, exact-ref checkout and review work succeeded, while authenticated push and remote-workflow triggering were unavailable because no write credential was present. This is a terminal capability result for the tested publish path, not `DIAGNOSTIC_INCOMPLETE`.

This protocol is not a DPA normative contract, creates no runtime authority and authorizes no production implementation. It is a mandatory Kit hardening candidate that MUST be carried into controlled-import planning and MUST NOT be dropped as incidental Lab process commentary.

## 2. Capability dimensions

Repository capability MUST be evaluated per requested operation. The mandatory dimensions are:

- **read/fetch** — repository metadata, refs, trees and file content;
- **write/push** — authenticated mutation of repository refs or content;
- **publish/workflow** — opening or updating remote review state and triggering required remote workflows;
- **local checkout** — clone, fetch and exact-ref checkout where local tooling is required.

Success in one dimension MUST NOT be generalized to another. In particular, successful read/fetch does not prove write/push or publish/workflow capability.

## 3. Failure model

A failed or absent tool call does not prove broad loss of repository access. Diagnosis MUST distinguish:

- connector unavailable;
- authentication absent or rejected for the requested capability;
- permission denial for the requested capability;
- repository not found;
- ref not found;
- path not found;
- target file too large for one response;
- transient tool failure;
- incomplete diagnosis;
- confirmed capability;
- confirmed read-only operation with unavailable write or publish capability.

## 4. Closed classification

Each tested capability dimension MUST resolve to exactly one current classification:

- `CAPABILITY_CONFIRMED`
- `CAPABILITY_PARTIAL`
- `CONNECTOR_UNAVAILABLE`
- `AUTHENTICATION_UNAVAILABLE`
- `PERMISSION_DENIED`
- `REPOSITORY_NOT_FOUND`
- `REF_NOT_FOUND`
- `PATH_NOT_FOUND`
- `TRANSIENT_TOOL_FAILURE`
- `DIAGNOSTIC_INCOMPLETE`

The aggregate assessment MUST name the dimension, for example:

- `READ_FETCH: CAPABILITY_CONFIRMED`;
- `WRITE_PUSH: AUTHENTICATION_UNAVAILABLE`;
- `PUBLISH_WORKFLOW: CAPABILITY_PARTIAL`.

`PERMISSION_DENIED` MUST NOT be asserted without explicit permission evidence or an unambiguous remote denial.

`AUTHENTICATION_UNAVAILABLE` is terminal for the tested write or publish path when the operation unambiguously requires a credential that is absent. It MUST NOT be converted into `DIAGNOSTIC_INCOMPLETE` merely because additional read retries are possible.

An agent that has not completed the applicable ladder in §5 MUST use `DIAGNOSTIC_INCOMPLETE` only for that capability dimension, not as a blanket repository classification.

## 5. Mandatory diagnostic ladders

### 5.1 Read/fetch ladder

Before stating that repository content cannot be accessed, the agent or tool MUST perform, where capabilities permit:

1. confirm the repository connector or read tool is available;
2. resolve authenticated identity when available, repository metadata and reported read permission;
3. read a small known file such as `README.md` on the default branch;
4. read the same known file on the requested branch, tag or exact commit;
5. consult the repository file map, index, manifest, PR changed-file list or repository search before declaring a target path absent;
6. read the requested file at the exact ref;
7. continue truncated output through explicit line ranges until complete;
8. retry transient failures after rechecking repository and ref state;
9. record the resulting read/fetch classification and evidence.

A single failed file operation MUST NOT terminate the ladder unless it returns an unambiguous terminal classification.

### 5.2 Write/push ladder

Before stating that repository mutation or push is available or unavailable, the agent or tool MUST:

1. identify the exact requested write operation;
2. identify the tool or credential path required for that operation;
3. distinguish reported repository write permission from usable authentication credentials;
4. perform only the bounded, user-authorized write or push attempt required by the workflow;
5. classify an unambiguous missing-credential error as `AUTHENTICATION_UNAVAILABLE` for that path;
6. classify an authenticated authorization denial as `PERMISSION_DENIED`;
7. avoid destructive credential probing or speculative writes;
8. record whether read/fetch remained available.

A missing credential is not disproven by repository metadata reporting write permission.

### 5.3 Publish/workflow ladder

Before claiming that review publication or CI triggering succeeded or is possible, the agent or tool MUST separately verify:

1. the required publication action, such as push, PR update or workflow dispatch;
2. the available authenticated connector or CLI path;
3. whether the branch or commit exists remotely;
4. whether the workflow trigger condition has actually occurred;
5. whether a remote run is visible for the expected commit;
6. the terminal classification for any blocked step.

Local review completion MUST NOT be represented as remote publication or CI execution.

## 6. Recovery rules

- If repository metadata and known-good reads succeed, read permission loss is disproven for the tested scope.
- If the default-ref read succeeds but the target-ref read fails, classify the problem as ref-specific until disproven.
- If the target ref succeeds but one path fails, discover the canonical path before using `PATH_NOT_FOUND`.
- If a response is truncated, continue reading by line range; truncation is not access failure.
- If a required read call is not attempted, the read result is `DIAGNOSTIC_INCOMPLETE`.
- If authenticated push fails because no credential is available, record `WRITE_PUSH: AUTHENTICATION_UNAVAILABLE`; do not repeat unrelated read diagnostics as though they could restore the credential.
- If a connector can commit or update PR state while a local CLI cannot push, classify each path separately and use only the authorized working path.
- If one call fails transiently while later calls succeed, the final classification is based on the completed applicable ladder, and the transient failure remains contextual evidence only.

## 7. Minimum evidence schema

```yaml
repository: owner/name
requested_operation: read|write|push|publish|workflow
connector_or_tool: github|git|gh|other
authenticated_identity: <login-or-unknown>
default_ref: main
target_ref: <branch-tag-or-sha>
capabilities:
  read_fetch:
    classification: CAPABILITY_CONFIRMED
    known_good_read: success
    target_read: success
    chunk_ranges: []
  write_push:
    classification: AUTHENTICATION_UNAVAILABLE
    permission_reported: true|false|unknown
    credential_available: true|false|unknown
    attempted_operation: <bounded-operation-or-not_run>
  publish_workflow:
    classification: CAPABILITY_PARTIAL
    remote_commit_visible: true|false|unknown
    workflow_run_visible: true|false|unknown
observed_errors: []
```

Evidence labels in this protocol are operational diagnosis vocabulary. They MUST NOT be added to DPA-100 document status, lifecycle state, consumer trust-state, freshness, finding or gate vocabulary.

## 8. Bootstrap and handoff requirements

A future Kit implementation SHOULD add a bounded repository-capability self-check when repository work is required.

A handoff SHOULD record:

- connector or tool and authenticated identity;
- repository and exact ref;
- last confirmed remote head;
- last successful known-good and target-file reads;
- read/fetch classification;
- write/push classification;
- publish/workflow classification;
- last successful remote publication or workflow run where relevant;
- unresolved tool, credential or permission errors.

A successor MUST revalidate rather than treating historical capability evidence as permanent authorization.

## 9. Planned Kit integration surfaces

Controlled Kit adoption MUST evaluate integration into existing authorities rather than creating a parallel subsystem:

- bootstrap/session-entry validation;
- repository and connector operations;
- diagnostic finding/report vocabulary;
- handoff package context;
- bounded evidence output;
- CLI and, where applicable, GUI diagnostics.

A candidate command may be exposed through an existing diagnostics or environment command family. The exact command name and implementation location remain `NEEDS_MAIN_REPO_VALIDATION`.

## 10. Acceptance criteria for the future Kit slice

The future Kit slice is incomplete until it demonstrates at least:

1. a single failed or omitted read cannot produce a false permission-loss claim;
2. repository, ref and path failures are distinguished;
3. large files are read through deterministic continuation;
4. read/fetch, write/push and publish/workflow capabilities are classified separately;
5. a missing write credential terminates honestly without looping through irrelevant read recovery;
6. local review completion cannot be represented as successful remote publication or CI triggering;
7. evidence records the applicable ladder and terminal classification;
8. bootstrap and handoff consumers can reuse the result without treating it as permanent authority;
9. no second repository registry, evidence system or state authority is introduced;
10. regression coverage includes both RC-READ-001 and RC-PUBLISH-001.

## 11. Import obligation

This artifact is a durable Kit hardening obligation.

During controlled import, the Maintainer MUST explicitly disposition it as one of:

- imported into an approved Kit work slice;
- superseded by a demonstrably equivalent existing Kit contract;
- rejected by a recorded Maintainer decision with rationale.

Silence, omission or Lab archival MUST NOT count as disposition.
