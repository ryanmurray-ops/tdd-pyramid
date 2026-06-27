def format_duty_response(duty_response):
    return {
        "success": duty_response["success"],
        "data": {
            "id": str(duty_response["data"].id),
            "number": duty_response["data"].number,
            "description": duty_response["data"].description
        },
        "error": duty_response["error"]  
    }

def format_duty_list(duties):
    return [
        {
            "id": str(duty.id),
            "number": duty.number,
            "description": duty.description
        }
        for duty in duties
    ]
    