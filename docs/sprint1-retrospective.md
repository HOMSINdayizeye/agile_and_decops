# Sprint 1 — Retrospective

**What went well**
- Clear backlog and DoD made slicing Sprint 1 (T-1/T-2/T-3) straightforward.
- Thin endpoints + in-memory store kept tests fast (6 tests, <0.1s).
- CI ran the suite automatically, catching issues before manual review.

**What could be better**
- No observability: when a request failed we had no log to inspect.
- No shared error handling — error responses were ad hoc.
- Endpoints mixed routing and logic, which will get messy as CRUD grows.

**Improvements for Sprint 2 (actionable, owned)**
1. **Add centralised structured logging** for every request (method, path,
   status, duration) so operators can debug without code changes. *(T-6)*
2. **Add a global error handler** that returns a tracked `error_id` on `500`
   and logs the exception, so failures are never silent. *(T-6)*
3. **Keep endpoints thin** — push logic into the store/service layer and add
   `update`/`delete` plus a `/metrics` endpoint to finish the CRUD + monitoring
   story. *(T-4, T-5, T-7)*
