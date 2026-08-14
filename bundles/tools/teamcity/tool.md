---
type: "Tool Guide"
title: "TeamCity"
description: "Source-aware guidance for TeamCity."
resource: "https://www.jetbrains.com/help/teamcity/teamcity-documentation.html"
okb_bundle_id: teamcity
timestamp: "2026-08-14T00:00:00Z"
tool_category: "CI/CD server and cloud, build-chain, agent, artifact, test, deployment, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect repositories, expose credentials, run builds or deployments, change pipelines, agents or permissions, publish artifacts, install plugins, call APIs, upgrade servers, or represent test, build, artifact, deployment, security, or release success"
---
# TeamCity Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.jetbrains.com/help/teamcity/teamcity-documentation.html
- https://www.jetbrains.com/teamcity/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable TeamCity pipeline, agent, and deployment governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect repositories, expose credentials, run builds or deployments, change pipelines, agents or permissions, publish artifacts, install plugins, call APIs, upgrade servers, or represent test, build, artifact, deployment, security, or release success.

## Guardrails

- Do not invent product or version applicability, repository or agent state, credential safety, test validity, build or dependency result, artifact provenance, deployment result, security, availability, or release readiness.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
