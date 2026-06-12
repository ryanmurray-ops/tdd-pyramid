class DutyService:
    def __init__(self, repository):
        self.repository = repository

        # TEMPORARY; Flask still depends on this attribute
        # Will be removed once Duties API fully migrates to repository
        self.duties = self.repository.get_all_duties()

    def create_duty(self, number, description):
        existing_duties = self.repository.get_all_duties()

        for duty in existing_duties:
            if duty["number"] == number:
                return None
            
        return self.repository.create_duty(number, description)
    
    def get_all_duties(self):
        return self.repository.get_all_duties()
    
    def get_duty_by_id(self, duty_id):
        return self.repository.get_duty_by_id(duty_id)
    
    def delete_duty(self, duty_id):
        return self.repository.delete_duty(duty_id)

    def update_duty(self, duty_id, data):
        duty = self.repository.get_duty_by_id(duty_id)

        if not duty:
            return {
                "success": False,
                "error": "Duty not found",
                "status_code": 404
            }
        
        if "number" in data:
            return {
                "success": False,
                "error": "Duty number cannot be changed",
                "status_code": 400
            }

        if "description" in data:
            duty["description"] = data["description"]

        return {
            "success": True,
            "duty": duty
        }