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

def test_get_coin_by_id_returns_correct_coin():
    client = app.test_client()
    coin = app.coin_service.create_coin("Automate")
    response = client.get(f"/coins/{coin.id}")
    assert response.status_code == 200
    assert response.json["id"] == coin.id
    assert response.json["name"] == "Automate"

def test_get_coin_by_id_returns_404_and_error_message_when_not_found():
    client = app.test_client()
    response = client.get("/coins/fake-id")
    assert response.status_code == 404
    assert response.json["error"] == "Coin not found"
