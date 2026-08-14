---
type: "Tool Guide"
title: "Optimizely Feature Experimentation"
description: "Source-aware guidance for Optimizely Feature Experimentation."
resource: "https://docs.developers.optimizely.com/feature-experimentation/docs"
okb_bundle_id: optimizely
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Feature flagging, rollout, experimentation, and measurement platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "instrument events, identify users, change flags or allocation, launch or stop experiments, deploy SDKs, expose keys, export data, make product decisions, or represent assignment, metric, significance, causality, or business impact"
---
# Optimizely Feature Experimentation Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.developers.optimizely.com/feature-experimentation/docs
- https://www.optimizely.com/products/feature-experimentation/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Optimizely feature flag and experiment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before instrument events, identify users, change flags or allocation, launch or stop experiments, deploy SDKs, expose keys, export data, make product decisions, or represent assignment, metric, significance, causality, or business impact.

## Guardrails

- Do not invent product applicability, user identity, audience or variation assignment, event accuracy, sample ratio, metric definition, statistical validity, significance, causality, rollout state, revenue effect, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
