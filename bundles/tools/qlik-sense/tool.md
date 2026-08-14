---
type: "Tool Guide"
title: "Qlik Sense"
description: "Source-aware guidance for Qlik Sense."
resource: "https://help.qlik.com/en-US/cloud-services/"
okb_bundle_id: qlik-sense
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Associative analytics, data modeling, visualization, automation, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect or reload production data, change scripts, models, metrics or section access, publish apps, schedule automation, train models, expose API keys, embed analytics, migrate deployments, or represent query, forecast, permission, security, or business results"
---
# Qlik Sense Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.qlik.com/en-US/cloud-services/
- https://qlik.dev/apis/rest/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Qlik Sense model, application, and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect or reload production data, change scripts, models, metrics or section access, publish apps, schedule automation, train models, expose API keys, embed analytics, migrate deployments, or represent query, forecast, permission, security, or business results.

## Guardrails

- Do not invent deployment or license applicability, schema, load completeness, metric definition, associative result, data freshness, section access, model accuracy, automation or API result, migration, business conclusion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
