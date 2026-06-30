import shutil
import stat

import pytest

from blog.parametrize_links import SLOP_ARTICLE, FULL_ARTICLE
from blog.parametrize_links.attributes import AttributeProvider, Attribute

GLOBAL_LINK_KEYS = {
    "site-baseurl", "cb-hacker", "cb-mundane", "chatgpt", "hera-school", "hera-school-url",
    "mailto-rIdd13r", "openai", "openai-blog", "profile-li", "li-newsletter",
    "fireship-gemini3", "gitomer-book", "mcp-overview",
    "mit-article-url", "mit-article-title", "mit-article",
    "rdd13r-gh", "rdd13r-gh-io", "rdd13r-gh-io-url", "rdd13r-gh-io-title",
    "release", "resume", "total-recall", "org-mimis-gildi",
    "hacker-culture-url", "hacker-culture", "dolly-2",
    "openrouter", "openrouter-rankings", "openrouter-url",
    "artificial-analysis", "commons-john-frum-effigy", "deepinfra", "fireworks-ai",
    "kimi-k2-thinking", "llama-cpp", "lm-studio", "mit-genai-divide", "mit-hbr",
    "ollama", "together-ai", "vailala", "rdd13r-style-guide",
}


@pytest.fixture
def slop_article(tmp_path):
    """Copy the pristine slop article into tmp, set read-only, and return it."""
    copy = tmp_path / SLOP_ARTICLE.name
    shutil.copy(SLOP_ARTICLE, copy)
    copy.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return copy

@pytest.fixture
def full_article(tmp_path):
    """Copy a thick article into tmp, set read-only, and return it."""
    full_copy = tmp_path / FULL_ARTICLE.name
    shutil.copy(FULL_ARTICLE, full_copy)
    full_copy.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return full_copy


@pytest.fixture
def mock_provider() -> AttributeProvider:
    """Stand-in global provider: a zero-arg callable yielding Attributes, executed later (deferred)."""
    some_links_ = (
        Attribute("site-baseurl", "/riddle-me-this", -1),
        Attribute("chatgpt", "https://chat.openai.com/[ChatGPT,window=_blank]", -1),
        Attribute("cb-hacker", "http://www.catb.org/jargon/html/H/hacker.html[hacker,window=_blank]", -1),
        Attribute("mailto-rIdd13r", "mailto:rIdd13r@pm.me?subject=Hello%20Riddler%20-%20Let%20us%20compete%3F[rIdd13r@pm.me]", -1),
        Attribute("hera-school", "https://gervi-hera-vitr.github.io/sindri-labs/[Héra Academy Laboratory,window=_blank,opts=nofollow]", -1),
        Attribute("resume", "https://github.com/Mimis-Gildi/riddle-me-this/releases/download/v13.1.0/VadimKuhay-Resume.pdf", -1),
    )
    return lambda: some_links_
