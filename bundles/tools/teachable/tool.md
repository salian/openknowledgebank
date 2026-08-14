---
type: "Tool Guide"
title: "Teachable"
description: "Source-aware guidance for Teachable."
resource: "https://support.teachable.com/hc/en-us"
okb_bundle_id: teachable
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Course, coaching, digital-product, student, payment, marketing, and creator platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "upload or publish protected content, enroll or assess learners, issue certificates, set prices, collect payments, change payouts or taxes, contact students, call APIs, or represent learning, completion, certification, revenue, tax, rights, or compliance"
---
# Teachable Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://support.teachable.com/hc/en-us
- https://teachable.com/features

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Teachable course, commerce, and learner-data review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before upload or publish protected content, enroll or assess learners, issue certificates, set prices, collect payments, change payouts or taxes, contact students, call APIs, or represent learning, completion, certification, revenue, tax, rights, or compliance.

## Guardrails

- Do not invent student identity, enrollment or progress, assessment validity, certificate, content rights, payment or payout, tax treatment, API result, conversion, revenue, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
