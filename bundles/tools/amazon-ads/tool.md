---
type: "Tool Guide"
title: "Amazon Ads"
description: "Source-aware guidance for Amazon Ads."
resource: "https://advertising.amazon.com/about-api"
okb_bundle_id: amazon-ads
timestamp: "2026-08-12T00:00:00Z"
tool_category: "Advertising platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or modify campaigns, change bids or budgets, upload audiences or creatives, use credentials, launch ads, or represent performance as validated"
---
# Amazon Ads Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://advertising.amazon.com/about-api

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Amazon Ads configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or modify campaigns, change bids or budgets, upload audiences or creatives, use credentials, launch ads, or represent performance as validated.

## Guardrails

- Do not invent account state, audience, targeting, budget, bid, creative approval, delivery, attribution, spend, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
