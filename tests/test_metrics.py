from app import create_app, store


def test_metrics_reports_task_and_request_counts(client):
    client.post("/tasks", json={"title": "A"})
    client.get("/tasks")
    res = client.get("/metrics")
    assert res.status_code == 200
    body = res.get_json()
    assert body["tasks_total"] == 1
    assert body["requests_total"] >= 2
    assert body["requests_by_status"].get("200") >= 2
