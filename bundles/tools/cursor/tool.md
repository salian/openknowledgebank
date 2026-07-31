---
type: Tool Guide
title: Cursor
description: Defines source-aware editor, codebase context, rules, model, agent, terminal, background task, MCP, privacy, and change review, evidence handling, and action boundaries.
resource: https://docs.cursor.com/
okb_bundle_id: cursor
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a cursor review brief with explicit evidence states.
confirmation_required:
- apply code edits, run terminal commands or tests, start background agents, connect MCP servers, send repository data, expose credentials, commit or push code, or deploy changes
---
# Cursor Source-Aware Tool Guide

Source-aware tool bundle for editor, codebase context, rules, model, agent, terminal, background task, MCP, privacy, and change review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://docs.cursor.com/
- https://cursor.com/security

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- Cursor version and plan, repository and branch, workspace trust, indexed scope, project and user rules, selected model, agent mode, terminal and MCP permissions, privacy settings, diffs, tests, logs, approvals, and rollback

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory evidence and label it as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, identifiers, versions, periods, scope, permissions, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer indexed context, rule precedence, model behavior, edit correctness, command result, data handling, MCP permission, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that apply code edits, run terminal commands or tests, start background agents, connect MCP servers, send repository data, expose credentials, commit or push code, or deploy changes.
