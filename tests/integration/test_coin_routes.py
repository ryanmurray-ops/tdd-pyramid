from app import app


def test_can_create_coin_via_api():
    client = app.test_client()

    response = client.post("/coins", json={
        "name": "Automate"
    })

    data = response.get_json()

    assert response.status_code == 201
    assert data["success"] is True
    assert data["data"]["name"] == "Automate"
    assert data["error"] is None