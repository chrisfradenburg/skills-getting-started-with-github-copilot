from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_delete_participant_removes_email_from_activity():
    response = client.delete(
        "/activities/Chess%20Club/participants?email=michael@mergington.edu"
    )

    assert response.status_code == 200
    payload = response.json()
    assert "michael@mergington.edu" not in payload["participants"]

    # restore state for later tests
    client.post(
        "/activities/Chess%20Club/signup?email=michael@mergington.edu"
    )
