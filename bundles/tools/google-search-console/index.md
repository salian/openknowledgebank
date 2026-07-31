---
type: Bundle Index
title: "Google Search Console"
description: "Source-aware tool bundle for Google Search Console properties, performance, indexing, URL inspection, sitemaps, reports, and review-ready search briefs."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - "google-search-console"
  - "seo"
  - "search-performance"
  - "tool"
aliases:
  - "Google Search Console"
problems_solved:
  - "Prepare a search console diagnosis brief without fabricating local facts."
  - "Separate verified, provided, assumed, and missing evidence."
  - "Produce review-ready decisions with explicit verification and approval boundaries."
industries:
  - "Marketing"
  - "Publishing"
  - "Commerce"
tools:
  - "Google Search Console"
frameworks:
  - "source-evidence matrix"
  - "organic-search-monitoring-and-diagnosis evidence matrix"
  - "qualified-review gate"
deliverables:
  - "Search Console diagnosis brief"
commands: []
skills: []
evaluations:
  - "Google Search Console source-awareness check"
okb_bundle_id: google-search-console
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - "seo-specialist-consultant"
adjacent_bundles: []
contributors:
  - "OpenKnowledgeBank"
maintainers:
  - "OpenKnowledgeBank"
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Use official Google Search Console sources for general context; local organic search monitoring and diagnosis, configuration, records, values, states, and permissions require inspected evidence."
  - "Task-specific work requires current evidence for property type, verified scope, and ownership, report, date range, search type, country, device, query, and page filters, metric definitions, freshness, and aggregation behavior, URL inspection and live-test evidence, indexing, canonical, robots, sitemap, and enhancement evidence, site changes and deployment dates, and analytics, server, rank, and source-of-record comparisons."
  - "Do not infer property scope, verification, performance values, indexing state, canonical selection, crawl state, sitemap state, site changes."
safety_notes:
  - "Minimize personal, customer, employee, financial, credential, and other sensitive data."
  - "Require explicit confirmation before changing users, submitting removals or validation requests, modifying sitemaps or site configuration, or publishing unsupported ranking claims."
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
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
    - task: "empty-evidence-integrity"
      baseline_score: 2
      okb_score: 12
      max_score: 12
    - task: "configuration-risk-review"
      baseline_score: 9
      okb_score: 12
      max_score: 12
    - task: "metric-or-report-reconciliation"
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores: []
  display_summary: "Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks."
  evidence_note: "Public listing scorecard excludes raw prompts and private run artifacts."
---

# Google Search Console

Source-aware tool bundle for Google Search Console properties, performance, indexing, URL inspection, sitemaps, reports, and review-ready search briefs.

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
- [tool.md](tool.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/google-search-console-brief.md](deliverables/google-search-console-brief.md)
