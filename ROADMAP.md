# Roadmap

Status: active

Status-date: 2026-07-15

## Specification sequence

1. DPA-000 — Vision and architectural principles — stable
2. DPA-100 — Foundations and terminology — stable
3. DPA-200 — Document model — review-ready
4. DPA-300 — Registry and lifecycle integration — draft under primary review preparation
5. DPA-400 — Renderer contract — planned
6. DPA-500 — Freshness and gates — planned
7. DPA-600 — Concurrency and workflow serialization — planned
8. DPA-700 — Migration and rollback — planned
9. DPA-800 — DP1–DP5 implementation specification — planned
10. DPA-900 — Future evolution — planned
11. Lab adoption with `agentic-project-kit`
12. Controlled import into `vfi64/agentic-project-kit`

The normative specification order is unchanged.

## Evidence-first sequencing exception

DPA-ADR-015 keeps DP1 as one formal slice with three internal stages:

1. Discovery
2. Probe
3. Assessment

Only Discovery is moved earlier.

The governed sequence is:

1. Complete DPA-200 adjudication and post-adjudication verification — complete.
2. Promote DPA-200 to `review-ready` — complete.
3. Execute read-only DP1 Discovery against one exact main-repository validation ref — complete.
4. Synchronize assumptions, main-repository context and bounded records — complete.
5. Draft DPA-300 from observed evidence — complete draft; primary review pending.
6. Execute bounded DPA-300-owned Probe questions only after DPA-300 becomes reviewable.
7. Continue DPA-400 and DPA-500 with the validated repository context.
8. Complete the remaining DP1 Probe and Assessment stages under DPA-800 governance.

Early Discovery does not constitute lab adoption, implementation or migration.

## DPA-300 active work

The first DPA-300 baseline contains:

- the normative registry/lifecycle integration contract;
- RL-001 through RL-020 traceability;
- registry/lifecycle, command-integration and plan-state diagrams;
- an internal invariant, ADR, evidence and failure-mode audit.

The immediate sequence is:

1. bind a Claude primary architecture review to the immutable baseline commit;
2. store the read-only review under `reviews/claude/`;
3. perform independent secondary technical verification;
4. adjudicate findings before changing normative text;
5. apply accepted corrections and synchronize derived artifacts;
6. run post-adjudication verification;
7. promote DPA-300 to `review-ready` only when its exit criteria pass.

## Confirmed candidate-command obligation

Exact-ref Discovery at `vfi64/agentic-project-kit@6a9da7d363ae3f97f347b79a2679f6f848d8cdf3` identified the active `CURRENT_HANDOFF.md` mutation path as:

`agentic-kit transfer admin-refresh-pr`
→ `transfer_repo_actions._refresh_operational_handoff_docs()`

The observed implementation appends refresh prose instead of routing `CURRENT_HANDOFF.md` through the existing bounded replacement primitive.

Governed obligations:

- **DPA-300:** registry/lifecycle-owned plan, validation, lock, complete-file replacement, verification, evidence and direct-write detection.
- **DPA-400:** pure renderer payload and no partition-byte ownership.
- **DPA-500:** marker, drift, direct-write and acceptance findings and gates.
- **DPA-600:** stale-base and competing-PR serialization.
- **DPA-700:** preservation and rollback without historical-prose merging.
- **DP1 Probe:** demonstrate governed bounded replacement in the existing command path.
- **DP1 Assessment:** decide whether `CURRENT_HANDOFF.md` is eligible for any production migration form.

No production form is selected by this obligation.

## Review-derived later-spec obligations

### DPA-400

- Static renderer resolution.
- Declared sources and contract-declared configuration.
- Purity, no boundary-byte output and one-target behavior.

### DPA-500

- Trust-state gates and acceptance transitions.
- Drift findings and staged enforcement.
- No time-only hard failure.

### DPA-600

- Base, source, target and contract drift guards.
- Cross-branch and cross-PR serialization.

### DPA-700

- Migration choice and no-migration outcome.
- Historical-region ownership and recoverable rollback.
- No automatic historical-prose merge.

### DPA-800

- DP1 Discovery, Probe and Assessment as internal stages of one slice.
- Exact-ref evidence obligations and DP1 exit criteria.
- Explicit Probe case for the `CURRENT_HANDOFF.md` admin-refresh command path.

## Prohibitions

- No production code or main-repository mutation in the lab.
- No `.agentic/` initialization before adoption.
- No production-form selection from candidate labels or model opinion.
- No architecture decision derived automatically from Discovery evidence.
- No parallel evidence system or maintained main-repository mirror.
- No Probe execution before the governing specification is reviewable.
- No review prose becomes normative without adjudication.