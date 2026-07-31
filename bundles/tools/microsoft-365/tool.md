---
type: Tool Guide
title: "Microsoft 365"
description: "Defines source-aware office productivity and collaboration, evidence handling, and action boundaries."
tool_category: "General office productivity, document creation/editing, and e-signature software"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review office productivity and collaboration from supplied evidence."
  - "Draft a microsoft 365 work and governance brief with explicit evidence states."
confirmation_required:
  - "sending messages, sharing files, changing content, permissions, retention, labels, tenant settings, or automations"
okb_bundle_id: microsoft-365
timestamp: "2026-07-31T00:00:00Z"
---

# Microsoft 365

Source-aware tool bundle for Microsoft 365 documents, collaboration, sharing, tenant controls, retention, automation, and review-ready work briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- tenant, subscription, and application scope
- file, site, mailbox, team, or workspace identity
- document version and content evidence
- sharing, membership, and permission state
- retention, sensitivity, compliance, and administrator policy
- automation and integration configuration
- audit, approval, and source-of-record evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before sending messages, sharing files, changing content, permissions, retention, labels, tenant settings, or automations.
