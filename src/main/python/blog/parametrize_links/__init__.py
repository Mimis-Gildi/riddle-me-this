"""parametrize_links -- parametrize links in an AsciiDoc article."""

from __future__ import annotations

import subprocess
from pathlib import Path

from .article import Article

project_root = Path(subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True
).stdout.strip())

SITE_ROOT = project_root / "site"
CONF_FILE = SITE_ROOT / "_config.yml"
POST_ROOT = SITE_ROOT / "_posts"
SLOP_ARTICLE = POST_ROOT / "2025-09-29-sources-passed-validation.adoc"
FULL_ARTICLE = POST_ROOT / "2023-06-10-LLMs-what-good-for.adoc"


def main() -> int:
    from .configuration import Configuration
    from .site import Site
    from .reporter import Reporter
    return Reporter(Site(Configuration(SITE_ROOT))).report()
