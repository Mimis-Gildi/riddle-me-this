"""parametrize_links -- parametrize links in an AsciiDoc article."""

from __future__ import annotations

from pathlib import Path

from .article import Article


def main(filename: str) -> None:
    Article(Path(filename))
