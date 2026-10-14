# Workflows

Workflow recipes chain several skills from this collection for a common Indian matter. Each recipe lists the skills in the order to run them, what to give each skill, what it hands back, and the STOP checkpoints where the advocate must review and approve before the next step.

You can follow a recipe by hand, one skill at a time, or ask `legal-task-router` to run it: "Follow workflows/cheque-dishonour-section-138.md for this matter."

## Rules every recipe follows

- **Limitation first.** Every deadline is computed with `limitation-calculator`, with working shown, and entered in `matter-deadline-tracker`. Do not rely on a period quoted in a recipe; recipes deliberately avoid stating periods or section numbers as settled.
- **STOP means stop.** At each STOP the skill hands back a draft or a decision for the advocate. Nothing moves on until the advocate approves, edits or rejects it.
- **Redact if your profile says so.** If `templates/dharmabot-profile.md` sets redaction to yes, run `client-data-redaction-checker` before any client document is processed.
- **Verify before filing.** The last step of every recipe that ends in a filing, notice or signed document is `pre-filing-verification-checker`. It checks authorities, facts and figures and signs a verification log.
- Every output is a draft for an enrolled advocate. See [DISCLAIMER.md](../DISCLAIMER.md).

## Recipes

| Recipe | Use it for |
| --- | --- |
| [civil-suit-to-first-hearing](civil-suit-to-first-hearing.md) | Taking a plaintiff's civil or commercial suit from intake to the first hearing |
| [defending-a-civil-suit](defending-a-civil-suit.md) | Defendant served with summons: written statement within time and interim applications |
| [arrest-to-bail-to-trial](arrest-to-bail-to-trial.md) | Accused from arrest through bail, chargesheet, discharge and trial preparation |
| [cheque-dishonour-section-138](cheque-dishonour-section-138.md) | Payee of a dishonoured cheque: notice, complaint and interim compensation |
| [gst-notice-to-appeal](gst-notice-to-appeal.md) | GST show-cause notice through reply, order and first appeal |
| [commercial-contract-review-and-negotiation](commercial-contract-review-and-negotiation.md) | Reviewing, negotiating and signing a commercial contract |
| [startup-fundraise](startup-fundraise.md) | Priced or convertible round: term sheet to closing filings |
| [property-purchase-due-diligence](property-purchase-due-diligence.md) | Buyer-side diligence and documentation for immovable property |
| [employee-termination-and-dispute](employee-termination-and-dispute.md) | Employer planning an exit, and any dispute that follows |
| [cross-border-dispute-and-enforcement](cross-border-dispute-and-enforcement.md) | Dispute with a foreign party, through to enforcement in India |

## Contributing a recipe

Use only skill ids that exist in this collection, keep each recipe between 30 and 60 lines, put a STOP before every draft that will leave the firm, and end with `pre-filing-verification-checker`. See [CONTRIBUTING.md](../CONTRIBUTING.md).
