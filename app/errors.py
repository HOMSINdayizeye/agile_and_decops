"""Global exception handlers and error tracking (FastAPI).

Maps HTTP exceptions to a consistent `{"error": ...}` JSON shape and turns
unhandled exceptions into tracked 500 responses so failures are never silent
(Sprint 1 retro item #2).
"""
import logging
import uuid

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.logging_config import get_logger


def register_exception_handlers(app: FastAPI) -> None:
    logger = get_logger()

    @app.exception_handler(StarletteHTTPException)
    async def http_exc_handler(request: Request, exc: StarletteHTTPException):
        msg = "not found" if exc.status_code == 404 else exc.detail
        return JSONResponse(status_code=exc.status_code, content={"error": msg})

    @app.exception_handler(Exception)
    async def unhandled_exc_handler(request: Request, exc: Exception):
        error_id = uuid.uuid4().hex[:12]
        logger.error("unhandled error id=%s: %s", error_id, exc, exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"error": "internal server error", "error_id": error_id},
        )
