---
name: rera-project-compliance-checker
description: Checks a promoter's or real estate agent's obligations under the Real Estate (Regulation and Development) Act, 2016 and the State RERA rules, covering project registration, the separate account and withdrawals, advertisements, quarterly updates, the model agreement for sale, carpet-area pricing, defect liability, extensions and agent registration, and builds a gap list and compliance calendar. Use when a developer asks for a RERA launch check, a pre-advertisement review, or an audit of an ongoing project. Do not use for an allottee's complaint; use rera-complaint-drafter.
---

# RERA Project Compliance Checker

Every output is a draft review for an advocate enrolled in India to check.

## Purpose

Tell a promoter or agent what RERA requires of this project in this State, what is already done, what is missing, and when each recurring obligation falls due.

## Jurisdiction gate

Record the State or UT and the planning area. RERA rules, forms, fees, the model agreement, and update frequencies vary by State. Confirm whether the project needs registration at all (thresholds on land area or number of units, believed to be in section 3; confirm), or falls under an exemption.

## Required inputs

Mark as **blocking**:
- State, project type (residential, commercial, plotted, mixed) and phase;
- land title and development rights (own land, JDA, lease);
- sanctioned plans and approvals obtained;
- launch status (pre-launch, launched, ongoing, completed) and whether any booking or advertisement has happened.

Also useful: the draft agreement for sale and allotment letter, brochures and advertisements, bank account set-up, chartered accountant and engineer certificates, agent agreements.

## Method

1. Retrieve the current official text of the Real Estate (Regulation and Development) Act, 2016, the State rules and regulations, the State model agreement for sale and the Authority's circulars. Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Registration: confirm it is obtained before any advertisement, marketing, booking or sale. List the documents filed and gaps.
3. Separate account: check the proportion of receipts to be deposited (commonly stated as 70%; confirm) and the certification needed for each withdrawal (engineer, architect, chartered accountant).
4. Advertisements: RERA number and website on every advertisement; no misleading claims; hand off broader claims review if needed.
5. Agreement for sale: compare with the State model and flag deviations; no more than the permitted advance before a registered agreement (confirm the percentage). Hand off detailed review to `builder-buyer-agreement-reviewer`.
6. Pricing on carpet area as defined in the Act; no sale on super built-up area.
7. Continuing duties: periodic updates on the Authority's website, annual audited accounts, structural defect liability, formation of the association, conveyance to allottees and the association, and extension of registration before expiry.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
8. Agents: registration of each agent and the promoter's duty to deal only with registered agents.
9. Put recurring dates into a calendar with `compliance-calendar-builder`.

## Output

1. Gap table: obligation · source provision · status · action · owner · deadline.
2. Compliance calendar.
3. Red-flag note on anything that could attract penalties or deregistration.

## Guardrails

- Never state penalty amounts or deadlines from memory.
- Never advise marketing before registration or ways to avoid the separate account.
- Rely only on documents supplied; do not certify approvals not seen.
