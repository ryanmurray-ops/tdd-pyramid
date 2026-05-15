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

    with patch("app.handle_create_duty") as mock_handler:
        mock_handler.return_value = {
            "success": True,
            "duty": "1 - My First Duty",
            "error": None
        }

        response = client.post("/", data={
            "number": "1",
            "description": "My First Duty"
        })

        response_text = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "1 - My First Duty" in response_text

        mock_handler.assert_called_once_with(
            "1",
            "My First Duty",
            ANY
        )

def test_home_route_shows_error_for_empty_duty_number():
    client = app.test_client()

    response = client.post("/", data={
        "number": "",
        "description": "My First Duty"
    })

    response_text = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Invalid duty number" in response_text

def test_home_route_shows_error_for_empty_duty_description():
    client = app.test_client()

    response = client.post("/", data={
        "number": "1",
        "description": ""
    })

    response_text = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Invalid duty description" in response_text

def test_home_route_shows_error_when_both_input_fields_are_empty():
    client = app.test_client()
    
    response = client.post("/", data={
        "number": "",
        "description": ""
    })

    html = response.get_data(as_text=True)

    assert "Duty number and description are required" in html

def test_home_route_shows_error_for_duplicate_duty_number():
    client = app.test_client()

    response = client.post("/", data={
        "number": "1",
        "description": "First Duty"
    })

    response = client.post("/", data={
        "number": "1",
        "description": "Duplicate Duty"
    })

    response_text = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Duplicate duty number" in response_text
    assert "1 - Duplicate Duty" not in response_text

def test_home_route_rejects_whitespace_duty_number():
    client = app.test_client()

    response = client.post("/", data={
        "number": " ",
        "description": "Valid description"
    })

    html = response = response.get_data(as_text=True)

    assert "Invalid duty number" in html

def test_home_route_uses_handle_create_duty():
    client = app.test_client()

    with patch("app.handle_create_duty") as mock_handler:
        mock_handler.return_value = {
            "success": True,
            "duty": "1 - My First Duty",
            "error": None
        }

        response = client.post("/", data={
            "number": "1",
            "description": "My First Duty"
        })

        html = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "1 - My First Duty" in html






