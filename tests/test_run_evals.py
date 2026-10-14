"""Tests for scripts/run_evals.py: parsing, selection and reporting. No network, no Claude calls."""

import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("run_evals", ROOT / "scripts" / "run_evals.py")
run_evals = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run_evals)


def ev(**kw):
    return json.dumps(kw)


STREAM = [
    ev(type="system", subtype="init"),
    ev(type="assistant", message={"content": [
        {"type": "tool_use", "name": "Skill", "input": {"skill": "dharmabot-legal-skills:limitation-calculator"}}]}),
    ev(type="assistant", message={"content": [
        {"type": "tool_use", "name": "Bash", "input": {"command": "py scripts/date_calc.py --start 2026-07-14 --to 2026-10-15"}}]}),
    ev(type="user", message={"content": [
        {"type": "tool_result", "is_error": True, "content": "Python was not found"}]}),
    ev(type="user", message={"content": [
        {"type": "tool_result", "is_error": False, "content": "93 days"}]}),
    "not json at all",
    ev(type="result", result="It is 93 days.", total_cost_usd=0.25, num_turns=4, is_error=False),
]


class ParseTests(unittest.TestCase):
    def test_parse_transcript(self):
        info = run_evals.parse_transcript(STREAM)
        self.assertEqual(info["skills"], ["dharmabot-legal-skills:limitation-calculator"])
        self.assertEqual(len(info["commands"]), 1)
        self.assertEqual(len(info["errors"]), 1)
        self.assertEqual(info["answer"], "It is 93 days.")
        self.assertEqual(info["turns"], 4)
        self.assertAlmostEqual(info["cost"], 0.25)

    def test_empty_transcript(self):
        info = run_evals.parse_transcript([])
        self.assertEqual(info["skills"], [])
        self.assertEqual(info["answer"], "")

    def test_skill_fired_matches_plugin_prefix(self):
        used = ["dharmabot-legal-skills:limitation-calculator"]
        self.assertTrue(run_evals.skill_fired(used, "limitation-calculator"))
        self.assertFalse(run_evals.skill_fired(used, "calculator"))
        self.assertFalse(run_evals.skill_fired([], "limitation-calculator"))


class SelectionTests(unittest.TestCase):
    def setUp(self):
        self.cases = run_evals.load_cases()
        self.pack_map = run_evals.load_pack_map()

    def test_every_case_names_a_known_skill(self):
        for c in self.cases:
            self.assertIn(c["skill"], self.pack_map, c["id"])

    def test_select_by_pack(self):
        picked = run_evals.select_cases(self.cases, self.pack_map, packs={"core"})
        self.assertTrue(picked)
        self.assertTrue(all(self.pack_map[c["skill"]] == "core" for c in picked))

    def test_select_by_id(self):
        picked = run_evals.select_cases(self.cases, self.pack_map, ids={"bail-date-mismatch"})
        self.assertEqual([c["id"] for c in picked], ["bail-date-mismatch"])

    def test_should_trigger_defaults(self):
        self.assertTrue(run_evals.should_trigger({"skill": "a-b-checker", "must_not": []}))
        self.assertFalse(run_evals.should_trigger({"skill": "a-b-checker", "should_trigger": False}))
        self.assertFalse(run_evals.should_trigger({"skill": "a-b-checker", "must_not": ["uses a-b-checker"]}))

    def test_trigger_cases_state_should_trigger(self):
        for c in self.cases:
            if c["kind"] == "trigger" and c["id"] in {
                "limitation-trigger-hours", "limitation-trigger-near-miss", "data-breach-trigger-within-time",
                "data-breach-trigger-near-miss", "it-rules-trigger-takedown-deadline", "it-rules-trigger-near-miss",
            }:
                self.assertIn("should_trigger", c, c["id"])


class ReportTests(unittest.TestCase):
    RESULTS = [
        {"id": "a", "pack": "core", "skill": "s1", "kind": "output", "passed": True, "trigger_ok": True,
         "expected_trigger": True, "skills_used": ["s1"], "status": 0, "items": [], "cost_run": 0.2, "cost_grade": 0.02},
        {"id": "b", "pack": "core", "skill": "s1", "kind": "gate", "passed": False, "trigger_ok": False,
         "expected_trigger": True, "skills_used": [], "status": 0,
         "items": [{"kind": "must", "text": "flags the mismatch", "pass": False, "reason": "did not say so"}],
         "cost_run": 0.1, "cost_grade": 0.01},
    ]

    def test_summary_totals(self):
        s = run_evals.summarise(self.RESULTS)
        self.assertEqual((s["total"], s["passed"], s["failed"]), (2, 1, 1))
        self.assertEqual(s["trigger_failures"], 1)
        self.assertEqual(s["by"]["pack"]["core"], [2, 1])
        self.assertAlmostEqual(s["cost"], 0.33)

    def test_report_lists_failure_reason(self):
        s = run_evals.summarise(self.RESULTS)
        md = run_evals.report_md(self.RESULTS, s, {"started": "now", "claude_version": "x", "model": None,
                                                    "grader_model": "sonnet"})
        self.assertIn("1 of 2 cases passed (50%)", md)
        self.assertIn("did not fire", md)
        self.assertIn("flags the mismatch", md)


if __name__ == "__main__":
    unittest.main()
