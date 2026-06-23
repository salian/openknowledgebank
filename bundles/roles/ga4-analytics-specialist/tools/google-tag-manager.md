---
type: Tool Guide
title: Google Tag Manager
description: Safe-use guide for implementation and tracking checks related to GA4.
tool_category: tag-management
resource: "https://support.google.com/tagmanager"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - review user-provided tag configuration
  - create QA checklist
  - suggest debugging steps
confirmation_required:
  - publish container
  - change tags
  - change triggers
  - change variables
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Google Tag Manager

Use GTM context when a GA4 metric movement may be caused by implementation changes.

Ask for container version history, GA4 tag setup, ecommerce event tags, triggers, variables, consent mode, and data layer changes. Do not publish or modify a container without explicit confirmation.
