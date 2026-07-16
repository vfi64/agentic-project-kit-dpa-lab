# DPA-900 — Future Evolution

Status: planned

## Deferred future-scope notes

- Evaluate risk-based independent-context verification for evidence-bearing normative and mutation-capable workflows.
- The relevant separation is authorship context versus verification context, not mandatory model-vendor diversity.
- Any later rule must be exact-ref bound, role-based and proportionate to risk.
- Low-risk editorial or fully deterministic changes require a bounded fast path.
- Independent-context verification must complement, not replace, deterministic tests, Maintainer adjudication and Probes against the real repository.

## Planned objective — sustainable governance and review economics

DPA-900 MUST define how the completed architecture reduces the long-term cost of safe evolution without weakening governance quality, evidence discipline or Maintainer control.

The objective is not fewer checks by default. The objective is proportionate assurance with smaller and more mechanically verifiable review surfaces.

The future contract MUST address at least:

1. risk-based review depth rather than one fixed review process for every change;
2. full review for new authorities, invariant changes, mutation paths, gates and other high-impact semantics;
3. diff-scoped equivalence verification for refactors and structurally large changes that claim unchanged meaning;
4. bounded fast paths for low-risk editorial and fully deterministic generated changes;
5. exact-ref independent-context verification for evidence-bearing high-risk work where authorship bias is material;
6. machine-checkable vocabulary, cross-reference, invariant, traceability and file-ownership consistency;
7. smaller normative ownership surfaces and elimination of competing normative homes;
8. explicit cost controls so verification effort remains proportionate to the risk reduced;
9. retention of deterministic tests, real-repository Probes and Maintainer adjudication as independent defense lines.

### Planned success criteria

The completed DPA evolution model MUST make future architecture and governance changes cheaper to validate than equivalent changes under the pre-DPA process, without reducing:

- semantic correctness;
- reproducibility;
- evidence quality;
- authority clarity;
- rollback safety;
- Maintainer visibility and decision rights.

Evidence of success SHOULD include measurable trends such as:

- fewer full-document rereads for editorial-equivalent changes;
- a higher proportion of consistency checks executed mechanically;
- smaller review diffs and fewer duplicated normative definitions;
- explicit classification of review paths by risk;
- fewer post-review synchronization defects;
- documented cases where a fast path was used without bypassing a required high-risk gate.

DPA-900 MUST define a governed fallback: if reduced-cost verification cannot establish equivalence or safety, the change returns to the full review path.

## Sequencing boundary

This objective is mandatory future planning scope but creates no active DPA-400 or DPA-500 requirement. Detailed specification begins only after applicable Probe evidence has bounded the remaining architecture and implementation risks.

This note preserves the observed lab learning without creating a current runtime specification or implementation obligation. Detailed treatment belongs to DPA-800/DPA-900 and later main-repository governance after the DPA-400/500 and Probe sequence.
