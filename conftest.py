import pytest
from config.settings import Settings
from core.api_client import APIClient


@pytest.fixture(scope="function")
def settings():
    return Settings()

@pytest.fixture
def api_client(settings):
    client = APIClient(**settings.get_config("demo"))
    yield client
    client.close()