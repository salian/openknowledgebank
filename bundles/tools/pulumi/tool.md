---
type: "Tool Guide"
title: "Pulumi"
description: "Source-aware guidance for Pulumi."
resource: "https://www.pulumi.com/docs/"
okb_bundle_id: pulumi
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Infrastructure as code, secrets, policy, deployment, and cloud-operations platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "read or modify state, preview or deploy infrastructure, import or destroy resources, expose secrets, change environments or policies, run automation, enable cloud deployments or AI, or represent infrastructure, drift, security, cost, or availability"
---
# Pulumi Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.pulumi.com/docs/
- https://www.pulumi.com/product/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Pulumi infrastructure, environment, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before read or modify state, preview or deploy infrastructure, import or destroy resources, expose secrets, change environments or policies, run automation, enable cloud deployments or AI, or represent infrastructure, drift, security, cost, or availability.

## Guardrails

- Do not invent provider or package compatibility, resource identity, state completeness, secret scope, preview safety, deployment result, drift, policy enforcement, cost, rollback, service availability, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
