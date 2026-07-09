# TaskFlow — a tiny task-management REST API

TaskFlow is a small **FastAPI** service demonstrating Agile + DevOps practices
across two simulated sprints. It supports creating, listing, updating, and
deleting tasks, plus health, metrics, structured logging, and error tracking.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m app            # uvicorn serves http://localhost:5000
```

## Test

```bash
python -m pytest -v
```

## Endpoints

| Method | Path           | Purpose                          |
|--------|----------------|----------------------------------|
| GET    | `/health`      | Liveness probe (status + version)|
| POST   | `/tasks`       | Create a task                    |
| GET    | `/tasks`       | List all tasks                   |
| PATCH  | `/tasks/<id>`  | Update a task's title/status     |
| DELETE | `/tasks/<id>`  | Delete a task                    |
| GET    | `/metrics`     | Basic usage metrics              |

See `docs/` for the backlog, sprint plans, reviews, and retrospectives.
