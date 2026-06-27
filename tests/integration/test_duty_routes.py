from app import app

def test_can_create_duty_via_api():
    client = app.test_client()

    response = client.post(
        "/duties",
        json={
            "number": "D5",
            "description": "CI/CD Pipeline"
        }
    )

    api_repsonse = response.get_json()

    assert response.status_code == 201
    assert api_repsonse["success"] is True
    assert api_repsonse["data"]["number"] == "D5"
    assert api_repsonse["data"]["description"] == "CI/CD Pipeline"
    assert api_repsonse["error"] is None

def test_can_get_all_duties_via_api():
    client = app.test_client()

    client.post("/duties", json={
        "number": "D5",
        "description": "CI/CD Pipeline"
    })

    client.post("/duties", json={
        "number": "D7",
        "description": "Monitoring"
    })

    response = client.get("/duties")

    api_response = response.get_json()

    duty_numbers = [duty["number"] for duty in api_response["data"]]

    assert response.status_code == 200
    assert api_response["success"] is True
    assert "D5" in duty_numbers
    assert "D7" in duty_numbers
    assert api_response["error"] is None

def test_can_get_duty_by_number_via_api():
    client = app.test_client()

    client.post("/duties", json={
        "number": "D5",
        "description": "CI/CD Pipeline"
    })

    response = client.get("/duties/D5")

    api_response = response.get_json()

    assert response.status_code == 200
    assert api_response["success"] is True
    assert api_response["data"]["number"] == "D5"
    assert api_response["data"]["description"] == "CI/CD Pipeline"
    assert api_response["error"] is None

def test_get_duty_by_number_returns_404_when_duty_not_found():
    client = app.test_client()

    response = client.get("/duties/Non-Existent-Duty")

    api_response = response.get_json()

    assert response.status_code == 404
    assert api_response["success"] is False
    assert api_response["data"] is None
    assert api_response["error"] == "Duty not found"

def test_can_update_duty_description_via_api():
    client = app.test_client()

    client.post("/duties", json={
        "number": "D5",
        "description": "CI/CD Pipeline"
    })

    response = client.put("/duties/D5", json={
        "description": "Updated Description"
    })

    api_response = response.get_json()

    assert response.status_code == 200
    assert api_response["success"] is True
    assert api_response["data"]["number"] == "D5"
    assert api_response["data"]["description"] == "Updated Description"
    assert api_response["error"] is None 
