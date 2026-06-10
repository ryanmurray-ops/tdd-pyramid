from coin import Coin
from models.coin_model import CoinModel
from models.duty_model import DutyModel

class DatabaseCoinRepository:
    def get_all_coins(self):
        coin_models = CoinModel.select()
        return [
            Coin(
                id=str(coin.id),
                name=coin.name,
                is_complete=coin.is_complete
            )
            for coin in coin_models
        ]

    def create_coin(self, coin):
        CoinModel.create(
            id=coin.id,
            name=coin.name,
            is_complete=coin.is_complete
        )

        return coin
    
    def get_coin_by_id(self, coin_id):
        coin_model = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin_model:
            return None

        return Coin(
            id=str(coin_model.id),
            name=coin_model.name,
            is_complete=coin_model.is_complete
        )

    def update_coin(self, coin_id, is_complete):
        coin_model = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin_model:
            return None
        
        coin_model.is_complete = is_complete
        coin_model.save()

        return Coin(
            id=str(coin_model.id),
            name=coin_model.name,
            is_complete=coin_model.is_complete
        )
    
    def delete_coin(self, coin_id):
        try:
            coin_model = CoinModel.get(CoinModel.id == coin_id)
        except CoinModel.DoesNotExist:
            return False
        
        coin_model.delete_instance()
        return True

    def get_coin_by_name(self, name):
        coin_model = CoinModel.get_or_none(CoinModel.name == name)

        if not coin_model:
            return None
        
        return Coin(
            id=str(coin_model.id),
            name=coin_model.name,
            is_complete=coin_model.is_complete
        )
    
    def get_duties_for_coin(self, coin_id):
        return list(
            DutyModel.select()
            .where(DutyModel.coin == coin_id)
        )

    def create_duty(self, coin_id, duty_number, description):
        existing_duty = DutyModel.get_or_none(
            (DutyModel.coin ==coin_id) &
            (DutyModel.number == duty_number) 
        )

        if existing_duty:
            return None
        
        duty = DutyModel.create(
            coin=coin_id,
            number=duty_number,
            description=description
        )

        return {
            "coin_id": coin_id,
            "number": duty.number,
            "description": duty.description
        }