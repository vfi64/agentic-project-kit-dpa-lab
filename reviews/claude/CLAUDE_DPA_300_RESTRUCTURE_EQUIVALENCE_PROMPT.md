# Claude Prompt — DPA-300 Promotion-Restructure Equivalence Verification

You are working in the private architecture laboratory `vfi64/agentic-project-kit-dpa-lab`.

Perform an independent, exact-ref, diff-scoped equivalence verification of the DPA-300 normative specification restructuring.

Do not modify the repository. Do not adjudicate. Do not rely on chat memory or author intent.

## Exact refs

Certified pre-promotion comparison ref:

`a86aa49851c96c39380a8eb4afad17763263fe00`

Promotion/restructure ref:

`e3f8b85c5eb76b8c6cae76dde317fd33f236ce88`

The target file is:

`specs/dpa/DPA-300-REGISTRY-LIFECYCLE-INTEGRATION.md`

Also inspect, only as needed to understand the certification boundary:

- `reviews/consolidated/DPA-300_POST_ADJUDICATION_DIFF_RECHECK.md`
- `reviews/consolidated/DPA-300_ADJUDICATION_RECORD.md`
- `decisions/DPA-ADR-016-ACCEPTANCE-STATE-AND-INTERRUPTED-RECOVERY.md`
- `decisions/DPA-ADR-017-PARENT-ENTRY-PARTITION-CONTRACT.md`
- `specs/dpa/DPA-100-FOUNDATIONS.md`
- `specs/dpa/DPA-200-DOCUMENT-MODEL.md`
- `traceability/DPA-300_TRACEABILITY.md`

## Role and independence

You are the independent equivalence verifier under DPA-ADR-020.

Disclose whether you authored the restructure. If you did, STOP with `INDEPENDENCE_BLOCKED`.

Prior review exposure does not by itself block the role, but you must verify the committed artifacts rather than intended meaning.

## Verification questions

For every load-bearing DPA-300 rule at the certified pre-promotion ref, determine whether the promotion/restructure ref:

1. preserves the rule with equivalent or stronger normative force;
2. moves the rule without semantic change;
3. rewords it with a real semantic relaxation or strengthening;
4. removes it;
5. introduces a new normative rule that was not reviewed;
6. changes owner, authority boundary or later-spec delegation;
7. changes status, classification or repository-evidence scope.

At minimum, verify individually:

- existing registry and lifecycle remain sole authorities;
- optional projection metadata and manual-document compatibility;
- parent-entry `PartitionContract` uniqueness and field ownership;
- renderer identifier/version fields;
- contract and plan fingerprint domains;
- Recover → Resolve → Inspect → Validate → Render → Plan → Preflight → Lock → Revalidate → Write → Verify → Record → Release ordering;
- dry-run and exact-plan-bound mutation;
- base/source/target/contract/renderer/partition/ownership drift guards;
- lifecycle-owned Workspace-resolved acceptance state;
- direct-write detection and independent drift classification;
- stale-lock and interrupted-refresh recovery;
- crashed-after-Write re-verification conditions;
- mandatory regeneration when recovered-plan validity cannot be proven;
- atomic complete-file replacement and preservation of non-projected bytes;
- payload, preserved-region, partition and expected complete-target fingerprints;
- immediate `written-unverified` after Write;
- no nested projection mutation;
- evidence remains non-authoritative;
- existing writer paths must route through lifecycle rather than a parallel command;
- `CURRENT_HANDOFF.md` remains conditional and no production form is selected;
- `NEEDS_MAIN_REPO_VALIDATION` fences remain intact;
- DPA-500/600/700/800 ownership boundaries remain intact.

## Required output

Produce a commit-ready English report with:

1. metadata and exact refs;
2. independence disclosure;
3. method;
4. changed-section map;
5. rule-by-rule equivalence table;
6. genuine semantic relaxations;
7. genuine semantic strengthenings;
8. removed rules;
9. newly introduced rules;
10. authority/ownership changes;
11. traceability or terminology effects;
12. certification-scope assessment;
13. PASS or FAIL;
14. exact bounded corrections, if any;
15. final recommendation.

Use these verdicts only:

- `PASS_EQUIVALENT` — every load-bearing rule is equivalent or stronger and every new rule is consistent and explicitly identified;
- `PASS_WITH_EXPLICIT_RATIFICATION` — bounded semantic differences exist and are fully enumerated for Maintainer ratification;
- `FAIL_NON_EQUIVALENT` — a material rule is missing, relaxed ambiguously, contradicted or impossible to map;
- `INDEPENDENCE_BLOCKED`.

Do not treat textual similarity as equivalence. Do not treat reorganization as harmless without mapping every load-bearing rule. Do not use main-repository evidence; this is a lab-artifact lineage verification.