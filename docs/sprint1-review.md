# Sprint 1 — Sprint Review

**Goal:** Deliver a usable MVP — create and read tasks with a working CI pipeline.

**Delivered stories**

| ID  | Story           | Status | Evidence |
|-----|-----------------|--------|----------|
| T-1 | Health endpoint | Done   | `GET /health` → `200 {"status":"ok","version":"0.1.0"}` |
| T-2 | Create task     | Done   | `POST /tasks` → `201`; rejects empty title with `400` |
| T-3 | List tasks      | Done   | `GET /tasks` → `200` array reflecting created tasks |

**Demo (example requests via the Flask test client / curl)**

```
$ curl localhost:5000/health
{"status":"ok","version":"0.1.0"}

$ curl -X POST localhost:5000/tasks -H 'Content-Type: application/json' -d '{"title":"Ship demo"}'
{"id":1,"title":"Ship demo","status":"todo"}

$ curl localhost:5000/tasks
[{"id":1,"title":"Ship demo","status":"todo"}]
```

**Testing evidence:** 6 unit tests passing (`docs/ci-test-run.log`).
**CI evidence:** `.github/workflows/ci.yml` runs the suite on every push/PR.

**Not done this sprint:** update, delete, logging/metrics (carried to Sprint 2).

**Product Owner acceptance:** MVP accepted — the core create/read loop works and
is protected by automated tests in CI.
