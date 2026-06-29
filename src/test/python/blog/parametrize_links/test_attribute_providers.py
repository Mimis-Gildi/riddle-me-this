"""Tests for the concrete AttributeProvider implementations."""

from functional import seq

from blog.parametrize_links import CONF_FILE
from blog.parametrize_links.attribute_providers import config_links_provider, static_links_provider, filter_provider, GLOBAL_POSITION
from blog.parametrize_links.attributes import Attribute


class TestGlobalAttributeProviders:
    """Tests the composite provider that collects static and config link attributes."""

    def test_global_link_attribute_collecting_provider(self):
        """ToDo: assert the collector merges static and config providers and applies the filter."""
        print("ToDo:")

class TestConfigFileAttributeProviders:
    """Tests the provider sourced from the config system of record (`_config.yml`)."""

    def test_mock_config_links_provider(self, mock_provider):
        """A mock standing in for the config provider honors the AttributeProvider contract -- deferred, zero-arg, yields exactly its Attributes with no file IO."""
        links = seq(mock_provider())

        assert links.len() == 6
        assert links.map(lambda link: link.position).for_all(lambda position: position == GLOBAL_POSITION)
        assert links.map(lambda link: link.key).to_set() == {
            "site-baseurl", "chatgpt", "cb-hacker", "mailto-rIdd13r", "hera-school", "resume",
        }

    def test_config_links_provider(self):
        """The provider surfaces exactly the config's `asciidoctor.attributes` -- every key, none extra, all at GLOBAL_POSITION."""
        links = seq(config_links_provider(CONF_FILE)())

        assert links.len() == 16
        assert links.map(lambda link: link.position).for_all(lambda position: position == GLOBAL_POSITION)
        assert links.map(lambda link: link.key).to_set() == {
            "icons", "cb-hacker", "cb-mundane", "chatgpt", "hera-school", "hera-school-url",
            "mailto-rIdd13r", "openai", "openai-blog", "profile-li", "publications-li",
            "rdd13r-gh", "release", "resume", "total-recall", "org-mimis-gildi",
        }

class TestStaticLinkProviders:
    """Tests a very small thing, two Jekyll injected links at various render points; offered as a future, same contract."""

    def test_static_link_provider(self):
        """Test currently two known Jekyll injections albeit not at the same time, offered here in one set."""
        links = seq(static_links_provider()())

        assert links.len() == 2
        assert links.to_set() == {
            Attribute("baseurl", "/riddle-me-this", -1),
            Attribute("site-baseurl", "/riddle-me-this", -1),
        }

class TestFilterProvider:
    """Tests all kinds of circumstances: inline, and a. mock vs. filter; b. _config.yml vs. filter; c. mock + _config.yml vs. filter."""

    def test_filter_provider_vs_inline_lambda(self):
        """Inline lamda generates one good attribute tripled versus multiples of mock attributes to strip out."""

        sequence = (seq([
            Attribute("chatgpt", "https://chat.openai.com/[ChatGPT,window=_blank]", -1),
            Attribute("chatgpt", "https://chat.openai.com/[ChatGPT,window=_blank]", -1),
            Attribute("chatgpt", "https://chat.openai.com/[ChatGPT,window=_blank]", -1),
            Attribute("icons", "font", -1),
            Attribute("icons", "font", -1),
            Attribute("baseurl", "/riddle-me-this", -1),
            Attribute("baseurl", "/riddle-me-this", -1),
        ]).filter(lambda attr: filter_provider()(attr.to_tuple())))

        assert 3 == sequence.len()
        assert 1 == sequence.distinct().len()
        assert sequence.for_all(lambda a: "chatgpt" == a.key)

    def test_a_filter_provider_vs_mock_attributes(self, mock_provider):
        """Test filter versus reference mock attributes in this project."""

        assert ({"site-baseurl",
                 "chatgpt",
                 "cb-hacker",
                 "mailto-rIdd13r",
                 "hera-school",
                 "resume"} == seq(
            mock_provider())
                .filter(lambda attr: filter_provider()(attr.to_tuple()))
                .map(lambda attr: attr.key)
                .to_set())

    def test_b_filter_provider_vs_config_provider(self):
        """Test filter versus real config attributes in this project."""
        keep = filter_provider()
        attributes = seq(config_links_provider(CONF_FILE)())
        kept = attributes.filter(lambda link: keep(link.to_tuple()))

        assert "icons" in attributes.map(lambda link: link.key).to_set()
        assert kept.len() == 15
        assert kept.map(lambda link: link.key).to_set() == attributes.map(lambda link: link.key).to_set() - {"icons", "baseurl"}

    def test_c_filter_provider_vs_both_providers(self, mock_provider):
        """Test filter versus real config attributes in this project joined with the mock attributes."""
        keep = filter_provider()
        attributes = seq([config_links_provider(CONF_FILE)(), mock_provider()]).flatten()
        kept = attributes.filter(lambda link: keep(link.to_tuple()))

        assert kept.len() == 21
        assert kept.map(lambda link: link.key).to_set() == attributes.map(lambda link: link.key).to_set() - {"icons", "baseurl"}