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

def test_duty_is_stored_for_coin(app, client):
    coin = app.coin_service.create_coin("Automate")

    client.post(
        f"/coins/{coin.id}/duties",
        json={
            "coin": "Automate",
            "duty_number": "1",
            "description": "My First Duty"
        }
    )

    duties = app.coin_service.repository.get_duties_for_coin(coin.id)

    assert len(duties) == 1
    assert duties[0]["number"] == "1"
    assert duties[0]["description"] == "My First Duty"

def test_cannot_create_duty_for_nonexistent_coin(app, client):
    response = client.post(
        "/coins/999/duties",
        json={
            "duty_number": "1",
            "description": "Should fail"
        }
    )
    
    assert response.status_code == 404

def test_cannont_create_duty_for_nonexistent_coin_and_return_error_message(app, client):
    response = client.post(
        "/coins/999/duties",
        json={
            "duty_number": "1",
            "description": "Should fail"
        }
    )
    
    response_data = response.get_json()

    assert response.status_code == 404
    assert response_data["error"] == 'Coin not found'


def test_cannot_create_duplicate_number_for_the_same_coin(app, client):
    coin = app.coin_service.create_coin("Automate")

    client.post(
        f"/coins/{coin.id}/duties",
        json={
            "duty_number": "1",
            "description": "My First Duty"
        }
    )

    response = client.post(
        f"/coins/{coin.id}/duties",
        json={
            "duty_number": "1",
            "description": "My First Duty"
        }
    )

    assert response.status_code == 409
    assert response.get_json()["error"] == "Duty already exists"