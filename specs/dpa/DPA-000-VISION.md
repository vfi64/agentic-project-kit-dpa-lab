# DPA-000 — Vision and Architectural Principles

Status: draft

## Vision

The Document Projection Architecture extends the existing `agentic-project-kit` document-management system so that registered documents may represent deterministic views of canonical repository-backed state.

## Core invariants

1. Canonical state never owns rendering logic.
2. Renderers never own write logic.
3. The lifecycle never invents domain state.
4. Workflow orchestration never invents document semantics.
5. The registry describes contracts, not executable plugins.
6. Renderers return text or bytes only.
7. Only the lifecycle writes projection targets.
8. Only workflow orchestration serializes across branches and pull requests.
9. Evidence is never runtime authority.
10. Runtime projection contracts live in the main repository's registry and lifecycle system.
