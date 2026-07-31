---
type: Tool Guide
title: "Google Workspace"
description: "Defines source-aware collaboration suite administration and content, evidence handling, and action boundaries."
tool_category: "collaboration suite administration and content"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review collaboration suite administration and content from supplied evidence."
  - "Draft a google workspace administration and sharing brief with explicit evidence states."
confirmation_required:
  - "sending messages, editing or sharing content, changing users or groups, changing admin or security settings, changing retention, or exporting data"
okb_bundle_id: google-workspace
timestamp: "2026-07-31T00:00:00Z"
---

# Google Workspace

Source-aware tool bundle for Google Workspace users, groups, organizational units, files, mail, calendars, sharing, security, audit, and controlled administration.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- tenant, edition, and enabled services
- users, groups, and organizational units
- documents, files, sites, mail, and calendars
- sharing and access settings
- admin, security, retention, and audit configuration
- export and approval evidence

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
- Do not infer file contents, sharing reach, user membership, mail delivery, retention behavior, and administrator access.
- Require accountable confirmation before sending messages, editing or sharing content, changing users or groups, changing admin or security settings, changing retention, or exporting data.
