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

def test_create_duty_returns_201(client):
    response = client.post("/duties", json={
        "number": "D1",
        "description": "My First Duty"
    })

    assert response.status_code == 201

def test_post_creates_duty_and_stores_via_service(app, client):
    response = client.post(
        "/duties",
        json={
            "number": "D1",
            "description": "My First Duty"
        }
    )

    duties = app.duty_service.get_all_duties()

    assert response.status_code == 201
    assert len(duties) == 1
    assert duties[0]["number"] == "D1"
    assert duties[0]["description"] == "My First Duty"

def test_post_duties_returns_400_when_number_missing(client):
    response = client.post(
        "/duties",
        json={
            "description": "My First Duty"
        }
    )

    assert response.status_code == 400

def test_post_duties_returns_error_message_when_number_missing(client):
    response = client.post(
        "/duties",
        json={
            "description": "My First Duty"
        }
    )

    error_response = response.get_json()

    assert response.status_code == 400
    assert error_response["error"] == "Number is required"

def test_post_duties_returns_400_when_description_missing(client):
    response = client.post(
        "/duties",
        json={
            "number": "D1"
        }
    )

    assert response.status_code == 400

def test_post_duties_returns_400_when_description_missing(client):
    response = client.post(
        "/duties",
        json={
            "number": "D1"
        }
    )

    error_response = response.get_json()

    assert response.status_code == 400
    assert error_response["error"] == "Description is required"
    