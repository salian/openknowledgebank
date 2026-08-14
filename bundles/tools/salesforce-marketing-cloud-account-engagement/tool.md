---
type: "Tool Guide"
title: "Salesforce Marketing Cloud Account Engagement"
description: "Source-aware guidance for Salesforce Marketing Cloud Account Engagement."
resource: "https://developer.salesforce.com/docs/marketing/pardot/overview"
okb_bundle_id: salesforce-marketing-cloud-account-engagement
timestamp: "2026-08-14T00:00:00Z"
tool_category: "B2B marketing automation, lead scoring, CRM synchronization, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or identify prospects, change consent, scores or grades, activate programs, send email, deploy tracking, synchronize CRM, call APIs, spend funds, or represent delivery, qualification, attribution, pipeline, or revenue"
---
# Salesforce Marketing Cloud Account Engagement Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developer.salesforce.com/docs/marketing/pardot/overview
- https://help.salesforce.com/s/articleView?id=mktg.pardot_basics.htm

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Account Engagement campaign and CRM-sync review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or identify prospects, change consent, scores or grades, activate programs, send email, deploy tracking, synchronize CRM, call APIs, spend funds, or represent delivery, qualification, attribution, pipeline, or revenue.

## Guardrails

- Do not invent prospect identity, consent, list membership, score or grade, campaign or program state, email delivery, CRM sync, API result, attribution, pipeline, conversion, revenue, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
