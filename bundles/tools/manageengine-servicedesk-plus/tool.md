---
type: "Tool Guide"
title: "ManageEngine ServiceDesk Plus"
description: "Source-aware guidance for ManageEngine ServiceDesk Plus."
resource: "https://www.manageengine.com/products/service-desk/"
okb_bundle_id: manageengine-servicedesk-plus
timestamp: "2026-08-14T00:00:00Z"
tool_category: "IT service management, asset, CMDB, workflow, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter tickets, assets, contracts, changes or releases, run scripts, change workflows or permissions, expose OAuth credentials, call production APIs, or represent SLA, change, asset, or service state"
---
# ManageEngine ServiceDesk Plus Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.manageengine.com/products/service-desk/
- https://www.manageengine.com/products/service-desk/sdpod-v3-api/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable ServiceDesk Plus ITSM configuration and change review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter tickets, assets, contracts, changes or releases, run scripts, change workflows or permissions, expose OAuth credentials, call production APIs, or represent SLA, change, asset, or service state.

## Guardrails

- Do not invent edition, module availability, request or asset identity, SLA calculation, approval, change risk, deployment result, script safety, API execution, service restoration, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
