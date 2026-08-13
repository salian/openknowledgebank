---
type: "Tool Guide"
title: "Contentful"
description: "Source-aware guidance for Contentful."
resource: "https://www.contentful.com/developers/docs/references/api-basics/"
okb_bundle_id: contentful
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Composable content management platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter content models, entries, assets or environments, issue tokens, install apps, run migrations, publish, unpublish or delete content, change roles, or represent delivery"
---
# Contentful Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.contentful.com/developers/docs/references/api-basics/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Contentful configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter content models, entries, assets or environments, issue tokens, install apps, run migrations, publish, unpublish or delete content, change roles, or represent delivery.

## Guardrails

- Do not invent space or environment state, content ownership or rights, schema compatibility, entry version, localization completeness, token safety, webhook result, cache freshness, publication or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
