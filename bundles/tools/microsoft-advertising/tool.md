---
type: "Tool Guide"
title: "Microsoft Advertising"
description: "Source-aware guidance for Microsoft Advertising."
resource: "https://learn.microsoft.com/en-us/advertising/"
okb_bundle_id: microsoft-advertising
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Digital advertising, campaign, audience, measurement, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or change campaigns, ads, audiences, tracking tags, bids or budgets, upload customer or product data, authorize APIs, spend funds, or represent delivery, conversion, attribution, compliance, or return"
---
# Microsoft Advertising Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://learn.microsoft.com/en-us/advertising/
- https://about.ads.microsoft.com/en/solutions

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Microsoft Advertising campaign and measurement review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or change campaigns, ads, audiences, tracking tags, bids or budgets, upload customer or product data, authorize APIs, spend funds, or represent delivery, conversion, attribution, compliance, or return.

## Guardrails

- Do not invent account identity, audience membership, consent, policy eligibility, ad approval, budget, bid, delivery, conversion, attribution, revenue, return on ad spend, API execution, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
