---
type: Example Output
title: Bundle-Assisted Output
okb_bundle_id: docusign
timestamp: "2026-07-09T00:00:00Z"
---

# Bundle-Assisted Output

## Direct Answer

We can plan the change, but we are not ready to modify the DocuSign template or CRM sync until the current template, recipient/routing, permissions, legal/compliance requirements, and integration behavior are verified.

## Source Note

Source note: DocuSign guidance should be checked against current DocuSign Support Center guidance for templates/sending and DocuSign Developer Center or eSignature REST API sources for status/integration behavior. Local evidence used: none provided. Missing before action or conclusion: template export or screenshots, recipient roles and signing order, field map, account permissions, legal/compliance approval requirements, CRM integration configuration, sandbox/test evidence, owner approval, and rollback plan.

## Evidence Needed

- Current MSA template name or export, documents, roles, recipients, routing/signing order, tabs/fields, notifications, reminders, expirations, and brand settings.
- Whether finance approval is a signer, approver, carbon-copy recipient, internal process step, or separate workflow requirement.
- Who owns the template and who can approve changes.
- CRM integration design: source environment, target object/field, status mapping, webhook/API/sync mechanism, authentication owner, logs, and reconciliation report.
- Legal/compliance/privacy/retention requirements for MSA routing and audit evidence.

## Proposed Plan

1. Verify current DocuSign template and account evidence.
2. Decide the finance approval model with legal, finance, sales operations, and DocuSign account owners.
3. Draft a recipient/routing and field map that labels all assumptions.
4. Test with a non-customer test envelope or sandbox/demo evidence where available.
5. Verify the CRM status sync against current DocuSign developer sources and the actual CRM integration configuration.
6. Prepare production rollout only after owner approval.

## Risk and Confirmation Boundary

Explicit confirmation is required before changing the live MSA template, sending envelopes, notifying recipients, changing recipient/routing/field behavior, exporting agreement data, activating webhook/API changes, or changing CRM production sync behavior.

## Validation and Rollback

Use a test envelope, recipient preview, status/report reconciliation, CRM test record, log review, and owner signoff. Roll back by restoring the previous template version or routing configuration and disabling or reverting the CRM sync change if monitored results diverge from expected status behavior.
