# Probe Evidence Capture Procedure

Status: active

Status-date: 2026-07-18

## 1. Purpose

This procedure defines bounded, ordered and non-authoritative evidence capture for PROBE-001, PROBE-002 and the DPA-400 renderer Probe.

Evidence records what was observed. It does not become canonical source, acceptance state, authorization, runtime configuration or a substitute for Maintainer adjudication.

## 2. Evidence layers

Each execution MUST keep these layers separate:

1. **Execution manifest** — frozen identities, environment, commands and case scope.
2. **Raw bounded observation** — return codes, structured results, hashes, changed-path manifests and bounded diagnostics.
3. **Case result** — expected result, actual result and `PASS`, `FAIL`, `PARTIAL`, `BLOCKED` or `NOT_RUN`.
4. **Interpretation** — classification of the discrepancy without changing observed facts.
5. **Maintainer adjudication** — accepted disposition and follow-up obligations.

No later layer may rewrite an earlier layer.

## 3. Required execution manifest

The manifest MUST contain:

- execution identity;
- exact freeze identity;
- Probe and case identifiers;
- main-repository exact SHA;
- Lab exact ref;
- fixture-set revision and per-fixture hashes;
- command or API invocation;
- environment and isolation identity;
- pre-state hashes;
- declared allowed and forbidden mutations;
- observation hooks used;
- cleanup and restoration method;
- operator identity;
- start and end timestamps as evidence metadata only.

## 4. Per-case evidence

Every case MUST record:

- case and fixture identity;
- normative anchors;
- expected observation and expected outcome rule;
- actual ordered phases or parser stages;
- actual return code or API result;
- target, registry, plan, lock, state, evidence and acceptance-state deltas as applicable;
- relevant pre-state and post-state hashes;
- bounded diagnostics;
- discovered implementation symbols and paths;
- cleanup result;
- limitations and unavailable checks;
- case outcome.

A case with incomplete required evidence cannot be `PASS`.

## 5. Bounded diagnostics

Diagnostics MUST:

- include only the minimum context required to reproduce and interpret the result;
- exclude secrets, credentials and unrelated environment content;
- avoid unbounded repository or document contents;
- identify truncation explicitly;
- preserve exact error identifiers and relevant paths when safe;
- retain raw output separately from interpretation when possible.

Hash-only evidence MUST NOT replace required semantic observations when the actual bounded structure is necessary to understand the result.

## 6. Ordering and crash safety

Evidence ordering MUST preserve the actual operation order.

For mutating or re-acceptance cases, capture at minimum:

1. pre-state;
2. frozen identities;
3. invocation start;
4. phase transitions or interruption boundary;
5. Write, Verify, acceptance-state and evidence-persistence results separately;
6. cleanup or recovery;
7. post-state;
8. case outcome;
9. interpretation;
10. later adjudication.

Evidence persistence failure MUST be recorded as a lifecycle or execution failure. It MUST NOT fabricate a successful completion or erase whether target bytes were written, verified or accepted.

## 7. Changed-path manifest

Every case MUST produce a changed-path manifest, including an explicit empty result.

For non-mutating cases, any unexplained change is a failure and blocks worktree reuse.

For mutating cases, every changed path MUST be classified as:

- expected temporary fixture state;
- expected governed target mutation;
- expected lifecycle or acceptance-state mutation;
- declared evidence output;
- cleanup action;
- unexpected mutation.

Unexpected mutation requires `FAIL` or `BLOCKED` according to whether the cause is understood and safely contained.

## 8. Repeat runs

Repeat executions MUST receive new execution identities and preserve prior records.

Comparison MUST distinguish:

- fields expected to remain identical;
- environment or timing metadata expected to vary;
- output or state differences that indicate nondeterminism;
- differences caused by changed refs or fixture revisions.

A rerun does not overwrite or retroactively repair the first result.

## 9. Additional-path discoveries

When a case reveals an additional parser, reader, writer, renderer caller, lock, state or recovery path:

1. record the exact path and symbol;
2. stop silent scope expansion;
3. classify its relation to the current case;
4. decide whether the current evidence remains valid;
5. add a bounded case or amend the fixture package if required;
6. freeze a new Lab ref before running the new or changed case.

## 10. Storage boundary

The exact main-repository evidence location remains `NEEDS_MAIN_REPO_VALIDATION`.

Whatever location is selected MUST:

- use existing evidence and repository authorities;
- remain bounded and reviewable;
- preserve immutable execution identities;
- avoid becoming a second runtime state store;
- support exact-ref traceability;
- keep observation, interpretation and adjudication distinct.

## 11. Minimum case record template

```text
execution_id:
freeze_id:
probe_id:
case_id:
fixture_id:
normative_anchors:
expected_observation:
expected_outcome_rule:
command_or_api:
return_code_or_result:
ordered_observations:
pre_state_hashes:
post_state_hashes:
changed_paths:
bounded_diagnostics:
implementation_paths:
cleanup_result:
limitations:
case_outcome:
interpretation_ref:
adjudication_ref:
```
