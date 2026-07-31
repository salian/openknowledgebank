---
type: Bundle Index
title: "Product Marketing Manager"
description: "Source-aware role bundle for product positioning, messaging, launches, market and competitive evidence, sales enablement, and decision-ready go-to-market briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags:
  - "product-marketing"
  - "go-to-market"
  - "positioning"
  - "role"
aliases:
  - "Product Marketing Manager"
problems_solved:
  - "Prepare a product marketing decision brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Software"
  - "Consumer and business products"
tools: []
frameworks:
  - "source-evidence matrix"
  - "product-marketing-strategy-and-launch-decisions evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Product marketing decision brief"
commands: []
skills: []
evaluations:
  - "Product Marketing Manager source-awareness check"
okb_bundle_id: product-marketing-manager
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "can-spam"
  - "figma"
  - "gdpr"
  - "hubspot-sales-hub"
  - "salesforce-service-cloud"
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc:
    - "11-2021.00"
  soc: []
  isco_08: []
  esco:
    - "1221"
limitations:
  - "Use official Product Marketing Manager sources for general context; local product marketing strategy and launch decisions, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for product and roadmap evidence, customer and market research, positioning and messaging drafts, competitive evidence, launch scope and channel plans, sales enablement feedback, and performance definitions and results."
  - "Do not infer customer needs, market size, competitor claims, product capabilities, roadmap commitments, launch dates, channel performance, win-loss causes."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before external claims, launch commitments, pricing, roadmap disclosure, customer communications, or campaign spend."
  - "Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers."
timestamp: "2026-07-31T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: "2026-07-31"
  method: "baseline-vs-okb-rubric"
  model: "openai/gpt-4o-mini"
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 6
  okb_score: 36
  absolute_lift: 30
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 1
      okb_score: 12
      max_score: 12
    - task: "role-prioritization-review"
      baseline_score: 3
      okb_score: 12
      max_score: 12
    - task: "role-source-reconciliation"
      baseline_score: 2
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 6/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Product Marketing Manager

Source-aware role bundle for product positioning, messaging, launches, market and competitive evidence, sales enablement, and decision-ready go-to-market briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, or approval. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request itself explicitly supports an item.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/product-marketing-manager-brief.md](deliverables/product-marketing-manager-brief.md)
