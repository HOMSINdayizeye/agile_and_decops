def test_list_tasks_is_empty_initially(client):
    res = client.get("/tasks")
    assert res.status_code == 200
    assert res.json() == []


def test_list_tasks_reflects_created_tasks(client):
    client.post("/tasks", json={"title": "A"})
    client.post("/tasks", json={"title": "B"})
    res = client.get("/tasks")
    titles = [t["title"] for t in res.json()]
    assert titles == ["A", "B"]


def test_list_tasks_returns_array_of_objects(client):
    client.post("/tasks", json={"title": "X"})
    body = client.get("/tasks").json()
    assert isinstance(body, list)
    assert set(body[0].keys()) >= {"id", "title", "status"}
