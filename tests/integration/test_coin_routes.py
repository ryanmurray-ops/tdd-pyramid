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

def test_can_get_all_coins_via_api():
    client = app.test_client()

    client.post("/coins", json={"name": "Automate"})
    client.post("/coins", json={"name": "Deploy"})

    response = client.get("/coins")
    api_response = response.get_json()

    coin_names = [coin["name"] for coin in api_response["data"]]

    assert response.status_code == 200
    assert api_response["success"] is True
    assert "Automate" in coin_names
    assert "Deploy" in coin_names
    assert api_response["error"] is None

def test_can_get_coin_by_id_via_endpoint():
    client = app.test_client()

    created_coin = client.post("/coins", json={"name": "Automate"})
    coin_data = created_coin.get_json()

    coin_id = coin_data["data"]["id"]

    response = client.get(f"/coins/{coin_id}")
    api_response = response.get_json()

    assert response.status_code == 200
    assert api_response["success"] is True
    assert api_response["data"]["name"] == "Automate"
    assert api_response["error"] is None