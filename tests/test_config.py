import pytest
import allure
from config.settings import Settings


@allure.epic("Фреймворк")
@allure.feature('Конфигурация')
class TestFrameWork:

    @allure.title('Проверка корректности содержимого окружений')
    @pytest.mark.parametrize("env", ["dev", "stage"])
    def test_correct_env(self, env, settings: Settings):
        config = settings.get_config(env)
        assert "base_url" in config and "timeout" in config

    @allure.title('Проверка ошибки при несуществующем окружении')
    @pytest.mark.parametrize("env", ["dev123", "stage123"])
    def test_incorrect_env(self, env, settings: Settings):
        with pytest.raises(ValueError, match="Такого окружения нет, вот доступные"):
            settings.get_config(env)

    @allure.title('Проверка разности urlов в окружениях')
    def test_different_urls_in_stages(self, settings: Settings):
        assert settings.get_config("dev")["base_url"] != settings.get_config("stage")["base_url"]
