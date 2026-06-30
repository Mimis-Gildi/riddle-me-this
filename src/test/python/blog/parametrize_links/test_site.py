"""Tests for Site — lazy orchestrator across all Jekyll content collections."""
import shutil

import pytest
from functional import seq

from blog.parametrize_links import SITE_ROOT, FULL_ARTICLE
from blog.parametrize_links.configuration import Configuration
from blog.parametrize_links.site import Site


@pytest.fixture(scope="module")
def real_site():
    return Site(Configuration(SITE_ROOT))


class TestSiteConstruction:

    def test_lazy_construction(self):
        site = Site(Configuration(SITE_ROOT))
        assert site._articles is None

    def test_articles_returns_seq(self, real_site):
        assert seq(real_site.articles()).non_empty()


class TestSiteArticles:

    def test_articles_count(self, real_site):
        assert real_site.articles().len() == 61

    def test_articles_all_have_globals(self, real_site):
        assert real_site.articles().filter(lambda a: len(a.links_global) == 0).empty()

    def test_links_declared_populated(self, real_site):
        assert real_site.articles().filter(lambda a: not isinstance(a.links_declared, tuple)).empty()

    def test_links_body_populated(self, real_site):
        assert real_site.articles().filter(lambda a: not isinstance(a.links_body, tuple)).empty()

    def test_tmp_single_article(self, tmp_path):
        posts = tmp_path / "_posts"
        posts.mkdir()
        shutil.copy(FULL_ARTICLE, posts / FULL_ARTICLE.name)
        (tmp_path / "_config.yml").write_text("", encoding="utf-8")
        site = Site(Configuration(tmp_path))
        assert site.articles().len() == 1


class TestSiteViolations:

    def test_body_link_violations_subset(self, real_site):
        violations = real_site.body_link_violations()
        assert violations.filter(lambda a: len(a.links_body) == 0).empty()

    def test_shadowed_globals_keys_in_global_set(self, real_site):
        global_keys = {a.key for a in real_site._config.global_links}
        assert (real_site.shadowed_globals()
                .filter(lambda pair: pair[1].key not in global_keys)
                .empty())

    def test_cross_article_duplicates_have_multiple_articles(self, real_site):
        assert (real_site.cross_article_duplicates()
                .filter(lambda kg: len(kg[1]) < 2)
                .empty())

    def test_cross_article_duplicates_multiple_articles_in_group(self, real_site):
        assert (real_site.cross_article_duplicates()
                .filter(lambda kg: len({a.path for a in kg[1]}) < 2)
                .empty())

    def test_promotion_candidates_http_only(self, real_site):
        assert (real_site.promotion_candidates()
                .filter(lambda ug: not ug[0].startswith(("http://", "https://")))
                .empty())

    def test_promotion_candidates_multi_article(self, real_site):
        assert (real_site.promotion_candidates()
                .filter(lambda ug: len(ug[1]) < 2)
                .empty())
