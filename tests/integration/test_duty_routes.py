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