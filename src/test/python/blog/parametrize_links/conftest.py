import shutil
import stat

import pytest
import yaml

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
    chatgpt = Attribute("chatgpt", "https://chat.openai.com/[ChatGPT,window=_blank]", -1)
    return lambda: (chatgpt,)
