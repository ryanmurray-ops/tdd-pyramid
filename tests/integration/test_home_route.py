from app import app
def test_huser_can_create_duty_via_home_route():
    client = app.test_client()

    response = client.post("/", data={
        "number": "1",
        "description": "My First Duty"
    })

    assert response.status_code == 200

def test_user_can_create_duty_via_home_route():
    client = app.test_client()

    response = client.post("/", data={
        "number": "1",
        "description": "My First Duty"
    })

    response_text = response.get_data(as_text=True)

    assert "1 - My First Duty" in response_text