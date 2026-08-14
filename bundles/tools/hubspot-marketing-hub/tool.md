---
type: "Tool Guide"
title: "HubSpot Marketing Hub"
description: "Source-aware guidance for HubSpot Marketing Hub."
resource: "https://www.hubspot.com/products/marketing"
okb_bundle_id: hubspot-marketing-hub
timestamp: "2026-08-13T00:00:00Z"
tool_category: "CRM-connected marketing automation, campaign, and attribution platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "collect contact data, enroll contacts, send email or social content, personalize pages, change consent or subscriptions, activate workflows or campaigns, spend funds, export data, or represent attribution or revenue"
---
# HubSpot Marketing Hub Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.hubspot.com/products/marketing

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current HubSpot product and knowledge documentation for the portal, subscription, and region.
- Account, contact, property, consent, subscription, segment, form, email, workflow, campaign, channel, integration, permission, attribution model, and report state.
- Privacy and marketing-law review, test audience, budget, measurement plan, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable HubSpot Marketing Hub campaign and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before collect contact data, enroll contacts, send email or social content, personalize pages, change consent or subscriptions, activate workflows or campaigns, spend funds, export data, or represent attribution or revenue.

## Guardrails

- Do not invent contact identity, consent, subscription, segment membership, personalization accuracy, send or delivery, campaign state, attribution, revenue, conversion, legal compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
