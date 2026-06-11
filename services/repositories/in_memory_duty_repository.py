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
    