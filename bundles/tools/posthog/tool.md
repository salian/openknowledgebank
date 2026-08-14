---
type: "Tool Guide"
title: "PostHog"
description: "Source-aware guidance for PostHog."
resource: "https://posthog.com/docs"
okb_bundle_id: posthog
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Product analytics, replay, experimentation, flags, data, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "install capture, identify users, record sessions, change masking, flags or experiment allocation, send surveys, connect destinations, run queries, enable AI, expose keys, or represent behavior, significance, causality, security, or revenue"
---
# PostHog Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://posthog.com/docs
- https://posthog.com/products

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable PostHog instrumentation and product-decision review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before install capture, identify users, record sessions, change masking, flags or experiment allocation, send surveys, connect destinations, run queries, enable AI, expose keys, or represent behavior, significance, causality, security, or revenue.

## Guardrails

- Do not invent person identity, consent, captured content, event completeness, cohort or flag assignment, experiment validity, significance, causality, AI output, query result, cost, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
