---
name: law-exam-study-planner
description: Builds study plans for law semester exams, the All India Bar Examination, State judicial services, CLAT-PG and other law entrance exams from the official syllabus and notification, with outlines, flashcards, MCQs, forecasts from past papers and an interactive tutor mode, updated for the BNS, BNSS, BSA and other recent statutes. Use when a student asks for a study plan, revision timetable, MCQs or flashcards for a law exam. Do not use for briefing a single case; use law-student-case-brief-summariser instead.
---

# Law Exam Study Planner

Every output is a draft study plan for the student to review against the official syllabus and notification.

## Purpose

Give the student a realistic plan tied to the official syllabus, with practice material that reflects the law as it now stands.

## Jurisdiction gate

- Identify the exam and the body that conducts it (university, Bar Council of India, the State Public Service Commission or High Court, the consortium for CLAT-PG).
- For judicial services, the syllabus and local laws differ by State; confirm the State.

## Temporal gate

- Use the syllabus and notification for the current exam cycle, and note its date.
- Many syllabuses moved from the IPC, CrPC and Evidence Act to the BNS, BNSS and BSA, but some papers still test the old codes or both. Follow the official syllabus and say which codes the plan covers.
- Check whether other recent laws in the syllabus (for example the DPDP Act, the Labour Codes, the Income-tax Act 2025) are in force and from when.

## Required inputs

**Blocking**:
- the exam, the year or cycle, and the State for judicial services;
- the exam date (or the number of days available) and hours per day;
- the student's current level and weak subjects.

Also useful: past papers, preferred books, and whether the student wants English or Hindi material.

## Method

1. Retrieve the official syllabus, exam notification and past papers from the conducting body's website, and record the date. If unavailable, say so and do not guess the pattern, marks or negative marking.
2. Map the syllabus into subjects and topics, with weightage from past papers where available.
3. Build the plan in phases: first coverage, then revision, then mock tests. Leave buffer days. Put weak subjects early.
4. For each topic, list the bare Act sections to read (confirm numbers from the Act), leading cases to know, and the time needed.
5. Generate practice material:
   - MCQs with four options, one answer and a short explanation citing the provision (confirm numbers from the text);
   - flashcards for definitions, timelines and landmark cases;
   - short answer prompts for mains.
6. Forecasts: identify topics that recur in past papers. Present them as patterns, not predictions.
7. Tutor mode: ask one question at a time, check the answer, explain, and adjust difficulty.

## Output

1. Calendar plan by week and day.
2. Topic checklist with weightage.
3. MCQ set with answers and explanations.
4. Flashcards.
5. Revision and mock-test schedule.

## Guardrails and hand-offs

- Never claim access to unpublished or leaked papers.
- Never state exam rules, marks or cut-offs without the official notification.
- Flag any MCQ that relies on a provision not yet verified `[verify]`.
- For old-to-new code mapping, hand off to `ipc-bns-concordance-mapper`; for case briefs, to `law-student-case-brief-summariser`.
