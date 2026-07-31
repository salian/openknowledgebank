---
type: Tool Guide
title: "Intercom"
description: "Defines source-aware customer messaging and support operations, evidence handling, and action boundaries."
tool_category: "customer messaging and support operations"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review customer messaging and support operations from supplied evidence."
  - "Draft a intercom support and reporting brief with explicit evidence states."
confirmation_required:
  - "sending or replying, changing routing or workflows, publishing help content, exporting personal data, or changing permissions"
okb_bundle_id: intercom
timestamp: "2026-07-31T00:00:00Z"
---

# Intercom

Source-aware tool bundle for Intercom inboxes, conversations, tickets, workflows, help content, customer data, reports, and controlled communications.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- workspace and plan
- inboxes, teams, routes, conversations, tickets, and tags
- people and company data
- workflows, bots, and automation
- report definitions, filters, and periods
- roles, permissions, exports, and privacy requirements

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer conversation state, routing behavior, customer identity, report meaning, automation outcome, and access rights.
- Require accountable confirmation before sending or replying, changing routing or workflows, publishing help content, exporting personal data, or changing permissions.
