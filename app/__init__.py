"""TaskFlow API — Sprint 1 scaffold.

Minimal Flask application exposing a health endpoint.
Endpoints for tasks are added in later iterations.
"""
from flask import Flask, jsonify

__version__ = "0.1.0"


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=__version__), 200

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
