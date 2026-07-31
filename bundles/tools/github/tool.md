---
type: Tool Guide
title: "GitHub"
description: "Defines source-aware software collaboration and repository operations, evidence handling, and action boundaries."
tool_category: "Code hosting & DevOps platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review software collaboration and repository operations from supplied evidence."
  - "Draft a github repository change brief with explicit evidence states."
confirmation_required:
  - "pushing commits, merging, closing issues, changing workflows, permissions, secrets, rulesets, releases, or deployments"
okb_bundle_id: github
timestamp: "2026-07-31T00:00:00Z"
---

# GitHub

Source-aware tool bundle for GitHub repository, pull request, issue, workflow, release, security, and permission evidence with review-ready change briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- repository and organization scope
- commit, branch, tag, and default-branch state
- pull requests, reviews, issues, and discussions
- checks, workflow runs, logs, and artifacts
- rulesets, environments, secrets, and permissions
- release and deployment evidence
- security and audit evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before pushing commits, merging, closing issues, changing workflows, permissions, secrets, rulesets, releases, or deployments.
