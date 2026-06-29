import uuid
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

def test_create_coin_returns_error_when_coin_already_exists_via_api():
    client = app.test_client()

    client.post("/coins", json={"name": "Automate"})

    create_coin = client.post("/coins", json={"name": "Automate"})
    api_response = create_coin.get_json()

    assert create_coin.status_code == 400
    assert api_response["success"] is False
    assert api_response["data"] is None
    assert api_response["error"] == "Coin already exists"

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

def test_can_get_coin_by_id_via_api():
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

def test_get_coin_by_id_returns_error_when_coin_not_found():
    client = app.test_client()

    response = client.get(f"/coins/{uuid.uuid4()}")

    api_response = response.get_json()

    assert response.status_code == 404
    assert api_response["success"] is False
    assert api_response["data"] is None
    assert api_response["error"] == "Coin not found"

def test_can_delete_coin_via_api():
    client = app.test_client()

    created_coin = client.post("/coins", json={"name": "Automate"})
    coin_data = created_coin.get_json()

    coin_id = coin_data["data"]["id"]

    delete_response = client.delete(f"/coins/{coin_id}")
    api_response = delete_response.get_json()

    assert delete_response.status_code == 200
    assert api_response["success"] is True
    assert api_response["data"] == "Coin deleted"
    assert api_response["error"] is None

def test_delete_coin_returns_error_when_coin_not_found():
    client = app.test_client()

    delete_response = client.delete(f"/coins/{uuid.uuid4()}")

    api_response = delete_response.get_json()

    assert delete_response.status_code == 404
    assert api_response["success"] is False
    assert api_response["data"] is None
    assert api_response["error"] == "Coin not found"

def test_can_update_coin_via_api():
    client = app.test_client()

    created_coin = client.post("/coins", json={"name": "Automate"})
    coin_data = created_coin.get_json()

    coin_id = coin_data["data"]["id"]

    update_response = client.put(f"/coins/{coin_id}", json={"name": "Deploy"})
    api_response = update_response.get_json()

    assert update_response.status_code == 200
    assert api_response["success"] is True
    assert api_response["data"]["name"] == "Deploy"
    assert api_response["error"] is None

def test_update_coin_returns_error_when_coin_not_found():
    client = app.test_client()

    update_response = client.put(f"/coins/{uuid.uuid4()}", json={"name": "Deploy"})
    api_response = update_response.get_json()

    assert update_response.status_code == 404
    assert api_response["success"] is False
    assert api_response["data"] is None
    assert api_response["error"] == "Coin not found"

def test_update_coin_returns_error_when_coin_already_exists():
    client = app.test_client()

    coin1 = client.post("/coins", json={"name": "Automate"}) 
    coin2 = client.post("/coins", json={"name": "Deploy"}) 

    coin2_id = coin2.get_json()["data"]["id"]

    update_response = client.put(f"/coins/{coin2_id}", json={"name": "Automate"})

    api_response = update_response.get_json()

    assert update_response.status_code == 400
    assert api_response["success"] is False
    assert api_response["data"] is None
    assert api_response["error"] == "Coin already exists"

def test_can_create_coin_with_duties_via_api():
    client = app.test_client()

    client.post("/duties", json={
        "number": "D5",
        "description": "CI/CD Pipeline"
    })

    response = client.post("/coins", json={
        "name": "Automate",
        "duties": ["D5"]
    })

    api_response = response.get_json()

    duty_numbers = [duty["number"] for duty in api_response["data"]["duties"]]

    assert response.status_code == 201
    assert api_response["success"] is True
    assert api_response["data"]["name"] == "Automate"

    assert "D5" in duty_numbers
    assert api_response["error"] is None

def test_create_coin_requires_at_least_one_duty():
    client = app.test_client()

    response = client.post("/coins", json={"name": "Automate"})

    api_response = response.get_json()

    assert response.status_code == 400
    assert api_response["success"] is False
    assert api_response["data"] is None
    assert api_response["error"] == "Coin must have at least one duty"