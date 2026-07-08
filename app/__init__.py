"""TaskFlow API — Sprint 2.

Adds observability (structured request logging + global error tracking) on top
of the Sprint 1 MVP, then the remaining CRUD + metrics endpoints.
"""
from flask import Flask, jsonify, request

from app import store
from app.errors import register_error_handlers
from app.logging_config import configure_logging, request_logging_middleware
from app import metrics

__version__ = "0.2.0"


def create_app() -> Flask:
    configure_logging()
    app = Flask(__name__)

    request_logging_middleware(app)
    register_error_handlers(app)

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=__version__), 200

    @app.post("/tasks")
    def create_task():
        body = request.get_json(silent=True) or {}
        title = (body.get("title") or "").strip()
        if not title:
            return jsonify(error="title is required"), 400
        task = store.add_task(title)
        return jsonify(task), 201

    @app.get("/tasks")
    def list_tasks():
        return jsonify(store.list_tasks()), 200

    @app.get("/metrics")
    def get_metrics():
        return jsonify(metrics.snapshot(len(store.list_tasks()))), 200

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
