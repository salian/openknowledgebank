---
type: "Tool Guide"
title: "Sierra"
description: "Source-aware guidance for Sierra."
resource: "https://sierra.ai/"
okb_bundle_id: sierra
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Customer-facing AI agent, action, integration, testing, and governance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "deploy customer-facing agents, connect systems, access or change customer records, issue refunds or credits, make commitments, send messages, expose credentials, alter guardrails, or represent identity, policy, resolution, transaction, compliance, or business outcomes"
---
# Sierra Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://sierra.ai/
- https://docs.sierra.ai/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Sierra customer-agent deployment and governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before deploy customer-facing agents, connect systems, access or change customer records, issue refunds or credits, make commitments, send messages, expose credentials, alter guardrails, or represent identity, policy, resolution, transaction, compliance, or business outcomes.

## Guardrails

- Do not invent customer identity, authorization, knowledge freshness, policy applicability, agent action, integration result, escalation, refund or credit, commitment, response accuracy, safety, compliance, resolution, revenue, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
