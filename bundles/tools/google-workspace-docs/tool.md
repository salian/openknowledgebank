---
type: Tool Guide
title: "Google Docs / Google Workspace"
description: "Defines source-aware collaborative document creation and review, evidence handling, and action boundaries."
tool_category: "Document collaboration"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review collaborative document creation and review from supplied evidence."
  - "Draft a google workspace document brief with explicit evidence states."
confirmation_required:
  - "editing documents, accepting suggestions, resolving comments, sharing, changing ownership, exporting, sending, or publishing"
okb_bundle_id: google-workspace-docs
timestamp: "2026-07-31T00:00:00Z"
---

# Google Docs / Google Workspace

Source-aware tool bundle for Google Docs and Workspace document collaboration, review, sharing, version, automation, and governance evidence.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- document identity, owner, and version
- content, comments, suggestions, and approvals
- sharing, access, and link settings
- workspace and administrator policy
- templates, add-ons, scripts, and integrations
- retention, classification, and export requirements
- source-of-record and publication destination

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before editing documents, accepting suggestions, resolving comments, sharing, changing ownership, exporting, sending, or publishing.
