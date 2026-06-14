class DutyService:
    def __init__(self, repository):
        self.repository = repository

        # TEMPORARY; Flask still depends on this attribute
        # Will be removed once Duties API fully migrates to repository
        self.duties = self.repository.get_all_duties()

    def create_duty(self, number, description):
        if description.strip() == "":
            return None
        
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
        duty = self.repository.get_duty_by_id(duty_id)
        
        if not duty:
            return None
        
        self.repository.delete_duty(duty_id)
        
        return duty

    def update_duty(self, duty_id, data):
        duty = self.repository.get_duty_by_id(duty_id)

        if not duty:
            return None

        if "number" in data:
            return "number_not_allowed"
        
        if "description" in data:
            if data["description"] == "":
                return "empty_description_not_allowed"

        if "description" in data:
            updated_duty = self.repository.update_duty(
                duty_id,
                data["description"]
            )
            return updated_duty

        return duty

    
