from validators import is_valid_duty_description, is_valid_duty_number


def test_is_valid_duty_number_returns_true_for_valid_input():
    result = is_valid_duty_number("1")

    assert result is True

def test_is_valid_duty_description_returns_true_for_valid_input():
    result = is_valid_duty_description("My First Duty")

    assert result is True