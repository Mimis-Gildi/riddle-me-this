#!/usr/bin/env python
"""
Validate that the LOCALLY SERVED site never renders the production self-domain.

Every internal reference in the rendered HTML must point at the local dev host
(http://127.0.0.1:<port>/...), never the GitHub Pages production domain
(https://mimis-gildi.github.io/...). A hardcoded production URL is the bug this
guards against: it breaks local preview and chains content to one domain.

What it does:
  1. Reads `url`, `baseurl`, `port` from site/_config.yml (no hardcoded values).
  2. Enumerates every page from the live sitemap (jekyll-sitemap plugin).
  3. Fetches each page from the local server and scans the rendered HTML.
  4. Reports EVERY occurrence of the production host, with the page URL and the
     offending link (attribute + value), so each violation is unambiguous.

Exit code: 0 = clean, 1 = violations found, 2 = could not run (server/config).

Run with the local Jekyll server up (see _config.yml `port`):
    python src/test/python/test_hardcoded_self_links.py
"""

import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ElementTreeXml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG = REPO_ROOT / "site" / "_config.yml"


def read_config_scalar(text, key):
    """Parse a top-level `key : value` scalar from _config.yml (quotes optional)."""
    m = re.search(rf'^{re.escape(key)}\s*:\s*"?([^"\n#]+?)"?\s*(?:#.*)?$', text, re.M)
    return m.group(1).strip() if m else None


def load_config():
    if not CONFIG.is_file():
        sys.exit(f"[error] config not found: {CONFIG}")
    text = CONFIG.read_text(encoding="utf-8")
    url = read_config_scalar(text, "url")
    baseurl = read_config_scalar(text, "baseurl") or ""
    port = read_config_scalar(text, "port")
    if not url or not port:
        sys.exit(f"[error] could not read url/port from {CONFIG} (url={url!r} port={port!r})")
    return url.rstrip("/"), baseurl.rstrip("/"), port


def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "self-link-validator"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def page_urls_from_sitemap(prod_host, local_host):
    """Pull <loc> entries from the local sitemap, remapped to the local host."""
    sitemap = f"{local_host}/sitemap.xml"
    try:
        xml = fetch(sitemap)
    except urllib.error.URLError as e:
        sys.exit(f"[error] cannot reach local sitemap {sitemap}: {e}\n"
                 f"        is the Jekyll server running on the configured port?")
    try:
        root = ElementTreeXml.fromstring(xml)
    except ElementTreeXml.ParseError as e:
        sys.exit(f"[error] sitemap is not valid XML ({sitemap}): {e}")
    # noinspection HttpUrlsUsage
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text.strip() for el in root.findall(".//sm:loc", ns) if el.text]
    if not locs:
        sys.exit(f"[error] sitemap has no <loc> entries: {sitemap}")
    # Sitemap emits production URLs; fetch their local equivalents.
    return [loc.replace(prod_host, local_host) for loc in locs]


# Capture an attribute (href/src/content/...) whose value contains the prod host,
# plus a fallback for any bare occurrence not inside a quoted attribute.
def find_violations(html, forbidden):
    hits = []
    for m in re.finditer(r'(\w[\w:-]*)\s*=\s*"([^"]*)"', html):
        attr, val = m.group(1), m.group(2)
        if forbidden in val:
            hits.append((attr, val))
    seen = {v for _, v in hits}
    for m in re.finditer(re.escape(forbidden) + r'[^\s"\'<>]*', html):
        val = m.group(0)
        if val not in seen:
            hits.append(("(bare-text)", val))
            seen.add(val)
    return hits


def main():
    prod_url, baseurl, port = load_config()
    forbidden = prod_url + "/"                       # e.g. https://mimis-gildi.github.io/
    local_host = f"http://127.0.0.1:{port}{baseurl}"  # e.g. http://127.0.0.1:4700/riddle-me-this

    print(f"production host (forbidden) : {forbidden}")
    print(f"local host (expected)       : {local_host}/")
    print()

    pages = page_urls_from_sitemap(prod_url, local_host)
    print(f"scanning {len(pages)} page(s) from sitemap ...\n")

    total = 0
    pages_with_violations = 0
    for page in pages:
        try:
            html = fetch(page)
        except urllib.error.URLError as e:
            print(f"[warn] could not fetch {page}: {e}")
            continue
        hits = find_violations(html, forbidden)
        if hits:
            pages_with_violations += 1
            print(f"VIOLATION  {page}")
            for attr, val in hits:
                print(f"    {attr}=\"{val}\"")
                total += 1
            print()

    print("-" * 60)
    if total:
        print(f"FAIL: {total} hardcoded production link(s) on "
              f"{pages_with_violations}/{len(pages)} page(s).")
        return 1
    print(f"PASS: no production host found across {len(pages)} page(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
