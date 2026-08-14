---
type: "Tool Guide"
title: "Rocket.Chat"
description: "Source-aware guidance for Rocket.Chat."
resource: "https://docs.rocket.chat/"
okb_bundle_id: rocket-chat
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Team messaging, omnichannel support, apps, API, and self-managed platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "send or delete messages, expose files or credentials, initiate calls, change routing, retention or permissions, install apps, run bots, authorize APIs, federate servers, deploy upgrades, or represent delivery, confidentiality, encryption, incident, or compliance state"
---
# Rocket.Chat Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.rocket.chat/
- https://developer.rocket.chat/apidocs/rocketchat-api

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Rocket.Chat collaboration, API, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before send or delete messages, expose files or credentials, initiate calls, change routing, retention or permissions, install apps, run bots, authorize APIs, federate servers, deploy upgrades, or represent delivery, confidentiality, encryption, incident, or compliance state.

## Guardrails

- Do not invent user identity, channel membership, message or file state, confidentiality, encryption coverage, retention, legal hold, permission, app or bot safety, API result, federation, backup, uptime, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
