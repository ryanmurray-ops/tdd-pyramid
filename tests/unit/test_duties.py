from duties import is_duplicate_duty_number


def test_returns_true_when_duplicate_duty_number_exists():
    duties = ["1 - My First Duty"]

    result = is_duplicate_duty_number("1", duties)

    assert result is True

def test_returns_false_when_duty_number_is_empty():
    result = is_empty_duty("", "My Duty")

    assert result is False