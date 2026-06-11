def test_get_duties_returns_200(client):
    response = client.get("/duties")

    assert response.status_code == 200