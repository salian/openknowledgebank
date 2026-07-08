---
type: Workflow
title: Research an Accounting Question
description: "Source-aware workflow for turning a U.S. GAAP question into a bounded draft analysis."
tags:
  - accounting-research
  - source-check
okb_bundle_id: us-gaap
timestamp: "2026-07-09T00:00:00Z"
---

# Research an Accounting Question

Use this workflow when the user asks for a U.S. GAAP treatment, accounting-policy view, memo outline, or disclosure analysis.

## Inputs

- Entity type and whether the entity is an SEC registrant.
- Reporting period, fiscal year end, and adoption status for relevant standards.
- Transaction facts and contracts or policy excerpts.
- Relevant ASC topic, paragraph, ASU, or source excerpt if the user has it.
- Materiality context and intended use.

## Process

1. State the accounting question in one sentence.
2. Identify the official source category to inspect: FASB Codification, FASB Accounting Standards Updates, SEC reporting sources, or user-provided policy/workpaper evidence.
3. Separate facts into verified source facts, user-provided facts, assumptions, and missing evidence.
4. Draft a preliminary view only to the level supported by the provided evidence.
5. List the exact evidence needed before final use.
6. Add a professional-review trigger when the output will affect filings, audit support, board materials, lender reporting, investor communication, regulator response, or accounting-policy adoption.

## Output Contract

Include:

- **Source note:** official source category, user-provided evidence, and missing sources.
- **Direct answer:** preliminary answer with confidence level.
- **Verified source facts:** only facts tied to inspected or user-provided source evidence.
- **User-provided facts:** facts supplied by the user.
- **Assumptions:** temporary assumptions used to draft.
- **Needs verification:** source checks required before final use.
- **Analysis:** issue-by-issue reasoning.
- **Professional-review trigger:** when applicable.

## Quality Bar

- Do not invent ASC citations, paragraph text, effective dates, or transition provisions.
- Do not treat an accounting conclusion as final without transaction facts, period, entity status, source evidence, and qualified review.
- If the user asks for a conclusion before source evidence is available, give the best research plan and clearly label any tentative view as unverified.
