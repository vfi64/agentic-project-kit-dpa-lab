# ROS Roadmap

Status: bootstrap proposal
Status-date: 2026-07-20

## Phase 0 — Authority and bootstrap

- establish repository mission and authority boundaries;
- define mandatory bootstrap order;
- record AGF, DPA and Kit dependencies as non-adopted inputs;
- prohibit duplicate runtime implementation.

## Phase 1 — Operating metamodel

- roles and permissions;
- work-package lifecycle;
- session entry and closeout;
- blocking and escalation rules;
- local versus cross-repository authority.

## Phase 2 — Repository profiles

Define bounded profiles such as:

- single-maintainer research repository;
- software implementation repository;
- architecture laboratory;
- scientific control repository;
- multi-repository program.

## Phase 3 — DPA context contracts

Specify the ROS requirements for:

- session context projection;
- work-package context projection;
- review context projection;
- handoff context projection;
- freshness and conflict reporting.

## Phase 4 — Kit capability mapping — blocked until Kit local adoption

Map each ROS contract to existing or required Agentic Project Kit capabilities. No ROS-local replacement CLI may be created merely because a Kit capability is pending.

## Phase 5 — Bounded pilot

Run one end-to-end workflow across capture, local planning, execution evidence and successor handoff.

## Phase 6 — Application profiles

Evaluate Wrapper and Comm-SCI repositories only after pilot adjudication.

## Current next step

Review `ARCHITECTURE.md` and `OPERATING_MODEL.md` against the current remote states of AGF, DPA and Kit, then establish a governed ROS bootstrap before detailed specification work.