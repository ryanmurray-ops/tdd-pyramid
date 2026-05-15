from duties import create_duty

def test_create_duty_returns_fromatted_string():
    result = create_duty("1", "My First Duty", [])

    assert result == "1 - My First Duty"

def test_create_duty_returns_error_when_duty_number_is_empty():
    duties = []
    result = create_duty("", "My First Duty", duties)

    assert result == "Invalid duty number"

def test_create_duty_returns_error_when_duty_description_is_empty():
    duties = []
    result = create_duty("1", "", duties)

    assert result == "Invalid duty description"

def test_create_duty_returns_error_when_both_input_fields_are_empty():
    duties = []
    result = create_duty("", "", duties)

    assert result == "Duty number and description are required"

def test_create_duty_returns_error_when_duty_number_already_exists():
    duties = ["1 - my First Duty"]
    result = create_duty("1", "Another Duty", duties)

    assert result == "Duplicate duty number"

    