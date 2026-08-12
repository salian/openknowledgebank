---
type: "Tool Guide"
title: "Amazon Bedrock"
description: "Source-aware guidance for Amazon Bedrock."
resource: "https://aws.amazon.com/bedrock/"
okb_bundle_id: amazon-bedrock
timestamp: "2026-08-12T00:00:00Z"
tool_category: "Managed generative AI platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "enable models, transmit data, create agents or knowledge bases, change IAM or guardrails, deploy inference, incur spend, or represent safety or quality approval"
---
# Amazon Bedrock Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://aws.amazon.com/bedrock/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Amazon Bedrock configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before enable models, transmit data, create agents or knowledge bases, change IAM or guardrails, deploy inference, incur spend, or represent safety or quality approval.

## Guardrails

- Do not invent region or model availability, data handling, permission, configuration, evaluation result, safety, cost, deployment state, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
