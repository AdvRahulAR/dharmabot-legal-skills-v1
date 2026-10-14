"""Unit tests for the bundled skill scripts. Run: python3 -m unittest discover tests"""

import datetime as dt
import importlib.util
import pathlib
import unittest

SKILLS = pathlib.Path(__file__).resolve().parent.parent / "plugins" / "dharmabot-legal-skills" / "skills"


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, SKILLS / rel)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


date_calc = load("date_calc", "limitation-calculator/scripts/date_calc.py")
check_quote = load("check_quote", "citation-verifier/scripts/check_quote.py")
D = dt.date


class DateCalcTests(unittest.TestCase):
    def last(self, *args, **kwargs):
        return date_calc.compute(*args, **kwargs)["last_day"]

    def test_days_exclude_start(self):
        # 30 days from 1 Jan: the period runs 2 Jan to 31 Jan.
        self.assertEqual(self.last(D(2026, 1, 1), "30d"), "2026-01-31")

    def test_days_include_start(self):
        self.assertEqual(self.last(D(2026, 1, 1), "30d", include_start=True), "2026-01-30")

    def test_ninety_days(self):
        self.assertEqual(self.last(D(2026, 3, 10), "90d"), "2026-06-08")

    def test_months_same_date(self):
        self.assertEqual(self.last(D(2026, 3, 10), "3m"), "2026-06-10")

    def test_months_end_of_short_month(self):
        self.assertEqual(self.last(D(2026, 1, 31), "1m"), "2026-02-28")
        self.assertEqual(self.last(D(2028, 1, 31), "1m"), "2028-02-29")

    def test_years(self):
        self.assertEqual(self.last(D(2026, 4, 1), "3y"), "2029-04-01")

    def test_exclusion_extends_deadline(self):
        # 30 days from 1 Jan ends 31 Jan; excluding 5-9 Jan (5 days) moves it to 5 Feb.
        r = date_calc.compute(D(2026, 1, 1), "30d", exclusions=[(D(2026, 1, 5), D(2026, 1, 9))])
        self.assertEqual(r["last_day"], "2026-02-05")
        self.assertEqual(r["excluded_days"], 5)

    def test_exclusion_before_period_ignored(self):
        r = date_calc.compute(D(2026, 1, 10), "10d", exclusions=[(D(2026, 1, 1), D(2026, 1, 5))])
        self.assertEqual(r["last_day"], "2026-01-20")
        self.assertEqual(r["excluded_days"], 0)

    def test_holiday_moves_to_next_open_day(self):
        r = date_calc.compute(D(2026, 1, 1), "30d", holidays=[D(2026, 1, 31), D(2026, 2, 1)])
        self.assertEqual(r["last_day"], "2026-02-02")

    def test_weekend_closed(self):
        # 31 Jan 2026 is a Saturday.
        r = date_calc.compute(D(2026, 1, 1), "30d", weekends_closed=True)
        self.assertEqual(r["last_day"], "2026-02-02")

    def test_no_holiday_list_warns(self):
        r = date_calc.compute(D(2026, 1, 1), "30d")
        self.assertTrue(any("NOT checked" in s for s in r["working"]))

    def test_bad_period(self):
        with self.assertRaises(ValueError):
            date_calc.parse_period("thirty days")


class CheckQuoteTests(unittest.TestCase):
    SOURCE = (
        "1. The appellant was arrested on 3 January.\n"
        "2. It is well settled that “bail is the rule and jail\n"
        "   the exception” in such cases.\n"
        "\fPage 2\n"
        "[3] The appeal is allowed.\n"
    )

    def test_exact(self):
        r = check_quote.check(self.SOURCE, "The appeal is allowed.")
        self.assertEqual(r["status"], "EXACT")
        self.assertEqual(r["matches"][0]["paragraph"], "3")
        self.assertEqual(r["matches"][0]["page"], 2)

    def test_normalised_spacing_and_quotes(self):
        r = check_quote.check(self.SOURCE, '"bail is the rule and jail the exception"')
        self.assertEqual(r["status"], "EXACT_AFTER_NORMALISING")
        self.assertEqual(r["matches"][0]["paragraph"], "2")

    def test_not_found_is_not_repaired(self):
        r = check_quote.check(self.SOURCE, "bail is the rule and jail is the exception")
        self.assertEqual(r["status"], "NOT_FOUND")

    def test_hash_is_stable(self):
        a = check_quote.check(self.SOURCE, "appeal")["sha256"]
        b = check_quote.check(self.SOURCE, "arrested")["sha256"]
        self.assertEqual(a, b)

    def test_empty_quote(self):
        with self.assertRaises(ValueError):
            check_quote.check(self.SOURCE, "   ")


if __name__ == "__main__":
    unittest.main()
