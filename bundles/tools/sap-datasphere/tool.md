---
type: "Tool Guide"
title: "SAP Datasphere"
description: "Source-aware guidance for SAP Datasphere."
resource: "https://help.sap.com/docs/SAP_DATASPHERE"
okb_bundle_id: sap-datasphere
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise data integration, warehouse, semantic, catalog, and governance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect production sources, replicate or transform data, change models or semantic definitions, share data products, grant roles, expose credentials, deploy content, consume capacity, or represent schema, lineage, security, quality, freshness, or business results"
---
# SAP Datasphere Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.sap.com/docs/SAP_DATASPHERE
- https://www.sap.com/products/data-cloud/datasphere.html

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SAP Datasphere architecture and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect production sources, replicate or transform data, change models or semantic definitions, share data products, grant roles, expose credentials, deploy content, consume capacity, or represent schema, lineage, security, quality, freshness, or business results.

## Guardrails

- Do not invent tenant or feature applicability, source schema, replication completeness, model or metric definition, lineage, data quality, freshness, row-level access, deployment, capacity, cost, query result, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
