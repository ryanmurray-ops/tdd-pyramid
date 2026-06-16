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