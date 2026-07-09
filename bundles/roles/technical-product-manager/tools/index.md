---
type: Tool Guide
title: Technical Product Manager Tool Surfaces
description: Common tool surfaces and safe-use boundaries for technical product-management assistance.
okb_bundle_id: technical-product-manager
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations: [summarize user-provided artifacts, draft review checklists, prepare questions, compare provided docs]
confirmation_required: [modify live tickets, update docs, change repositories, update API specs, alter flags, export data, send messages]
timestamp: 2026-07-09T00:00:00Z
---

# Tool Surfaces

Common TPM work may involve Jira, Linear, Confluence, Notion, Figma, Miro, Postman, OpenAPI specs, GitHub, GitLab, LaunchDarkly, Datadog, Grafana, Amplitude, Mixpanel, Productboard, and Aha!.

These are examples of surfaces, not guaranteed integrations. Verify workspace access, permissions, source-of-record status, and user intent before relying on any tool output.

## Safe Uses

- Summarize user-provided docs, specs, tickets, diagrams, and notes.
- Draft questions for engineering, design, data, security, privacy, support, and go-to-market owners.
- Prepare a review checklist or decision memo from provided evidence.
- Compare two user-provided artifacts and identify unresolved differences.

## Confirmation Required

Ask for explicit confirmation before modifying live tickets, docs, repositories, API specs, schemas, analytics definitions, flags, release notes, dashboards, roadmaps, or customer communications.
