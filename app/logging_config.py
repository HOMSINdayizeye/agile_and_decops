"""Structured logging configuration.

Provides a single configured logger used across the app and a Flask hook that
logs every request (method, path, status, duration) — the observability gap
called out in the Sprint 1 retrospective.
"""
import logging
import time

from app import metrics

LOGGER_NAME = "taskflow"


def configure_logging(level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s [taskflow] %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
    )
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger


def get_logger() -> logging.Logger:
    return logging.getLogger(LOGGER_NAME)


def request_logging_middleware(app) -> None:
    """Log method, path, status and duration for every request."""

    @app.before_request
    def _start_timer():
        from flask import g

        g._start = time.perf_counter()

    @app.after_request
    def _log_request(response):
        from flask import g, request

        duration_ms = (time.perf_counter() - getattr(g, "_start", time.perf_counter())) * 1000
        get_logger().info(
            "request %s %s -> %s (%.1f ms)",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
        )
        metrics.record_request(response.status_code)
        return response
