# Claude Falsifying Architecture Review — Federated System Foundation

**Notice: `NON_AUTHORITATIVE_EXTERNAL_REVIEW`.** This document is an independent, falsification-oriented external review projection. It grants the DPA Lab no authority over AGF, ROS or the Kit. Every substantive statement is attributable to the source repository and exact ref named below. **Maintainer adjudication is still pending; this review adjudicates nothing.**

- Review status: complete / final (pre-adjudication)
- Reviewer model: Claude Opus 4.8 (Anthropic)
- Review date: 2026-07-21
- Reviewed package commit: `ea84c80e4531d3a3e5ba3f3e2ed51ab2969ebc97` (DPA-Lab branch `review/system-foundation-package`, path `reviews/external/system-foundation/`)
- Reviewed PR heads: AGF PR #2 `93f34672cbd153839efad9303d2e9bbf2938406a`; DPA-Lab PR #7 `80a6e72926cc0b8b72eb2978bff8a1d91c3821d0`; ROS PR #2 `9eee8139d23c3e03f3c7f2ee2fbf711f6e7ed896`.

## Source and authentication boundaries

- **Independently verified:** DPA-Lab PR #7 (compared byte-for-byte against the live public PR) and all Kit repository facts in F1 (branch existence, heads, divergence from main, commit subjects/dates, changed files), checked against public `vfi64/agentic-project-kit`.
- **Source-attributed, not independently authenticated:** all AGF PR #2 and ROS PR #2 content (private repositories; verifiable only for package-byte integrity, not private-origin authenticity).
- **Maintainer-confirmed, not independently re-verified here:** the pull-request numbers and open status in F1 (Kit PR #1867, PR #1865) and the statement that PR #1867 predates the later system-foundation hold. The GitHub PR API was rate-limited (HTTP 403) during this review, so PR identity/state and creation-time ordering rest on maintainer-supplied GitHub data; the underlying branch commits and their author/committer dates were verified from git directly.

## 1. Pre-review gate results (recap)

All four mandated gates PASS at the exact package commit: manifest completeness; per-file `content_sha256` and `git_blob_sha1` match for all 9 files; declared changed-file sets (AGF 5, DPA 1, ROS 3) match; authority/snapshot/source classification unambiguous. `REVIEW_PACKAGE_INVALID` was not raised.

The one independently verifiable source (DPA PR #7) is content-identical to the live PR, differing only by a single trailing newline (live 3041 bytes, package 3040 bytes) — exactly the normalization the binding `hash_contract` declares. Package finding **P1 (MINOR):** `hash_contract.copy_rule` ("byte-identical copies") contradicts `content_sha256` ("no trailing newline"); the verifiable file proves non-byte-identity. Correct the wording to "byte-identical after declared normalization." AGF/ROS bytes are therefore "content-identical modulo declared normalization," not "byte-identical to the private source."

## 2. Executive summary

The proposed system is a layered federation — AGF (governance method) over DPA (knowledge/projection) over the Kit (runtime) over ROS (operating model) over applications — with GitHub repositories as declarative long-term memory and bounded LLM context projections as the session interface. The documents are unusually disciplined about authority language, evidence gating, and refusing to let projections or upstream repos silently become downstream authorities. That discipline is real and worth preserving.

Under falsification the baseline does not yet hold as a finished foundation. The layering is presented as a clean vertical stack but is not one; AGF is overscoped as method owner, universal schema owner and cross-repo program planner at once; the two AGF architecture documents specify two incompatible graph models; ROS reproduces a large fraction of Kit-owned concepts and is protected from becoming a "second Kit" only by assertion; there is a latent bootstrap cycle (AGF validity depends on a Kit pilot, Kit adoption depends on AGF) held open only by a manual hold; and the load-bearing value assumptions are unmeasured. Independently, the Kit "non-change" evidence is incomplete and false in its general form.

The direction is salvageable and in places good. The current baseline needs structural revision before it is safe to build on.

## 3. Architecture verdict

**MAJOR REVISION.** Carried, after the F1 correction below, by F2–F5 plus the corrected F1. Not ACCEPT/ACCEPT WITH CHANGES because the required changes are structural. Not REJECT because the direction is sound and most material is reusable.

## 4. Major findings

### F1 — The Kit "non-change" evidence is incomplete and false in its general form (corrected)

`kit/NON_CHANGE_EVIDENCE.md` states that no Kit file was created or modified for the initiative and discloses only the temporary branch `planning/agf-dpa-ros-adoption-hold` "without commits."

Independently verified against public `vfi64/agentic-project-kit`:

- `planning/agf-dpa-ros-adoption-hold` = `6a9da7d…` = Kit main HEAD, 0 divergent commits. "Without commits" is TRUE.
- `agent/agf-capture-ledger` (`2269dec…`) diverges from main (0 behind) with commits "Add AGF capture ledger profile" and "Seed Kit governance capture ledger" (2026-07-20), creating `.agentic/governance/capture-events.jsonl` and `.agentic/governance/capture-profile.json`.
- `agent/record-ros-review-economy-research` (`2a2a564…`) diverges (0 behind) with commit "Record ROS and review-economy research conclusions" (2026-07-19), creating `docs/reference/AGENTIC_CODING_RESEARCH_INPUTS.md`.

Maintainer-confirmed (not re-verified here): these are open Kit PRs **#1867** (head `2269dec…`, `agent/agf-capture-ledger`) and **#1865** (head `2a2a564…`, `agent/record-ros-review-economy-research`), and PR #1867 was created **before** the later system-foundation hold rule was formulated.

**Corrected finding.** The blanket claim that no files/commits were created for AGF/ROS work is false, because it omits pre-existing Kit branches and, in particular, open PR #1867, which already creates exactly the AGF governance capture-ledger state (`.agentic/governance/…`). The evidence is therefore **incomplete and, in its general form, inaccurate**.

**What is NOT established.** A *retroactive breach* of the hold is **not** proven. My independent evidence shows the capture-ledger commit and the hold document share the same date (2026-07-20); it does not establish intra-day ordering. Per maintainer-confirmed PR creation time, PR #1867 predates the hold rule. The earlier claim "the hold was already broken" is therefore withdrawn.

**Correct disposition.**

1. PR #1867 is **`PRE_EXISTING_UNADJUDICATED_KIT_WORK`**: it produces the capture-ledger pre-existing state whose further Kit adoption is now to be gated until local Mac / Agentic-Kit adjudication.
2. It must be **disclosed** in the non-change evidence and placed **under the new hold**; until local adjudication it must not be continued, counted as adoption, or merged.
3. PR #1865 is a **related research pre-existing item** (dated 2026-07-19, explicitly claims no adoption); it must be disclosed but is a weaker contradiction than PR #1867.
4. The non-change evidence and the hold text must be corrected to record this pre-existing state rather than assert a clean boundary.

Severity: MAJOR — evidentiary integrity and disclosure failure (independent of the withdrawn breach claim).

### F2 — AGF is overscoped (method owner, universal schema owner, program planner at once)

`AGENTIC_SYSTEM_ARCHITECTURE.md` gives AGF the common object/relation vocabulary and "federated graph domains" spanning reasoning, planning, execution, representation and operation — but representation is DPA's, execution is the Kit's, and planning/operation are ROS's. `SYSTEM_FOUNDATION_MASTERPLAN.md` also places the cross-repo program plan (sequencing DPA/Kit/ROS) inside AGF, while `AUTHORITY_AND_INTERCHANGE_MODEL.md` says AGF does not own downstream planning. AGF is simultaneously methodology, system-wide schema authority and program planner, contradicting its own non-goal "no universal central planner" and inflating coupling.

### F3 — The two AGF documents specify two incompatible graph models

`AUTHORITY_AND_INTERCHANGE_MODEL.md` describes loose federation (versioned interchange records, adoption states, never implicit authority). `AGENTIC_SYSTEM_ARCHITECTURE.md` describes one connected "federated graph" with cross-domain typed relations spanning repos. These are different architectures (import/export of validated records versus a shared live typed graph with hand-maintained cross-repo edges). The package does not choose; maintainability cannot be assessed while both coexist.

### F4 — ROS reproduces Kit-owned concepts and is not structurally prevented from becoming a second Kit

ROS specifies roles, a work-package lifecycle state machine (`CAPTURED`…`SUPERSEDED`), session entry, an execution contract, evidence requirements, gates, closeout and multi-repo coordination — much of it overlapping Kit capabilities (handoffs, gates, lifecycle, evidence capture, workspace, planning) and DPA-owned concepts (trust states, acceptance). "ROS must not become a second Kit" is asserted repeatedly but backed by no criterion, test or gate that would fail on drift. The defense is authorial restraint, not structure.

### F5 — A latent bootstrap circular dependency exists, held open by a manual hold (corrected)

The authority graph is acyclic by construction, but the realization graph is not: AGF's model can be validated only by the Stage-5 pilot, which requires the Kit runtime; the Kit will later adopt AGF/DPA/ROS. So AGF-validity depends on Kit and Kit-adoption depends on AGF — a bootstrap cycle currently held open only by the manual "hold Kit until Mac." This finding does not depend on any completed breach: the point is structural. If the hold gate slips in future, the cycle reasserts; the architecture is acyclic only under a manually maintained scheduling gate, which should be made an explicit, testable invariant rather than a prose intention.

## 5. Minor findings

- F6 — Governance overlap AGF↔DPA: DPA-100–500 already own acceptance authority, gates, trust states and freshness enforcement; AGF now claims "meta-governance." The split between AGF governance method and DPA projection-acceptance governance is unspecified.
- F7 — No named owner for the cross-repo interchange schema/versioning, nor for resolving conflicting adopted versions.
- F8 — Projection-type proliferation (session/work-package/review/handoff) may be one parameterized projection with a scope/role/token-budget argument; no projection cost/eviction/priority model is defined.
- F9 — Pre-existing capture work sits outside the governed sequence (corrected): the AGF capture-ledger (PR #1867) is unadjudicated Kit work outside the masterplan's governed Stage-3 sequence. No temporal sequencing *violation* is proven; the required action is to adjudicate and retrofit it into the governed sequence (or revert it) rather than let it accrete as de facto adoption.
- P1 — manifest `copy_rule` vs `content_sha256` wording contradiction (see §1).

## 6. Risks

- R1 (high): the connective runtime (interchange validation, graph validation, projection rendering, capture governance) is unbuilt and blocked behind Kit-at-Mac; today the system is three specification repos with no operable runtime and cannot dogfood itself.
- R2 (high): hand-maintained cross-repo typed edges plus per-repo × per-object-type × per-version adoption state, maintained without a graph engine, transactions, referential-integrity enforcement or cross-repo serialization — the DPA-600 concurrency problem multiplied across repos.
- R3 (medium): unbounded growth of append-only `.agentic/governance/capture-events.jsonl` in Git history, no compaction story.
- R4 (medium): two masterplans (AGF system masterplan and DPA `MASTERPLAN.md`) coordinating overlapping work invite an authority clash on disagreement.
- R5 (medium, corrected): the non-change evidence being incomplete and false in its general form is a **disclosure/accuracy failure** (not a proven breach). It nonetheless reduces confidence in the initiative's other self-reported boundaries that a reviewer cannot independently check (AGF/ROS private), so those boundaries need explicit, verifiable disclosure.

## 7. Authority violations

- A1: AGF masterplan sequences downstream DPA/Kit/ROS work while the authority matrix denies AGF downstream planning ownership (F2).
- A2: AGF's federated-graph-domains claim the object/relation vocabulary of representation (DPA), execution (Kit) and operation (ROS) (F2).
- A3 (corrected): pre-existing unadjudicated Kit capture-ledger work (PR #1867) must be brought under the new hold as `PRE_EXISTING_UNADJUDICATED_KIT_WORK`. This is **not** a proven retroactive authority violation; the concrete authority defect is the incomplete/false non-change disclosure (A4), not a demonstrated breach.
- A4: the non-change evidence artifact under-reports actual Kit branch/PR state, weakening its evidentiary authority (F1).

## 8. Simplification proposals

- S1 — Choose loose federation (per-repo graphs + validated versioned interchange records); delete the single shared "federated graph with cross-domain typed relations." Removes hand-maintained cross-repo edges; matches the authority model. (Resolves F3, R2.)
- S2 — Trim AGF to governance/reasoning method + evidence/review/adjudication/adoption/falsification vocabulary + a minimal shared meta-vocabulary; remove the program masterplan and multi-domain schema ownership from AGF. (Resolves F2, A1, A2.)
- S3 — Shrink ROS to a thin operating-policy profile (roles, authority contexts, cross-repo coordination); return work-package lifecycle, evidence and gates to the Kit; or do not stand ROS up as a separate repo until a pilot proves it needs independence. Whether ROS stays a Kit operating profile or later becomes an independent specification repository should be **decided by the pilot, not by the current architecture assertion.** (Resolves F4.)
- S4 — Move the cross-repo plan into one clearly non-authoritative coordination artifact with a named owner, distinct from AGF method. (Resolves R4, part of A1.)
- S5 — Collapse the projection-type catalog into one parameterized projection contract with scope/role/token-budget plus an explicit eviction/priority rule. (Resolves F8.)
- S6 — Correct `copy_rule` wording (P1).

## 9. Missing evidence

- E1: no baseline showing the federated typed graph is cheaper/more reliable than Git + Markdown + thin validated manifests.
- E2: no measurement that bounded context projections improve LLM task success or reduce context versus repo retrieval (no metric, baseline or threshold).
- E3: no evidence independent agents can use the shared typed vocabulary consistently.
- E4: no evidence the graph/interchange reduces rather than increases dual maintenance (the capture ledger already duplicates state the Kit registry/lifecycle track).
- E5: PR identity/open-status for #1867/#1865 and the intra-day hold ordering — maintainer-confirmed, not independently re-verified (API rate-limited).
- E6: AGF/ROS source authenticity against their private repos — unverifiable without read access.

## 10. Open research questions

- Q1: what measurable edge-maintenance and projection-regeneration cost per change makes the federated graph net-negative versus a monorepo or a single materialized-view repo?
- Q2: what is the minimal shared meta-vocabulary that lets independent agents interoperate without AGF owning every domain's schema?
- Q3: can cross-repo referential integrity be enforced with GitHub as substrate, or is a build-time materialized index required (and who owns it)?
- Q4: what is the provenance-survival and successor-continuation success rate for an LLM working only from projections, no chat memory, across a real multi-repo task?
- Q5: is ROS separable from the Kit at all, or is an "operating model" inherently a Kit profile? (Pilot-decidable.)

## 11. Recommended order of next work (corrected)

1. Correct F1 disclosure: record open PRs #1867 and #1865 in the non-change evidence; classify #1867 as `PRE_EXISTING_UNADJUDICATED_KIT_WORK`; place it under the new hold (no continuation, adoption or merge before local Mac/Kit adjudication); correct the hold text to acknowledge the pre-existing capture-ledger state. (No claim of a retroactive breach.)
2. Decide the graph model (S1); a system with two graph models cannot be reviewed further.
3. Trim AGF (S2, S4) and decide ROS scope (S3).
4. Specify the AGF↔DPA governance split (F6); name the interchange/version and program-plan owners (F7).
5. Define measurable falsification criteria, baselines and thresholds (F10-class gaps, E1–E4) before any adoption.
6. Only then run the Stage-5 bounded pilot with pre-registered metrics against a monorepo/Markdown baseline.
7. Keep Kit adoption blocked until the above are resolved and native Kit commands are available.

## 12. Must be resolved before any Kit adoption (corrected)

- F1 disclosure corrected; PR #1867 placed under the hold as `PRE_EXISTING_UNADJUDICATED_KIT_WORK` and neither continued, adopted nor merged pending local adjudication; PR #1865 disclosed.
- Graph model chosen (S1); AGF trimmed (S2/S4); ROS scope decided (S3).
- AGF↔DPA governance split defined (F6); interchange/version and program-plan authority named (F7).
- Measurable success/failure criteria and baselines defined (E1–E4).
- Pilot executed and adjudicated with provenance/authority/continuation evidence.

## 13. May wait until after the first pilot

- Full multi-domain typed graph and richer relation catalog (only if the pilot proves the graph earns its cost).
- Projection-type refinement beyond the minimal parameterized contract.
- ROS repository profiles catalog and application-repo (Wrapper / Comm-SCI) evaluation.
- Adoption-state tooling and cross-repo evidence-reference automation.

## 14. If a better architecture exists

Keep four *concerns* but not four *runtimes*: the Kit as the single runtime and evidence/gate authority; AGF as a small method + meta-vocabulary spec; DPA as the representation/projection spec; ROS as a Kit *operating profile* rather than a separate runtime repo (pilot-decidable). Treat each repo's graph as local; connect repos only through validated, versioned interchange records (no shared live graph). Materialize a query/index view at build time from Git rather than treating raw Git files as the graph. This removes the second-runtime risk (F4), the cross-repo edge-maintenance cost (R2), the AGF overscope (F2) and the dual-graph contradiction (F3), while retaining authority separation, evidence gating and projection-based memory. It is superior on minimality, maintainability and operability; inferior only if a genuine cross-repo live-query requirement is later proven — which is what the pilot should test.
