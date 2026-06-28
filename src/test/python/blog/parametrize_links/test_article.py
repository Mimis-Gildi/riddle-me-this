"""Tests for the Article container -- imports the real package, no loader hack."""

import pytest

from blog.parametrize_links.article import Article
from blog.parametrize_links.attribute_providers import GLOBAL_POSITION, global_link_attributes


class TestArticleInvocation:
    """Test the Article container basic invocation."""

    @pytest.fixture(autouse=True)
    def _tmp(self, tmp_path):
        self.tmp_path = tmp_path

    def test_rejects_non_adoc_suffix(self):
        """Suffix not .adoc -> raises ValueError."""
        with pytest.raises(ValueError) as value_off:
            Article(self.tmp_path / "note.txt")

        assert "not an AsciiDoc file: " in str(value_off.value)

    def test_missing_adoc_file_raises(self):
        """Suffix ok, but the read bombs when the .adoc file is absent."""
        with pytest.raises(FileNotFoundError):
            Article(self.tmp_path / "ghost.adoc")

    def test_accepts_readable_adoc(self):
        """Suffix ok and readable text -> constructs cleanly, keeps the path."""
        post = self.tmp_path / "post.adoc"
        post.write_text("= Title\n", encoding="utf-8")
        assert Article(post).path == post

    def test_real_slop_article(self, slop_article):
        """A real Slop article -> constructs cleanly, keeps the path."""
        article = Article(slop_article)

        assert 12832 == article._content_length
        assert "8cb016f3b9a649cd1dbd100efe413afaeb241614" == article._file_checksum

        assert article.path == slop_article

class TestArticleObject:

    @pytest.fixture(autouse=True)
    def _slop(self, slop_article):
        self.slop_article = slop_article

    @pytest.fixture(autouse=True)
    def _tmp(self, tmp_path):
        self.tmp_path = tmp_path

    @pytest.fixture(autouse=True)
    def _mock_provider(self, mock_provider):
        self.mocked_provider = mock_provider

    def test_init_attributes(self):
        """Test the affinity of the protected attributes once the right slop is loaded."""
        slop = Article(self.slop_article)

        assert 12832 == slop._content_length
        assert "8cb016f3b9a649cd1dbd100efe413afaeb241614" == slop._file_checksum
        assert slop.path == self.slop_article

        with pytest.raises(RuntimeError) as text_set_error:
            slop.text = "My new text!"
        assert "This operation can only be invoked once." in str(text_set_error.value)

        with pytest.raises(RuntimeError) as checksum_set_error:
            slop.file_checksum = "My new checksum: xoxoxoxoxo"
        assert "This operation can only be invoked once." in str(checksum_set_error.value)

        with pytest.raises(RuntimeError) as length_set_error:
            slop.content_length = -1
        assert "This operation can only be invoked once." in str(length_set_error.value)


    def test_global_attributes_mocked(self):
        """accept stores the provider as-is (deferred), returns self, and is write-once, reduce provider, validate content."""

        mocked_article = Article(self.slop_article).accept_global_link_attributes(self.mocked_provider)

        assert mocked_article.links_provider_global is self.mocked_provider

        with pytest.raises(RuntimeError) as once_error:
            mocked_article.accept_global_link_attributes(self.mocked_provider)
        assert "This operation can only be invoked once." in str(once_error.value)

    def test_global_attributes_actual(self):
        self.fail()


# def test_accept_global_link_attributes(self):
#     self.fail()
