# Sprint 2 — Sprint Review

**Goal:** Complete the CRUD lifecycle and add observability, applying the three
Sprint 1 retrospective improvements.

**Delivered stories**

| ID  | Story                       | Status | Evidence |
|-----|-----------------------------|--------|----------|
| T-4 | Update task                 | Done   | `PATCH /tasks/<id>` updates title/status → `200`; `404` if missing; rejects empty title `400` |
| T-5 | Delete task                 | Done   | `DELETE /tasks/<id>` → `204`; `404` if missing; removed from list |
| T-6 | Logging + error tracking    | Done   | Every request logged (method/path/status/ms); `500` returns tracked `error_id` and is logged |
| T-7 | Metrics endpoint            | Done   | `GET /metrics` returns `requests_total`, `requests_by_status`, `tasks_total` |

**Retro improvements applied (from Sprint 1)**
1. ✅ Centralised structured logging → `app/logging_config.py` (request middleware).
2. ✅ Global error handler with tracked `error_id` → `app/errors.py`.
3. ✅ Thin endpoints + service/store layer + `/metrics` → `app/store.py`, `app/metrics.py`.

**Demo (curl)**

```
$ curl -X POST localhost:5000/tasks -H 'Content-Type: application/json' -d '{"title":"Draft RFC"}'
{"id":1,"title":"Draft RFC","status":"todo"}

$ curl -X PATCH localhost:5000/tasks/1 -H 'Content-Type: application/json' -d '{"status":"done"}'
{"id":1,"title":"Draft RFC","status":"done"}

$ curl localhost:5000/metrics
{"requests_total":3,"requests_by_status":{"200":2,"201":1,"204":0},"tasks_total":1}

$ curl -X DELETE localhost:5000/tasks/1 -i | head -1
HTTP/1.1 204 NO CONTENT
```

**Testing evidence:** 15 unit tests passing (`docs/ci-test-run.log`).
**CI evidence:** `.github/workflows/ci.yml` runs the full suite on every push/PR.

**Product Owner acceptance:** Full CRUD + monitoring accepted. Backlog complete
(all 7 stories Done).
