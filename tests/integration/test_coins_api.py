from app import app

def test_get_coins_returns_200():
    client = app.test_client()
    response = client.get("/coins")
    assert response.status_code == 200