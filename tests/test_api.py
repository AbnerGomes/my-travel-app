from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_miles_calculator():
    response = client.get("/milhas/calculadora?price=4500&miles=30000")
    assert response.status_code == 200
    data = response.json()
    assert data["cpm"] == 150.0
    assert data["label"] == "bom"
