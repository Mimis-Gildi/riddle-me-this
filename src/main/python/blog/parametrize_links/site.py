"""Site — lazy orchestrator: discovers all Jekyll content, loads Articles in parallel."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from functional import seq

from .article import Article
from .article_attribute_providers import (
    read_declared_link_attributes_provider,
    read_body_link_attributes_provider,
)
from .configuration import Configuration
from .promotion_candidates import find_promotion_candidates


class Site:

    def __init__(self, config: Configuration):
        self._config = config
        self._articles: tuple[Article, ...] | None = None

    def _build_article(self, path: Path) -> Article:
        article = Article(path)
        return (
            article
            .accept_global_link_attribute_provider(lambda: iter(self._config.global_links))
            .accept_header_defined_attribute_provider(read_declared_link_attributes_provider(article))
            .accept_body_discovery_attribute_provider(read_body_link_attributes_provider(article))
            .apply_global_links_acquisition()
            .apply_header_links_acquisition()
            .apply_document_body_links_acquisition()
        )

    def articles(self):
        if self._articles is None:
            paths = (
                self._config.collections
                .flat_map(lambda d: seq(d.glob("*.adoc")))
                .to_list()
            )
            with ThreadPoolExecutor() as executor:
                self._articles = tuple(executor.map(self._build_article, paths))
        return seq(self._articles)

    def body_link_violations(self):
        return self.articles().filter(lambda a: len(a.links_body) > 0)

    def shadowed_globals(self):
        global_keys = {a.key for a in self._config.global_links}
        return (
            self.articles()
            .flat_map(lambda a: seq(a.links_declared)
                .filter(lambda d: d.key in global_keys)
                .map(lambda d: (a, d)))
        )

    def cross_article_duplicates(self):
        return (
            self.articles()
            .flat_map(lambda a: seq(a.links_declared)
                .map(lambda d: (d.key, d.value, a))
                .distinct_by(lambda t: t[0]))
            .group_by(lambda triple: triple[0])
            .filter(lambda kg: seq(kg[1]).map(lambda t: t[1]).distinct().len() > 1)
            .map(lambda kg: (kg[0], seq(kg[1]).map(lambda t: t[2]).to_list()))
        )

    def promotion_candidates(self):
        return (
            self._config.collections
            .flat_map(lambda d: find_promotion_candidates(d))
        )
