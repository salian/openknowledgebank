---
type: Tool Guide
title: TikTok Ads Manager
description: Defines source-aware TikTok Ads Manager campaign, creative, audience, measurement, and spend review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a TikTok campaign change brief with explicit evidence states.
confirmation_required:
- create or launch ads, change budget or bid, upload audiences or events, install tracking code, publish creative, or incur spend
okb_bundle_id: tiktok-ads-manager
timestamp: '2026-07-31T00:00:00Z'
---
# TikTok Ads Manager

Source-aware tool bundle for TikTok Ads Manager campaign, creative, audience, measurement, and spend review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://ads.tiktok.com/business/en/solutions/ads-manager
- https://ads.tiktok.com/help/article/advertising-on-tiktok-ads-manager?lang=en
- https://ads.tiktok.com/help/article/tiktok-pixel?lang=en-GB

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- business and ad account, user role, permissions, market, policy, and interface version
- objective, campaign, ad group, ad, creative, audience, exclusions, placement, schedule, budget, bid, billing, Pixel or Events API, events, consent, deduplication, attribution, reporting definitions, tests, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer delivery, event receipt, audience eligibility, conversion count, attribution, performance, spend, policy compliance, or forecast.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create or launch ads, change budget or bid, upload audiences or events, install tracking code, publish creative, or incur spend.
