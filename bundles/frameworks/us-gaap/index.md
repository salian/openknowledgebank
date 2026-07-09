---
type: Bundle Index
title: US GAAP
description: "Framework hub bundle for source-aware U.S. GAAP research, accounting-policy memos, and GAAP-versus-non-GAAP reconciliation without inventing accounting citations or entity-specific conclusions."
schema_version: 0.1.0
bundle_format: okf-compatible
category: frameworks
tags:
  - us-gaap
  - accounting
  - financial-reporting
  - fasb
  - sec-reporting
aliases:
  - U.S. GAAP
  - Generally Accepted Accounting Principles
  - Generally Accepted Accounting Principles (US)
  - FASB GAAP
problems_solved:
  - Structure source-aware U.S. GAAP research questions.
  - Draft accounting research memos that separate verified source facts, user-provided facts, assumptions, and open verification items.
  - Review GAAP versus non-GAAP reconciliation questions without treating either number as automatically correct.
  - Prevent invented ASC citations, effective dates, disclosure requirements, and entity-specific accounting conclusions.
industries:
  - cross-industry
  - finance
  - accounting
  - public-company-reporting
tools:
  - FASB Accounting Standards Codification
  - FASB Accounting Standards Updates
  - SEC EDGAR
frameworks:
  - US GAAP
  - FASB Accounting Standards Codification
deliverables:
  - Accounting research memo
commands: []
skills: []
evaluations:
  - GAAP source awareness check
okb_bundle_version: 0.1.0
trust_tier: trusted
status: blocked
license: CC-BY-4.0
related_bundles: []
adjacent_bundles:
  - sox
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
  - "Not professional accounting, audit, tax, legal, securities, valuation, or investment advice."
  - "Does not reproduce FASB Codification text or replace inspection of current authoritative sources."
  - "Requires user-provided transaction facts, reporting period, entity status, policy elections, and source excerpts before final conclusions."
  - "Governmental accounting standards issued by GASB are out of scope."
safety_notes:
  - "Require qualified professional review before filing, audit support, board approval, lender delivery, investor communication, regulator response, or accounting-policy adoption."
  - "Do not claim access to Codification, EDGAR filings, contracts, workpapers, accounting systems, or auditor files unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: blocked
  last_evaluated: null
  method: baseline-vs-okb-rubric
  tasks_count: 3
  display_summary: "Measured evaluation model outputs have been generated; publication is blocked until reviewer scoring, aggregate scores, and a public-safe listing scorecard are completed."
  evidence_note: "No measured score is claimed yet. Baseline and OKB-assisted model outputs exist in the private run; reviewed aggregate scores and listing scorecard are pending."
okb_bundle_id: us-gaap
timestamp: "2026-07-09T00:00:00Z"
---

# US GAAP

This bundle helps an agent handle U.S. GAAP as a source-sensitive financial-reporting framework. It is designed for research planning, accounting-policy memo drafting, and GAAP-versus-non-GAAP reconciliation while keeping authoritative sources, local facts, assumptions, and professional-review needs explicit.

## Required Answer Habit

For U.S. GAAP work, include a short **Source note** naming the official source category used, the user-provided local evidence used, and missing source evidence required before a draft analysis becomes a conclusion.

## Start Here

- [framework.md](framework.md)
- [workflows/research-accounting-question.md](workflows/research-accounting-question.md)
- [workflows/reconcile-gaap-non-gaap.md](workflows/reconcile-gaap-non-gaap.md)
- [deliverables/accounting-research-memo.md](deliverables/accounting-research-memo.md)
- [evaluations/gaap-source-awareness-check.md](evaluations/gaap-source-awareness-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use FASB Codification and FASB Accounting Standards Updates for nongovernmental U.S. GAAP research. Use SEC reporting sources for registrant disclosure and non-GAAP presentation context. Use user-provided evidence for entity status, reporting period, transaction facts, policy elections, materiality, disclosures, workpapers, and auditor or regulator positions.
