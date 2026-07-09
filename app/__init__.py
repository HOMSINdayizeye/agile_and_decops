"""TaskFlow API — FastAPI implementation (migrated from Flask in Sprint 2)."""
from fastapi import FastAPI, HTTPException, status

from app import store
from app import metrics
from app.models import Task, TaskCreate, TaskUpdate
from app.errors import register_exception_handlers
from app.logging_config import configure_logging, LoggingMiddleware

__version__ = "0.3.0"


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title="TaskFlow", version=__version__)
    app.add_middleware(LoggingMiddleware)
    register_exception_handlers(app)

    @app.get("/health")
    def health():
        return {"status": "ok", "version": __version__}

    @app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
    def create_task(payload: TaskCreate):
        title = payload.title.strip()
        if not title:
            raise HTTPException(status_code=400, detail="title is required")
        return store.add_task(title)

    @app.get("/tasks", response_model=list[Task])
    def list_tasks():
        return store.list_tasks()

    @app.patch("/tasks/{task_id}", response_model=Task)
    def update_task(task_id: int, payload: TaskUpdate):
        title = payload.title
        if title is not None:
            title = title.strip()
            if not title:
                raise HTTPException(status_code=400, detail="title must not be empty")
        updated = store.update_task(task_id, title=title, status=payload.status)
        if updated is None:
            raise HTTPException(status_code=404, detail="task not found")
        return updated

    @app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_task(task_id: int):
        if not store.delete_task(task_id):
            raise HTTPException(status_code=404, detail="task not found")
        return None

    @app.get("/metrics")
    def get_metrics():
        return metrics.snapshot(store.count())

    return app
