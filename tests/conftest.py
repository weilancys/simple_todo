import pytest
from simple_todo import create_app

@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()
