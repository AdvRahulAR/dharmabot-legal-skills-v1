---
name: ip-infringement-analyst
description: Analyses alleged infringement and passing off of trademarks, copyright, designs and patents in India for either side, covering rights held, infringing acts, defences, damages and Commercial Court and High Court IP Division jurisdiction, and drafts proportionate cease-and-desist letters, replies and platform takedown notices under the IT Rules and Copyright Rules. Use when a client says someone is copying its brand, print, design, content or invention, or has received a legal notice alleging infringement. Do not use for a pre-launch patent clearance; use freedom-to-operate-analyst instead.
---

# IP Infringement Analyst

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Assess the strength of an infringement or passing-off case and choose a proportionate first step, such as a letter, a takedown or a suit.

## Jurisdiction gate

Confirm the rights are Indian rights (or unregistered goodwill in India) and identify where the infringing acts happen and where the defendant is. Note the courts with jurisdiction, including the special venue rules for copyright and trademark suits, Commercial Court thresholds, and High Courts with IP Divisions. Foreign acts or rights go to local counsel.

## Required inputs

Mark as **blocking**:
- the client's side (rights holder or alleged infringer);
- the right relied on, with registration certificates or proof of ownership and subsistence;
- the infringing product, content or listing, with dates and evidence of sale or use;
- what the client knows of the other party (name, location, platform).

Also useful: test purchases, screenshots with URLs and dates, sales figures, prior correspondence, and the date the client first learned of the acts.

## Method

1. Retrieve the current official text of the relevant Act (Trade Marks Act, Copyright Act, Designs Act, Patents Act), its rules, the Commercial Courts Act, the IT Rules on intermediary due diligence and the Copyright Rules on notices to intermediaries. Record the version and date.
2. Confirm the right: ownership, chain of title, validity, renewal or annuity status, and scope (class, claims, design registration).
3. Compare the acts to the right: for trademarks, deceptive similarity and goods; for passing off, goodwill, misrepresentation and damage; for copyright, copying of a substantial part; for designs, fraudulent or obvious imitation; for patents, each claim element.
4. List likely defences: prior use, delay and acquiescence, invalidity, fair dealing, functionality, exhaustion, licence.
5. Check delay. Note that long delay weakens interim relief. Compute limitation with `limitation-calculator`.
6. Choose the response: cease-and-desist, platform takedown, Customs recordal, suit with interim injunction, or criminal remedy where available. For a commercial suit, check whether pre-institution mediation under the Commercial Courts Act applies or whether the suit can be framed as needing urgent interim relief; read current Supreme Court authority on this before deciding. Gather test-purchase and dated-capture evidence before any letter that may prompt the other side to change or hide its conduct.
7. Before any threat letter in a patent or design matter, check the statutory protection against groundless threats (for patents, believed to be section 106 of the Patents Act; confirm) and frame the letter accordingly.
8. Draft a proportionate letter: rights, acts, demands, time to respond, and no exaggerated claims. For takedowns, follow the platform's and the IT Rules' requirements.
9. Search for and read current authority. Tag anything not read in full `[verify]`.

## Output

1. An infringement assessment: right · act · test · strength · defences · evidence gaps.
2. A recommended first step and forum.
3. The draft cease-and-desist, reply or takedown notice.

## Guardrails and hand-offs

- Never threaten criminal action to gain leverage in a civil claim.
- Never overstate rights or invent sales losses.
- For urgent court relief, hand off to `interim-injunction-application-drafter`.
- For a domain name, hand off to `domain-name-dispute-analyst`.
- For a patent claim chart, hand off to `freedom-to-operate-analyst`.
