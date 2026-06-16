from models.duty_model import DutyModel

class DutyService:
    def __init__(self):
        self.duties = [] # LEGACY (Temporary Phase 1 compatability)

    def create_duty(self, number, description):
        duty = DutyModel.create(
            number=number,
            description=description
        )
        return duty
    
    def get_all_duties(self):
        return list(DutyModel.select())
    
    def get_duty_by_number(self, number):
        return DutyModel.get_or_none(
            DutyModel.number == number
        )
    
    def update_duty_description(self, number, description):
        duty = DutyModel.get_or_none(
            DutyModel.number == number
        )

        if not duty:
            return None
        
        duty.description = description
        duty.save()

        return duty