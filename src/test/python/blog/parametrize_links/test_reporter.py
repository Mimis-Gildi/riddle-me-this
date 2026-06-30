"""Tests for Reporter — structured console output and optional CSV export."""
import pytest
from functional import seq

from blog.parametrize_links import SITE_ROOT
from blog.parametrize_links.configuration import Configuration
from blog.parametrize_links.reporter import Reporter
from blog.parametrize_links.site import Site


@pytest.fixture(scope="module")
def real_reporter():
    return Reporter(Site(Configuration(SITE_ROOT)))


class TestReporterReport:

    def test_report_returns_int(self, real_reporter):
        assert isinstance(real_reporter.report(), int)

    def test_report_exit_code_valid(self, real_reporter):
        assert real_reporter.report() in (0, 1)

    def test_report_section_headers(self, real_reporter, capsys):
        real_reporter.report()
        out = capsys.readouterr().out.lower()
        assert "body link violations" in out
        assert "shadowed globals" in out
        assert "cross-article duplicates" in out
        assert "promotion candidates" in out

    def test_report_clean_returns_0(self, capsys):
        class _CleanSite:
            def body_link_violations(self): return seq([])
            def shadowed_globals(self): return seq([])
            def cross_article_duplicates(self): return seq([])
            def promotion_candidates(self): return seq([])

        assert Reporter(_CleanSite()).report() == 0

    def test_report_dirty_returns_1(self, capsys):
        from blog.parametrize_links import SLOP_ARTICLE
        from blog.parametrize_links.article import Article

        dirty_article = Article(SLOP_ARTICLE)

        class _DirtySite:
            def body_link_violations(self): return seq([dirty_article])
            def shadowed_globals(self): return seq([])
            def cross_article_duplicates(self): return seq([])
            def promotion_candidates(self): return seq([])

        assert Reporter(_DirtySite()).report() == 1


class TestReporterCsvs:

    def test_to_csvs_creates_files(self, real_reporter, tmp_path):
        real_reporter.to_csvs(tmp_path)
        assert (tmp_path / "body_violations.csv").exists()
        assert (tmp_path / "shadowed_globals.csv").exists()
        assert (tmp_path / "cross_article_duplicates.csv").exists()
        assert (tmp_path / "promotion_candidates.csv").exists()

    def test_to_csvs_have_header_rows(self, real_reporter, tmp_path):
        real_reporter.to_csvs(tmp_path)
        assert "article" in (tmp_path / "body_violations.csv").read_text(encoding="utf-8").splitlines()[0]
        assert "key" in (tmp_path / "shadowed_globals.csv").read_text(encoding="utf-8").splitlines()[0]
        assert "key" in (tmp_path / "cross_article_duplicates.csv").read_text(encoding="utf-8").splitlines()[0]
        assert "url" in (tmp_path / "promotion_candidates.csv").read_text(encoding="utf-8").splitlines()[0]
