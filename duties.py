def is_duplicate_duty_number(number, duties):
    for duty in duties:
        if duty.startswith(f"{number} -"):
            return True
    return False

def is_valid_duty_number(number):
    return bool(number)
