from app import app

def test_get_coins_returns_200():
    client = app.test_client()
    response = client.get("/coins")
    assert response.status_code == 200

def test_get_coins_returns_empty_list():
    client = app.test_client()
    response = client.get("/coins")
    assert response.status_code == 200
    assert response.json == []

def test_get_all_coins_returns_created_coins():
    client = app.test_client()
    app.coin_service.create_coin("Automate")
    app.coin_service.create_coin("Assemble")
    response = client.get("/coins")
    coins_response = response.get_json()
    assert response.status_code == 200
    assert len(coins_response) == 2
    assert coins_response[0]["name"] == "Automate"
    assert coins_response[1]["name"] == "Assemble"


def test_get_coin_by_id_returns_correct_coin():
    client = app.test_client()
    coin = app.coin_service.create_coin("Automate")
    response = client.get(f"/coins/{coin.id}")
    assert response.status_code == 200
    assert response.json["id"] == coin.id
    assert response.json["name"] == "Automate"

def test_get_coin_by_id_returns_404_and_error_message_when_not_found():
    client = app.test_client()
    response = client.get("/coins/non-existent-id")
    assert response.status_code == 404
    assert response.json["error"] == "Coin not found"

def test_create_coin_via_api_returns_201_and_coin():
    client = app.test_client()
    response = client.post("/coins", json={
        "name": "Automate"
    })
    assert response.status_code == 201
    assert response.json["name"] == "Automate"
    assert "id" in response.json

def test_create_coin_returns_400_when_name_already_exists():
    client = app.test_client()
    client.post("/coins", json={"name": "Automate"})
    response = client.post("/coins", json={"name": "Automate"})
    assert response.status_code == 400

def test_create_coin_returns_error_message_when_name_already_exists():
    client = app.test_client()
    client.post("/coins", json={"name": "Automate"})
    response = client.post("/coins", json={"name": "Automate"})
    assert response.status_code == 400
    assert response.json["error"] == "Coin already exists"

def test_put_coin_endpoint_returns_200():
    coin = app.coin_service.create_coin("Automate")
    client = app.test_client()
    response = client.put(
        f"/coins/{coin.id}",
        json={"is_complete": True}
    )
    assert response.status_code == 200

def test_put_coin_updates_completion_status():
    coin = app.coin_service.create_coin("Automate")
    client = app.test_client()
    client.put(
        f"/coins/{coin.id}",
        json={"is_complete": True}
    )
    assert coin.is_complete == True

def test_put_unknown_coin_returns_404():
    client = app.test_client()
    response = client.put(
        "/coins/{coin.id}",
        json={"is_complete": True}
    )
    assert response.status_code == 404

def test_put_unknown_coin_returns_404():
    client = app.test_client()
    response = client.put(
        "/coins/non-existent-id",
        json={"is_complete": True}
    )
    assert response.status_code == 404

def test_put_unknown_coin_returns_error_message():
    client = app.test_client()
    response = client.put(
        "/coins/non-existent-id",
        json={"is_complete": True}
    )
    coin_update_request = response.get_json()
    assert response.status_code == 404
    assert coin_update_request["error"] == "Coin not found"

def test_delete_coin_endpoint_returns_200():
    coin = app.coin_service.create_coin("Automate")
    client = app.test_client()
    response = client.delete(f"/coins/{coin.id}")  
    assert response.status_code == 200

def test_delete_coin_removes_coin_from_service():
    coin = app.coin_service.create_coin("Automate")
    client = app.test_client()
    client.delete(f"/coins/{coin.id}")
    result = app.coin_service.get_coin_by_id(coin.id)
    assert result is None

def test_delete_unknown_coin_returns_404():
    client = app.test_client()
    response = client.delete("/coins/non-existent-id")
    assert response.status_code == 404

def test_delete_unknown_coin_returns_error_message():
    client = app.test_client()
    response = client.delete("/coins/non-existent-id")
    error_response = response.get_json()
    assert error_response["error"] == "Coin not found"
