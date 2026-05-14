def create_duty(number, description, duties):
    return f"{number} - {description}"

def is_valid_duty_number(number):
    return bool(number)

def is_valid_duty_description(description):
    return bool(description)

def is_duplicate_duty_number(number, duties):
    for duty in duties:
        if duty.startswith(f"{number} -"):
            return True
    return False


