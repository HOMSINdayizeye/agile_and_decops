from app import create_app, store


def _create(client, title="Task"):
    return client.post("/tasks", json={"title": title}).json()["id"]


def test_update_changes_title_and_status(client):
    task_id = _create(client)
    res = client.patch(f"/tasks/{task_id}", json={"title": "Renamed", "status": "done"})
    assert res.status_code == 200
    body = res.json()
    assert body["title"] == "Renamed"
    assert body["status"] == "done"


def test_update_rejects_empty_title(client):
    task_id = _create(client)
    res = client.patch(f"/tasks/{task_id}", json={"title": "   "})
    assert res.status_code == 400


def test_update_returns_404_for_missing(client):
    res = client.patch("/tasks/999", json={"status": "done"})
    assert res.status_code == 404


def test_delete_removes_task(client):
    task_id = _create(client)
    res = client.delete(f"/tasks/{task_id}")
    assert res.status_code == 204
    assert all(t["id"] != task_id for t in client.get("/tasks").json())


def test_delete_returns_404_for_missing(client):
    res = client.delete("/tasks/999")
    assert res.status_code == 404
