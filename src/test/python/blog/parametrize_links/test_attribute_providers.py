"""Tests for the concrete AttributeProvider implementations."""

import yaml
from functional import seq

from blog.parametrize_links import CONF_FILE
from conftest import GLOBAL_LINK_KEYS
from blog.parametrize_links.attribute_providers import global_link_attribute_collecting_provider, config_links_provider, \
    static_links_provider, filter_provider, GLOBAL_POSITION
from blog.parametrize_links.attributes import Attribute


class TestGlobalAttributeProviders:
    """Tests the composite provider that collects static and config link attributes."""

    def test_global_link_attribute_collecting_provider(self):
        """Assert the collector merges static and config providers and applies the filter."""

        assert (seq(global_link_attribute_collecting_provider(
                       static_links_provider(),
                       config_links_provider(CONF_FILE),
                       filter_provider())())
                   .map(lambda attr: attr.key)
                   .to_set()) == GLOBAL_LINK_KEYS


class TestConfigFileAttributeProviders:
    """Tests the provider sourced from the config system of record (`_config.yml`)."""

    def test_mock_config_links_provider(self, mock_provider):
        """A mock standing in for the config provider honors the AttributeProvider contract -- deferred, zero-arg, yields exactly its Attributes with no file IO."""

        mock_state = lambda: seq([
            Attribute("site-baseurl", "/riddle-me-this", -1),
            Attribute("chatgpt", "https://chat.openai.com/[ChatGPT,window=_blank]", -1),
            Attribute("cb-hacker", "http://www.catb.org/jargon/html/H/hacker.html[hacker,window=_blank]", -1),
            Attribute("mailto-rIdd13r", "mailto:rIdd13r@pm.me?subject=Hello%20Riddler%20-%20Let%20us%20compete%3F[rIdd13r@pm.me]", -1),
            Attribute("hera-school", "https://gervi-hera-vitr.github.io/sindri-labs/[Héra Academy Laboratory,window=_blank,opts=nofollow]", -1),
            Attribute("resume", "https://github.com/Mimis-Gildi/riddle-me-this/releases/download/v13.1.0/VadimKuhay-Resume.pdf", -1),
        ]).order_by(lambda attr: attr.key)

        assert seq(mock_provider()).intersection(mock_state()).order_by(lambda a: a.key) == mock_state()

    def test_config_links_provider(self):
        """The provider surfaces exactly the config's `asciidoctor.attributes` -- every key, none extra, all at GLOBAL_POSITION."""
        links = seq(config_links_provider(CONF_FILE)())

        assert links.len() == 55
        assert links.map(lambda link: link.position).to_set() == {GLOBAL_POSITION}
        assert links.map(lambda link: link.key).to_set() == GLOBAL_LINK_KEYS - {"site-baseurl"} | {"icons"}


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

        assert sequence.len() == 3
        assert sequence.distinct().len() == 1
        assert sequence.map(lambda a: a.key).to_set() == {"chatgpt"}

    def test_a_filter_provider_vs_mock_attributes(self, mock_provider):
        """Test filter versus reference mock attributes in this project."""

        assert (seq(mock_provider())
                .filter(lambda attr: filter_provider()(attr.to_tuple()))
                .map(lambda attr: attr.key)
                .to_set()) == {"site-baseurl", "chatgpt", "cb-hacker", "mailto-rIdd13r", "hera-school", "resume"}

    def test_b_filter_provider_vs_config_provider(self):
        """Test filter versus real config attributes in this project."""

        assert (seq(config_links_provider(CONF_FILE)())
                   .filter(lambda attr: filter_provider()(attr.to_tuple()))
                   .map(lambda attr: attr.key)
                   .to_set()) == GLOBAL_LINK_KEYS - {"site-baseurl"}

    def test_c_filter_provider_vs_both_providers(self, mock_provider):
        """Test filter versus real config attributes in this project joined with the mock attributes."""

        assert (seq([config_links_provider(CONF_FILE)(), mock_provider()]).flatten()
                   .filter(lambda attr: filter_provider()(attr.to_tuple()))
                   .map(lambda attr: attr.key)
                   .to_set()) == GLOBAL_LINK_KEYS
