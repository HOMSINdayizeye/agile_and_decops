# TaskFlow — Product Vision

**TaskFlow** is a lightweight REST API that lets a small team create, track,
update, and delete tasks so they always know what needs doing and what is done.

> Vision (1 sentence): A tiny, reliable task-management service that any client
> (CLI, web, or mobile) can use to manage a shared to-do list through a clean
> HTTP API.

---

# Definition of Done (DoD)

A backlog item is **Done** only when **all** of the following are true:

1. Code implements the story and meets its Acceptance Criteria.
2. Unit (and integration where applicable) tests are written and **pass**.
3. New code is covered by the CI pipeline and the pipeline is green.
4. Logging/observability is added for the new behaviour (no silent failures).
5. The change is committed with a clear, descriptive message (iterative commits).
6. Documentation (README / endpoint notes) is updated if behaviour changed.
7. Product Owner accepts the demo in the Sprint Review.

---

# Product Backlog

Relative sizing uses Fibonacci story points (1, 2, 3, 5, 8).
Priority: **P1** (must have) → **P3** (nice to have).

| ID  | User Story                                                                 | Priority | Points | Acceptance Criteria (summary)                                                                 |
|-----|----------------------------------------------------------------------------|----------|--------|-----------------------------------------------------------------------------------------------|
| T-1 | As a user I want a health endpoint so I know the service is alive         | P1       | 1      | `GET /health` returns `200` with `{"status":"ok"}`; includes uptime/version.                  |
| T-2 | As a user I want to create a task so I can capture work to do              | P1       | 3      | `POST /tasks` with `{title}` returns `201` + created task with `id`, `status="todo"`. Rejects empty title with `400`. |
| T-3 | As a user I want to list tasks so I can see my to-do list                  | P1       | 2      | `GET /tasks` returns `200` with an array; reflects created tasks.                             |
| T-4 | As a user I want to update a task so I can change title/status             | P2       | 3      | `PATCH /tasks/<id>` updates fields; returns `200`; `404` when missing.                        |
| T-5 | As a user I want to delete a task so I can remove completed/irrelevant ones| P2       | 2      | `DELETE /tasks/<id>` returns `204`; `404` when missing; subsequent GET omits it.              |
| T-6 | As an operator I want structured logs + error tracking so I can debug      | P3       | 3      | Every request is logged; errors return `500` with a tracked error id and are logged.         |
| T-7 | As an operator I want a metrics endpoint so I can monitor usage            | P3       | 2      | `GET /metrics` returns task count + request counters as JSON.                                 |

**Prioritised order (for sprint planning):** T-1 → T-2 → T-3 → T-4 → T-5 → T-6 → T-7

---

# Sprint Plans

## Sprint 1 (Execution)
Goal: Deliver a usable MVP — create and read tasks with a working CI pipeline.

| ID  | Story            | Points |
|-----|------------------|--------|
| T-1 | Health endpoint  | 1      |
| T-2 | Create task      | 3      |
| T-3 | List tasks       | 2      |
|     | **Total**        | **6**  |

Definition of Done applies. CI must run the test suite on every push.

## Sprint 2 (Execution & Improvement)
Goal: Complete the CRUD lifecycle and add observability, applying Sprint 1 retro items.

| ID  | Story                | Points |
|-----|----------------------|--------|
| T-4 | Update task          | 3      |
| T-5 | Delete task          | 2      |
| T-6 | Logging + error track| 3      |
| T-7 | Metrics endpoint     | 2      |
|     | **Total**            | **10** |

Retro improvements carried in from Sprint 1 (see `docs/sprint1-retrospective.md`):
1. Add centralised structured logging from the start.
2. Add a shared error handler so failures are tracked and never silent.
3. Keep endpoints thin and delegate logic to a service layer (testability).
