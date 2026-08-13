---
type: "Tool Guide"
title: "Campaign Monitor"
description: "Source-aware guidance for Campaign Monitor."
resource: "https://www.campaignmonitor.com/api/"
okb_bundle_id: campaign-monitor
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Email marketing platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or update subscribers, change consent or suppression, authenticate senders, create, schedule or send campaigns, activate journeys, use credentials, or represent delivery or conversion"
---
# Campaign Monitor Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.campaignmonitor.com/api/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Campaign Monitor configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or update subscribers, change consent or suppression, authenticate senders, create, schedule or send campaigns, activate journeys, use credentials, or represent delivery or conversion.

## Guardrails

- Do not invent subscriber identity, consent, subscription or suppression, sender authority, content approval, delivery, engagement, conversion, attribution, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
