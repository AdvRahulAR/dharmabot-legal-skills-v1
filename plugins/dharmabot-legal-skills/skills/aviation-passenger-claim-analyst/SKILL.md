---
name: aviation-passenger-claim-analyst
description: Analyses air passenger claims and aviation regulatory issues in India, covering airline liability under the Carriage by Air Act 1972 (Montreal Convention limits for delay, baggage and injury), DGCA Civil Aviation Requirements on denied boarding, cancellation, delay and passengers with disabilities, consumer remedies, and operator questions such as permits, aircraft leasing and Cape Town Convention implementation. Use when a flight was cancelled or delayed, baggage was lost, or a passenger was injured. Do not use to draft the consumer complaint; use consumer-complaint-drafter.
---

# Aviation Passenger Claim Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Identify what the passenger can claim, from whom, under which regime, and within what time.

## Jurisdiction gate

Identify the itinerary (domestic or international, origin and destination, stopovers), the operating and marketing carriers, and where the ticket was bought. The Carriage by Air Act applies different schedules depending on whether the journey is international and which convention the States involved have ratified. Foreign passenger-rights rules (for example EU or UK rules) may also apply; mark those "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

The Bharatiya Vayuyan Adhiniyam 2024 replaced the Aircraft Act 1934, and a 2025 Act implements the Cape Town Convention for aircraft objects. DGCA passenger-rights requirements are revised from time to time. Check commencement and the version in force on the date of travel.

## Required inputs

Mark as **blocking**:
- the ticket or booking, with flight numbers and dates;
- what happened (denied boarding, cancellation, delay length, baggage lost, damaged or delayed, injury);
- whether the passenger gave written notice to the airline, and when.

Also useful: boarding passes, property irregularity report, receipts for expenses, airline correspondence, and medical records for injury.

## Method

1. Retrieve the current official text of the Carriage by Air Act and its schedules, the current DGCA CAR on facilities to passengers affected by denied boarding, cancellation and delay, the CAR on persons with disabilities, and the Consumer Protection Act. Record versions and dates.
2. Classify the journey and the applicable schedule. Identify the carrier liable.
3. Map claims:
   - **Baggage**: destruction, loss, damage or delay; written complaint time limits; liability limits in Special Drawing Rights, revised periodically (retrieve the current figures).
   - **Delay**: proven damage, subject to limits and the carrier's reasonable-measures defence.
   - **Injury or death**: strict liability tier and fault-based tier above it.
   - **DGCA compensation and facilities**: refunds, meals, hotel, and fixed compensation by block time, with exceptions for extraordinary circumstances.
4. Check time limits: the two-year limit to bring an action under the Montreal regime, and short complaint periods for baggage. Compute with `limitation-calculator`.
5. Choose remedies: airline grievance, AirSewa, consumer commission, or civil suit. Note whether convention limits bind the consumer forum; search for and read current authority.
6. For operator questions (permits, leasing, deregistration and repossession), outline the regulatory steps and refer filings to `licence-application-drafter`.
7. Tag anything not read in full `[verify]`.

## Output

1. A claims table: head · regime · conditions · limit (to confirm) · evidence.
2. Deadlines and the recommended forum.
3. A draft notice or grievance to the airline, if asked.

## Guardrails and hand-offs

- Never state SDR limits or DGCA compensation figures from memory.
- Never advise inflating losses.
- For the consumer complaint, hand off to `consumer-complaint-drafter`.
- Before delivery, send citations to `citation-verifier`.
