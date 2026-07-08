---
type: Tool Guide
title: Figma
description: "Defines safe, source-aware use of Figma in OpenKnowledgeBank bundles."
tool_category: "Collaborative interface design, prototyping, design-system, and handoff platform"
okb_bundle_id: figma
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - Plan Figma design, prototype, design-system, and handoff work from user-provided evidence.
  - Review components, variables, libraries, Dev Mode context, comments, permissions, and exports for readiness.
  - Explain Figma concepts using official Figma documentation categories.
confirmation_required:
  - Edit, delete, move, publish, duplicate, rename, branch, merge, or restructure Figma files, pages, frames, components, variables, styles, libraries, or prototypes.
  - Change sharing, permissions, ownership, team/project settings, link access, comments, notifications, exports, or published assets.
  - Run plugins, integrations, API actions, MCP-connected actions, or exports that access private design content.
timestamp: "2026-07-09T00:00:00Z"
---

# Figma Tool Guide

Figma is a collaborative design and prototyping platform used for interface design, FigJam collaboration, design systems, Dev Mode handoff, comments, libraries, variables, and design-to-development workflows.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## What This Bundle Is For

- Planning Figma design handoff and implementation-readiness reviews.
- Turning design requests into source-scoped evidence requests.
- Reviewing file structure, components, variables, styles, libraries, prototypes, comments, Dev Mode evidence, exports, accessibility checks, and permissions.
- Supporting role bundles that use Figma for product design, UI design, UX design, design systems, front-end implementation, marketing design, or product management.

## What This Bundle Is Not

- A complete Figma Design, FigJam, Dev Mode, REST API, plugin, pricing, plan, beta-feature, or release reference.
- A substitute for designer, developer, design-system owner, accessibility specialist, security, privacy, procurement, legal, or Figma administrator review.
- A claim that the agent has access to the user's Figma files, organization, team, libraries, Dev Mode output, comments, or permissions.

## Source Discipline

Use exact Figma facts only when grounded in official Figma documentation or user-provided local evidence. Treat the following as local evidence requirements:

- file, project, team, page, frame, section, layer, branch, version, owner, and collaborator evidence;
- component, instance, variant, style, variable, library, token, icon, asset, documentation, and description evidence;
- prototype flow, interaction, animation, overlay, device, accessibility, content, and usability evidence;
- Dev Mode, inspect, measurement, asset export, code reference, component mapping, implementation, and repository evidence;
- sharing, link access, permissions, ownership, comments, notifications, exports, privacy, security, and approval evidence.

## Figma Guardrails

- Treat official Figma docs as product behavior source categories, not proof of a user's local file, organization, library, or permission configuration.
- Verify file, page, frame, component, style, variable, library, prototype, comment, and permission evidence before recommending edits or conclusions.
- Separate design intent, design-system source of truth, Dev Mode handoff, and implemented code status.
- Treat visual screenshots as partial evidence until the file structure, component source, interaction states, responsive behavior, accessibility, and permissions are checked.
- Require explicit confirmation before edits, exports, comments, permission changes, library/component/variable updates, plugin/integration/API actions, or broad sharing.

## Source Note Template

```text
Source note: Figma guidance is based on official Figma source categories for [design files / components / libraries / variables / prototypes / Dev Mode / sharing and permissions / developer API]. Local evidence used: [file link, screenshot, frame/page list, component/library details, variable/style list, prototype flow, comment thread, Dev Mode view, permission evidence, export, policy, or codebase evidence provided by user]. Missing before action or conclusion: [current doc/version check, file inspection, design-system owner approval, implementation evidence, accessibility review, permission review, data classification, export rights, or stakeholder approval].
```
