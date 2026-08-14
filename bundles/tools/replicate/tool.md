---
type: "Tool Guide"
title: "Replicate"
description: "Source-aware guidance for Replicate."
resource: "https://replicate.com/docs"
okb_bundle_id: replicate
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Hosted model, prediction, training, deployment, and inference API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "upload confidential or protected data, run public or private models, train or deploy models, expose tokens, activate webhooks, spend compute funds, publish outputs, or represent model identity, privacy, accuracy, safety, performance, or cost"
---
# Replicate Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://replicate.com/docs
- https://replicate.com/docs/reference/http

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Replicate model, prediction, and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before upload confidential or protected data, run public or private models, train or deploy models, expose tokens, activate webhooks, spend compute funds, publish outputs, or represent model identity, privacy, accuracy, safety, performance, or cost.

## Guardrails

- Do not invent model or version availability, provenance, input schema, data retention, output accuracy, safety, prediction or deployment state, webhook delivery, hardware, latency, token use, price, charge, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
