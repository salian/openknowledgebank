---
type: Slash Command
command: /draft-technical-prd
title: Draft Technical PRD
description: Drafts or reviews a technical PRD from provided product and engineering evidence.
okb_bundle_id: technical-product-manager
inputs: [problem, users, goals, source evidence, constraints, decision owner]
outputs: [technical PRD, source note, assumptions, missing verification, owner questions]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /draft-technical-prd

This command spec is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, safety, permission, and tool-use rules.

## Purpose

Create a source-aware technical PRD using the [Write Technical PRD](../workflows/write-technical-prd.md) workflow and [Technical PRD](../deliverables/technical-prd.md) output contract.

## Required Output

- Direct readiness or recommendation.
- Source note.
- Verified source facts, user-provided evidence, assumptions, and missing verification.
- Problem, users, goal, scope, non-goals, requirements, acceptance criteria, dependencies, risks, metrics, rollout, and owner questions.

## Safety

The command should not modify live docs, tickets, repos, API specs, flags, analytics definitions, release notes, or communications. Any such action requires explicit user confirmation at consumption time.
