from duties import handle_create_duty

def test_handle_create_duty_success():
    duties = []

    result = handle_create_duty("1", "My First Duty", duties)

    assert result["success"] is True
    assert result["duty"] == "1 - My First Duty"
    assert result ["error"] is None
