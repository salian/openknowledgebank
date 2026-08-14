---
type: "Tool Guide"
title: "Google Chat"
description: "Source-aware guidance for Google Chat."
resource: "https://workspace.google.com/products/chat/"
okb_bundle_id: google-chat
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Enterprise messaging, spaces, collaboration, and app platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "send or delete messages, create spaces, add external members, share files, assign tasks, install apps, grant scopes, migrate content, change retention, or represent delivery"
---
# Google Chat Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://workspace.google.com/products/chat/
- https://developers.google.com/workspace/chat

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Google Workspace and Chat developer documentation for the tenant and edition.
- Tenant, space, member, external access, app, OAuth scope, retention, DLP, integration, and audit-log state.
- Message authority, privacy and security review, test, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Google Chat collaboration and administration review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before send or delete messages, create spaces, add external members, share files, assign tasks, install apps, grant scopes, migrate content, change retention, or represent delivery.

## Guardrails

- Do not invent identity, membership, message content, delivery, task state, file access, app behavior, OAuth authorization, retention, migration completeness, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
