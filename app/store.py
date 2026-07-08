"""In-memory task store.

Kept deliberately simple (a dict) so the API is easy to test. Swapping this for
a real database later would not change the endpoint layer.
"""
import itertools
import threading

_counter = itertools.count(1)
_lock = threading.Lock()
_tasks = {}


def add_task(title: str, status: str = "todo") -> dict:
    with _lock:
        task_id = next(_counter)
        task = {"id": task_id, "title": title, "status": status}
        _tasks[task_id] = task
    return task


def list_tasks() -> list:
    with _lock:
        return [dict(t) for t in _tasks.values()]


def get_task(task_id: int):
    with _lock:
        task = _tasks.get(task_id)
        return dict(task) if task else None


def reset_store() -> None:
    with _lock:
        _tasks.clear()
