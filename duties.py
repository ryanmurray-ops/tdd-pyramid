
from constants import ERRORS
from validators import is_duplicate_duty_number, is_valid_duty_description, is_valid_duty_number

def create_duty(number, description, duties):
    if not is_valid_duty_number(number) and not is_valid_duty_description(description):
        return None, 'Duty number and description are required'
    
    if not is_valid_duty_number(number):
        return None, "Invalid duty number"

    if not is_valid_duty_description(description):
        return None, "Invalid duty description"
    
    if is_duplicate_duty_number(number, duties):
        return None, "Duplicate duty number"

    return f"{number} - {description}", None

def handle_create_duty(number, description, duties):
    duty, error = create_duty(number, description, duties)

    if error in ERRORS:
        return {"success": False, "duty": None, "error": error}
    
    return {"success": True, "duty": duty, "error": None}

