---
type: Bundle Index
title: Paid Search / PPC Specialist
description: Source-aware role bundle for paid-search planning, keyword and query review, ad and landing-page QA, conversion measurement, and approval-ready optimization briefs.
schema_version: 0.1.0
bundle_format: okf-compatible
category: roles
tags:
- paid-search
- ppc
- search-advertising
- role
aliases:
- Paid Search Specialist
- PPC Specialist
problems_solved:
- Prepare paid search campaign and optimization brief without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce review-ready decisions with explicit verification and approval boundaries.
industries:
- Marketing
- Advertising
tools: []
frameworks:
- source-evidence matrix
- search-campaign evidence matrix
- qualified-review gate
deliverables:
- Paid search campaign and optimization brief
commands: []
skills: []
evaluations:
- Paid Search / PPC Specialist source-awareness check
okb_bundle_id: paid-search-ppc-specialist
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- ccpa
- gdpr
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 13-1161.01
  soc: []
  isco_08: []
  esco:
  - '2431.2'
limitations:
- Use as occupational context; account configuration, keywords, search terms, ads, budgets, conversions, attribution, consent, and results require current evidence.
- Task-specific work requires current evidence for campaign objective and account export, keyword, match, negative, and search-term evidence, approved ads, claims, and landing pages, budget and bidding authority, conversion and attribution configuration, consent and tracking policy, dated performance export.
- Do not infer account state, keywords, search terms, spend, conversion rate, attribution, quality score, access.
safety_notes:
- Minimize personal, customer, employee, financial, credential, and other sensitive data.
- Require explicit confirmation before spend, bids, targeting, claims, tracking, consent, landing pages, or campaign changes.
- Route legal, privacy, security, compliance, financial, employment, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 10
  okb_score: 32
  absolute_lift: 22
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 10
    max_score: 12
  - task: role-prioritization-review
    baseline_score: 4
    okb_score: 12
    max_score: 12
  - task: role-source-reconciliation
    baseline_score: 3
    okb_score: 10
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 10/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Paid Search / PPC Specialist

Source-aware role bundle for paid-search planning, keyword and query review, ad and landing-page QA, conversion measurement, and approval-ready optimization briefs.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts
and explain which decision each artifact supports.

## Start Here

- [overview.md](overview.md)
- [role.md](role.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/paid-search-brief.md](deliverables/paid-search-brief.md)
