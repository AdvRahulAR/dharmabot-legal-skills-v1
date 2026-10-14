#!/usr/bin/env python3
"""Check whether a quotation appears verbatim in a source text.

Usage:
    python3 check_quote.py --source judgment.txt --quote "exact words"
    python3 check_quote.py --source judgment.txt --quote-file quote.txt [--json]

Results:
    EXACT                    the quote appears character for character
    EXACT_AFTER_NORMALISING  it appears once spacing, line breaks, curly
                             quotes and dashes are normalised
    NOT_FOUND                it does not appear, even after normalising

The script never repairs or fuzzily matches a quote. It reports the nearest
paragraph number (lines starting "12." or "[12]" or "12)") and page marker
(form feeds or lines like "Page 7"), plus a SHA-256 hash of the source file
so the check can be repeated. Standard library only; no network access.
"""

import argparse
import hashlib
import json
import re
import sys
import unicodedata

_TRANSLATE = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "–": "-", "—": "-", "−": "-",
    " ": " ", " ": " ", " ": " ",
}

_PARA_RE = re.compile(r"^\s*(?:\[(\d{1,4})\]|(\d{1,4})[.)])\s")
_PAGE_RE = re.compile(r"^\s*page\s+(\d{1,5})\b", re.IGNORECASE)


def normalise(text):
    """Return (normalised_text, index_map) where index_map[i] is the offset
    in the original text of normalised character i."""
    text = unicodedata.normalize("NFC", text)
    out = []
    index_map = []
    last_space = False
    for i, ch in enumerate(text):
        ch = _TRANSLATE.get(ch, ch)
        if ch.isspace():
            if last_space:
                continue
            ch = " "
            last_space = True
        else:
            last_space = False
        out.append(ch)
        index_map.append(i)
    return "".join(out).strip(), index_map


def locate(source, offset):
    """Nearest paragraph number and page before offset, plus line number."""
    before = source[:offset]
    line_no = before.count("\n") + 1
    page = before.count("\f") + 1 if "\f" in source else None
    para = None
    for line in before.splitlines():
        m = _PARA_RE.match(line)
        if m:
            para = m.group(1) or m.group(2)
        p = _PAGE_RE.match(line)
        if p:
            page = int(p.group(1))
    return {"line": line_no, "paragraph": para, "page": page}


def check(source, quote):
    quote = quote.strip()
    if not quote:
        raise ValueError("quote is empty")
    result = {"sha256": hashlib.sha256(source.encode("utf-8")).hexdigest()}
    hits = [m.start() for m in re.finditer(re.escape(quote), source)]
    if hits:
        result["status"] = "EXACT"
        result["matches"] = [locate(source, h) for h in hits]
        return result
    norm_source, index_map = normalise(source)
    norm_quote, _ = normalise(quote)
    hits = [m.start() for m in re.finditer(re.escape(norm_quote), norm_source)]
    if hits:
        result["status"] = "EXACT_AFTER_NORMALISING"
        result["matches"] = [locate(source, index_map[h]) for h in hits]
        return result
    result["status"] = "NOT_FOUND"
    result["matches"] = []
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", required=True, help="text file of the authority")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--quote", help="the quoted words")
    group.add_argument("--quote-file", help="file containing the quoted words")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args(argv)

    with open(args.source, encoding="utf-8") as f:
        source = f.read()
    if args.quote_file:
        with open(args.quote_file, encoding="utf-8") as f:
            quote = f.read()
    else:
        quote = args.quote

    result = check(source, quote)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result["status"])
        for m in result["matches"]:
            print(f"  line {m['line']}, paragraph {m['paragraph'] or '-'}, page {m['page'] or '-'}")
        print(f"  source sha256 {result['sha256']}")
    return 0 if result["status"] != "NOT_FOUND" else 1


if __name__ == "__main__":
    sys.exit(main())
