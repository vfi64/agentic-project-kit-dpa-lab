# Package P Limited PPR-M03 Rereview Prompt

Status: active

Status-date: 2026-07-19

Review repository: `vfi64/agentic-project-kit-dpa-lab`

Exact corrected review ref: `c12eb19acb07325958e06800f5591aa3bf5f03c7`

Immutable review branch: `review/package-p-ppr-m03-20260719-r2`

Superseded preliminary corrected ref: `375d3d2aab65531229fd0432cd4bc35bda2c448d`

Original review ref: `18d0fd08b27d97aef1b06b5a75079527290ca8e4`

Original finding: `PPR-M03`

## Assignment

Perform a limited independent rereview of only the accepted PPR-M03 correction and its direct synchronization consequences.

Work exclusively from the exact corrected review ref. Do not review the moving working branch. Do not edit any repository file or branch.

## Mandatory bootstrap

Read the normal Lab bootstrap in the order defined by `LAB_BOOTSTRAP.md`. Then read at minimum:

1. `STATUS.md`;
2. `MASTERPLAN.md` and `MASTERPLAN_REMOTE_PREPARATION.md`;
3. `specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`;
4. `specs/dpa/DPA-500-FRESHNESS-AND-GATES.md`;
5. ADR-016 and ADR-021;
6. `probes/PROBE_EXECUTION_AND_EVIDENCE_CONTRACT.md`;
7. `probes/PROBE-002-MANUAL.md`;
8. `probes/PROBE-002-FIXTURE-MANIFEST.md`;
9. `reviews/claude/CLAUDE_PACKAGE_P_REVIEW.md`;
10. `reviews/adjudication/PACKAGE_P_REVIEW_ADJUDICATION.md`;
11. `reviews/PACKAGE_P_REVIEW_CORRECTION_AUDIT.md`.

## Exact questions

Determine only whether:

1. P002-C059 correctly represents a gate-set identity change on otherwise unchanged accepted bytes as the trigger for gate-set re-acceptance;
2. P002-C059 preserves the prohibition on rendering or target mutation during re-acceptance;
3. P002-C059 remains subject to all non-gate context guards and does not permit re-acceptance after source, configuration, contract, renderer, partition, ownership, target-semantics, required-base or acceptance-context drift;
4. `F002-REACCEPT-GATESET-TRIGGER` is a sufficient semantic fixture for that case without inventing main-repository serialization;
5. P002-C060 correctly represents `block-new` and `strict` as fail-closed for new projection or new acceptance attempts when mandatory safety cannot be established;
6. P002-C060 correctly permits previously accepted legacy content to remain readable only under the declared compatibility stage and does not let compatibility authorize a new mutation or acceptance;
7. `F002-STAGE-BLOCK-NEW-VS-LEGACY` is a sufficient semantic fixture without selecting implementation;
8. the manual and manifest now contain exactly 60 declared cases and bidirectional mappings;
9. the two added cases remain distinct from P002-C037, P002-C056 and the other existing cases;
10. no correction changed normative DPA text, selected production mechanisms, claimed execution or released DPA-600/DPA-700 restrictions.

## Scope prohibition

Do not reopen PPR-M01, PPR-M02, PPR-m01 through PPR-m04 or PPR-e01 through PPR-e03 unless a direct contradiction caused by P002-C059 or P002-C060 is found.

Do not inspect or infer current main-repository implementation behavior. No Probe has run and no executable fixture has been materialized.

## Required output

Return exactly one verdict:

- `ACCEPT`;
- `ACCEPT_WITH_CHANGES`;
- `REJECT`.

For every finding provide:

- stable finding ID beginning `PPR-M03-RR-`;
- severity: `BLOCKER`, `MAJOR`, `MINOR` or `EDITORIAL`;
- exact file and section;
- normative anchor;
- observed defect;
- consequence;
- smallest safe correction;
- whether another new Lab ref and rereview are required.

Also state:

- exact ref reviewed;
- whether PPR-M03 is fully resolved;
- whether Package P may proceed to final Maintainer closure;
- whether local fixture-materialization planning may begin after closure;
- whether Probe execution remains blocked;
- whether DPA-600 remains frozen and DPA-700 unstarted;
- review method and limitations.

Begin by confirming exact ref identity and completed bootstrap. Then complete the rereview without implementation or file changes.
