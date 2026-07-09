---
type: Example Output
title: Bundle-Assisted Output
okb_bundle_id: zendesk
timestamp: "2026-07-09T00:00:00Z"
---

# Bundle-Assisted Output

Direct answer: there is not enough evidence to design or activate the Zendesk automation yet. I can draft a review plan and evidence request.

Source note: Zendesk source categories needed are Zendesk Help for automations and current automation condition/action behavior, Zendesk Help or account evidence for SLA/routing behavior, and user-provided Admin Center evidence for local fields, organizations, groups, triggers, automations, and notification rules. Missing before action: account configuration, sandbox/test evidence, approver, monitoring, and rollback owner.

Evidence needed:

- How VIP customers are represented: organization, user field, tag, custom field, SLA, or external integration.
- Current ticket statuses, priorities, forms, groups, views, triggers, automations, SLA policies, and notification rules.
- Whether any existing trigger or automation already escalates or notifies on similar criteria.
- Exact support lead destination and whether a notification should be internal-only or customer-facing.
- Test account or sample tickets.

Plan:

1. Inspect current Zendesk Help for automation behavior and account evidence for existing business rules.
2. Map the intended condition, action, timing, and nullifying condition so the automation does not repeatedly fire.
3. Check conflicts with triggers, SLAs, routing, views, and reporting.
4. Test on representative non-production or controlled sample tickets.
5. Require explicit approval before activation.
6. Monitor first runs and roll back if routing, notification, SLA, or customer experience deviates from the acceptance criteria.
