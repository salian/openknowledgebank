---
type: "Tool Guide"
title: "Qualtrics XM"
description: "Source-aware guidance for Qualtrics XM."
resource: "https://www.qualtrics.com/support/"
okb_bundle_id: qualtrics-xm
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Survey, experience management, research, workflow, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "collect personal or sensitive responses, identify participants, distribute surveys, pay incentives, change anonymity or retention, trigger workflows, export data, call APIs, analyze employee feedback, or represent sample validity, sentiment, causality, employment, or business conclusions"
---
# Qualtrics XM Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.qualtrics.com/support/
- https://api.qualtrics.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Qualtrics XM research and data-governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before collect personal or sensitive responses, identify participants, distribute surveys, pay incentives, change anonymity or retention, trigger workflows, export data, call APIs, analyze employee feedback, or represent sample validity, sentiment, causality, employment, or business conclusions.

## Guardrails

- Do not invent respondent identity, consent, anonymity, confidentiality, sample representativeness, response completeness, weighting, text-analysis accuracy, statistical validity, causality, employee conclusion, API result, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
