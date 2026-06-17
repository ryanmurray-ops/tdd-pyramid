from models.duty_model import DutyModel

class DutyService:
    def __init__(self):
        self.duties = [] # LEGACY (Temporary Phase 1 compatability)

    def _success(self, data):
        return {
            "success": True,
            "data": data,
            "error": None
        }
    
    def _error(self, message):
        return {
            "success": False,
            "data": None,
            "error": message
        }

    def create_duty(self, number, description):
        existing_duty = DutyModel.get_or_none(DutyModel.number == number)

        if existing_duty:
            return self._error("Duty already exists")
        
        duty = DutyModel.create(number=number,description=description)
        
        return self._success(duty)
    
    def get_all_duties(self):
        duties = list(DutyModel.select())

        return self._success(duties)
    
    def get_duty_by_number(self, number):
        duty = DutyModel.get_or_none(DutyModel.number == number)

        if not duty:
            return self._error("Duty not found")

        return self._success(duty)
    
    def update_duty_description(self, number, description):
        duty = DutyModel.get_or_none(DutyModel.number == number)

        if not duty:
            return {
            "success": False,
            "data": None,
            "error": "Duty not found"
        }
        
        duty.description = description
        duty.save()

        return {
            "success": True,
            "data": duty,
            "error": None
        }