from app import create_app, store


def test_health_returns_ok(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_create_task_returns_201_and_task(client):
    res = client.post("/tasks", json={"title": "Write report"})
    assert res.status_code == 201
    body = res.json()
    assert body["title"] == "Write report"
    assert body["status"] == "todo"
    assert isinstance(body["id"], int)


def test_create_task_rejects_empty_title(client):
    res = client.post("/tasks", json={"title": "   "})
    assert res.status_code == 400
    assert res.json()["error"] == "title is required"
