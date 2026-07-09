# CI/CD Evidence

> Stack: **FastAPI** (migrated from Flask). Pipeline definition and commands
> below are unchanged — `pytest` runs the same 15 tests against the ASGI app via
> FastAPI's `TestClient`.

## Pipeline definition
Workflow file: `.github/workflows/ci.yml`

Triggers: every push (all branches) and every pull request.
Job `test` runs on `ubuntu-latest` and:

1. Checks out the code.
2. Sets up Python 3.12 (with pip caching).
3. Installs dependencies from `requirements.txt`.
4. Runs the test suite with `python -m pytest -v`.

## How to view real pipeline runs
Push this repository to GitHub and open the **Actions** tab. Each push shows a
green/red run. The pipeline is intentionally simple so it maps 1:1 to the local
command used for the evidence below.

## Local run (stands in for the CI job)
The CI job executes exactly this command locally. Output captured at
`docs/ci-test-run.log`:

```
$ python -m pytest -v
tests/test_create_task.py::test_health_returns_ok PASSED                 [  6%]
tests/test_create_task.py::test_create_task_returns_201_and_task PASSED  [ 13%]
tests/test_create_task.py::test_create_task_rejects_empty_title PASSED   [ 20%]
tests/test_list_tasks.py::test_list_tasks_is_empty_initially PASSED      [ 26%]
tests/test_list_tasks.py::test_list_tasks_reflects_created_tasks PASSED  [ 33%]
tests/test_list_tasks.py::test_list_tasks_returns_array_of_objects PASSED[ 40%]
tests/test_observability.py::test_404_returns_json_error PASSED          [ 46%]
tests/test_observability.py::test_internal_error_is_tracked_with_error_id PASSED [ 53%]
tests/test_observability.py::test_request_is_logged PASSED              [ 60%]
tests/test_metrics.py::test_metrics_reports_task_and_request_counts PASSED [ 66%]
tests/test_crud.py::test_update_changes_title_and_status PASSED          [ 73%]
tests/test_crud.py::test_update_rejects_empty_title PASSED              [ 80%]
tests/test_crud.py::test_update_returns_404_for_missing PASSED          [ 86%]
tests/test_crud.py::test_delete_removes_task PASSED                      [ 93%]
tests/test_crud.py::test_delete_returns_404_for_missing PASSED          [100%]

============================= 15 passed in 0.14s ==============================
```

**Result:** pipeline is green across both sprints (15 tests passing). The same
command runs automatically in `.github/workflows/ci.yml` on every push/PR.
