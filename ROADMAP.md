# Roadmap

Status: active
Status-date: 2026-07-15

## Specification sequence

1. DPA-000 — Vision and architectural principles — stable
2. DPA-100 — Foundations and terminology — stable
3. DPA-200 — Document model — draft under post-review consolidation
4. DPA-300 — Registry and lifecycle integration — planned
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

1. Complete DPA-200 adjudication and post-adjudication verification.
2. Promote DPA-200 to `review-ready` when its exit criteria pass.
3. Execute read-only DP1 Discovery under `integration/DP1_DISCOVERY_CONTRACT.md` against one exact main-repository validation ref.
4. Synchronize `ASSUMPTIONS.md`, `MAIN_REPOSITORY_CONTEXT.md` and bounded records under `evidence/repo-facts/`.
5. Draft DPA-300 from observed evidence rather than unchecked repository assumptions.
6. Execute DP1 Probe after a reviewable DPA-300 contract exists.
7. Complete DP1 Assessment after Discovery and Probe evidence are available.
8. Continue DPA-400 and DPA-500 with the validated repository context.

Early Discovery does not constitute lab adoption, implementation or migration.

## DPA-200 completion work

Current required order:

1. Consolidate DPA-ADR-013 and DPA-ADR-014 into the DPA-200 owner text.
2. Synchronize the document-form matrix.
3. Regenerate region-ownership and trust-state diagrams.
4. Add DM-011 and re-key taxonomy, invalidity and trust-transition traceability.
5. Run bounded post-adjudication verification.
6. Promote DPA-200 and its matrix to `review-ready` only after verification passes.

## DP1 Discovery scope

Discovery asks factual Ist-state questions only:

- registry loaders, schema and validation paths;
- candidate reader and writer graphs;
- observed authority inputs;
- finding types, severities, producers and consumers;
- lifecycle planning, locking, writing and evidence paths;
- Workspace and path-resolution APIs;
- locking and workflow inventory;
- gates and CI mapping;
- history and rollback inputs.

Discovery MUST NOT answer whether an observed mechanism is sufficient for DPA. Suitability and compatibility belong to Probe.

## Review-derived later-spec obligations

### DPA-300

- Registry representation and fail-loud validation.
- Lifecycle planning, locking, atomic write and direct-write detection.
- Boundary-partition validation and crash recovery.

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

## Prohibitions

- No production code or main-repository mutation in the lab.
- No `.agentic/` initialization before adoption.
- No production-form selection from candidate labels or model opinion.
- No architecture decision derived automatically from Discovery evidence.
- No parallel evidence system or maintained main-repository mirror.
