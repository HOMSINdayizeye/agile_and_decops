# CI/CD Evidence — Sprint 1

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
tests/test_create_task.py::test_health_returns_ok PASSED                 [ 16%]
tests/test_create_task.py::test_create_task_returns_201_and_task PASSED  [ 33%]
tests/test_create_task.py::test_create_task_rejects_empty_title PASSED   [ 50%]
tests/test_list_tasks.py::test_list_tasks_is_empty_initially PASSED      [ 66%]
tests/test_list_tasks.py::test_list_tasks_reflects_created_tasks PASSED  [ 83%]
tests/test_list_tasks.py::test_list_tasks_returns_array_of_objects PASSED[100%]

============================== 6 passed in 0.04s ==============================
```

**Result:** pipeline would pass (all tests green).
