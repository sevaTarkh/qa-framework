import pytest

from config.settings import Settings



@pytest.fixture
def settings():
    settings1 = Settings()
    return settings1