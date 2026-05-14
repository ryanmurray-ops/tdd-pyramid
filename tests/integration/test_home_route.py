from app import app
def test_huser_can_create_duty_via_home_route():
    client = app.test_client()

    response = client.post("/", data={
        "number": "1",
        "description": "My First Duty"
    })

    assert response.status_code == 200