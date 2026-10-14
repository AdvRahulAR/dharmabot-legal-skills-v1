#!/usr/bin/env python3
"""Deadline arithmetic for Indian limitation and procedural periods.

Usage:
    python3 date_calc.py --start 2026-03-10 --period 90d
    python3 date_calc.py --start 2026-01-31 --period 1m --exclude 2026-02-02:2026-02-10 \
        --holidays holidays.txt --weekends-closed --json
    python3 date_calc.py --start 2026-08-03 --to 2026-10-15
    python3 date_calc.py --start 2026-08-03 --to 2026-10-15 --period 60d

Rules applied (each can be checked against the working printed):
  * The day of the starting event is excluded by default, as section 12(1)
    of the Limitation Act, 1963 provides. Use --include-start to count it.
  * Periods in days are counted day by day. Periods in months or years are
    calendar periods: the same date in the later month, or the last day of
    that month if it is shorter (e.g. 31 Jan + 1 month -> 28/29 Feb).
  * Excluded spans (inclusive, e.g. from the copy application to the date the
    copy was made ready, not the date it was collected) push
    the last day forward by the number of their days that fall after the
    start of the period and on or before the running last day.
  * If the last day falls on a holiday in --holidays (or a weekend with
    --weekends-closed), it moves to the next day the court is open
    (section 4 of the Limitation Act, 1963).

With --to, the script also counts the days elapsed from --start to --to,
printed both ways (start day excluded and start day counted), so a stated
count such as "40 days in custody" can be checked against the actual dates.
It does not choose between the two counts.

The script does not decide which period applies or when time starts. That
is legal analysis for the advocate. Standard library only.
"""

import argparse
import calendar
import datetime as dt
import json
import re
import sys

_PERIOD_RE = re.compile(r"^(\d+)\s*([dmy])$", re.IGNORECASE)


def parse_date(text):
    return dt.date.fromisoformat(text.strip())


def parse_period(text):
    m = _PERIOD_RE.match(text.strip())
    if not m:
        raise ValueError(f"period must look like 30d, 3m or 1y, got {text!r}")
    return int(m.group(1)), m.group(2).lower()


def add_months(day, months):
    month_index = day.month - 1 + months
    year = day.year + month_index // 12
    month = month_index % 12 + 1
    last = calendar.monthrange(year, month)[1]
    return dt.date(year, month, min(day.day, last))


def parse_span(text):
    if ":" in text:
        a, b = text.split(":", 1)
    else:
        a = b = text
    start, end = parse_date(a), parse_date(b)
    if end < start:
        raise ValueError(f"excluded span ends before it starts: {text}")
    return start, end


def compute(start, period, include_start=False, exclusions=(), holidays=(), weekends_closed=False):
    amount, unit = parse_period(period)
    steps = []
    # When the start day is excluded, the period begins the next day.
    first_day = start if include_start else start + dt.timedelta(days=1)
    steps.append(
        f"Start event {start.isoformat()}; "
        + ("start day counted." if include_start else f"start day excluded, period runs from {first_day.isoformat()}.")
    )

    if unit == "d":
        last = first_day + dt.timedelta(days=amount - 1)
        steps.append(f"{amount} day(s) counted from {first_day.isoformat()} ends on {last.isoformat()}.")
    else:
        months = amount if unit == "m" else amount * 12
        anchor = start if not include_start else start - dt.timedelta(days=1)
        last = add_months(anchor, months)
        steps.append(
            f"{amount} {'month' if unit == 'm' else 'year'}(s) from {anchor.isoformat()} "
            f"(calendar reckoning) ends on {last.isoformat()}."
        )

    # Apply exclusions: count excluded days within the running window, repeat
    # until stable because extending the window can bring more days inside it.
    spans = sorted(exclusions)
    counted = set()
    changed = True
    while changed:
        changed = False
        for s, e in spans:
            d = max(s, first_day)
            while d <= min(e, last):
                if d not in counted:
                    counted.add(d)
                    last += dt.timedelta(days=1)
                    changed = True
                d += dt.timedelta(days=1)
    if spans:
        steps.append(
            f"Excluded {len(counted)} day(s) from spans "
            + ", ".join(f"{s.isoformat()} to {e.isoformat()}" for s, e in spans)
            + f"; last day becomes {last.isoformat()}."
        )

    closed = set(holidays)
    moved_from = last
    while last in closed or (weekends_closed and last.weekday() >= 5):
        last += dt.timedelta(days=1)
    if last != moved_from:
        steps.append(
            f"{moved_from.isoformat()} is a closed day; moved to next open day {last.isoformat()}."
        )
    elif not closed and not weekends_closed:
        steps.append("No holiday list supplied: last day NOT checked against court holidays.")

    return {
        "start_event": start.isoformat(),
        "period": period,
        "last_day": last.isoformat(),
        "weekday": last.strftime("%A"),
        "excluded_days": len(counted),
        "working": steps,
    }


def elapsed(start, end):
    """Days from start to end, counted both ways. Neither count is chosen."""
    if end < start:
        raise ValueError(f"--to date {end.isoformat()} is before --start {start.isoformat()}")
    excluding = (end - start).days
    return {
        "from": start.isoformat(),
        "to": end.isoformat(),
        "days_excluding_start": excluding,
        "days_including_start": excluding + 1,
        "working": [
            f"From {start.isoformat()} to {end.isoformat()}: {excluding} day(s) with the start day excluded, "
            f"{excluding + 1} day(s) with both the start day and the end day counted."
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Limitation and deadline arithmetic")
    parser.add_argument("--start", required=True, help="date of starting event, YYYY-MM-DD")
    parser.add_argument("--period", help="e.g. 30d, 3m, 1y (required unless --to is given)")
    parser.add_argument("--to", help="count days elapsed from --start to this date, YYYY-MM-DD")
    parser.add_argument("--include-start", action="store_true", help="count the start day")
    parser.add_argument("--exclude", action="append", default=[], help="excluded span YYYY-MM-DD:YYYY-MM-DD (repeatable)")
    parser.add_argument("--holidays", help="file with one YYYY-MM-DD closed date per line")
    parser.add_argument(
        "--weekends-closed",
        action="store_true",
        help="treat every Saturday and Sunday as closed (only if the court never sits then; prefer --holidays)",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if not args.period and not args.to:
        parser.error("give --period, --to, or both")

    holidays = []
    if args.holidays:
        with open(args.holidays, encoding="utf-8") as f:
            for line in f:
                line = line.split("#", 1)[0].strip()
                if line:
                    holidays.append(parse_date(line))

    output = {}
    if args.to:
        output["elapsed"] = elapsed(parse_date(args.start), parse_date(args.to))
    if args.period:
        output["deadline"] = compute(
            parse_date(args.start),
            args.period,
            include_start=args.include_start,
            exclusions=[parse_span(x) for x in args.exclude],
            holidays=holidays,
            weekends_closed=args.weekends_closed,
        )
    if args.json:
        # A deadline-only run keeps the original flat JSON shape.
        print(json.dumps(output if args.to else output["deadline"], indent=2))
        return 0
    if args.to:
        for step in output["elapsed"]["working"]:
            print("- " + step)
    if args.period:
        result = output["deadline"]
        for step in result["working"]:
            print("- " + step)
        print(f"Last day: {result['last_day']} ({result['weekday']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
