---
type: "Tool Guide"
title: "SuiteCRM"
description: "Source-aware guidance for SuiteCRM."
resource: "https://docs.suitecrm.com/8.x/"
okb_bundle_id: suitecrm
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source CRM, workflow, reporting, API, customization, deployment, and upgrade platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or identify people, send communications, change sales or service records, run workflows, issue OAuth credentials, call APIs, install customizations, deploy or upgrade systems, or represent consent, pipeline, forecast, case resolution, migration, security, or compliance"
---
# SuiteCRM Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.suitecrm.com/8.x/
- https://docs.suitecrm.com/developer/api/developer-setup-guide/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SuiteCRM 8 operations, API, and upgrade governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or identify people, send communications, change sales or service records, run workflows, issue OAuth credentials, call APIs, install customizations, deploy or upgrade systems, or represent consent, pipeline, forecast, case resolution, migration, security, or compliance.

## Guardrails

- Do not invent version or API applicability, person identity or consent, record state, workflow execution, credential safety, API result, customization behavior, migration, backup or restore, security, pipeline, resolution, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
