---
type: Workflow
title: Review Power BI Publishing and Permissions
description: "Checklist workflow for source-aware Power BI publishing, sharing, export, embedding, and permission risk review."
okb_bundle_id: microsoft-power-bi
timestamp: "2026-07-09T00:00:00Z"
---

# Review Power BI Publishing and Permissions

Use this workflow before recommending Power BI publishing, app audience changes, sharing changes, exports, embedding, refresh actions, subscriptions, alerts, gateway/credential changes, or API automation.

## Evidence to Request

- Workspace, app, report, dashboard, semantic model, dataflow, owner, environment, and deployment evidence.
- Workspace roles, item permissions, group/user membership, app audiences, sharing links, export/download settings, embed settings, subscriptions, alerts, and tenant/admin setting evidence.
- RLS/OLS roles, filters, test-as results, security group mappings, and workspace role context.
- Refresh schedule, refresh history, gateway, credential, lineage, source system, data classification, and owner approval evidence.
- Current Microsoft Learn source check for exact REST API scopes, endpoints, payloads, admin settings, service principal behavior, capacity/licensing prerequisites, or release-specific behavior.

## Review Checks

1. Confirm what action is being proposed and whether it changes live content, access, data movement, refresh behavior, credentials, or user-facing communication.
2. Verify that the requester has authority from the workspace/content owner and data owner.
3. Compare intended audience with workspace roles, item permissions, app audiences, RLS/OLS roles, export settings, sharing links, and embed settings.
4. Check whether the action could expose sensitive, confidential, regulated, customer, employee, row-level, or financial data.
5. Confirm rollback: previous version, owner, affected users, notification plan, and how to reverse the change.
6. Require explicit user confirmation before any risky action.

## Output Contract

Return a publish/permission readiness decision, source note, verified evidence, missing evidence, risk list, required approvals, rollback plan, and explicit confirmation request for any live action.
