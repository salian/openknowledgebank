---
type: Tool Guide
title: "Google Ads"
description: "Defines source-aware paid advertising planning and performance review, evidence handling, and action boundaries."
tool_category: "Paid search/social advertising platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review paid advertising planning and performance review from supplied evidence."
  - "Draft a google ads decision and change brief with explicit evidence states."
confirmation_required:
  - "publishing ads, changing targeting, budgets, bids, conversion actions, experiments, billing, or account access"
okb_bundle_id: google-ads
timestamp: "2026-07-31T00:00:00Z"
---

# Google Ads

Source-aware tool bundle for Google Ads campaign planning, conversion and attribution review, budget and bidding analysis, reporting reconciliation, and controlled change briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- account and campaign scope
- objectives and conversion-action definitions
- targeting, keywords, audiences, and exclusions
- ads, assets, landing pages, and approvals
- budgets and bidding settings
- date, attribution, currency, and reporting settings
- change history and experiment evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before publishing ads, changing targeting, budgets, bids, conversion actions, experiments, billing, or account access.
