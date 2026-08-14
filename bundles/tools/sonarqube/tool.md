---
type: "Tool Guide"
title: "SonarQube"
description: "Source-aware guidance for SonarQube."
resource: "https://www.sonarsource.com/products/sonarqube/"
okb_bundle_id: sonarqube
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Code quality, static analysis, security, quality-gate, CI, and governance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "scan proprietary code, change rules or quality gates, suppress or resolve findings, expose tokens, block merges, connect repositories, or represent issue validity, vulnerability, risk, coverage, quality, compliance, or release readiness"
---
# SonarQube Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.sonarsource.com/products/sonarqube/
- https://docs.sonarsource.com/sonarqube-server/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SonarQube analysis and quality-gate governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before scan proprietary code, change rules or quality gates, suppress or resolve findings, expose tokens, block merges, connect repositories, or represent issue validity, vulnerability, risk, coverage, quality, compliance, or release readiness.

## Guardrails

- Do not invent product or edition applicability, source completeness, rule applicability, issue validity, vulnerability or exploitability, hotspot review, coverage, quality-gate result, compliance, or release readiness.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
