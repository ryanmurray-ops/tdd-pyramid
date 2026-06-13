from models.duty_model import DutyModel

class DatabaseDutyRepository:
    def get_all_duties(self):
        return []
    
    def create_duty(slef, coin_id, number, description):
        duty = DutyModel.create(
            coin=coin_id,
            number=number,
            description=description
        )

        return {
            "coin_id": coin_id,
            "number": duty.number,
            "description": duty.description
        }