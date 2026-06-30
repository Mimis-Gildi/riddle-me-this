"""Tests for the Article container -- imports the real package, no loader hack."""

import pytest

from functional import seq

from blog.parametrize_links import CONF_FILE
from blog.parametrize_links.article import Article
from blog.parametrize_links.article_attribute_providers import read_declared_link_attributes_provider
from blog.parametrize_links.attribute_providers import GLOBAL_POSITION, global_link_attribute_collecting_provider, \
    static_links_provider, config_links_provider, filter_provider


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
    """Test basic behavior of Article object including text initiation and global configuration load."""

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
        """Accept mocked provider, store the provider as-is (deferred), return self, and is write-once, reduce provider, validate content, and sideeffect print."""

        mocked_article = Article(self.slop_article).accept_global_link_attribute_provider(self.mocked_provider)

        assert mocked_article.links_provider_global is self.mocked_provider

        with pytest.raises(RuntimeError) as once_error:
            mocked_article.accept_global_link_attribute_provider(self.mocked_provider)
        assert "This operation can only be invoked once." in str(once_error.value)

        mocked_global_links_applied_article = mocked_article.apply_global_links_acquisition()
        assert mocked_global_links_applied_article.links_provider_global == self.mocked_provider

        mocked_global_links = mocked_global_links_applied_article.links_global
        assert all(link in mocked_global_links for link in self.mocked_provider())

        mocked_global_links_applied_article.print_global_links()


    def test_global_attributes_actual(self):
        """Accept REAL provider, store the provider as-is (deferred), returns self, and is write-once, reduce provider, validate content, and sideeffect print."""
        real_provider = global_link_attribute_collecting_provider(
            static_links_provider(),
            config_links_provider(CONF_FILE),
            filter_provider())

        actual_article = (Article(self.slop_article)
            .accept_global_link_attribute_provider(real_provider)
            .apply_global_links_acquisition()
            .print_global_links())

        assert {"site-baseurl", "cb-hacker", "cb-mundane", "chatgpt", "hera-school", "hera-school-url",
                "mailto-rIdd13r", "openai", "openai-blog", "profile-li", "li-newsletter",
                "fireship-gemini3", "gitomer-book", "mcp-overview",
                "mit-article-url", "mit-article-title", "mit-article",
                "rdd13r-gh", "release", "resume", "total-recall", "org-mimis-gildi"} == (
            seq(actual_article.links_global).map(lambda attr: attr.key).to_set())


class TestArticleContentReadingObject:
    """Test advanced behavior of article by reading global configuration and article content."""

    def test_read_article_header_link_attributes(self, full_article):
        """Read full article having global configuration and article header content."""
        article = Article(full_article)
        actual = (article
            .accept_global_link_attribute_provider(global_link_attribute_collecting_provider(
                static_links_provider(), config_links_provider(CONF_FILE), filter_provider()))
            .accept_header_defined_attribute_provider(read_declared_link_attributes_provider(article))
            .apply_global_links_acquisition()
            .apply_header_links_acquisition()
            .print_global_links()
            .print_declared_links())

        assert 40 == seq(actual.links_declared).len()
        assert {"jarvis", "nomads", "demogroup", "anonymous", "cliques", "scene", "culture", "mit",
                "lugaru", "tales", "spaces", "brakha", "carpathia", "dolly-2", "hfce", "crackers",
                "active-inference", "verses", "g-io", "g-community", "g-ai-onboarding", "g-dev-profile",
                "g-k-models", "g-dtensor", "g-io-session", "g-palm2-api", "g-maker-suite", "g-tensorflow",
                "g-research", "g-kaggle", "g-attn", "m-llama", "s-alpaca", "bsd-vicuna", "bsd-vicuna-topics",
                "db-dolly", "db-dolly-hf", "open-assistant", "o-a-hf", "all-oss-lm-models"} == (
            seq(actual.links_declared).map(lambda attr: attr.key).to_set())
