---
type: Tool Guide
title: LinkedIn Ads (Campaign Manager)
description: Defines source-aware LinkedIn Campaign Manager planning, measurement, permissions, and controlled activation, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a LinkedIn campaign change brief with explicit evidence states.
confirmation_required:
- create or launch a campaign, change budget or bid, upload audiences or conversion events, install tracking, publish creative, or generate and use access tokens
okb_bundle_id: linkedin-campaign-manager
timestamp: '2026-07-31T00:00:00Z'
---
# LinkedIn Ads (Campaign Manager)

Source-aware tool bundle for LinkedIn Campaign Manager planning, measurement, permissions, and controlled activation, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://learn.microsoft.com/en-us/linkedin/marketing/overview?view=li-lms-2026-03
- https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access?view=li-lms-2026-06
- https://learn.microsoft.com/en-us/linkedin/marketing/conversions/getting-access-conversions?view=li-lms-2026-04

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- ad account, authenticated member, role, API or UI version, and permissions
- objective, campaign group, campaign, creative, audience, exclusions, geography, schedule, budget, bid, billing, conversion rules, Insight Tag or Conversions API setup, identifiers, consent, deduplication, attribution, reporting definitions, tests, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer delivery, audience size, conversion count, attribution, performance, spend, policy compliance, or forecast.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create or launch a campaign, change budget or bid, upload audiences or conversion events, install tracking, publish creative, or generate and use access tokens.
