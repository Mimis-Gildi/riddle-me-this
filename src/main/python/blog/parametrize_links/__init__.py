"""parametrize_links -- parametrize links in an AsciiDoc article."""

from __future__ import annotations

import subprocess
from pathlib import Path

import yaml

from blog.parametrize_links.attribute_providers import global_link_attributes

from .article import Article

project_root = Path(subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True
).stdout.strip())

SITE_ROOT = project_root / "site"
CONF_FILE = SITE_ROOT / "_config.yml"
POST_ROOT = SITE_ROOT / "_posts"
SLOP_ARTICLE = POST_ROOT / "2025-09-29-sources-passed-validation.adoc"


def main(filename: str) -> None:
    cfg = yaml.safe_load(CONF_FILE.read_text(encoding="utf-8"))
    baseurl = [("site-baseurl", cfg["baseurl"])] if cfg.get("baseurl") else []

    article = Article(Path(filename))
    # article = article.accept_global_link_attributes(cfg, baseurl) This was slop - needs another function`
    # article = article.print_global_links()
    # article = article.print_global_links()
