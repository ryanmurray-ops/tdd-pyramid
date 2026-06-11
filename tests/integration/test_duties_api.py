def test_get_duties_returns_200(client):
    response = client.get("/duties")

    assert response.status_code == 200

def test_get_duties_returns_empty_list(client):
    response = client.get("/duties")

    assert response.status_code == 200
    assert response.json == []

def test_get_duties_can_return_data_from_services(app, client):
    app.duty_service.create_duty(
        number="D1",
        description="My First Duty"
    )

    response = client.get("/duties")

    assert response.status_code == 200
    assert response.json == [
        {
            "id": response.json[0]["id"],
            "number": "D1",
            "description": "My First Duty"           
        }
    ]