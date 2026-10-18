from email.policy import default

import pytest
from config.settings import Settings
from core.api_client import APIClient
from services.posts_service import PostsService


@pytest.fixture(scope="function")
def settings():
    return Settings()

@pytest.fixture
def env_name(request):
    return request.config.getoption("--env")

@pytest.fixture
def api_client(settings, env_name):
    client = APIClient(**settings.get_config(env_name))
    yield client
    client.close()

@pytest.fixture
def posts_service(api_client):
    return PostsService(api_client)

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default="demo",
        help="Какой окружение использовать: dev/stage/demo",
    )