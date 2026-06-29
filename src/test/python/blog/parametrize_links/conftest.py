import shutil
import stat

import pytest

from blog.parametrize_links import SLOP_ARTICLE
from blog.parametrize_links.attributes import AttributeProvider, Attribute


@pytest.fixture
def slop_article(tmp_path):
    """Copy the pristine slop article into tmp, set read-only, and return it."""
    copy = tmp_path / SLOP_ARTICLE.name
    shutil.copy(SLOP_ARTICLE, copy)
    copy.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return copy


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
