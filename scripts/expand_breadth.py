"""
expand_breadth.py — semi-automated breadth-first citation expansion.

Run this on YOUR OWN machine (not in a sandboxed environment without internet
access to api.semanticscholar.org).

What it does:
  1. Reads your papers.csv, finds rows tagged 'core-anchor' or 'core-related'.
  2. For each, queries Semantic Scholar for its direct citations and references
     (hop 1 of the BFS).
  3. Writes candidates to `candidates_hop1.csv` — title, year, venue, abstract,
     link — for you to triage (NOT auto-merged into papers.csv; breadth-first
     still requires a human eyeballing the abstract).

Usage:
    pip install requests
    python expand_breadth.py

Notes:
  - Semantic Scholar's public API is rate-limited (100 req/5min unauthenticated).
    This script sleeps between calls; for a large seed set, get a free API key
    from https://www.semanticscholar.org/product/api and set SS_API_KEY below.
  - This only pulls titles/abstracts, consistent with the "triage before you
    read" step in the breadth-first protocol.
"""

import csv
import time
import requests

SS_API_KEY = None  # optional: paste your free Semantic Scholar API key here
BASE = "https://api.semanticscholar.org/graph/v1/paper"
HEADERS = {"x-api-key": SS_API_KEY} if SS_API_KEY else {}


def search_paper_id(title):
    """Find the Semantic Scholar paper ID for a given title (best-effort match)."""
    r = requests.get(
        f"{BASE}/search",
        params={"query": title, "limit": 1, "fields": "paperId,title"},
        headers=HEADERS,
    )
    r.raise_for_status()
    data = r.json().get("data", [])
    return data[0]["paperId"] if data else None


def get_citations_and_references(paper_id):
    """Pull direct citing papers and referenced papers for one paper ID."""
    fields = "title,year,venue,abstract,externalIds"
    out = []
    for relation in ("citations", "references"):
        r = requests.get(
            f"{BASE}/{paper_id}/{relation}",
            params={"fields": fields, "limit": 50},
            headers=HEADERS,
        )
        if r.status_code != 200:
            continue
        for item in r.json().get("data", []):
            p = item.get(relation[:-1] if relation == "citations" else "citedPaper", None)
            # API shape varies by relation; handle both defensively
            p = item.get("citingPaper") or item.get("citedPaper") or item
            if p and p.get("title"):
                out.append(
                    {
                        "title": p.get("title", ""),
                        "year": p.get("year", ""),
                        "venue": p.get("venue", ""),
                        "abstract": (p.get("abstract") or "")[:300],
                        "relation": relation,
                        "doi": (p.get("externalIds") or {}).get("DOI", ""),
                    }
                )
        time.sleep(1.2)  # be polite to the rate limit
    return out


def main():
    with open("papers.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    seeds = [r for r in rows if "core-anchor" in r.get("tags", "") or "core-related" in r.get("tags", "")]
    print(f"Found {len(seeds)} seed papers (core-anchor / core-related).")

    all_candidates = []
    seen_titles = {r["title"].strip().lower() for r in rows}

    for seed in seeds:
        title = seed["title"]
        print(f"Looking up: {title}")
        try:
            pid = search_paper_id(title)
        except Exception as e:
            print(f"  skip (lookup failed: {e})")
            continue
        if not pid:
            print("  no match found on Semantic Scholar, skipping")
            continue
        candidates = get_citations_and_references(pid)
        for c in candidates:
            if c["title"].strip().lower() not in seen_titles:
                c["seed_paper"] = title
                all_candidates.append(c)
                seen_titles.add(c["title"].strip().lower())
        time.sleep(1.5)

    if not all_candidates:
        print("No new candidates found.")
        return

    with open("candidates_hop1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["title", "year", "venue", "abstract", "relation", "doi", "seed_paper"]
        )
        w.writeheader()
        w.writerows(all_candidates)

    print(f"\nWrote {len(all_candidates)} new candidates to candidates_hop1.csv")
    print("Next: triage each (title+abstract only) and promote the relevant ones into papers.csv.")


if __name__ == "__main__":
    main()
