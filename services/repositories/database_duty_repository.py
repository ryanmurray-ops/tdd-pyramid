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
            "id": duty.id,
            "coin_id": coin_id,
            "number": duty.number,
            "description": duty.description
        }
    
    def get_duty_by_id(self, duty_id):
        duty = DutyModel.get_or_none(DutyModel.id == duty_id)

        return {
            "id": duty.id,
            "coin_id": str(duty.coin.id),
            "number": duty.number,
            "description": duty.description
        }
    
    def delete_duty(self, duty_id):
        duty = DutyModel.get_or_none(DutyModel.id == duty_id)

        duty.delete_instance()

        return True