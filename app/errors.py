"""Global error handling and error tracking.

Registers handlers that turn exceptions into tracked, structured 500 responses
so failures are never silent (Sprint 1 retro item #2).
"""
import uuid

from flask import Flask, jsonify

from app.logging_config import get_logger


def register_error_handlers(app: Flask) -> None:
    logger = get_logger()

    @app.errorhandler(404)
    def not_found(err):
        return jsonify(error="not found"), 404

    @app.errorhandler(500)
    def internal_error(err):
        error_id = uuid.uuid4().hex[:12]
        logger.error("unhandled error id=%s: %s", error_id, err, exc_info=True)
        return jsonify(error="internal server error", error_id=error_id), 500
