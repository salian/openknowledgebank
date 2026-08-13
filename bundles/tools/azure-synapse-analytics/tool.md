---
type: "Tool Guide"
title: "Azure Synapse Analytics"
description: "Source-aware guidance for Azure Synapse Analytics."
resource: "https://azure.microsoft.com/en-us/products/synapse-analytics/"
okb_bundle_id: azure-synapse-analytics
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Cloud analytics service"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "provision or resize resources, connect data sources, execute queries or pipelines, change networking or access, expose secrets or data, delete resources, or represent analytics as validated"
---
# Azure Synapse Analytics Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://azure.microsoft.com/en-us/products/synapse-analytics/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Azure Synapse Analytics configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before provision or resize resources, connect data sources, execute queries or pipelines, change networking or access, expose secrets or data, delete resources, or represent analytics as validated.

## Guardrails

- Do not invent tenant or workspace state, data contents or quality, query or pipeline safety, permissions, cost, execution result, security posture, recovery, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
