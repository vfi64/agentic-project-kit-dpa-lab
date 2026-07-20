# DPA-400 Renderer Fixture Manifest

Status: draft

Status-date: 2026-07-19

Manual: `probes/DPA-400-RENDERER-PROBE-MANUAL.md`

Execution-state: not run

## 1. Fixture rules

- Fixtures model semantic inputs and prohibited capabilities before concrete callable serialization is selected.
- Every materialized fixture requires a stable ID, revision and content hash.
- Negative fixtures differ from a valid parent by one declared mutation or capability attempt.
- Source and configuration fixtures are immutable for one invocation.
- Capability probes must be isolated and must not risk production state.
- Concrete renderer IDs, module paths, signatures and sandbox mechanics remain `NEEDS_MAIN_REPO_VALIDATION`.

## 2. Resolution fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F400-RENDERER-KNOWN | One reviewed static mapping entry | R400-C001, R400-C005 |
| F400-RENDERER-UNKNOWN | Unknown renderer ID | R400-C002 |
| F400-RENDERER-DUPLICATE | Duplicate ID or ambiguous alias | R400-C003 |
| F400-RENDERER-DYNAMIC | Import path, URL, shell, expression or plugin reference | R400-C004 |
| F400-INTERFACE-INCOMPATIBLE | Unsupported callable interface version | R400-C006 |
| F400-SEMANTIC-VERSION-UNAVAILABLE | Missing or unsupported semantic version | R400-C007 |
| F400-IMPLEMENTATION-EVIDENCE-ONLY | Implementation identity changes, semantic version unchanged | R400-C008 |
| F400-SEMANTIC-VERSION-PLAN-DRIFT | Semantic version changes after immutable plan capture | R400-C009 |

## 3. Invocation-context fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F400-CONTEXT-VALID | One target, ordered sources, immutable config | R400-C010, R400-C011, R400-C012 |
| F400-SOURCE-MISSING | Required declared source absent | R400-C013 |
| F400-CONFIG-MALFORMED | Unknown or malformed config | R400-C014 |
| F400-CAPABILITY-OBJECTS | Mutable runtime objects offered to renderer | R400-C015 |
| F400-AMBIENT-PATH-READ | Renderer attempts reread, traversal, glob or discovery | R400-C016 |
| F400-UNDECLARED-FALLBACK | Prior target, evidence, history, env or time fallback | R400-C017 |
| F400-SOURCE-AS-CODE | Declared source text attempts to trigger executable interpretation | R400-C018 |
| F400-SECRET-ENV-EXPOSURE | Secrets, credentials or unrelated environment values exposed absent an accepted bounded-need contract | R400-C019 |

## 4. Output fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F400-OUTPUT-TEXT | Valid Unicode text | R400-C020 |
| F400-OUTPUT-BYTES | Valid immutable bytes | R400-C020 |
| F400-OUTPUT-INVALID-TYPE | Path, handle, stream, callback, command, finding or map | R400-C021 |
| F400-COMPLETE-TARGET | Complete-target payload independent of prior target | R400-C022 |
| F400-REGION-PAYLOAD | Region payload only | R400-C023 |
| F400-REGION-OVERREACH | Includes markers, separators, preserved or parent bytes | R400-C023 |
| F400-EMPTY-ALLOWED | Empty output permitted by target semantics | R400-C024 |
| F400-EMPTY-FORBIDDEN | Empty output prohibited | R400-C024 |
| F400-OUTPUT-INVALID | Encoding, normalization or target-semantics violation | R400-C025 |
| F400-MULTI-TARGET | Infers or returns sibling targets | R400-C026 |

## 5. Determinism fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F400-REPEAT-SAME-PROCESS | Repeated identical invocation | R400-C027 |
| F400-REPEAT-FRESH-PROCESS | Fresh-process repetition | R400-C028 |
| F400-ORDERING | Source/config order variation under fixed contract | R400-C029 |
| F400-INCIDENTAL-CONTEXT | Locale, timezone, cwd, env, platform, hash seed, enumeration, time | R400-C030 |
| F400-CACHE-LOSS-REUSE | Cache absent and present | R400-C031 |
| F400-GLOBAL-HISTORY | Mutable global or prior invocation state | R400-C032 |

## 6. Purity fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F400-FILESYSTEM-WRITE | Create/modify/delete file attempt | R400-C033 |
| F400-NETWORK | Network attempt | R400-C034 |
| F400-SUBPROCESS | Process or shell attempt | R400-C035 |
| F400-LOCK-OR-REFRESH | Lock or nested refresh attempt | R400-C036 |
| F400-NESTED-RENDERER | Invoke another renderer | R400-C037 |
| F400-STATE-MUTATION | Registry/lifecycle/evidence/acceptance/trust/gate mutation | R400-C038 |
| F400-GIT-MUTATION | Commit/branch/PR/repository mutation | R400-C039 |
| F400-INPUT-GLOBAL-MUTATION | Input or semantic cache/global mutation | R400-C040 |
| F400-TEMPLATE-INJECTION | Template/import/traversal/shell-expansion attempt | R400-C041 |

## 7. Lifecycle-boundary fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F400-LIFECYCLE-CALLER | Rendering requested through existing lifecycle caller | R400-C042 |
| F400-DIRECT-COMMAND-WRITE | Command attempts direct renderer call/write or plan bypass | R400-C043 |
| F400-OUTPUT-NONAUTHORITY | Successful payload observed before lifecycle plan capture | R400-C044 |

## 8. Failure and resource fixtures

| Fixture ID | Purpose | Cases |
|---|---|---|
| F400-COMPUTE-ERROR | Deterministic computation failure | R400-C045 |
| F400-FAILURE-ENVELOPE | Bounded diagnostic envelope | R400-C046, R400-C047 |
| F400-SEMANTIC-BOUND | Versioned deterministic resource bound exceeded | R400-C048 |
| F400-OPERATIONAL-ABORT | Safety abort independent of semantic result | R400-C049 |
| F400-OPERATIONAL-RETRY | Identical plan retried after abort with guards rechecked | R400-C050 |
| F400-OUTPUT-TRUNCATED | Truncated, malformed or over-bound output | R400-C051 |
| F400-FALLBACK-ATTEMPT | Primary failure followed by alternate renderer attempt | R400-C052 |
| F400-PRIOR-ACCEPTED | Existing accepted target/state before failed render | R400-C053 |
| F400-CAPABILITY-VIOLATION | Any detected prohibited capability attempt | R400-C054 |
| F400-ADDITIONAL-PATH | Newly discovered mapping/caller/capability/input | R400-C055 |

## 9. Materialization gate

Executable fixtures must not be created until the exact-ref static mapping, lifecycle caller, callable boundary, immutable-input representation and capability-observation method are remotely inventoried and locally confirmed; safe isolation is demonstrated; and concrete paths, IDs, commands and hashes are added here.

## 10. Completeness check

Before review:

- exactly 55 declared cases exist, R400-C001 through R400-C055;
- every declared case maps to at least one fixture;
- every fixture maps to at least one declared case;
- all successful output fixtures return one payload only;
- prohibited-capability fixtures prove absence of target and state mutation;
- source text remains data and secrets remain outside the invocation context absent an accepted bounded-need contract;
- commands route rendering through lifecycle and cannot bypass plan capture;
- implementation evidence and semantic version remain distinct;
- operational abort and semantic failure remain distinct;
- no fixture creates a second renderer registry, lifecycle or runtime authority;
- all concrete mappings remain `NEEDS_MAIN_REPO_VALIDATION`.
