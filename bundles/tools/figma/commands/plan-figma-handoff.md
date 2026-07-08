---
type: Slash Command
command: /plan-figma-handoff
title: Plan Figma Handoff
description: "Create a source-scoped Figma handoff or design-review plan without inventing file, component, variable, prototype, Dev Mode, or permission details."
okb_bundle_id: figma
inputs:
  - design question or implementation goal
  - Figma file, page, frame, component, library, prototype, or Dev Mode evidence
  - codebase, design-system, accessibility, export, and permission constraints
outputs:
  - Figma readiness answer
  - required local evidence
  - design and handoff plan
  - validation and permission checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-figma-handoff

Purpose: produce a Figma design handoff or review plan that is ready for designer, developer, and file-owner review, not an unsafely executed file edit, export, comment, integration action, or permission change.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Product/design question, target audience, platform, implementation target, and success criteria.
- Figma file, page, frame, section, component, instance, style, variable, library, prototype, comment, Dev Mode, screenshot, export, or API/tool evidence, if available.
- Codebase, design-system source of truth, component mapping, token, asset, responsive, accessibility, and QA constraints.
- Figma team, project, owner, collaborator, permission, sharing, export, privacy, security, and approval constraints.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the Figma handoff or review now.
2. Source note: official Figma source categories, user-provided Figma/local evidence, and missing verification.
3. Verified facts: what is confirmed by official sources or user-provided file/team/library/Dev Mode evidence.
4. Missing evidence: file, frame, component, variable, prototype, Dev Mode, codebase, accessibility, export, permission, or approval inputs needed.
5. Design handoff plan: frames, components, variables, assets, interactions, responsive states, content, acceptance criteria, and assumptions.
6. Design-system and implementation review: source components, tokens/variables/styles, library status, code mapping, gaps, and owner questions.
7. Sharing and permission review: owner, audience, link access, comments, exports, sensitive content, and approval boundary.
8. Validation and confirmation boundary: QA, accessibility, design-system owner review, implementation check, rollback, and actions requiring explicit confirmation.

## Confirmation Boundary

Do not edit, delete, publish, export, comment, run plugins/integrations/API/MCP actions, change permissions, update libraries/components/variables/styles, or share links outside the intended audience without explicit user confirmation and authorized access.
