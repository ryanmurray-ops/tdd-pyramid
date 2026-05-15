
from constants import ERRORS

def create_duty(number, description, duties):
    if not is_valid_duty_number(number) and not is_valid_duty_description(description):
        return 'Duty number and description are required'
    
    if not is_valid_duty_number(number):
        return "Invalid duty number"

    if not is_valid_duty_description(description):
        return "Invalid duty description"
    
    if is_duplicate_duty_number(number, duties):
        return "Duplicate duty number"

    return f"{number} - {description}", None

def is_valid_duty_number(number):
    return bool(number and number.strip())

def is_valid_duty_description(description):
    return bool(description and description.strip())

def is_duplicate_duty_number(number, duties):
    for duty in duties:
        if duty.startswith(f"{number} -"):
            return True
    return False

def handle_create_duty(number, description, duties):
    duty, error = create_duty(number, description, duties)

    if error in ERRORS:
        return {"success": False, "duty": None, "error": error}
    
    return {"success": True, "duty": duty, "error": None}

