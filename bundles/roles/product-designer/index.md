---
type: Bundle Index
title: Product Designer
description: Entry point for the Product Designer OpenKnowledge bundle.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [product-design, ux-design, ui-design, interaction-design, prototyping, accessibility, design-systems]
aliases: [UX designer, UI designer, UI/UX designer, digital product designer, experience designer]
problems_solved:
  - turn product context into design briefs and concept directions
  - review user flows, wireframes, prototypes, and UI states
  - separate user evidence from design assumptions
  - prepare accessibility-aware design review notes
  - structure design handoff for engineering
industries: [software, saas, digital-products, internal-tools, consumer-apps]
tools: [Figma, FigJam, Miro, Maze, UserTesting, Dovetail, Jira, Linear, Notion, Confluence, Storybook]
frameworks: [Double Diamond, design thinking, Jobs-to-be-Done, heuristic evaluation, journey mapping, accessibility POUR]
deliverables: [design brief, design review note, prototype test plan, handoff checklist]
commands: [/draft-design-brief, /review-ui-flow]
skills: []
evaluations: [product-design-quality-check]
okb_bundle_id: product-designer
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles: [ada, figma, product-manager, wcag]
adjacent_bundles: [product-manager]
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings:
  onet_soc: ["15-1255.00"]
  soc: ["15-1255"]
  isco_08: ["2166"]
  esco: ["2166"]
limitations:
  - Product design scope varies by organization; verify local role ownership, design process, and decision rights.
  - Does not replace user research, legal accessibility review, brand approval, product leadership, or engineering feasibility review.
  - Does not include tool-specific API automation or workspace-specific design-system details.
safety_notes:
  - Confirm before modifying live design files, tickets, research repositories, product specs, roadmap artifacts, or customer-facing communications.
  - Treat customer research, unreleased product strategy, design files, analytics, and roadmap plans as confidential unless the user confirms they are safe to use.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 16
  okb_score: 21
  absolute_lift: 5
  task_scores:
    - task: checkout-flow-review
      baseline_score: 2
      okb_score: 9
      max_score: 12
    - task: onboarding-prototype-plan
      baseline_score: 7
      okb_score: 6
      max_score: 12
    - task: design-brief-from-sparse-context
      baseline_score: 7
      okb_score: 6
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 16/36 to 21/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
timestamp: 2026-07-09T00:00:00Z
---

# Product Designer

This bundle helps an agent support product design work: framing design problems, reviewing flows and interfaces, preparing prototype plans, checking accessibility-sensitive risks, and creating handoff-ready design notes.

## Core Concepts

- [Role](role.md)
- [Responsibilities](responsibilities/index.md)
- [Evidence-Led Design](frameworks/evidence-led-design.md)
- [Accessibility-Aware Design](frameworks/accessibility-aware-design.md)

## Workflows

- [Design Brief to Concept](workflows/design-brief-to-concept.md)
- [Design Review](workflows/design-review.md)

## Deliverables and Commands

- [Design Brief](deliverables/design-brief.md)
- [Design Review Note](deliverables/design-review-note.md)
- [Prototype Test Plan](deliverables/prototype-test-plan.md)
- [/draft-design-brief](commands/draft-design-brief.md)
- [/review-ui-flow](commands/review-ui-flow.md)

Use this bundle as design decision support. It is not authority to alter live design artifacts, send feedback, claim accessibility compliance, or make product commitments without confirmation.
