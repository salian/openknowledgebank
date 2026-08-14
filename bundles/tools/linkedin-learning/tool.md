---
type: "Tool Guide"
title: "LinkedIn Learning"
description: "Source-aware guidance for LinkedIn Learning."
resource: "https://learn.microsoft.com/en-us/linkedin/learning/"
okb_bundle_id: linkedin-learning
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise learning content, administration, reporting, and LMS integration platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "provision learners, assign content, expose learner activity, configure SSO or OAuth, grant API keys, send xAPI statements, import or export records, or represent completion, skill, or qualification"
---
# LinkedIn Learning Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://learn.microsoft.com/en-us/linkedin/learning/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable LinkedIn Learning integration and learning-record review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before provision learners, assign content, expose learner activity, configure SSO or OAuth, grant API keys, send xAPI statements, import or export records, or represent completion, skill, or qualification.

## Guardrails

- Do not invent learner identity, access, assignment, activity, completion, skill, content entitlement, API authorization, SSO or xAPI delivery, report accuracy, qualification, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
