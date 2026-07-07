"""
check_rendered_site.py -- scan every rendered page for unresolved AsciiDoc attributes
and broken links.

Drives from Jekyll's sitemap.xml — the authoritative list of every published URL.

Phase 1: fetch each page, report lines containing {attr-name} patterns.
Phase 2: collect all href links and check for 404s (local links only).

Usage:
    python src/test/python/blog/check_rendered_site.py [base_url]

Default base_url: http://localhost:4700/riddle-me-this
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse

import requests

ATTR_RE = re.compile(r'\{[a-z][a-z0-9\-]+\}')
HREF_RE = re.compile(r'href="([^"]+)"')
SITEMAP_NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'


def collect_urls(base: str, session: requests.Session) -> list[tuple[str, str]]:
    """Fetch sitemap.xml and return (label, url) for every published page."""
    sitemap_url = f"{base}/sitemap.xml"
    r = session.get(sitemap_url, timeout=10)
    r.raise_for_status()
    root = ET.fromstring(r.text)
    urls = []
    for url_el in root.findall(f'{{{SITEMAP_NS}}}url'):
        loc = url_el.findtext(f'{{{SITEMAP_NS}}}loc', '').strip()
        if loc:
            label = loc.split('/')[-1] or loc.split('/')[-2] + '/'
            urls.append((label, loc))
    return urls


def check_unresolved(label: str, url: str, session: requests.Session) -> list[str]:
    try:
        r = session.get(url, timeout=10)
    except Exception as e:
        return [f"  FETCH ERROR: {e}"]
    if r.status_code != 200:
        return [f"  HTTP {r.status_code}"]
    hits = []
    for i, line in enumerate(r.text.splitlines(), 1):
        matches = ATTR_RE.findall(line)
        if matches:
            # skip likely false positives: CSS vars, JS template literals
            real = [m for m in matches if not line.strip().startswith(('var(', '//', '*', '/*'))]
            if real:
                preview = line.strip()[:120]
                hits.append(f"  line {i:4d}: {real} in: {preview}")
    return hits


def collect_links(url: str, session: requests.Session) -> list[str]:
    try:
        r = session.get(url, timeout=10)
    except Exception:
        return []
    return HREF_RE.findall(r.text)


def check_links(label: str, page_url: str, links: list[str], base: str, session: requests.Session) -> list[str]:
    broken = []
    seen = set()
    for href in links:
        if href.startswith(('#', 'mailto:', 'javascript:')):
            continue
        if href.startswith('/'):
            full = f"http://{urlparse(page_url).netloc}{href}"
        elif href.startswith('http'):
            full = href
        else:
            full = urljoin(page_url, href)
        if full in seen:
            continue
        seen.add(full)
        # Only check local links to avoid hammering external sites
        if urlparse(full).netloc != urlparse(page_url).netloc:
            continue
        try:
            r = session.head(full, timeout=8, allow_redirects=True)
            if r.status_code == 404:
                broken.append(f"  404: {full}")
        except Exception as e:
            broken.append(f"  ERR: {full} ({e})")
    return broken


def main(base: str = "http://localhost:4700/riddle-me-this") -> None:
    base = base.rstrip('/')

    session = requests.Session()
    session.headers['User-Agent'] = 'site-checker/1.0'

    urls = collect_urls(base, session)
    print(f"Checking {len(urls)} pages from sitemap on {base}\n")

    # Phase 1: unresolved attributes
    print("=" * 70)
    print("PHASE 1: Unresolved AsciiDoc attributes")
    print("=" * 70)
    unresolved_pages = 0
    for label, url in urls:
        hits = check_unresolved(label, url, session)
        if hits:
            unresolved_pages += 1
            print(f"\n{label}")
            print(f"  {url}")
            for h in hits:
                print(h)

    if unresolved_pages == 0:
        print("  None found.")

    # Phase 2: local 404s
    print(f"\n{'=' * 70}")
    print("PHASE 2: Local broken links (404)")
    print("=" * 70)
    broken_pages = 0
    for label, url in urls:
        links = collect_links(url, session)
        broken = check_links(label, url, links, base, session)
        if broken:
            broken_pages += 1
            print(f"\n{label}")
            print(f"  {url}")
            for b in broken:
                print(b)

    if broken_pages == 0:
        print("  None found.")

    print(f"\nDone. {unresolved_pages} pages with unresolved attrs, {broken_pages} pages with broken local links.")


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4700/riddle-me-this"
    main(base)