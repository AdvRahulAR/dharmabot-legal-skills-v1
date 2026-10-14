---
name: witness-protection-application-drafter
description: Drafts witness protection applications to the Competent Authority under the Witness Protection Scheme, 2018 approved by the Supreme Court, and under any State scheme notified under the Bharatiya Nagarik Suraksha Sanhita, 2023, with threat-analysis inputs, measures sought (identity protection, in-camera trial, relocation, escort) and confidentiality. Use when a witness in a criminal trial is being threatened, followed or pressured and the advocate wants protection orders. Do not use to draft a fresh complaint about the threats; use criminal-complaint-drafter.
---

# Witness Protection Application Drafter

Every output is a draft for an advocate or public prosecutor in India to check and sign.

## Purpose

Get protection for a threatened witness quickly, with a confidential application that gives the Competent Authority what it needs to order a threat analysis and interim measures.

## Jurisdiction gate

Confirm the case is pending investigation or trial in India and record the State and district. Identify the scheme that applies: the State's own scheme notified under the BNSS (believed to be section 398; confirm) or the 2018 scheme approved in Mahender Chawla v. Union of India (Supreme Court, 2018; confirm current treatment). Identify the Competent Authority in that district.

## Temporal gate

Record the date of the FIR. If it predates 1 July 2024, check whether the State scheme or the 2018 scheme applies, and confirm with `crpc-bnss-transition-analyst`.

## Required inputs

Mark as **blocking**:
- the case number, court, offences and stage;
- the witness's role and why the evidence matters;
- each threat with date, mode (call, visit, social media), and who made it, as the witness reports it;
- any complaint already made to the police.

Also useful: call logs or screenshots, the witness's family and work circumstances, and the protection the witness actually wants.

## Method

1. Retrieve the current official text of the State's witness protection scheme (or the 2018 scheme), its forms and categories, and the BNSS provisions on evidence through video and in-camera trial. Record the source and date.
2. Classify the threat category under the scheme from the facts supplied. Do not overstate it.
3. Draft the application in the scheme's form. Ask for an urgent threat analysis report and interim protection.
4. List measures sought in order of need: monitoring of calls, change of phone number, escort, identity protection, testimony by video or with screens, in-camera hearing, and relocation.
5. Mark the application and annexures confidential. Recommend sealed filing and limited copies.
6. Note related steps: a complaint about the threats (hand to `criminal-complaint-drafter`), and a cancellation of bail plea if the accused is on bail.
7. For a child witness, hand child-specific safeguards to `pocso-case-analyst`.

## Output

1. Witness protection application with a confidential annexure of threats.
2. Interim protection request.
3. A note of related steps and who acts.

## Guardrails and hand-offs

- Never invent or enlarge threats; use the witness's account and evidence only.
- Never disclose the witness's identity or address beyond what filing requires.
- The prosecutor, advocate or witness files; this skill only drafts.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
