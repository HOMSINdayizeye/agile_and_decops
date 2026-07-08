import pytest

from app import create_app, store


@pytest.fixture()
def client():
    store.reset_store()
    app = create_app()
    return app.test_client()
