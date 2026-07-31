---
type: Tool Guide
title: "Zapier"
description: "Defines source-aware workflow automation planning and review, evidence handling, and action boundaries."
tool_category: "Workflow automation"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review workflow automation planning and review from supplied evidence."
  - "Draft a zapier automation brief with explicit evidence states."
confirmation_required:
  - "testing with live data, turning automations on, replaying tasks, changing connections, sending messages, modifying records, or incurring usage"
okb_bundle_id: zapier
timestamp: "2026-07-31T00:00:00Z"
---

# Zapier

Source-aware tool bundle for Zapier triggers, actions, data mappings, filters, paths, connections, task history, testing, and controlled automation briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- account, plan, workspace, and ownership scope
- trigger and action app versions
- connection and permission boundaries
- field schemas, sample data, mappings, filters, paths, and delays
- test records, task history, errors, and replay evidence
- privacy, retention, rate, and usage requirements
- publish, rollback, and approval evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before testing with live data, turning automations on, replaying tasks, changing connections, sending messages, modifying records, or incurring usage.
