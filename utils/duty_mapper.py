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
    