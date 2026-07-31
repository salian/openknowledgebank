---
type: Tool Guide
title: "Slack"
description: "Defines source-aware team communication and collaboration, evidence handling, and action boundaries."
tool_category: "Team communication and collaboration platforms"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review team communication and collaboration from supplied evidence."
  - "Draft a slack communication and governance brief with explicit evidence states."
confirmation_required:
  - "sending or editing messages, inviting users, changing channels, permissions, retention, apps, workflows, tokens, or exports"
okb_bundle_id: slack
timestamp: "2026-07-31T00:00:00Z"
---

# Slack

Source-aware tool bundle for Slack workspace, channel, message, app, permission, retention, workflow, and controlled communication briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- workspace, organization, channel, and thread scope
- message content, timestamp, author, and edit state
- membership, roles, and permissions
- apps, scopes, tokens, workflows, and integrations
- retention, legal hold, export, and administrator policy
- notification and communication approvals
- audit and source-of-record evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before sending or editing messages, inviting users, changing channels, permissions, retention, apps, workflows, tokens, or exports.
