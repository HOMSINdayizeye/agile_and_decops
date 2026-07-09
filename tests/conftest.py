import pytest
from fastapi.testclient import TestClient

from app import create_app, store


@pytest.fixture()
def client():
    store.reset_store()
    # raise_server_exceptions=False lets our 500 handler run and be asserted.
    return TestClient(create_app(), raise_server_exceptions=False)
