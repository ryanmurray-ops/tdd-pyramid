from duties import is_duplicate_duty_number


def test_returns_true_when_duplicate_duty_number_exists():
    duties = ["1 - My Firsst Duty"]

    result = is_duplicate_duty_number("1", duties)

    assert result is True