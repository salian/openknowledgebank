---
type: "Tool Guide"
title: "Prismic"
description: "Source-aware guidance for Prismic."
resource: "https://prismic.io/docs"
okb_bundle_id: prismic
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Headless website CMS, Page Builder, API, and release platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "change content models, create or alter content, publish releases, upload protected media, run migrations, trigger webhooks, expose tokens, change access, deploy sites, or represent content, translation, preview, delivery, SEO, or availability"
---
# Prismic Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://prismic.io/docs
- https://prismic.io/product

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Prismic content-model and release review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before change content models, create or alter content, publish releases, upload protected media, run migrations, trigger webhooks, expose tokens, change access, deploy sites, or represent content, translation, preview, delivery, SEO, or availability.

## Guardrails

- Do not invent repository or environment state, model or field identity, content rights, translation, release or publication state, token scope, API result, migration completeness, build, SEO result, uptime, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
