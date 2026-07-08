---
type: Bundle Index
title: Figma
description: "Tool bundle for source-aware Figma design, prototype, design-system, Dev Mode, handoff, and sharing-permission planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - figma
  - design
  - prototyping
  - design-systems
  - developer-handoff
aliases:
  - Figma Design
  - FigJam
  - Figma Dev Mode
problems_solved:
  - Plan Figma design handoff without inventing file, frame, component, variable, or permission details.
  - Separate official Figma product behavior from user-provided file, library, Dev Mode, prototype, and team evidence.
  - Review design-system, prototype, export, sharing, and permissions risk before action.
  - Produce handoff readiness plans with source notes, validation checks, and confirmation boundaries.
industries:
  - software
  - digital-products
  - design
  - marketing
  - ecommerce
tools:
  - Figma
  - Figma Design
  - FigJam
  - Dev Mode
  - Figma libraries
  - Figma variables
frameworks:
  - verify-first design handoff
  - design-system source-of-truth review
  - prototype readiness review
  - sharing and permission confirmation boundary
deliverables:
  - Figma handoff readiness plan
commands:
  - /plan-figma-handoff
skills: []
evaluations:
  - Figma handoff plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
adjacent_bundles:
  - agile
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Not a complete Figma Design, FigJam, Dev Mode, API, plugin, pricing, plan, connector, beta-feature, or release reference."
  - "Requires user-provided Figma file, page, frame, component, variable, style, prototype, comment, Dev Mode, library, permission, and policy evidence before final conclusions."
  - "Does not replace product design, design-system, accessibility, security, privacy, legal, procurement, or administrator review."
safety_notes:
  - "Require explicit confirmation before editing, deleting, publishing, exporting, moving, commenting, changing permissions, updating libraries/components/variables/styles, running plugins/integrations, or sharing Figma links."
  - "Do not claim access to Figma files, teams, projects, organizations, libraries, components, variables, comments, prototypes, permissions, or Dev Mode output unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: blocked
  last_evaluated: "2026-07-09"
  method: baseline-vs-okb-rubric
  tasks_count: 0
  display_summary: "Measured evaluation is blocked until a Figma task set and model/provider configuration are selected."
  evidence_note: "No raw prompts or outputs are included in the public bundle."
okb_bundle_id: figma
timestamp: "2026-07-09T00:00:00Z"
---

# Figma

This bundle helps an agent use Figma as a source-aware design, prototyping, design-system, and developer-handoff tool. It is designed for Figma file review, handoff planning, prototype readiness, library/component/variable checks, Dev Mode evidence requests, and sharing-permission review.

It is a companion tool bundle, not a replacement for role bundles such as product designer, design systems designer, UI designer, UX designer, or front-end UI developer.

## Required Answer Habit

For source-sensitive Figma work, include a short **Source note** naming the official Figma source category, the user-provided file/team/library/Dev Mode evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-figma-handoff.md](commands/plan-figma-handoff.md)
- [workflows/review-figma-design-handoff.md](workflows/review-figma-design-handoff.md)
- [workflows/review-figma-sharing-and-permissions.md](workflows/review-figma-sharing-and-permissions.md)
- [deliverables/figma-handoff-readiness-plan.md](deliverables/figma-handoff-readiness-plan.md)
- [evaluations/figma-handoff-plan-quality-check.md](evaluations/figma-handoff-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Figma Help, Figma developer documentation, and official Figma product pages for product behavior, plus user-provided Figma file, library, prototype, Dev Mode, permission, and policy evidence. Do not invent file names, pages, frames, layers, components, variants, variables, styles, prototypes, comments, owners, permissions, API behavior, plugin behavior, exports, or implementation status.
