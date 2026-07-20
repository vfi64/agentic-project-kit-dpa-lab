# Agentic Project Kit Adoption Hold

Status: BLOCKED
Recorded: 2026-07-20
Target repository: `vfi64/agentic-project-kit`

## Reason

The Maintainer currently has no Mac access. The Kit's established Agentic-Kit commands must be used for document registration, planning integration, lifecycle updates, validation, gates, protected-diff review, pull request completion and handoff. A remote prose-only mutation would bypass the repository's own governance.

## Prohibited until unblock

- adding AGF/DPA/ROS planning documents directly to the Kit;
- changing `PROJECT_DIRECTION.yaml` or Masterplan Q2 from this initiative;
- registering documents or rules manually;
- claiming Kit adoption or implementation;
- treating the temporary Git branch as a governed plan.

## Unblock condition

`MAINTAINER_AT_MAC_AND_AGENTIC_KIT_COMMANDS_AVAILABLE = true`

## Required first local action

From a fresh, evidence-verified Kit main state:

1. run the repository bootstrap and handoff validation;
2. inspect current Direction, planning, document registry, rule registry and lifecycle state using native commands;
3. determine the correct local planning object for AGF/DPA/ROS adoption without disturbing Masterplan Q2;
4. create bounded implementation slices;
5. execute the normal tests, audits, protected-diff, PR and handoff workflow.

## Intended capability areas for later evaluation

- capture-ledger commands and projections;
- graph/schema registry and validation;
- promotion and adoption records;
- DPA context projection rendering;
- ROS work-package runtime support;
- cross-repository evidence references;
- integration with deterministic successor handoff packages.

## Authority

This record is an AGF coordination reminder only. It is not authoritative Kit planning and creates no Kit obligation until locally adopted through the Kit's own governed process.