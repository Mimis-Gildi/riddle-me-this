"""Tests for the concrete Article AttributeProvider implementations."""
from functional import seq

from blog.parametrize_links import POST_ROOT
from blog.parametrize_links.article import Article
from blog.parametrize_links.article_attribute_providers import read_declared_link_attributes_provider, read_body_link_attributes_provider


class TestArticleDeclaredLinkAttributeProviders:
    """Tests for the AttributeProviders that extract link attributes from the article header."""

    def test_declared_link_attributes_provider(self, full_article):
        """Accept real article and extract real link attributes from the article header adhering to what I always do - a well organized article."""
        links = seq(read_declared_link_attributes_provider(Article(full_article))())
        assert links.len() == 37
        assert links.map(lambda attr: attr.key).to_set() == {
                "jarvis", "nomads", "demogroup", "anonymous", "scene", "mit",
                "lugaru", "tales", "spaces", "brakha", "carpathia", "hfce", "crackers",
                "active-inference", "verses", "g-io", "g-community", "g-ai-onboarding", "g-dev-profile",
                "g-k-models", "g-dtensor", "g-io-session", "g-palm2-api", "g-maker-suite", "g-tensorflow",
                "g-research", "g-kaggle", "g-attn", "m-llama", "s-alpaca", "bsd-vicuna", "bsd-vicuna-topics",
                "db-dolly", "db-dolly-hf", "open-assistant", "o-a-hf", "all-oss-lm-models"}


class TestArticleBodyLinkAttributeProviders:
    """Tests for the AttributeProviders that discover raw inline links from the article body."""

    def test_body_link_attributes_provider_stub(self, full_article):
        """Smoke: provider returns a seq of Attributes with non-empty keys and http(s) values."""
        links = seq(read_body_link_attributes_provider(Article(full_article))())
        assert links.filter(lambda attr: not attr.key).to_list() == []
        assert links.filter(lambda attr: not attr.value.startswith(("http://", "https://"))).to_list() == []

    def test_generate_body_links_csv(self):
        """Write body-links-review.csv at project root with suggested_key and blank your_key column."""
        import csv
        from blog.parametrize_links import POST_ROOT
        out = POST_ROOT.parent.parent / "body-links-review.csv"
        with out.open('w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['article', 'suggested_key', 'your_key', 'url', 'display_text'])
            for path in sorted(POST_ROOT.glob('*.adoc')):
                for attr in read_body_link_attributes_provider(Article(path))():
                    url = attr.value.split('[')[0]
                    display = attr.value[len(url) + 1:].rstrip(']') if '[' in attr.value else ''
                    w.writerow([path.stem, attr.key, '', url, display])
        print(out)

    # noinspection PyNoneFunctionAssignment
    def test_all_posts_body_links(self):
        """Print all raw inline body links found across every post — for inspection."""
        (
            seq(POST_ROOT.glob("*.adoc"))
            .map(lambda path: (path.stem, seq(read_body_link_attributes_provider(Article(path))()).to_list()))
            .filter(lambda pair: pair[1])
            .for_each(lambda pair: [
                print(f"\n--- {pair[0]} ---"),
                [print(f"  {attr.key:<35} {attr.value[:80]}") for attr in pair[1]],
            ])
        )