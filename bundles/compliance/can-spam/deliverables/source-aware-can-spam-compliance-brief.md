---
type: Deliverable
title: Source-Aware CAN-SPAM Compliance Brief
description: Review-ready brief format for CAN-SPAM questions that separates official sources, campaign evidence, assumptions, and missing evidence.
okb_bundle_id: can-spam
required_inputs:
  - user question and intended decision
  - current official CAN-SPAM source categories
  - user-provided campaign and suppression evidence
outputs:
  - direct answer
  - source note
  - evidence table
  - issue classification
  - missing evidence
  - risk boundary
  - next steps
quality_criteria:
  - separates official-source facts, user facts, assumptions, and missing evidence
  - avoids final legal or send-readiness conclusions from incomplete facts
  - requires professional review and explicit confirmation for risky actions
timestamp: "2026-07-08T22:23:14Z"
---

# Source-Aware CAN-SPAM Compliance Brief

Use this deliverable when the user needs a concise CAN-SPAM analysis for review.

## Required Sections

### Direct Answer

State the likely issue, the confidence level, and whether the answer is a triage view or a reliance-ready conclusion. Most outputs should be triage unless current official sources and user evidence have both been inspected.

### Source Note

Name:

- the official FTC, statutory, or regulatory source category used;
- the user-provided campaign, list, sender, opt-out, or suppression evidence used for this specific answer;
- any missing source or fact still needed before the answer can be relied on;
- any adjacent law, platform, state, sector, or international issue that was not analyzed.

### Evidence Table

| Claim | Status | Source or Evidence | Caveat |
| --- | --- | --- | --- |
| Official-source fact | Verified / needs verification | FTC guidance, eCFR Part 316, U.S. Code, or GovInfo | Include date or version when available |
| Campaign fact | Provided / missing | Email copy, header, ESP screenshot, suppression export, policy, contract, or user statement | Identify owner or freshness when known |
| Draft assumption | Assumed | Stated assumption | Do not treat as conclusion |

### Issue Classification

Classify the issue. Explain whether it concerns commercial/transactional purpose, sender identity, subject line, ad identification, physical address, opt-out mechanism, opt-out timing, suppression-list use, third-party sender responsibility, sexually oriented material labeling, enforcement risk, or an adjacent issue.

### Missing Evidence

List missing official sources, user documents, technical evidence, or business facts. If exact timing, statutory section, rule text, penalty amount, exemption, or message classification matters, require current source inspection.

### Risk Boundary

State whether professional legal or compliance review is required before reliance. Require explicit user confirmation before any email send, campaign edit, list upload, contact export, suppression-list change, unsubscribe-flow change, vendor instruction, or legal communication.

### Next Steps

Give the smallest useful next actions: inspect source, collect evidence, verify implementation, prepare reviewer questions, pause a risky send, or draft a review packet.

## Quality Bar

The brief should be useful to a legal or compliance reviewer because it exposes source status and evidence gaps. It should not sound more certain than the inspected sources and user evidence support.
