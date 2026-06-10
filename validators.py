def is_valid_duty_number(number):
    return bool(number and number.strip())

def is_valid_duty_description(description):
    return bool(description and description.strip())

def is_valid_duty_number(number):
    return bool(number and number.strip())

def is_duplicate_duty_number(number, duties):
    for duty in duties:

        if isinstance(duty, str):
            duty_number = duty.split(" - ")[0]
            if duty_number == number:
                return True
            
        # in-memory repo format
        if isinstance(duty, dict):
            if duty.get("number") == number:
                return True
    return False

def validate_duty_request(duty_data):
    if not is_valid_duty_number(duty_data.get("duty_number")):
        return "duty_number is required"
    
    if not is_valid_duty_description(duty_data.get("description")):
        return "description is required"
    
    return None