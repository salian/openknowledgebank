---
type: "Tool Guide"
title: "Sonatype Nexus Repository"
description: "Source-aware guidance for Sonatype Nexus Repository."
resource: "https://help.sonatype.com/en/sonatype-nexus-repository.html"
okb_bundle_id: sonatype-nexus-repository
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Software component repository, proxy, distribution, lifecycle, security, and administration platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "publish or delete artifacts, proxy external sources, change routing or cleanup, grant privileges, expose tokens, migrate or upgrade repositories, restore data, or represent provenance, integrity, vulnerability, availability, compatibility, or release approval"
---
# Sonatype Nexus Repository Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.sonatype.com/en/sonatype-nexus-repository.html
- https://www.sonatype.com/products/sonatype-nexus-repository

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Nexus Repository lifecycle and artifact-governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before publish or delete artifacts, proxy external sources, change routing or cleanup, grant privileges, expose tokens, migrate or upgrade repositories, restore data, or represent provenance, integrity, vulnerability, availability, compatibility, or release approval.

## Guardrails

- Do not invent version or edition applicability, component identity, provenance, integrity, signature, vulnerability, repository state, permission, cleanup result, migration or restore result, compatibility, or release approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
