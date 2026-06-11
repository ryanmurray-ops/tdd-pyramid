def test_get_duties_returns_200(client):
    response = client.get("/duties")

    assert response.status_code == 200

def test_get_duties_returns_empty_list(client):
    response = client.get("/duties")

    assert response.status_code == 200
    assert response.json == []