# Probe Adjudication Procedure

Status: active

Status-date: 2026-07-19

## 1. Purpose

This procedure governs how PROBE-001, PROBE-002 and DPA-400 renderer Probe evidence is interpreted and dispositioned after execution.

Probe evidence does not silently amend architecture, select implementation or promote a specification. Maintainer adjudication is required for every discrepancy that affects architecture, implementation scope, fixture expectations, rerun obligations or status.

## 2. Preconditions

Adjudication MUST NOT begin until:

- the execution and freeze identities are fixed;
- raw bounded observations are preserved;
- case outcomes are recorded;
- cleanup or recovery is dispositioned;
- limitations and unavailable checks are explicit;
- observation and interpretation records are distinct.

A `BLOCKED` case may be adjudicated only as blocked evidence with a defined unblocking or deferral decision.

## 3. Primary discrepancy classes

Every discrepancy MUST receive exactly one primary class:

1. `implementation-conforms` — observed behavior satisfies the tested DPA requirement;
2. `implementation-missing` — required behavior is not implemented or not exposed;
3. `implementation-differs` — behavior exists but conflicts with the current DPA contract;
4. `architecture-incomplete-or-falsified` — an assumption or normative clause is not viable as written;
5. `fixture-or-harness-defect` — the test input, observation method or expectation is defective;
6. `additional-path-discovered` — another relevant parser, reader, writer, renderer, lock, state or recovery path exists;
7. `evidence-insufficient-or-blocked` — the result cannot be established safely or completely.

Secondary notes MAY identify multiple consequences, but they MUST NOT replace the single primary class.

## 4. Required adjudication questions

For each discrepancy, the Maintainer MUST decide:

- what was actually observed at the exact ref;
- which DPA requirement, ADR and Probe expectation applies;
- whether the observation is current implementation capability, absence, incompatibility or unavailable measurement;
- whether architecture remains unchanged;
- whether a bounded normative amendment is required;
- whether the fixture or evidence procedure must change;
- whether implementation planning may proceed, remains blocked or requires a narrower slice;
- whether the same case or related cases require rerun;
- whether another exact ref must be frozen;
- whether an additional repository path enters the validated inventory;
- whether any prior conclusion is narrowed or invalidated;
- whether a Maintainer-only decision remains open.

## 5. Allowed dispositions

One or more explicit dispositions MAY follow the primary class:

- `no-change`;
- `record-current-capability`;
- `implementation-work-required`;
- `bounded-architecture-amendment-required`;
- `fixture-amendment-required`;
- `evidence-procedure-amendment-required`;
- `new-case-required`;
- `rerun-required`;
- `refreeze-required`;
- `scope-narrowed`;
- `deferred-with-blocker`;
- `maintainer-decision-required`.

A disposition MUST identify its owner and completion evidence.

## 6. Architecture amendments

When adjudication requires a normative amendment:

1. preserve the original Probe evidence and adjudication record;
2. identify the smallest affected normative surface;
3. update specification, ADR, traceability, diagram, Probe expectation and status surfaces together where applicable;
4. preserve an exact amendment ref;
5. perform Maintainer adjudication of the amendment;
6. run independent post-adjudication verification when required by status and risk;
7. rerun affected Probe cases when expectations or tested semantics changed;
8. do not promote status until all required verification and rerun obligations are dispositioned.

Probe evidence constrains amendments but does not itself become normative text.

## 7. Implementation consequences

An `implementation-missing` or `implementation-differs` result does not automatically authorize a code change.

Implementation may proceed only when:

- architecture and evidence are synchronized;
- the implementation slice extends existing authorities rather than creating parallel systems;
- current exact-ref mappings are confirmed locally;
- affected frozen writer/lifecycle paths have been released by PROBE-002 adjudication;
- focused, negative, recovery and integration tests are defined;
- rollback and evidence obligations are explicit.

## 8. Rerun rules

A rerun is mandatory when:

- the fixture or harness was defective;
- a normative amendment changes the expected behavior;
- the implementation under test changes;
- a newly discovered path affects case completeness;
- the frozen ref or material fixture bytes change;
- evidence was insufficient for a required conclusion.

A rerun MUST use a new execution identity and, when applicable, a new freeze identity. Prior results remain preserved and are not rewritten.

## 9. Probe-level conclusion

A Probe-level conclusion MUST summarize case counts by outcome, discrepancy classes, unresolved blockers, required amendments, implementation permissions or blocks, fixture/evidence changes, rerun/refreeze obligations, exact refs, limitations and Maintainer decision.

`PASS` does not by itself make a DPA specification `stable`, authorize DP2 or prove the whole main repository conforms.

`PARTIAL` may support bounded conclusions but MUST identify precisely which requirements remain unmeasured.

## 10. Cross-Probe adjudication

After PROBE-001, PROBE-002 and renderer Probe conclusions are available:

1. compare their exact refs and fixture revisions;
2. resolve conflicting observations before architectural promotion or DP2 release;
3. revalidate DPA-300 through DPA-500 against the combined evidence;
4. ensure parser compatibility, lifecycle capability, renderer boundaries and gate semantics form one coherent implementation plan;
5. preserve each Probe's independent outcome rather than collapsing all evidence into one verdict;
6. issue an explicit DP2-baseline release decision or keep DP2 blocked.

When Probe refs diverge, combined conclusions are bounded to the intersection of unchanged governed identities. Divergent refs invalidate or narrow cross-Probe conclusions unless the justification required by `EXACT_REF_FREEZE_PROCEDURE.md` §5 is recorded, impact-analyzed and explicitly accepted by the Maintainer.

## 11. Minimum adjudication record template

```text
adjudication_id:
execution_id:
freeze_id:
probe_id:
case_id_or_scope:
exact_main_ref:
exact_lab_ref:
observed_behavior:
expected_behavior:
normative_anchors:
primary_class:
dispositions:
architecture_change:
implementation_consequence:
fixture_or_evidence_change:
additional_paths:
rerun_required:
refreeze_required:
owner:
completion_evidence:
maintainer_decision:
limitations:
```
