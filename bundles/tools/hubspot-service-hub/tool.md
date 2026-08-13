---
type: "Tool Guide"
title: "HubSpot Service Hub"
description: "Source-aware guidance for HubSpot Service Hub."
resource: "https://www.hubspot.com/products/service"
okb_bundle_id: hubspot-service-hub
timestamp: "2026-08-13T00:00:00Z"
tool_category: "CRM-connected help desk, knowledge, customer success, and AI service platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "reply to customers, change tickets or CRM records, publish knowledge, expose a portal, deploy AI, alter routing or SLAs, grant access, export data, or represent resolution, satisfaction, or retention"
---
# HubSpot Service Hub Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.hubspot.com/products/service

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current HubSpot product and knowledge documentation for the portal, subscription, and region.
- Account, customer, contact, company, ticket, entitlement, channel, routing, SLA, knowledge, portal, AI source, workflow, integration, permission, and report state.
- Customer privacy, response and action authority, tests, monitoring, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable HubSpot Service Hub support and retention review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before reply to customers, change tickets or CRM records, publish knowledge, expose a portal, deploy AI, alter routing or SLAs, grant access, export data, or represent resolution, satisfaction, or retention.

## Guardrails

- Do not invent customer identity, ticket ownership or state, entitlement, SLA, response accuracy, knowledge validity, AI output or action, resolution, satisfaction, retention, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
