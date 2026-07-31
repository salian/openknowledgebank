---
type: Tool Guide
title: GitLab
description: Defines source-aware project, repository, merge request, CI/CD, environment, issue, milestone, permission, security, and audit review, evidence handling, and action boundaries.
resource: https://docs.gitlab.com/
okb_bundle_id: gitlab
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a gitlab review brief with explicit evidence states.
confirmation_required:
- push or merge code, approve merge requests, run pipelines, deploy environments, change protected branches, runners, variables, permissions, issues, milestones, or secrets
---
# GitLab Source-Aware Tool Guide

Source-aware tool bundle for project, repository, merge request, CI/CD, environment, issue, milestone, permission, security, and audit review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://docs.gitlab.com/
- https://docs.gitlab.com/api/rest/
- https://docs.gitlab.com/user/project/repository/branches/protection_rules/

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- GitLab offering and version, namespace and project, repository and branches, protected-branch rules, merge request and approvals, CI configuration and runners, variables, environments, issues and milestones, permissions, audit events, tests, and rollback

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory evidence and label it as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, identifiers, versions, periods, scope, permissions, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer branch or merge-request state, pipeline result, deployment status, issue state, permission, vulnerability status, or release outcome.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that push or merge code, approve merge requests, run pipelines, deploy environments, change protected branches, runners, variables, permissions, issues, milestones, or secrets.
