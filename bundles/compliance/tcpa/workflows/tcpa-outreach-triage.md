---
type: Workflow
title: TCPA Outreach Triage
description: Triage a call, text, robocall, robotext, or fax scenario with source discipline before any compliance conclusion.
tags:
  - tcpa
  - workflow
  - triage
  - consent
  - do-not-call
okb_bundle_id: tcpa
inputs:
  - outreach channel and purpose
  - message, script, or fax copy
  - consent evidence
  - revocation and suppression evidence
  - DNC screening evidence when telemarketing may be involved
  - vendor and platform evidence
outputs:
  - source-aware TCPA compliance brief
timestamp: "2026-07-08T23:17:15Z"
---

# TCPA Outreach Triage

Use this workflow to structure a TCPA-sensitive answer. It is a review workflow, not authorization to place calls, send texts, send faxes, or change live outreach systems.

## 1. Classify The Outreach

Identify the channel and purpose:

- live call;
- prerecorded or artificial voice call;
- autodialed call;
- text or SMS/MMS message;
- fax advertisement;
- mixed workflow;
- marketing, sales, service, reminder, informational, survey, emergency, debt collection, or another stated purpose.

If the channel, purpose, sender, recipient, or number type is unclear, treat the conclusion as blocked until the user provides evidence.

## 2. Name The Source Categories

Prepare a visible **Source note** that names the source categories checked or still needed:

- FCC TCPA and robocall/robotext guidance;
- current eCFR 47 CFR 64.1200;
- current 47 U.S.C. Section 227 text when statutory language matters;
- FTC Telemarketing Sales Rule and National Do Not Call sources when telemarketing or DNC issues are relevant;
- current state, sector, platform, carrier, privacy, or contract sources when the scenario may trigger them;
- user-provided consent, revocation, DNC, vendor, platform, and campaign evidence.

Do not present a final legal conclusion from memory.

## 3. Build The Evidence Matrix

Separate facts into four buckets:

| Bucket | Examples |
| --- | --- |
| Verified from source | Current official source excerpts or citations inspected for this answer |
| Provided by user | Consent record, web form, call recording, lead source, message copy, STOP logs, DNC screen, vendor contract, platform setting |
| Assumed for draft | Temporary assumptions used only to explain what would matter |
| Needs verification | Any missing official source, consent scope, revocation status, number type, recipient relationship, exemption claim, state-law issue, or platform capability |

## 4. Check High-Risk Issues

Do not decide compliance until the answer addresses:

- whether the outreach is marketing, informational, service-related, emergency, fax advertising, or another category;
- whether the technology used matters under the current FCC source;
- who is the seller, caller, texter, sender, lead generator, agency, or platform operator;
- whether consent exists, what it covered, who obtained it, when it was obtained, and whether it was revoked;
- whether National DNC, internal DNC, state DNC, and suppression requirements have been checked where relevant;
- whether the message/script/fax contains required identity, opt-out, or disclosure elements under the current source;
- whether vendor contracts and platform settings align with the claimed compliance process.

## 5. Give A Direct But Bounded Answer

Answer the user's question directly, but do not overstate certainty. Good answer patterns include:

- "Based on the evidence provided, this is not ready for a compliance conclusion because..."
- "This appears to raise TCPA and related telemarketing issues; the next source and evidence checks are..."
- "If the current official source and the missing records confirm X, the risk analysis may change, but that is not verified here."

## 6. Require Confirmation For Risky Actions

Before any action that places calls, sends texts, sends faxes, uploads lists, changes consent capture, changes suppression logic, exports contacts, contacts regulators, or sends legal communications, require explicit user confirmation and professional review.

## Output Contract

The final output should include:

- direct answer and confidence level;
- Source note;
- outreach scope;
- evidence provided;
- missing evidence;
- source-grounded issues;
- adjacent source checks;
- risk boundary;
- next checks before any risky action.

## Related

- [Source-Aware TCPA Compliance Brief](../deliverables/source-aware-tcpa-compliance-brief.md)
- [TCPA Source-Awareness Check](../evaluations/tcpa-source-awareness-check.md)
- [References](../references/index.md)
