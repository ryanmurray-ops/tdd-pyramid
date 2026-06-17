from models.duty_model import DutyModel

class DutyService:
    def __init__(self):
        self.duties = [] # LEGACY (Temporary Phase 1 compatability)

    def create_duty(self, number, description):
        duty = DutyModel.create(
            number=number,
            description=description
        )
        return {
            "success": True,
            "data": duty,
            "error": None
        }
    
    def get_all_duties(self):
        duties = list(DutyModel.select())

        return {
            "success": True,
            "data": duties,
            "error": None
        }
    
    def get_duty_by_number(self, number):
        duties = DutyModel.get_or_none(DutyModel.number == number)

        return {
            "success": True,
            "data": duties,
            "error": None
        }
    
    def update_duty_description(self, number, description):
        duty = DutyModel.get_or_none(
            DutyModel.number == number
        )

        if not duty:
            return None
        
        duty.description = description
        duty.save()

        return {
            "success": True,
            "data": duty,
            "error": None
        }