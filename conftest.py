import pytest
from config.settings import Settings
from core.api_client import APIClient
from services.posts_service import PostsService


@pytest.fixture(scope="function")
def settings():
    return Settings()

@pytest.fixture
def api_client(settings):
    client = APIClient(**settings.get_config("demo"))
    yield client
    client.close()

@pytest.fixture
def posts_service(api_client):
    return PostsService(api_client)