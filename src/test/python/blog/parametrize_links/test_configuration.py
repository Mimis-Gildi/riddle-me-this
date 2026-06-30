"""Tests for Configuration — site-level config reader and collection discoverer."""
import pytest
import yaml

from functional import seq

from blog.parametrize_links import SITE_ROOT
from blog.parametrize_links.attribute_providers import GLOBAL_POSITION
from blog.parametrize_links.configuration import Configuration
from conftest import GLOBAL_LINK_KEYS


@pytest.fixture
def real_config():
    return Configuration(SITE_ROOT)


@pytest.fixture
def tmp_config(tmp_path):
    posts = tmp_path / "_posts"
    posts.mkdir()
    (posts / "article.adoc").write_text("= Article\n", encoding="utf-8")
    (tmp_path / "_config.yml").write_text("", encoding="utf-8")
    return tmp_path


@pytest.fixture
def tmp_config_no_asciidoctor(tmp_path):
    posts = tmp_path / "_posts"
    posts.mkdir()
    (posts / "article.adoc").write_text("= Article\n", encoding="utf-8")
    (tmp_path / "_config.yml").write_text("title: My Blog\n", encoding="utf-8")
    return tmp_path


class TestConfigurationConstruction:

    def test_conf_file_path(self, real_config):
        assert real_config.conf_file == SITE_ROOT / "_config.yml"

    def test_missing_site_root_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            Configuration(tmp_path / "nonexistent")

    def test_conf_file_must_exist(self, tmp_path):
        tmp_path.mkdir(exist_ok=True)
        with pytest.raises(FileNotFoundError):
            Configuration(tmp_path)


class TestConfigurationCollections:

    def test_collections_are_paths(self, real_config):
        assert seq(real_config.collections).filter(lambda p: not isinstance(p, __import__('pathlib').Path)).empty()

    def test_collections_all_exist(self, real_config):
        assert seq(real_config.collections).filter(lambda p: not p.exists()).empty()

    def test_collections_contain_posts(self, real_config):
        assert seq(real_config.collections).exists(lambda p: p.name == "_posts")

    def test_collections_contain_pages(self, real_config):
        assert seq(real_config.collections).exists(lambda p: p.name == "_pages")

    def test_collections_all_have_adoc_files(self, real_config):
        assert seq(real_config.collections).filter(
            lambda p: not seq(p.glob("*.adoc")).non_empty()
        ).empty()

    def test_tmp_single_posts_collection(self, tmp_config):
        config = Configuration(tmp_config)
        assert seq(config.collections).map(lambda p: p.name).to_set() == {"_posts"}


class TestConfigurationGlobalLinks:

    def test_global_links_non_empty(self, real_config):
        assert len(real_config.global_links) > 0

    def test_global_links_is_tuple(self, real_config):
        assert isinstance(real_config.global_links, tuple)

    def test_global_links_keys(self, real_config):
        assert GLOBAL_LINK_KEYS <= {a.key for a in real_config.global_links}

    def test_global_links_all_global_position(self, real_config):
        assert seq(real_config.global_links).map(lambda a: a.position).to_set() == {GLOBAL_POSITION}

    def test_empty_config_no_crash(self, tmp_config_no_asciidoctor):
        config = Configuration(tmp_config_no_asciidoctor)
        assert isinstance(config.global_links, tuple)
