---
type: Tool Guide
title: "WordPress"
description: "Defines source-aware website content and platform administration, evidence handling, and action boundaries."
tool_category: "website content and platform administration"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review website content and platform administration from supplied evidence."
  - "Draft a wordpress site and change brief with explicit evidence states."
confirmation_required:
  - "publishing or deleting content, installing or updating themes, plugins, or core, changing users or roles, or changing production configuration"
okb_bundle_id: wordpress
timestamp: "2026-07-31T00:00:00Z"
---

# WordPress

Source-aware tool bundle for WordPress content, themes, plugins, users, settings, updates, staging, security, performance, and controlled production changes.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- hosting, WordPress version, site, and network scope
- roles and capabilities
- themes, plugins, and versions
- content, media, comments, and publication state
- settings and permalinks
- backups, staging, security, cache, and SEO configuration

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer production state, plugin compatibility, role capability, content status, backup recoverability, and cache behavior.
- Require accountable confirmation before publishing or deleting content, installing or updating themes, plugins, or core, changing users or roles, or changing production configuration.
