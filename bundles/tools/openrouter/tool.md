---
type: "Tool Guide"
title: "OpenRouter"
description: "Source-aware guidance for OpenRouter."
resource: "https://openrouter.ai/docs/"
okb_bundle_id: openrouter
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Multi-provider model routing, API, and inference marketplace"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "send confidential data to model providers, expose keys, select or route providers, invoke tools, spend credits, log prompts or outputs, publish generated claims, or represent model identity, privacy, accuracy, safety, latency, or cost"
---
# OpenRouter Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://openrouter.ai/docs/
- https://openrouter.ai/models

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable OpenRouter model-routing and data-governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before send confidential data to model providers, expose keys, select or route providers, invoke tools, spend credits, log prompts or outputs, publish generated claims, or represent model identity, privacy, accuracy, safety, latency, or cost.

## Guardrails

- Do not invent model or provider availability, routing outcome, data retention, privacy policy applicability, tool execution, output accuracy, safety, token use, latency, price, charge, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
