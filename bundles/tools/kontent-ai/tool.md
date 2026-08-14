---
type: "Tool Guide"
title: "Kontent.ai"
description: "Source-aware guidance for Kontent.ai."
resource: "https://kontent.ai/features/"
okb_bundle_id: kontent-ai
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Headless and agentic content management, governance, and delivery platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "change content models, create or alter content, move workflow state, publish or unpublish, grant API keys, run migrations, deploy agents or MCP actions, or represent compliance or delivery"
---
# Kontent.ai Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://kontent.ai/features/
- https://kontent.ai/learn/docs/apis

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Kontent.ai content architecture and agent governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before change content models, create or alter content, move workflow state, publish or unpublish, grant API keys, run migrations, deploy agents or MCP actions, or represent compliance or delivery.

## Guardrails

- Do not invent content rights, model or item state, translation, workflow approval, publication, API-key scope, agent action, AI accuracy, governance certification applicability, delivery, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
