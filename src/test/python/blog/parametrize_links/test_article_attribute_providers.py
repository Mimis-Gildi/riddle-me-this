"""Tests for the concrete Article AttributeProvider implementations."""
from functional import seq

from blog.parametrize_links.article import Article
from blog.parametrize_links.article_attribute_providers import read_declared_link_attributes_provider, read_body_link_attributes_provider
from conftest import FULL_ARTICLE_DECLARED_KEYS
from blog.parametrize_links.attributes import LINK_VALUE_PREFIXES


class TestArticleDeclaredLinkAttributeProviders:
    """Tests for the AttributeProviders that extract link attributes from the article header."""

    def test_declared_link_attributes_provider(self, full_article):
        """Accept real article and extract real link attributes from the article header."""
        links = seq(read_declared_link_attributes_provider(Article(full_article))())
        assert links.len() == len(FULL_ARTICLE_DECLARED_KEYS)
        assert links.map(lambda attr: attr.key).to_set() == FULL_ARTICLE_DECLARED_KEYS


class TestArticleBodyLinkAttributeProviders:
    """Tests for the AttributeProviders that discover raw inline links from the article body."""

    def test_body_link_attributes_provider_stub(self, full_article):
        """Smoke: provider returns a seq of Attributes with non-empty keys and http(s) values."""
        links = seq(read_body_link_attributes_provider(Article(full_article))())
        assert links.filter(lambda attr: not attr.key).to_list() == []
        assert links.filter(lambda attr: not attr.value.startswith(LINK_VALUE_PREFIXES)).to_list() == []