def create_duty(number, description, duties):
    if not is_valid_duty_number(number):
        return "Invalid duty number"

    if not is_valid_duty_description(description):
        return "Invalid duty description"
    
    if is_duplicate_duty_number(number, duties):
        return "Duplicate duty number"

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


