---
type: "Tool Guide"
title: "Google Ads Keyword Planner"
description: "Source-aware guidance for Google Ads Keyword Planner."
resource: "https://business.google.com/en-all/ad-tools/keyword-planner/"
okb_bundle_id: google-keyword-planner
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Paid-search keyword research, historical data, and forecasting tool"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or change campaigns, set bids or budgets, target sensitive audiences, publish forecasts as commitments, spend funds, or represent traffic, conversion, cost, or return"
---
# Google Ads Keyword Planner Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://business.google.com/en-all/ad-tools/keyword-planner/
- https://support.google.com/google-ads/answer/7337243

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Google Ads Keyword Planner help for the account, market, and date.
- Account access, billing eligibility, seed, match assumptions, location, language, network, date range, export, and forecast inputs.
- Sensitive-category policy, budget owner, measurement plan, validation, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Google Ads keyword research and forecast review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or change campaigns, set bids or budgets, target sensitive audiences, publish forecasts as commitments, spend funds, or represent traffic, conversion, cost, or return.

## Guardrails

- Do not invent keyword completeness, exact demand, future volume, bid or cost, ranking, traffic, conversion, campaign state, profitability, policy eligibility, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
