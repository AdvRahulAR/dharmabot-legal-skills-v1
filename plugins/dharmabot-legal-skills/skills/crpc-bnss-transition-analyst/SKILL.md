---
name: crpc-bnss-transition-analyst
description: Works out whether the old codes (IPC, CrPC, Indian Evidence Act) or the new ones (BNS, BNSS, BSA) govern each stage of an Indian criminal matter, from the dates of offence, FIR, investigation, charge-sheet, trial and appeal, applying the repeal and savings provisions. Use when a matter straddles 1 July 2024, when a pleading must cite the right code, or when someone asks "is this under CrPC or BNSS". Do not use for pure section look-ups; use ipc-bns-concordance-mapper.
---

# CrPC–BNSS Transition Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Decide, stage by stage, which substantive, procedural and evidence law applies, and explain why, so pleadings and applications cite the correct provisions.

## Jurisdiction gate

Confirm the proceeding is before an Indian court or authority. Ask whether a special statute with its own procedure applies (for example NDPS, PMLA, POCSO, UAPA), because its own transition rules and its interaction with the general code must then be checked.

## Temporal gate

This skill is the temporal gate for the other criminal skills. The new codes came into force on 1 July 2024, but not every provision did. For example, section 106(2) of the BNS (the hit-and-run offence; believed to be the section, confirm against the official text) and its BNSS First Schedule entry were held back. Before relying on any provision, confirm from the commencement notifications (S.O. 848(E) to 850(E) of 23 February 2024 and any later notification) that it is in force.

## Required inputs

Mark as **blocking**: date (or date range) of the alleged offence; date of registration of the FIR or complaint; and the current stage of the proceeding (investigation, charge-sheet filed, cognizance taken, charge framed, trial, appeal, revision).

Also useful: dates of arrest, charge-sheet, cognizance, framing of charge and judgment; the court; and any earlier order already applying one code or the other.

## Method

1. Retrieve the official text of the repeal and savings provisions of each new statute: the BNS (repeal of the IPC), the BNSS (repeal of the CrPC, believed to be section 531) and the BSA (repeal of the Indian Evidence Act, believed to be section 170). Confirm the section numbers and wording from the source; do not rely on these notes.
2. **Substantive law (offence and punishment).** Start from Article 20(1) of the Constitution: a person cannot be convicted under a law not in force when the act was done, or given a greater penalty than the law then in force allowed. Apply the BNS savings clause to the offence date.
3. **Procedure.** Apply the BNSS savings clause to the stage the matter had reached on 1 July 2024: what was pending then, and which steps came after. Search for, retrieve and cite current Supreme Court and jurisdictional High Court authority on how pending investigations, inquiries, trials and appeals are treated. Present the authority found, with citation and date, and mark it `[verify]` if it could not be read in full.
4. **Evidence.** Apply the BSA savings clause and current authority to evidence led before and after 1 July 2024, especially electronic-record certificates.
5. Build a stage table: stage · date · governing statute · provision relied on · basis (savings clause or authority).
6. Flag every point where authorities conflict or no authority was found. These are points for the advocate to research further.

## Output

1. A one-paragraph conclusion: which code governs each stage.
2. The stage table.
3. The provisions to cite in the next application or pleading, in both old and new numbering where useful (via `ipc-bns-concordance-mapper`).
4. A list of open questions and unverified points.

## Guardrails and hand-offs

- Never assume that a pre-July-2024 offence is wholly governed by the old codes, or that a post-July-2024 FIR is wholly governed by the new ones. Analyse each stage.
- Never invent a judgment, citation or paragraph number. Tag anything not read in full `[verify]`.
- Hand off to `bnss-bail-application-drafter`, `fir-ingredients-analyst` or `bsa-electronic-evidence-certificate-drafter` once the governing law is settled.
