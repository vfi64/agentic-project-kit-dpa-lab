# ChatGPT Technical Verification Audit — DPA Phase A Foundation

Status: complete
Status-date: 2026-07-15
Audit type: technical verification, not an independent blind first review
Repository: `vfi64/agentic-project-kit-dpa-lab`
Architecture baseline audited: `1a73ec435a09d0367cb7e9f123241d9f61550b0f`
Review-integration state inspected: `1bf72d1313335b6acfe5af960dd7315f42a7756a`
Primary review verified: `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md`

## 1. Method and scope

This audit verifies the Phase A architecture and Claude Fable 5 review against the exact repository artifacts. It is not represented as a blind independent first review because the auditor had already read the Claude review.

The audit checks:

- whether each Claude finding follows from repository evidence;
- whether severity and proposed disposition are proportionate;
- whether material contradictions or omissions remain;
- whether the planned adjudication sequence is sufficient;
- whether any recommendation would create a parallel runtime or governance system.

No main-repository implementation claim is upgraded. No normative DPA specification is changed by this audit.

## 2. Executive assessment

Overall result: **ACCEPT_WITH_CHANGES**

Phase A may proceed to formal adjudication: **YES**

Phase A may be declared stable now: **NO**

Foundational architecture contradiction: **NO**

Hidden parallel runtime system: **NO**

New runtime authority: **NO**

Confidence: **HIGH** for internal consistency findings; **NOT APPLICABLE** for current main-repository implementation facts.

The core architecture is coherent. The authority model, pure-renderer boundary, lifecycle-owned mutation, workflow-owned cross-ref serialization, static renderer resolution, derivational freshness and evidence-driven migration hierarchy form a consistent system.

The unresolved work is primarily ownership, vocabulary and governance closure. Claude's review is technically strong. Two adjustments are required:

1. F-M03 should be treated as a major Phase A governance defect but not as a major architecture defect.
2. The model-specific review requirement is itself too rigid. Review roles and evidence quality should be normative; specific vendors or models should not be mandatory.

## 3. Verification of Claude Major findings

### F-M01 — Status vocabulary is not closed

Verdict: **VERIFIED**

Evidence:

- DPA-100 §2 defines six repository-fact classifications.
- Traceability uses `PLANNED`, `REVIEW-READY`, `PARTIAL` and `SATISFIED FOR INTERNAL BASELINE` as if they belonged to the same vocabulary.
- MAIN_REPOSITORY_CONTEXT and dependent artifacts use qualified forms of `VERIFIED` that are not defined.
- Document lifecycle statuses `planned` and `active` are also used without a separate declared status namespace.

Assessment:

Claude correctly identifies a namespace collision. The defect is not merely missing labels; epistemic classification, document maturity and progress tracking are mixed.

Recommended disposition:

Accept ADR-009 scope, but do not create one large status lattice. Define three separate closed namespaces:

1. repository-fact classification;
2. document maturity/lifecycle status;
3. work or exit-progress status.

A recorded baseline should be represented by evidence scope and ref metadata, not by inventing an increasingly qualified `VERIFIED` value.

Maintainer decision required: **YES**

### F-M02 — Duplicated invariant catalog with numbering drift

Verdict: **VERIFIED**

Evidence:

- LAB_EXECUTION_CONTRACT §7 contains 17 numbered invariants.
- DPA-000 contains a substantively overlapping but non-identical invariant catalog.
- Traceability introduces grouped `INV-01` through `INV-13`, so an identifier does not map one-to-one to one invariant.

Assessment:

Claude correctly identifies both ownership ambiguity and referential instability. Future tests, ADRs and reviews cannot safely cite an invariant number while three representations exist.

Recommended disposition:

Accept ADR-010 with this outcome:

- DPA-000 owns the canonical DPA invariant register.
- Every invariant receives one stable ID and one normative statement.
- LAB_EXECUTION_CONTRACT references that register and keeps lab-operation-only rules outside it.
- Traceability is a derived one-to-one view and never owns invariant meaning.

Maintainer decision required: **YES**

### F-M03 — Recorded baseline lacks in-lab evidence records

Verdict: **VERIFIED WITH SEVERITY QUALIFICATION**

Evidence:

- MAIN_REPOSITORY_CONTEXT and LAB_EXECUTION_CONTRACT require concise records under `evidence/repo-facts/`.
- The directory was absent at the reviewed ref.
- MAIN_REPOSITORY_CONTEXT was used as a reproduction source for claims contained in that same document.

Assessment:

The circular reference is real and the stored evidence does not meet the lab's own declared bar. However, the defect does not weaken the DPA runtime architecture. It weakens the credibility and reproducibility of the recorded planning baseline.

Recommended disposition:

Accept ADR-011, but classify the finding as:

- **Major Phase A governance/evidence defect**;
- **not a foundational architecture defect**.

Create only minimal static records containing exact ref, subject, inspected paths or command/method, date and revalidation scope. Do not create evidence tooling, a mirror or a second evidence authority.

Maintainer decision required: **YES**

## 4. Verification of Claude Minor findings

### F-m01 — Divergent Phase A exit criteria

Verdict: **VERIFIED**

The execution contract must own the normative exit criteria. STATUS must be a tracking projection. Review templates may ask stricter questions but must not silently redefine phase completion.

### F-m02 — `truth source` wording conflicts with defined terminology

Verdict: **VERIFIED**

Replace normative uses with `runtime authority`. This is editorial and does not require a new ADR.

### F-m03 — Missing invariant-to-decision links

Verdict: **VERIFIED**

Add a decision column after the invariant register is normalized. Do not patch the current grouped table before ADR-010.

### F-m04 — `fresh` overloaded for projection state and repository ref

Verdict: **VERIFIED**

Define `validation ref` as the exact fetched repository commit used for a validation act. Preserve `fresh` exclusively for derivational projection freshness.

### F-m05 — `planned` and `active` document statuses undefined

Verdict: **VERIFIED**

These belong to a document-status namespace, separate from fact classifications and progress assessments.

### F-m06 — `canonical source` not explicitly defined

Verdict: **PARTIALLY VERIFIED**

DPA-100 §5.4 already defines a declared source as a canonical input, so the intended containment is present. The remaining problem is terminological: `canonical source` is used as a phrase without a formal alias definition. Add an explicit alias or avoid the phrase. This is minor editorial terminology work, not a substantive authority gap.

### F-m07 — Standalone architecture diagram diverges from DPA-100 model

Verdict: **VERIFIED**

Either align it with the normative relationship model or mark it explicitly non-normative and simplified. A diagram may omit detail, but it must not suggest different ownership or gate inputs.

## 5. Architecture consistency audit

### 5.1 Authority model

Result: **PASS**

Runtime, projection, planning, evidentiary and historical roles are distinguishable. The lab does not elevate itself to production authority.

### 5.2 Registry boundary

Result: **PASS WITH DEFERRED DETAIL**

The registry declares bounded contracts and stable identifiers, not arbitrary imports. Exact schema remains correctly deferred to DP1.

### 5.3 Renderer boundary

Result: **PASS WITH TERMINOLOGY CLEANUP**

Renderers are pure, single-target and non-recursive. The `relevant versioned configuration` input channel must be defined before DPA-400 so that renderer semantic inputs remain closed and fingerprintable.

### 5.4 Lifecycle boundary

Result: **PASS**

Lifecycle owns validation, planning, local locking and writes. The architecture correctly avoids renderer-owned writes and separate mutation paths.

### 5.5 Workflow and concurrency boundary

Result: **PASS WITH LATER-SPEC OBLIGATION**

The distinction between local lock and cross-ref serialization is correct. DPA-600 must define enforceable merge-time revalidation rather than rely on descriptive process prose.

### 5.6 Evidence boundary

Result: **PASS**

Evidence is explicitly non-authoritative. F-M03 concerns missing planning evidence records, not an evidence-as-runtime-input architecture leak.

### 5.7 Freshness and gates

Result: **PASS WITH LATER-SPEC OBLIGATION**

Derivational freshness is sound. DPA-500 must define how an unvalidated branch-local output is prevented from being consumed as trusted current state before gate completion.

### 5.8 Migration and rollback

Result: **PASS WITH LATER-SPEC OBLIGATION**

The full/split/managed-head/no-migration hierarchy is sound. DPA-700 must require rollback inputs to be recoverable from governed repository history or an explicitly authorized source; rollback cannot depend on an invented history authority.

## 6. Additional findings

### TVA-M01 — Review governance is vendor-bound instead of role-bound

Severity: **MAJOR GOVERNANCE**

The Phase A plan and status require named Claude, ChatGPT and Gemini reviews. A model may lack repository access, may be unavailable or may change product behavior. This creates an irrelevant process blocker unrelated to architecture quality.

Required adjudication:

Define required review roles, not vendors:

1. primary architecture review;
2. secondary technical verification or independent review by a distinct reviewer;
3. maintainer adjudication;
4. consolidated review.

A reviewer is acceptable only when it can inspect the exact ref and produce evidence-linked findings. An access-blocked response is not a review.

This change must not retroactively describe this ChatGPT audit as blind-independent. It is a technical verification audit.

### TVA-m01 — Common-baseline semantics need explicit treatment

Severity: **MINOR**

Claude reviewed `1a73ec...`; later planning integration exists at `1bf72d...`. The consolidated adjudication must distinguish:

- architecture findings against the reviewed baseline;
- planning completeness against the later integration ref.

It must not claim all reviewers inspected identical trees unless they did.

### TVA-m02 — Review output verdict vocabulary is inconsistent

Severity: **MINOR**

Claude uses `ACCEPT_WITH_CHANGES`; prompts and prior responses also used `PASS_WITH_CHANGES`, `BLOCK`, `REJECT` and `BLOCKED`. Review outcome and access outcome must be separate namespaces.

Recommended states:

- review result: `ACCEPT`, `ACCEPT_WITH_CHANGES`, `MAJOR_REWORK`, `REJECT`;
- execution/access result: `COMPLETE`, `ACCESS_BLOCKED`, `INPUT_INCOMPLETE`.

### TVA-m03 — Consumer trust boundary needs an explicit requirement anchor

Severity: **MINOR, LATER-SPEC BLOCKER**

A generated target may exist in a branch before lifecycle/gate validation completes. DPA-200 and DPA-500 must define whether consumers may treat branch-local output as trusted and how consumption is gated or visibly qualified.

## 7. Traceability verification

The post-Claude planning integration captures all Claude findings, later-spec obligations, tests, evidence and rollback concerns. It is suitable as planning traceability but remains derived.

Required future corrections after ADR-009 and ADR-010:

- use one status namespace per column;
- map one invariant ID to one invariant;
- add explicit decision links;
- add motivation rows for dry-run, manual-document compatibility and consumer-before-validation risk;
- distinguish reviewed architecture baseline from later planning-integration ref;
- record TVA-M01 through TVA-m03 as review-originated obligations.

No planned implementation is falsely presented as completed.

## 8. Risk assessment

### Architecture risk

**LOW TO MODERATE** before DPA-200–DPA-700 completion. No foundational flaw is present, but region ownership, target semantics, configuration inputs and consumer trust require closure.

### Governance risk

**MODERATE** until status namespaces, invariant ownership, evidence bar and role-based review requirements are adjudicated.

### Main-repository integration risk

**UNKNOWN / NEEDS_MAIN_REPO_VALIDATION**. The architecture correctly acknowledges that exact schema, modules, locks, writers, readers and gates require DP1 evidence.

### Parallel-system risk

**LOW**, provided minimal evidence records remain static records and no independent projection CLI, registry, evidence store or gate suite is introduced.

## 9. Maintainer adjudication recommendations

### DPA-ADR-009

Recommended decision:

- Keep repository-fact classifications closed.
- Define separate closed namespaces for document maturity and work/exit progress.
- Represent recorded-baseline scope through explicit metadata and evidence records, not a qualified `VERIFIED` subtype.

### DPA-ADR-010

Recommended decision:

- DPA-000 owns the canonical stable-ID invariant register.
- LAB_EXECUTION_CONTRACT references it.
- Lab-only governance rules remain outside the DPA invariant register.
- Traceability is one-to-one and derived.

### DPA-ADR-011

Recommended decision:

- Require minimal static exact-ref records.
- Record method, inspected subjects, date and revalidation requirement.
- Prohibit evidence tooling or a maintained main-repository mirror in the lab.

### Review-governance decision

Recommended additional decision or execution-contract amendment:

- Replace named-model requirements with role-based review requirements.
- Count Claude's review as the primary architecture review.
- Count this document as the secondary technical verification audit.
- Treat Gemini access failures as execution records only, not reviews or architecture verdicts.

## 10. Phase A recommendation

Phase A is ready for maintainer adjudication now.

Before Phase A can be stable:

1. adjudicate ADR-009, ADR-010 and ADR-011;
2. adjudicate the role-based review-governance correction;
3. apply accepted normative terminology and ownership changes;
4. create minimal baseline evidence records if ADR-011 is accepted;
5. regenerate traceability and align the diagram;
6. record later-spec obligations without pretending they are implemented;
7. run a final consistency review against the resulting exact ref.

A Gemini architecture review is not required when Gemini cannot inspect the exact repository ref. Repeated access-blocked attempts add no evidence.

## 11. Final verdict

**ACCEPT_WITH_CHANGES**

The Phase A architecture is coherent and suitable for adjudication. Stability is blocked by governance closure and accepted corrective edits, not by a foundational architecture defect.
