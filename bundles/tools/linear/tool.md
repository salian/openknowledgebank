---
type: Tool Guide
title: Linear Tool Guide
description: Tool bundle for source-aware Linear planning, issue triage, project/cycle review, GraphQL API evidence handling, and safe workflow recommendations.
okb_bundle_id: linear
resource:
  url: "https://linear.app/developers"
  label: Linear Developers
timestamp: "2026-07-09T00:00:00Z"
---

# Linear Tool Guide

Use this tool guide when the user asks for Linear help and the answer depends on source facts, local evidence, or a decision that may affect real work.

## Grounded Source Classes

- Linear provides developer documentation for apps, integrations, GraphQL API, authentication, and SDK use.
- Linear workspace objects and workflow behavior depend on local teams, projects, cycles, statuses, labels, automations, and permissions.

## Local Evidence Needed

Ask for or inspect: ['workspace, team, issue, project, cycle, label, status, priority, assignee, estimate, dependency, automation, Git integration, and API permission evidence'].

## Core Moves

1. State the user's decision or artifact request.
2. Separate official source facts from user-provided local evidence.
3. Identify assumptions and missing verification before recommendations.
4. Define terms, scope, time horizon, owner, and decision status.
5. Recommend the smallest useful next step.
6. Require explicit confirmation before creating, editing, assigning, closing, deleting, importing, exporting, or automating Linear issues, projects, cycles, teams, comments, integrations, webhooks, or API actions.

## Output Contract

Every answer should distinguish verified source facts, user-provided evidence, assumptions for the current draft, missing evidence, risks, and confirmation boundaries.
