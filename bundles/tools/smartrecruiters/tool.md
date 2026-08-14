---
type: "Tool Guide"
title: "SmartRecruiters"
description: "Source-aware guidance for SmartRecruiters."
resource: "https://developers.smartrecruiters.com/docs/the-smartrecruiters-platform"
okb_bundle_id: smartrecruiters
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise recruiting, applicant tracking, hiring workflow, marketplace, API, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "process applicant data, post jobs, screen or rank candidates, schedule interviews, send messages, create offers, enable AI, connect HR systems, or make employment, eligibility, compensation, diversity, or compliance decisions"
---
# SmartRecruiters Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developers.smartrecruiters.com/docs/the-smartrecruiters-platform
- https://www.smartrecruiters.com/recruiting-software/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SmartRecruiters hiring workflow and AI governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before process applicant data, post jobs, screen or rank candidates, schedule interviews, send messages, create offers, enable AI, connect HR systems, or make employment, eligibility, compensation, diversity, or compliance decisions.

## Guardrails

- Do not invent candidate identity, consent, qualification, score or rank, interview result, offer, compensation, bias or fairness, AI output, integration result, employment decision, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
