from models.duty_model import DutyModel

class DatabaseDutyRepository:
    def get_all_duties(self):
        duties = DutyModel.select()

        return [
            {
                "id": duty.id,
                "coin_id": str(duty.coin.id),
                "number": duty.number,
                "description": duty.description
            }
            for duty in duties
        ]
    
    def create_duty(self, coin_id, number, description):
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