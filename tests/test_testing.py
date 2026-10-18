import pytest
from config.settings import Settings

class TestFrameWork:

    def test_sum(self):
        assert 1 + 1 == 2

    @pytest.mark.parametrize("env", ["dev", "stage"])
    def test_correct_env(self, env, settings: Settings):
        assert ("base_url" in settings.get_config(env) and
                "timeout" in settings.get_config(env))

    @pytest.mark.parametrize("env", ["dev123", "stage123"])
    def test_incorrect_env(self, env, settings: Settings):
        with pytest.raises(ValueError, match=f"Такого окружения нет, вот доступные {settings.config}"):
            settings.get_config(env)

    def test_different_urls_in_stages(self, settings: Settings):
        assert settings.get_config("dev")["base_url"] != settings.get_config("stage")["base_url"]
