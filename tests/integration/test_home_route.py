from app import app
from unittest.mock import ANY, patch

def test_home_route_returns_200():
    client = app.test_client()

    response = client.post("/", data={
        "number": "1",
        "description": "My First Duty"
    })

    assert response.status_code == 200

def test_user_can_create_duty_via_home_route():
    client = app.test_client()

    with patch("app.create_duty") as mock_create_duty:
        mock_create_duty.return_value = "1 - My First Duty"

        response = client.post("/", data={
            "number": "1",
            "description": "My First Duty"
        })

        response_text = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "1 - My First Duty" in response_text

        mock_create_duty.assert_called_once_with(
            "1",
            "My First Duty",
            ANY
        )
