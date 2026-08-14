---
type: "Tool Guide"
title: "LearnDash"
description: "Source-aware guidance for LearnDash."
resource: "https://learndash.com/support/"
okb_bundle_id: learndash
timestamp: "2026-08-14T00:00:00Z"
tool_category: "WordPress learning management, assessment, groups, and reporting platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "publish courses, create or change enrollments, extend access, grade assignments or essays, change progress, scores or certificates, send group email, export learner data, run MCP actions, or represent completion"
---
# LearnDash Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://learndash.com/support/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable LearnDash LMS configuration and learning-record review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before publish courses, create or change enrollments, extend access, grade assignments or essays, change progress, scores or certificates, send group email, export learner data, run MCP actions, or represent completion.

## Guardrails

- Do not invent learner identity, enrollment, access, submission, grade, score, progress, completion, certificate, report accuracy, automation result, accessibility, qualification, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
