def test_can_create_duty_for_an_existing_coin(app, client):
    coin = app.coin_service.create_coin("Automate")

    response = client.post(
        f"/coins/{coin.id}/duties",
        json={
            "duty_number": "1",
            "description": "My First Duty"
        }
    )
    
    assert response.status_code == 201
