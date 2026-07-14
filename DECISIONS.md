# Decisions

## DPA-ADR-001 — Extend the existing document-management system

Status: ACCEPTED

The DPA shall extend the existing document registry, lifecycle, freshness, evidence, workspace resolver and gate mechanisms. It shall not create a parallel projection-management system.

## DPA-ADR-002 — Lab is non-authoritative

Status: ACCEPTED

The lab contains proposals, reviews and normative design documents. Runtime authority remains exclusively in the main repository after validated adoption.

## DPA-ADR-003 — Renderer responsibility boundary

Status: PROVISIONALLY_ACCEPTED

Renderers compute text or bytes only. The document lifecycle validates, plans, locks and writes. Workflow orchestration serializes across branches and pull requests.
