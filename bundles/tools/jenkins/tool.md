---
type: Tool Guide
title: "Jenkins"
description: "Defines source-aware continuous integration and delivery automation, evidence handling, and action boundaries."
tool_category: "CI/CD automation server"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review continuous integration and delivery automation from supplied evidence."
  - "Draft a jenkins pipeline and change brief with explicit evidence states."
confirmation_required:
  - "running jobs, changing pipelines, plugins, credentials, permissions, agents, artifacts, releases, or deployments"
okb_bundle_id: jenkins
timestamp: "2026-07-31T00:00:00Z"
---

# Jenkins

Source-aware tool bundle for Jenkins controller, agent, job, pipeline, plugin, credential, build, release, and controlled automation briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- Jenkins version and controller scope
- agents, labels, executors, and node state
- job, pipeline, multibranch, and Jenkinsfile definitions
- plugins, dependencies, and compatibility evidence
- credentials references and permission boundaries
- build parameters, logs, artifacts, and test results
- environment, deployment, rollback, and approval evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before running jobs, changing pipelines, plugins, credentials, permissions, agents, artifacts, releases, or deployments.
