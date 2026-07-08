import logging

from app import create_app


def test_404_returns_json_error(client):
    res = client.get("/does-not-exist")
    assert res.status_code == 404
    assert res.get_json()["error"] == "not found"


def test_internal_error_is_tracked_with_error_id(client, caplog):
    # Force an unhandled exception through a temporary route to exercise the
    # global 500 handler and confirm it returns a trackable error_id.
    app = client.application

    @app.get("/boom")
    def boom():
        raise RuntimeError("kaboom")

    logging.getLogger("taskflow").propagate = True
    caplog.set_level(logging.ERROR, logger="taskflow")
    res = client.get("/boom")

    assert res.status_code == 500
    body = res.get_json()
    assert body["error"] == "internal server error"
    assert "error_id" in body and len(body["error_id"]) == 12
    assert any(
        ("unhandled error id=" + body["error_id"]) in r.message
        for r in caplog.records
    )


def test_request_is_logged(client, caplog):
    logging.getLogger("taskflow").propagate = True
    caplog.set_level(logging.INFO, logger="taskflow")
    client.get("/health")
    assert any("request GET /health" in r.message for r in caplog.records)
