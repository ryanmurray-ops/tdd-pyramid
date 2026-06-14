import uuid

class InMemoryDutyRepository:
    def __init__(self):
        self._duties = []

    def get_all_duties(self):
        return self._duties
    
    def create_duty(self, number, description):
        duty = {
            "id": str(uuid.uuid4()),
            "number": number,
            "description": description
        }

        self._duties.append(duty)
        return duty
    
    def get_duty_by_id(self, duty_id):
        for duty in self._duties:
            if duty["id"] == duty_id:
                return duty
        return None
    
    def delete_duty(self, duty_id):
        for duty in self._duties:
            if duty["id"] == duty_id:
                self._duties.remove(duty)
                return duty

        return None
    
    def update_duty(self, duty_id, description):
        for duty in self._duties:
            if duty["id"] == duty_id:
                duty["description"] = description
                return duty
        return None