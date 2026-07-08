# Sprint 2 — Retrospective

**What went well (vs Sprint 1)**
- The three retro actions were all completed: structured logging, tracked
  error handling, and a thin endpoint/service split. This directly improved
  debuggability and testability.
- Test count grew from 6 → 15 with no slowdown (<0.2s); CI stayed green.
- Endpoints stayed small because logic lived in `app/store.py`, making new
  features (update/delete/metrics) quick to add and easy to test.

**What could be better (lessons learned)**
- The in-memory store resets on restart — fine for a prototype, but persistence
  (SQLite/Postgres) would be the next step for a real service.
- CI only runs tests; no build artifact, lint, or coverage gate yet.
- No contract/integration test against a running server (only the Flask test
  client).

**Process improvements for the next iteration**
1. Add a `lint` + `coverage` step to CI and fail the build below a threshold.
2. Persist tasks (e.g., SQLite) so data survives restarts and demos.
3. Add a smoke/integration test that boots the app and hits `/health` + `/metrics`.
4. Tag releases (e.g., `v0.2.0`) at the end of each sprint for traceability.

**Overall reflection**
The two sprints show a clear maturity step: Sprint 1 delivered a minimal MVP
with no observability; Sprint 2 closed that gap by acting on the retrospective.
Commit history demonstrates iterative delivery (one concern per commit) rather
than a big-bang drop.
