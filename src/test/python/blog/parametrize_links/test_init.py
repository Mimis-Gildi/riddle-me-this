"""Tests for __init__ constants and main entry point."""
from pathlib import Path

from blog.parametrize_links import SITE_ROOT, CONF_FILE, POST_ROOT, SLOP_ARTICLE, FULL_ARTICLE, main


class TestInitConstants:

    def test_site_root_is_path_and_exists(self):
        assert isinstance(SITE_ROOT, Path)
        assert SITE_ROOT.exists()

    def test_conf_file_is_path_and_exists(self):
        assert isinstance(CONF_FILE, Path)
        assert CONF_FILE.exists()

    def test_post_root_is_path_and_exists(self):
        assert isinstance(POST_ROOT, Path)
        assert POST_ROOT.exists()

    def test_slop_article_is_path_and_exists(self):
        assert isinstance(SLOP_ARTICLE, Path)
        assert SLOP_ARTICLE.exists()

    def test_full_article_is_path_and_exists(self):
        assert isinstance(FULL_ARTICLE, Path)
        assert FULL_ARTICLE.exists()


class TestInitMain:

    def test_main_returns_int(self, capsys):
        assert isinstance(main(), int)

    def test_main_exit_code_valid(self, capsys):
        assert main() in (0, 1)

    def test_main_csv_produces_files(self, tmp_path, capsys):
        assert main(csv_dir=tmp_path) in (0, 1)
        assert (tmp_path / "body_violations.csv").exists()
        assert (tmp_path / "promotion_candidates.csv").exists()
