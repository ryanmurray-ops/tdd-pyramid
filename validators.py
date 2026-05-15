def is_valid_duty_number(number):
    return bool(number and number.strip())

def is_valid_duty_description(description):
    return bool(description and description.strip())

def is_duplicate_duty_number(number, duties):
    for duty in duties:
        duty_number = duty.split(" - ")[0]
        if duty_number == number:
            return True
    return False