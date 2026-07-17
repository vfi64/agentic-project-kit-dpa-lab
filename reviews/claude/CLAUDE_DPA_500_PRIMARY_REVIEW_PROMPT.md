# Claude DPA-500 Primary Architecture Review Prompt

You are performing an independent primary architecture review of DPA-500 in the private repository `vfi64/agentic-project-kit-dpa-lab`.

## 1. Exact review baseline

Review exactly this immutable repository ref:

`60d6457f0473365789ece4f885a48ea5320b01ff`

Do not review a moving branch head. Do not substitute a later commit. If the exact ref is unavailable, return `ACCESS_BLOCKED` and stop.

The baseline is the post-audit DPA-500 draft and pre-review closeout. The durable Lab gate run bound to this ref is:

- workflow: `DPA lab gates`
- run: `29582601216`
- result: `success`

The green Lab gate is repository-integrity evidence only. It is not architecture approval, Probe evidence, implementation evidence or main-repository conformance.

## 2. Repository and authority boundary

The lab repository is authoritative only for planning history, accepted architecture decisions and pre-import normative specifications.

The main repository `vfi64/agentic-project-kit` remains the sole authority for production implementation, runtime contracts, registry contents, lifecycle behavior, findings, gates, releases and handoff state.

Do not inspect or make claims about a newer main-repository state during this review. Repository-specific implementation claims marked `NEEDS_MAIN_REPO_VALIDATION` must remain fenced.

## 3. Independence disclosure

Before the verdict, state whether this reviewing context:

1. authored or applied any DPA-500 normative text;
2. authored or applied the pre-review corrections;
3. participated in the pre-review audit or its closeout;
4. has prior exposure to DPA-500 content.

Prior exposure does not automatically block the review, but authorship of the reviewed normative changes must be disclosed clearly. Return `INDEPENDENCE_BLOCKED` only if you cannot provide a meaningfully independent review.

## 4. Mandatory bootstrap order

Before evaluating DPA-500, read these files completely and in this exact order at the review ref:

1. `README.md`
2. `LAB_BOOTSTRAP.md`
3. `MAIN_REPOSITORY_CONTEXT.md`
4. `LAB_EXECUTION_CONTRACT.md`
5. `GOVERNANCE.md`
6. `STATUS.md`
7. `ROADMAP.md`
8. `DECISIONS.md`
9. `ASSUMPTIONS.md`
10. `specs/dpa/README.md`
11. `specs/dpa/DPA-000-VISION.md`
12. `specs/dpa/DPA-100-FOUNDATIONS.md`
13. `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
14. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`
15. `specs/dpa/DPA-400-RENDERER-CONTRACT.md`
16. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`
17. `traceability/DPA-500_TRACEABILITY.md`
18. `diagrams/dpa-500-freshness-gates.mmd`
19. `reviews/consolidated/DPA-500_PRE_REVIEW_AUDIT.md`
20. `reviews/consolidated/DPA-500_PRE_REVIEW_AUDIT_CLOSEOUT.md`
21. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
22. `integration/IMPORT_PLAN.md`
23. every accepted decision directly referenced by DPA-500, especially DPA-ADR-013, DPA-ADR-014, DPA-ADR-016, DPA-ADR-017, DPA-ADR-019 and DPA-ADR-020.

Do not trust the pre-review audit or closeout without checking their claims against the normative text.

## 5. Primary review objective

Determine whether DPA-500 is architecturally coherent, reviewable and safe to advance into Maintainer adjudication.

This is not a proofreading-only review. Test the architecture for contradictions, authority leakage, vocabulary drift, incomplete failure semantics, unsafe staged enforcement, false implementation claims and missing traceability.

## 6. Required review fields

### A. Vocabulary and dimensional separation

Verify that DPA-500 preserves the DPA-100 closed vocabularies and keeps these dimensions distinct:

1. freshness classification: `fresh`, `stale`, `invalid`, `indeterminate`;
2. DPA-100 consumer trust state: `computed`, `plan-captured`, `written-unverified`, `accepted`, `abandoned`;
3. DPA-100 drift class: base, source, target, contract, renderer, partition, ownership;
4. projection-specific finding subreason;
5. lifecycle attempt outcome;
6. gate decision: `pass`, `warning`, `failure`;
7. enforcement stage: `observe`, `warn`, `block-new`, `strict`;
8. finding severity and user-facing wording.

Check for accidental reuse of `stale`, `invalid`, `indeterminate`, `warn`, `error`, `block`, `abandoned` or other tokens across incompatible dimensions.

### B. Freshness model completeness

Evaluate whether the mandatory freshness dimensions are complete and mutually coherent:

- contract;
- source;
- configuration;
- renderer;
- target;
- target semantics;
- gate set;
- acceptance state;
- base/ref context.

Identify any missing dimension, duplicated dimension, ambiguous ownership or false equivalence.

### C. Acceptance-state contract

Check that:

- acceptance state remains lifecycle state and not evidence;
- it is scoped to one registered target;
- required identities and fingerprints are sufficient for later comparison;
- timestamps are metadata rather than semantic freshness authority;
- malformed or missing state fails safely;
- state is never reconstructed silently from target bytes or evidence;
- successful rendering alone can never create `accepted`.

### D. Drift and finding model

Verify that DPA-500 uses the closed DPA-100 drift classes and treats acceptance-state defects, gate-set mismatch, nondeterminism, operational aborts, diagnostics and persistence failures as findings or lifecycle failures rather than new drift classes.

Check whether configuration drift and target-semantics drift are mapped unambiguously to source, contract, partition or ownership drift according to declared authority.

Flag any case where two distinct failures would become indistinguishable.

### E. Gate semantics

Evaluate the use of `pass`, `warning` and `failure`.

Check that:

- mandatory evaluation failure always fails closed for mutation, acceptance and integration;
- `warning` cannot authorize acceptance when a mandatory check failed;
- a read-only audit may report failure without mutation;
- gate decisions do not overwrite freshness classification or trust state;
- no lab workflow is represented as production gate authority.

### F. Staged enforcement

Evaluate `observe`, `warn`, `block-new` and `strict`.

Check that:

- all transitions are explicit, reviewable and reversible;
- elapsed time cannot activate stricter enforcement;
- legacy compatibility cannot weaken safety for new mutation or acceptance;
- unknown findings fail closed where mutation safety or authority interpretation is affected;
- the stage token `warn` cannot be confused with gate `warning`;
- no production strict mode is activated by lab prose.

### G. Renderer integration

Verify consistency with DPA-400 for:

- identifier drift;
- interface incompatibility;
- semantic-version drift;
- implementation evidence remaining evidence-only;
- nondeterminism;
- side effects and capability violations;
- semantic resource bounds;
- operational aborts;
- bounded failure diagnostics.

Check that operational aborts are not semantic output and are not misclassified as renderer drift merely because execution stopped.

### H. Complete-target and registered-region handling

Check independent treatment of:

- payload fingerprint;
- preserved-region fingerprint;
- partition contract;
- partition bytes and boundaries;
- complete-target fingerprint;
- byte ownership.

Verify that manual or historical bytes are never regenerated merely to clear projection staleness.

### I. Recovery and crash safety

Evaluate the `written-unverified` recovery contract.

Check whether DPA-500 clearly distinguishes:

- verified bytes;
- acceptance-state persistence;
- evidence persistence;
- interrupted attempt state;
- permitted completion of recording;
- mandatory regeneration or Maintainer remediation.

Identify any path that could falsely promote interrupted bytes to accepted state.

### J. Authority and parallel-system audit

Verify that DPA-500 does not create:

- a second findings taxonomy;
- a second gate runner;
- a second freshness engine;
- a second acceptance database;
- a new runtime authority;
- a lab-controlled production strict switch;
- a renderer-owned finding, trust or gate authority.

### K. Main-repository validation boundary

Check every repository-specific statement.

Confirm that concrete codes, severity mappings, acceptance-state schema/path, gate-set representation, strict switches, command integration, persistence order, required checks and compatibility behavior remain `NEEDS_MAIN_REPO_VALIDATION` where appropriate.

Flag any unsupported `VERIFIED`, implementation or Probe claim.

### L. Traceability and diagram audit

Compare the normative text with:

- `traceability/DPA-500_TRACEABILITY.md`;
- `diagrams/dpa-500-freshness-gates.mmd`.

Check that they neither omit important semantics nor create competing normative meaning.

### M. Review-ready criteria

Determine whether the normative content is sufficient for adjudication. Do not recommend direct promotion merely because the architecture appears sound; primary review findings still require Maintainer disposition and any required verification path.

## 7. Required targeted searches

Search the current tree for at least:

- trust-state uses of `stale`, `invalid` or `unknown`;
- gate outcomes `warn`, `block` or `error`;
- drift-class tokens outside the DPA-100 closed list;
- `boundary drift`;
- `implementation version`;
- `renderer contract version`;
- time-only freshness or strict activation;
- claims that Lab CI proves architecture or main-repository conformance;
- claims that DPA-500 is already `review-ready`, `stable`, implemented or adopted.

Classify each occurrence as current normative text, valid historical review prose, prompt text, validator text or actual defect.

## 8. Severity model

Use:

- **Major** — architecture contradiction, authority leak, unsafe mutation/acceptance path, closed-vocabulary violation, missing mandatory failure behavior, false implementation claim or review-blocking incompleteness;
- **Minor** — bounded semantic ambiguity, incomplete test/traceability obligation, terminology weakness or recoverability gap that does not invalidate the architecture;
- **Editorial** — wording, organization or reference issue without semantic impact.

Every finding must identify exact file and section, explain the consequence and propose the smallest bounded correction.

## 9. Verdict vocabulary

Return exactly one overall verdict:

- `ACCEPT`
- `ACCEPT_WITH_CHANGES`
- `REJECT`
- `ACCESS_BLOCKED`
- `INDEPENDENCE_BLOCKED`

Use `ACCEPT` only when no normative correction is required before adjudication.

Use `ACCEPT_WITH_CHANGES` when the architecture is viable but bounded corrections are required.

Use `REJECT` only when the current architecture requires substantial redesign.

## 10. Required report structure

Return one complete English Markdown report suitable for committing as:

`reviews/claude/CLAUDE_DPA_500_PRIMARY_REVIEW.md`

Use this structure:

1. Title
2. Metadata
3. Independence disclosure
4. Bootstrap completion statement
5. Method
6. Reviewed files
7. Exact review ref
8. Overall verdict
9. Executive summary
10. Major findings
11. Minor findings
12. Editorial findings
13. Vocabulary/dimensional-separation audit
14. Freshness and acceptance-state audit
15. Drift/finding and gate audit
16. Staged-enforcement audit
17. Renderer integration audit
18. Region/partition audit
19. Recovery/crash-safety audit
20. Authority and parallel-system audit
21. Main-repository validation boundary
22. Traceability and diagram audit
23. Targeted-search results
24. Remaining `NEEDS_MAIN_REPO_VALIDATION` obligations
25. Limitations and `ACCESS_BLOCKED` items
26. Smallest bounded correction set
27. Promotion recommendation

## 11. Promotion wording

If the verdict supports eventual advancement, use this exact bounded wording:

> DPA-500 may proceed to Maintainer adjudication after all required review findings are dispositioned. Any later promotion to `review-ready` must be a separate status-only commit and does not establish production implementation, Probe success or main-repository conformance.

Do not claim that DPA-500 is already review-ready.

## 12. No repository mutation

Perform no repository writes, commits, branch changes, PR changes or workflow reruns. Return only the complete report, followed by a short German summary containing:

- overall verdict;
- number of major, minor and editorial findings;
- whether normative changes are required;
- whether DPA-500 may proceed to Maintainer adjudication;
- recommended next step.
