import pytest
import allure
from config.settings import Settings

class TestFrameWork:

    def test_sum(self):
        assert 1 + 1 == 2

    @pytest.mark.parametrize("env", ["dev", "stage"])
    def test_correct_env(self, env, settings: Settings):
        assert ("base_url" in settings.get_config(env).keys() and
                "timeout" in settings.get_config(env).keys())

    @pytest.mark.parametrize("env", ["dev123", "stage123"])
    def test_incorrect_env(self, env, settings: Settings):
        assert settings.get_config(env) == ValueError