from duties import create_duty

def test_create_duty_returns_fromatted_string():
    result = create_duty("1", "My First Duty", [])

    assert result == "1 - My First Duty"