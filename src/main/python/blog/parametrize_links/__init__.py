"""parametrize_links -- parametrize links in an AsciiDoc article."""

from __future__ import annotations

import subprocess
from pathlib import Path

from blog.parametrize_links.attribute_providers import global_link_attribute_collecting_provider, \
    static_links_provider, \
    config_links_provider, \
    filter_provider
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


def main(filename: str) -> None:

    article_to_process = (Article(Path(filename))
        .accept_global_link_attribute_provider(
            global_link_attribute_collecting_provider(
                static_links_provider(),
                config_links_provider(CONF_FILE),
                filter_provider()))
        .apply_global_links_acquisition()
        .print_global_links())

    print(article_to_process.links_global)
