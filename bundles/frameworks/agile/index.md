---
type: Bundle Index
title: Agile
description: "Framework hub bundle for applying Agile values and principles to software delivery without confusing the umbrella with a specific method."
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
  - agile
  - software-delivery
  - product-development
  - engineering-process
  - delivery-management
aliases:
  - Agile software delivery
  - Agile Manifesto
  - Agile methods
  - agile development
problems_solved:
  - Anchor Agile guidance in the Manifesto values and principle themes.
  - Choose between Agile method families based on context instead of labels.
  - Diagnose process theater that lacks feedback, working software, or adaptation.
  - Separate umbrella Agile guidance from Scrum, Kanban, XP, SAFe, and other method mechanics.
industries:
  - software
  - digital-products
  - technology
tools: []
frameworks:
  - Agile Manifesto
  - Scrum
  - Kanban Method
  - Extreme Programming
  - SAFe
  - Lean Software Development
deliverables:
  - agile operating brief
commands:
  - /choose-agile-method
skills: []
evaluations:
  - Agile guidance quality check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - product-manager
adjacent_bundles:
  - ga4-analytics-specialist
  - performance-marketer
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
  - "Not a complete implementation guide for Scrum, Kanban, XP, SAFe, DSDM, LeSS, Crystal, FDD, Scrumban, Disciplined Agile, or Nexus."
  - "Requires user-provided team, workflow, delivery, quality, and tool evidence before judging an organization's actual agility."
  - "Does not replace professional advice for contractual, HR, compliance, or regulated delivery decisions."
safety_notes:
  - "Require confirmation before changing live boards, workflows, reports, staffing plans, contract commitments, release policies, or customer communications."
  - "Do not claim access to private delivery metrics, tickets, source repositories, or planning artifacts unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 18
  okb_score: 25
  absolute_lift: 7
  task_scores:
    - task: framework-fit-review
      baseline_score: 3
      okb_score: 10
      max_score: 12
    - task: artifact-quality-review
      baseline_score: 7
      okb_score: 5
      max_score: 12
    - task: implementation-change-plan
      baseline_score: 8
      okb_score: 10
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 18/36 to 25/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: agile
timestamp: "2026-07-09T00:00:00Z"
---

# Agile

This bundle helps an agent use Agile as an umbrella software-delivery framework. It anchors advice in the Manifesto for Agile Software Development and its principle themes while avoiding the common mistake of treating Agile as a synonym for one method, one ceremony set, or one work-tracking tool.

## Required Answer Habit

For Agile work, include a short **Source note** naming the framework source category, the user-provided team or delivery evidence used, and missing evidence required before treating a recommendation as specific to the user's organization.

## Start Here

- [framework.md](framework.md)
- [frameworks/agile-principles.md](frameworks/agile-principles.md)
- [commands/choose-agile-method.md](commands/choose-agile-method.md)
- [workflows/agile-alignment-review.md](workflows/agile-alignment-review.md)
- [workflows/choose-method-family.md](workflows/choose-method-family.md)
- [deliverables/agile-operating-brief.md](deliverables/agile-operating-brief.md)
- [evaluations/agile-guidance-quality-check.md](evaluations/agile-guidance-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use the Agile Manifesto site for the core values and principles. Use user-provided local evidence for a team's actual workflow, delivery cadence, feedback loops, engineering practices, constraints, and metrics. Do not invent team-specific practices, tool settings, roles, or metrics.
