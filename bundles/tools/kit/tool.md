---
type: "Tool Guide"
title: "Kit"
description: "Source-aware guidance for Kit."
resource: "https://developers.kit.com/"
okb_bundle_id: kit
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Creator email marketing, automation, commerce, and developer platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or identify subscribers, change tags or consent, send broadcasts, enroll sequences, activate automations, sell products, grant OAuth access, deploy apps or MCP actions, or represent delivery or revenue"
---
# Kit Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developers.kit.com/
- https://help.kit.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Kit email, automation, and developer integration review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or identify subscribers, change tags or consent, send broadcasts, enroll sequences, activate automations, sell products, grant OAuth access, deploy apps or MCP actions, or represent delivery or revenue.

## Guardrails

- Do not invent subscriber identity, consent, tag or segment membership, send or delivery, automation execution, purchase, payment, OAuth scope, app behavior, revenue, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
