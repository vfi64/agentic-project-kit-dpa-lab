# Repository Operating System Architecture

Status: bootstrap proposal
Status-date: 2026-07-20

## Mission

ROS defines the operating model for repositories used by humans and LLM agents. It coordinates roles, work packages, operating states, evidence expectations, handoffs and multi-repository workflows.

## Position in the system

- AGF defines reusable governance and reasoning methodology.
- DPA defines structured knowledge and projection architecture.
- Agentic Project Kit provides executable repository, validation, handoff and GitHub tooling.
- ROS defines how those capabilities are operated across repository work.
- Applications adopt ROS profiles while retaining their own domain authority.

## Hard boundary

ROS must not become a second Agentic Project Kit. It specifies operational contracts and profiles; executable implementation should use or extend Kit runtime capabilities through governed adoption.

ROS is not authoritative for:

- Kit implementation state;
- DPA specification state;
- AGF framework acceptance;
- application-domain truth;
- another repository's local plan or release state.

## Core concepts

- Repository
- Role
- Agent session
- Work package
- Operating state
- Authority context
- Evidence requirement
- Gate
- Handoff
- Escalation
- Closeout
- Multi-repository dependency

## Work-package chain

A normal work package should make the following chain explicit:

`intent → authority → bounded context → local plan item → execution → evidence → review → closeout → successor context`

## Long-term memory

ROS consumes repository-local, DPA-governed context projections. It does not treat chat memory as authority and does not require loading a whole repository graph into every agent session.

## Initial non-goals

- no CLI implementation in this repository during architecture bootstrap;
- no duplication of `.agentic/` runtime state;
- no universal central task queue;
- no automatic cross-repository mutation;
- no application-specific scientific rules.