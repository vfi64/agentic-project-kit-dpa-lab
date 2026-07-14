# Gemini Review Prompt — DPA Phase A

Status: active
Status-date: 2026-07-14
Repository: `vfi64/agentic-project-kit-dpa-lab`
Review ref: `1bf72d1313335b6acfe5af960dd7315f42a7756a`
Access mode: read-only

Copy the prompt below into Gemini.

---

You are performing an independent architecture review of the Document Projection Architecture (DPA) laboratory.

This is NOT a design session.

You have READ-ONLY access. Do NOT modify files, rewrite specifications, produce patches, or propose implementation code. Your output is a review document only.

## Repository and exact review ref

Repository:

`vfi64/agentic-project-kit-dpa-lab`

Review exactly this immutable commit:

`1bf72d1313335b6acfe5af960dd7315f42a7756a`

The repository is public. Do not rely on search-engine indexing. Open the exact GitHub files directly at this commit. If normal GitHub pages fail, replace `github.com/.../blob/...` with `raw.githubusercontent.com/.../...` while preserving the exact commit SHA and path.

Repository root at the exact commit:

`https://github.com/vfi64/agentic-project-kit-dpa-lab/tree/1bf72d1313335b6acfe5af960dd7315f42a7756a`

## Mandatory read order

Read these exact files completely and in this order:

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
13. `traceability/PHASE_A_TRACEABILITY.md`
14. `reviews/README.md`
15. `reviews/claude/CLAUDE_FABLE_5_PHASE_A_REVIEW.md`
16. `reviews/consolidated/PHASE_A_ADJUDICATION_INTAKE.md`
17. `planning/PHASE_A_REVIEW_BACKLOG.md`
18. `integration/MAIN_REPO_VALIDATION_CHECKLIST.md`
19. `integration/IMPORT_PLAN.md`

Direct file URL pattern:

`https://github.com/vfi64/agentic-project-kit-dpa-lab/blob/1bf72d1313335b6acfe5af960dd7315f42a7756a/<PATH>`

Raw file URL pattern:

`https://raw.githubusercontent.com/vfi64/agentic-project-kit-dpa-lab/1bf72d1313335b6acfe5af960dd7315f42a7756a/<PATH>`

Do not review newer commits or branch tips.

## Authority

Use this authority order:

1. exact repository content at the reviewed commit;
2. `MAIN_REPOSITORY_CONTEXT.md` for its recorded main-repository snapshot only;
3. `LAB_EXECUTION_CONTRACT.md`;
4. accepted decisions in `DECISIONS.md`;
5. normative DPA specifications;
6. consolidated reviews;
7. individual reviews;
8. assumptions and proposals;
9. model memory.

Model memory is never authoritative. Do not invent current main-repository facts. Do not upgrade any repository-specific claim beyond its stored evidence classification.

## Review objective

Perform an independent review of the Phase A foundation and critically adjudicate Claude's review.

Do NOT optimize for agreement.

For every Claude finding, return exactly one verdict:

- `ACCEPT`
- `PARTIALLY_ACCEPT`
- `REJECT`

For each verdict provide:

- exact reasoning;
- exact repository evidence by file and section;
- architectural consequence;
- recommended adjudication disposition.

Independently search for contradictions or omissions Claude missed, including:

- authority leaks;
- hidden parallel systems;
- ownership ambiguity;
- invariant conflicts;
- registry and renderer boundary defects;
- lifecycle and workflow inconsistencies;
- concurrency gaps;
- migration and rollback gaps;
- traceability gaps;
- terminology conflicts;
- governance or review-process weaknesses;
- incorrect evidence classifications;
- missing later-spec obligations.

## Required output

Return one Markdown review with exactly these sections:

1. `Review metadata`
   - repository
   - reviewed commit
   - model/version
   - reviewed files
   - access method
2. `Executive assessment`
   - overall result
   - Phase A readiness
   - architecture quality
   - review confidence
3. `Claude finding adjudication`
   - every Claude Major and Minor finding
   - verdict, reasoning, evidence, disposition
4. `Additional findings`
   - Major
   - Minor
   - Editorial
5. `Authority audit`
6. `Invariant audit`
7. `Decision audit`
8. `Traceability audit`
9. `Terminology audit`
10. `Failure-mode audit`
11. `Main-repository validation audit`
12. `Recommended adjudication changes`
   - accepted Claude findings
   - modified Claude findings
   - rejected Claude findings
   - additional findings to add
13. `Phase A exit recommendation`
14. `Final verdict`

The final verdict must be exactly one of:

- `ACCEPT`
- `ACCEPT_WITH_CHANGES`
- `MAJOR_REWORK`
- `REJECT`

## Constraints

- Do not modify the repository.
- Do not produce code or patches.
- Do not rewrite normative specifications.
- Do not propose production implementation.
- Do not invent main-repository evidence.
- Remain within Phase A.
- Treat Claude's review as non-normative evidence input.
- If direct access to the exact public URLs fails, report the precise URL and failure mode. Do not claim that the repository is private or unavailable merely because search indexing failed.
