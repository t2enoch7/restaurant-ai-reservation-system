import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def sample_reservation():
    return {
        "guest_id": "g_456",
        "party_size": 4,
        "requested_time": "2025-07-08T19:00:00Z",
        "preferences": ["quiet", "window"]
    }


def test_create_reservation_success(sample_reservation):
    response = client.post("/reservation/create", json=sample_reservation)
    assert response.status_code == 200
    assert "reservation_id" in response.json()


def test_check_availability():
    response = client.post("/reservation/check", json={
        "party_size": 2,
        "time": "2025-07-08T20:00:00Z"
    })
    assert response.status_code == 200
    assert "available_tables" in response.json()
    assert isinstance(response.json()["available_tables"], list)
