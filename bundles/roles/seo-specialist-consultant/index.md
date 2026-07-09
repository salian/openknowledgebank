---
type: Bundle Index
title: SEO Specialist / Consultant
description: Entry point for the SEO Specialist / Consultant OpenKnowledge bundle.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [seo, search, marketing, content, technical-seo]
aliases: [SEO consultant, SEO specialist, search engine optimization consultant, SEO strategist]
problems_solved:
  - Draft SEO audits without inventing tool access, rankings, or crawl findings.
  - Turn search performance evidence into source-scoped diagnoses and next actions.
  - Create content optimization briefs grounded in query intent and page evidence.
  - Avoid spam, manipulative tactics, and unsupported ranking guarantees.
industries: [marketing, ecommerce, b2b-saas, local-services, media]
tools: [Google Search Console, Google Analytics, crawler exports, keyword tools, rank tracking exports]
frameworks: [crawl-index-rank triage, intent-to-page fit, source-scoped SEO diagnosis]
deliverables: [SEO audit brief, content optimization brief, search performance diagnosis]
commands: [/draft-seo-audit]
skills: []
evaluations: [SEO quality check]
okb_bundle_id: seo-specialist-consultant
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles: [performance-marketer]
adjacent_bundles: []
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings:
  onet_soc: ["13-1161.01"]
  soc: []
  isco_08: []
  esco: ["2431.4"]
limitations:
  - Not a complete Google Search Console, crawler, analytics, CMS, or structured data implementation guide.
  - Requires user-provided site, report, crawl, keyword, SERP, and analytics evidence for final conclusions.
  - Does not guarantee rankings, traffic, indexing, rich results, or revenue outcomes.
safety_notes:
  - Require confirmation before modifying live CMS content, robots.txt, sitemaps, redirects, canonicals, structured data, internal links at scale, analytics/search settings, or exports.
  - Do not recommend spam, link buying, cloaking, doorway pages, deceptive automation, or attempts to manipulate generative AI search responses.
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 14
  okb_score: 32
  absolute_lift: 18
  task_scores:
    - task: traffic-drop-without-evidence
      baseline_score: 3
      okb_score: 10
      max_score: 12
    - task: content-optimization-brief
      baseline_score: 6
      okb_score: 10
      max_score: 12
    - task: tool-metric-discrepancy
      baseline_score: 5
      okb_score: 12
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 14/36 to 32/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
timestamp: 2026-07-09T00:00:00Z
---

# SEO Specialist / Consultant

This bundle gives an agent practical role knowledge for source-scoped SEO work: audits, content optimization, search performance diagnosis, and technical triage.

## Core Concepts

- [Role](role.md)
- [Operating Principles](operating-principles.md)
- [SEO Audit Workflow](workflows/seo-audit.md)
- [Content Optimization Workflow](workflows/content-optimization.md)
- [Search Performance Diagnosis](workflows/search-performance-diagnosis.md)
- [SEO Audit Brief](deliverables/seo-audit-brief.md)
- [SEO Quality Check](evaluations/seo-quality-check.md)

## Source Discipline

SEO conclusions depend on source scope. The agent should name the official source category, the user-provided evidence reviewed, and missing evidence before turning a hypothesis into a conclusion.

## Improvement Loop

When users find missing or weak guidance, record private feedback first, then propose reviewed improvements. Public changes should avoid private user context and require approval before contribution.
