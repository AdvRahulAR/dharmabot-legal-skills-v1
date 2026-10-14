---
name: law-student-case-brief-summariser
description: Produces student case briefs of Indian and leading foreign cases in FIRAC form (facts, issues, rule, analysis, conclusion), separating ratio from obiter, noting dissents and later developments, and offers Socratic drill questions and likely viva or cold-call questions for LLB and LLM students. Use when a law student asks to brief a case for class, prepare for a viva, or be quizzed on a judgment. Do not use for practice-grade case notes for a matter; use judgment-case-note-summariser instead.
---

# Law Student Case Brief Summariser

Every output is a draft study aid for the student to check against the judgment; it is not a substitute for reading it.

## Purpose

Help a student understand a case well enough to explain and defend it in class, a viva or an exam.

## Jurisdiction gate

- Record the court, bench strength and country. Indian cases are explained with their binding value; foreign cases are marked persuasive in India.
- If the course is on foreign law, say the brief follows the judgment's own jurisdiction.

## Required inputs

**Blocking**:
- the case name, and ideally the full text or the citation;
- the course or subject and the point the teacher is focusing on, if known.

If the student gives only a name that could match more than one case, ask which one before briefing.

Also useful: the syllabus, class notes and the reading list edition.

## Method

1. Retrieve the official or reported text of the judgment (court website, a reliable reporter or library database), and record the citation and the date accessed. For very long judgments (for example the Kesavananda Bharati case, decided by a 13-judge bench of the Supreme Court in 1973), say which opinions and paragraphs the brief draws on.
2. Facts: the essential facts and procedural history only.
3. Issues: as the court framed them.
4. Rule: the legal provisions and principles applied.
5. Analysis: the court's reasoning in steps, with paragraph numbers.
6. Conclusion: the holding and the order.
7. Ratio and obiter: separate them and explain the test used. For multi-judge benches, explain how the majority view is identified and where it is contested.
8. Dissents and concurrences: who, and the main point.
9. Later developments: only those the student supplies or that you have read; otherwise say "check later treatment". Never invent subsequent history.
10. Drill mode on request: ask one question at a time, wait for the answer, then give feedback. Mix recall, application and critique questions, and finish with likely viva or cold-call questions.

## Output

1. One-page FIRAC brief with paragraph references.
2. Ratio and obiter table.
3. Ten drill questions with model points (shown after the student answers in drill mode).
4. A "read the original" list of key paragraphs.

## Guardrails and hand-offs

- Do not write graded assignments or case comments for submission as the student's own work; offer feedback instead.
- Never fabricate quotations, paragraph numbers or later cases; tag uncertain points `[verify]`.
- For exam planning, hand off to `law-exam-study-planner`; for practice-grade notes, to `judgment-case-note-summariser`.
