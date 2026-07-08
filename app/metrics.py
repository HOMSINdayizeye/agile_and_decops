"""Lightweight in-process metrics.

Counters are incremented by the request logging middleware and exposed via the
`/metrics` endpoint so operators can watch traffic and task volume.
"""
import itertools
import threading

_lock = threading.Lock()
_request_count = 0
_status_counts = {}


def record_request(status_code: int) -> None:
    global _request_count
    with _lock:
        _request_count += 1
        _status_counts[status_code] = _status_counts.get(status_code, 0) + 1


def snapshot(task_count: int) -> dict:
    with _lock:
        return {
            "requests_total": _request_count,
            "requests_by_status": dict(_status_counts),
            "tasks_total": task_count,
        }


def reset_metrics() -> None:
    global _request_count
    with _lock:
        _request_count = 0
        _status_counts.clear()
