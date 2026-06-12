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

def test_post_duties_returns_400_when_number_and_description_missing(client):
    response = client.post(
        "/duties", json={}
    )

    assert response.status_code == 400

def test_post_duties_returns_400_when_number_and_description_missing(client):
    response = client.post(
        "/duties", json={}
    )

    error_response = response.get_json()

    assert response.status_code == 400
    assert error_response["error"] == "Number and Description are required"
  
def test_post_duties_rejects_duplicate_number(app, client):
    app.duty_service.create_duty(
        number="D1",
        description="My First Duty"
    )

    response = client.post("/duties", json={
        "number": "D1",
        "description": "Duplicate Duty"
    })

    assert response.status_code == 400
    assert response.get_json()["error"] == "Duty already exists"

def test_get_single_duty_endpoint_returns_200_when_exists(app, client):
    duty = app.duty_service.create_duty(
        number="D1",
        description="My First Duty"
    )

    response = client.get(f"/duties/{duty['id']}")

    assert response.status_code == 200

def test_get_single_duty_endpoint_returns_correct_data(app, client):
    duty = app.duty_service.create_duty(
        number="D1",
        description="My First Duty"
    )

    response = client.get(f"/duties/{duty['id']}")
    response_data = response.get_json()

    assert response.status_code == 200
    assert response_data["number"] == "D1"
    assert response_data["description"] == "My First Duty"

def test_get_single_duty_returns_404_when_not_found(client):
    response = client.get("/duties/non-existent-id")

    assert response.status_code == 404

def test_get_single_duty_returns_404_when_not_found(client):
    response = client.get("/duties/non-existent-id")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Duty not found"

def test_delete_duty_returns_200_when_exists(app, client):
    duty = app.duty_service.create_duty("D1", "My First Duty")
    
    response = client.delete(f"/duties/{duty['id']}")

    assert response.status_code == 200