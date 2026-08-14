---
type: "Tool Guide"
title: "Salesforce Marketing Cloud Engagement"
description: "Source-aware guidance for Salesforce Marketing Cloud Engagement."
resource: "https://www.salesforce.com/marketing/engagement/"
okb_bundle_id: salesforce-marketing-cloud-engagement
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise cross-channel messaging, journey, automation, data, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "ingest or identify customer data, change consent or suppression, send messages, activate journeys or automations, connect Data Cloud or CRM, expose package credentials, call APIs, spend funds, or represent delivery, attribution, conversion, or revenue"
---
# Salesforce Marketing Cloud Engagement Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.salesforce.com/marketing/engagement/
- https://developer.salesforce.com/docs/marketing/marketing-cloud/overview

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Marketing Cloud Engagement journey and data review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before ingest or identify customer data, change consent or suppression, send messages, activate journeys or automations, connect Data Cloud or CRM, expose package credentials, call APIs, spend funds, or represent delivery, attribution, conversion, or revenue.

## Guardrails

- Do not invent subscriber identity, consent, contact-key mapping, data extension state, suppression, send or delivery, journey execution, automation, API result, attribution, conversion, revenue, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
