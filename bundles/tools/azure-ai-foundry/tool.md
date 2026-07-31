---
type: Tool Guide
title: Azure AI Foundry
description: Defines source-aware project, model catalog, deployment, prompt, agent, evaluation, content filter, quota, identity, network, and monitoring review, evidence handling, and action boundaries.
resource: https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry
okb_bundle_id: azure-ai-foundry
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a azure ai foundry review brief with explicit evidence states.
confirmation_required:
- deploy or invoke models or agents, enable tools, change content filters, quotas, identities, networks, endpoints, or data connections; send sensitive data; expose credentials; or incur spend
---
# Azure AI Foundry Source-Aware Tool Guide

Source-aware tool bundle for project, model catalog, deployment, prompt, agent, evaluation, content filter, quota, identity, network, and monitoring review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry
- https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/general-purpose-evaluators
- https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- Azure tenant, subscription, region, Foundry project, model and version, deployment type, quota, endpoint and authentication method, prompts, tools and data connections, evaluation dataset and metrics, content filters, networking, logging, costs, approvals, and rollback

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory evidence and label it as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, identifiers, versions, periods, scope, permissions, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer model availability, output quality, safety, quota, cost, data handling, deployment state, evaluation result, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that deploy or invoke models or agents, enable tools, change content filters, quotas, identities, networks, endpoints, or data connections; send sensitive data; expose credentials; or incur spend.
