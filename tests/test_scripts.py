"""Unit tests for the bundled skill scripts. Run: python3 -m unittest discover tests"""

import contextlib
import datetime as dt
import importlib.util
import io
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "dharmabot-legal-skills" / "skills"
SHARED_SCRIPTS = ROOT / "shared" / "scripts"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


date_calc = load("date_calc", SHARED_SCRIPTS / "date_calc.py")
check_quote = load("check_quote", SKILLS / "citation-verifier" / "scripts" / "check_quote.py")
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

    def test_elapsed_both_counts(self):
        # Remand on 3 Aug 2026, counted to 15 Oct 2026: 73 days, or 74 with the start day.
        r = date_calc.elapsed(D(2026, 8, 3), D(2026, 10, 15))
        self.assertEqual(r["days_excluding_start"], 73)
        self.assertEqual(r["days_including_start"], 74)

    def test_elapsed_same_day(self):
        r = date_calc.elapsed(D(2026, 8, 3), D(2026, 8, 3))
        self.assertEqual((r["days_excluding_start"], r["days_including_start"]), (0, 1))

    def test_elapsed_end_before_start(self):
        with self.assertRaises(ValueError):
            date_calc.elapsed(D(2026, 8, 3), D(2026, 8, 2))

    def test_custody_limit_dates(self):
        self.assertEqual(self.last(D(2026, 8, 3), "60d"), "2026-10-02")
        self.assertEqual(self.last(D(2026, 8, 3), "60d", include_start=True), "2026-10-01")

    def test_cli_needs_period_or_to(self):
        with self.assertRaises(SystemExit):
            date_calc.main(["--start", "2026-08-03"])

    def test_cli_to_only(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            date_calc.main(["--start", "2026-08-03", "--to", "2026-10-15", "--json"])
        self.assertEqual(json.loads(buf.getvalue())["elapsed"]["days_excluding_start"], 73)

    def test_cli_period_json_shape_unchanged(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            date_calc.main(["--start", "2026-03-10", "--period", "90d", "--json"])
        self.assertEqual(json.loads(buf.getvalue())["last_day"], "2026-06-08")

    def test_hours_period(self):
        r = date_calc.compute(dt.datetime(2026, 10, 15, 14, 30), "6h")
        self.assertEqual(r["last_day"], "2026-10-15T20:30")

    def test_hours_cross_midnight(self):
        r = date_calc.compute(dt.datetime(2026, 10, 15, 22, 0), "6h")
        self.assertEqual(r["last_day"], "2026-10-16T04:00")
        self.assertTrue(any("not moved for holidays" in s for s in r["working"]))

    def test_hours_needs_time(self):
        with self.assertRaises(ValueError):
            date_calc.compute(D(2026, 10, 15), "6h")

    def test_hours_reject_holidays(self):
        with self.assertRaises(ValueError):
            date_calc.compute(dt.datetime(2026, 10, 15, 9, 0), "2h", holidays=[D(2026, 10, 15)])

    def test_days_with_time_start_unchanged(self):
        self.assertEqual(self.last(dt.datetime(2026, 3, 10, 18, 0), "90d"), "2026-06-08")

    def test_elapsed_hours(self):
        r = date_calc.elapsed(dt.datetime(2026, 10, 15, 22, 0), dt.datetime(2026, 10, 16, 4, 30))
        self.assertEqual(r["hours_elapsed"], 6.5)

    def test_elapsed_mixed_rejected(self):
        with self.assertRaises(ValueError):
            date_calc.elapsed(dt.datetime(2026, 10, 15, 22, 0), D(2026, 10, 16))

    def test_parse_date_with_time(self):
        self.assertEqual(date_calc.parse_date("2026-10-15T14:30"), dt.datetime(2026, 10, 15, 14, 30))


class SharedScriptCopyTests(unittest.TestCase):
    """Copies made by scripts/build.py must match shared/scripts apart from the generated-copy line."""

    def test_copies_in_sync(self):
        for shared in SHARED_SCRIPTS.glob("*.py"):
            source = shared.read_text(encoding="utf-8").splitlines()
            copies = list(SKILLS.glob(f"*/scripts/{shared.name}"))
            self.assertTrue(copies, f"no skill bundles {shared.name}")
            for copy in copies:
                lines = [l for l in copy.read_text(encoding="utf-8").splitlines() if not l.startswith("# Generated copy of")]
                self.assertEqual(lines, source, f"{copy} is stale; run scripts/build.py")


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
