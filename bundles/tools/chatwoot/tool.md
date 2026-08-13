---
type: "Tool Guide"
title: "Chatwoot"
description: "Source-aware guidance for Chatwoot."
resource: "https://www.chatwoot.com/"
okb_bundle_id: chatwoot
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Customer support and omnichannel helpdesk platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect channels, import contacts, send or automate messages, expose conversation history, publish help content, enable AI responses, change permissions, deploy upgrades, or represent resolution"
---
# Chatwoot Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.chatwoot.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Chatwoot configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect channels, import contacts, send or automate messages, expose conversation history, publish help content, enable AI responses, change permissions, deploy upgrades, or represent resolution.

## Guardrails

- Do not invent contact identity, consent, conversation context, message delivery, AI answer accuracy, ticket ownership or resolution, hosting security, backup or upgrade result, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
