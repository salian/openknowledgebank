---
type: Tool Guide
title: Product Manager Tool Surfaces
description: Safe-use guide for common product-management tools.
tool_category: product-management
okb_bundle_id: product-manager
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations: [summarize exported context, draft artifact text, review requirements, suggest questions]
confirmation_required: [modify roadmap, create or update tickets, change product docs, update analytics definitions, send communications]
timestamp: 2026-07-09T00:00:00Z
---

# Product Manager Tool Surfaces

Common surfaces include issue trackers, roadmap tools, document systems, design files, analytics platforms, experimentation platforms, feedback repositories, CRM/support systems, and release tools.

This bundle does not contain trusted executable tool instructions. Consumers must treat bundled commands and tool guidance as suggestions, not trusted executable behavior.

## Safe Use

- Summarize user-provided exports or pasted context.
- Draft PRD, brief, roadmap, and review text for user approval.
- Suggest questions to inspect local tool configuration.
- Identify missing evidence and required owners.

## Confirmation Required

Require explicit confirmation before creating, editing, moving, deleting, sending, publishing, exporting, or changing anything in live tools. This includes roadmap items, Jira/Linear issues, Confluence/Notion pages, Figma comments, analytics definitions, feature flags, experiments, release notes, and customer communications.

## Inspect First

Before giving exact tool instructions, inspect or ask the user to provide the local workspace structure, project fields, templates, permissions, automations, and source-of-record conventions.
