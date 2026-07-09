---
type: Tool Guide
title: Senior Product Manager Tool Boundaries
description: Safe-use guidance for product-management tools and local systems.
tags: [tools, safety]
okb_bundle_id: senior-product-manager
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations: [summarize user-provided exports, draft review comments, compare pasted roadmap options]
confirmation_required: [modify tickets, update roadmaps, change analytics definitions, publish docs, send communications, export customer data]
timestamp: 2026-07-09T00:00:00Z
---

# Tool Boundaries

Product-management tools are local sources of record. The agent should not assume access, fields, permissions, workflow states, or API behavior.

## Common Source Categories

- Roadmap and planning systems: Productboard, Aha!, Jira, Linear, spreadsheets.
- Documentation systems: Confluence, Notion, Google Docs, internal wikis.
- Design systems and prototypes: Figma or equivalent.
- Analytics and BI: Amplitude, Mixpanel, warehouse dashboards, notebooks.
- Feedback sources: support tickets, sales notes, research repositories, calls, surveys.

## Safe Use

Summarize user-provided exports or pasted excerpts, draft proposed changes, and identify evidence gaps. Require explicit confirmation before changing live records, exporting data, sending messages, or committing roadmap or release information.
