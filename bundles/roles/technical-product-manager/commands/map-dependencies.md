---
type: Slash Command
command: /map-dependencies
title: Map Technical Dependencies
description: Maps technical product dependencies, blockers, owners, risks, and verification gaps.
okb_bundle_id: technical-product-manager
inputs: [initiative goal, known systems, teams, services, tickets, docs, risk tolerance]
outputs: [critical path, dependency table, risks, assumptions, owner questions]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /map-dependencies

This command spec is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, safety, permission, and tool-use rules.

## Purpose

Create a source-aware dependency map using the [Map Technical Dependencies](../workflows/map-technical-dependencies.md) workflow and [Dependency Map](../deliverables/dependency-map.md) output contract.

## Required Output

- Critical path and highest-risk blocker summary.
- Source note.
- Dependency table with owner, source evidence, state, risk, decision needed, next action, and verification status.
- Assumptions and missing verification.

## Safety

The command should not create or update tickets, docs, repos, flags, roadmaps, or messages without explicit user confirmation at consumption time.
