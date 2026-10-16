import pytest

from config.settings import Settings



@pytest.fixture(scope="session")
def settings():
    settings1 = Settings()
    return settings1