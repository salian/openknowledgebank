---
type: Workflow
title: OSHA Obligation Triage
description: Source-aware workflow for turning an OSHA question into an evidence-backed compliance brief.
tags:
  - osha
  - triage
  - compliance
okb_bundle_id: osha
timestamp: "2026-07-09T00:00:00Z"
---

# OSHA Obligation Triage

Use this workflow when the user asks whether OSHA applies, what standard or source family is triggered, whether something is recordable or reportable, or what to do next.

## Inputs

- User question and intended decision.
- Jurisdiction, state-plan, employer, establishment, industry, worksite, and worker facts.
- Task, process, equipment, chemical, exposure, injury/illness, inspection, citation, policy, training, or control evidence.
- Current official sources from OSHA, DOL, eCFR, Federal Register, state-plan authorities, or another relevant official source.

## Output Contract

The final answer should include:

- **Direct answer:** state the likely OSHA issue and whether the conclusion is verified, provisional, or blocked.
- **Source note:** name the official source category, user-provided evidence, and missing source or fact.
- **Source-family classification:** map the issue to federal OSHA, state plan, general duty, Part 1904, Part 1910, Part 1926, poster, HazCom, enforcement, or hazard-specific sources.
- **Verified facts:** list what was checked against official sources.
- **User-provided facts:** list facts supplied by the user.
- **Assumptions:** label draft assumptions clearly.
- **Missing evidence:** name what blocks a conclusion.
- **Next steps:** identify source inspection, evidence collection, professional review, or operational action.

## Triage Steps

1. Classify the question using [source-and-standard-map.md](../requirements/source-and-standard-map.md).
2. Check whether federal OSHA or a state-plan source must govern the answer.
3. Ask for only the minimum workplace, hazard, incident, or policy evidence needed; avoid collecting unnecessary personal or medical details.
4. Separate source-confirmed facts from user facts and assumptions.
5. Produce a brief using [source-aware-osha-compliance-brief.md](../deliverables/source-aware-osha-compliance-brief.md).
6. Mark any legal, regulatory, reporting, citation, enforcement, safety-control, medical, or live-system action as requiring professional review and explicit user confirmation.

## Quality Bar

A good answer does not guess applicability, recordability, reportability, exposure limits, controls, penalties, abatement, or deadlines. It states what can be concluded from inspected sources and provided evidence, then names the missing evidence needed before relying on the answer.
