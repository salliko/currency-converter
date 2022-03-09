from app.main import app

import pytest

from starlette.testclient import TestClient


@pytest.fixture(scope='module')
def test_app():
    """Функция возвращает тестовый клиент."""
    client = TestClient(app)
    yield client
