"""Tests for the Article container -- imports the real package, no loader hack."""

import pytest

from blog.parametrize_links.article import Article


def test_rejects_non_adoc_suffix(tmp_path):
    # suffix != ".adoc" -> ValueError, before any read.
    with pytest.raises(ValueError):
        Article(tmp_path / "note.txt")


def test_missing_adoc_file_raises(tmp_path):
    # suffix ok, but the read bombs when the .adoc file is absent.
    with pytest.raises(FileNotFoundError):
        Article(tmp_path / "ghost.adoc")


def test_accepts_readable_adoc(tmp_path):
    # suffix ok and readable text -> constructs cleanly, keeps the path.
    post = tmp_path / "post.adoc"
    post.write_text("= Title\n", encoding="utf-8")
    assert Article(post).path == post
