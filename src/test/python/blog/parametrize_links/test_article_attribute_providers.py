"""Tests for the concrete Article AttributeProvider implementations."""
from functional import seq

from blog.parametrize_links.article import Article
from blog.parametrize_links.article_attribute_providers import read_declared_link_attributes_provider


class TestArticleDeclaredLinkAttributeProviders:
    """Tests for the AttributeProviders that extract link attributes from the article header."""

    def test_declared_link_attributes_provider(self, full_article):
        """Accept real article and extract real link attributes from the article header adhering to what I always do - a well organized article."""
        links = seq(read_declared_link_attributes_provider(Article(full_article))())
        assert links.len() == 37
        assert {"jarvis", "nomads", "demogroup", "anonymous", "scene", "mit",
                "lugaru", "tales", "spaces", "brakha", "carpathia", "hfce", "crackers",
                "active-inference", "verses", "g-io", "g-community", "g-ai-onboarding", "g-dev-profile",
                "g-k-models", "g-dtensor", "g-io-session", "g-palm2-api", "g-maker-suite", "g-tensorflow",
                "g-research", "g-kaggle", "g-attn", "m-llama", "s-alpaca", "bsd-vicuna", "bsd-vicuna-topics",
                "db-dolly", "db-dolly-hf", "open-assistant", "o-a-hf", "all-oss-lm-models"} == (
            links.map(lambda attr: attr.key).to_set())