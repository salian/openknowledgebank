---
type: "Tool Guide"
title: "Zoom Team Chat"
description: "Source-aware guidance for Zoom Team Chat."
resource: "https://www.zoom.com/en/products/team-chat/"
okb_bundle_id: zoom-team-chat
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Team messaging, channel, file, collaboration, administration, integration, API, and governance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create channels, invite or identify people, send or delete messages, share files, install apps or bots, call APIs, change retention, or represent delivery, identity, consent, confidentiality, retention, or compliance"
---
# Zoom Team Chat Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.zoom.com/en/products/team-chat/
- https://developers.zoom.us/docs/api/team-chat/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product and developer documentation for the applicable plan, region, and date.
- Inspected account, channel, message, permission, integration, retention, and audit evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Zoom Team Chat communication, integration, and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create channels, invite or identify people, send or delete messages, share files, install apps or bots, call APIs, change retention, or represent delivery, identity, consent, confidentiality, retention, or compliance.

## Guardrails

- Do not invent plan or feature availability, user identity or consent, channel membership, message or file state, delivery, app or API result, confidentiality, retention, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
