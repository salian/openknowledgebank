---
type: "Tool Guide"
title: "Pendo"
description: "Source-aware guidance for Pendo."
resource: "https://support.pendo.io/"
okb_bundle_id: pendo
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Product analytics, in-app guidance, feedback, replay, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "install tracking, identify visitors or accounts, record sessions, change masking or consent, publish guides or polls, collect feedback, enable AI, export data, or represent user intent, adoption, causality, satisfaction, or business impact"
---
# Pendo Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://support.pendo.io/
- https://www.pendo.io/product/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Pendo instrumentation and product-evidence review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before install tracking, identify visitors or accounts, record sessions, change masking or consent, publish guides or polls, collect feedback, enable AI, export data, or represent user intent, adoption, causality, satisfaction, or business impact.

## Guardrails

- Do not invent visitor identity, consent, captured content, tag accuracy, event completeness, segment membership, guide delivery, feedback representativeness, NPS, AI output, causality, adoption, revenue effect, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
