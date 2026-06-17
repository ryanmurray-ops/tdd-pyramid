from models.coin_model import CoinModel
from models.duty_model import DutyModel

class CoinService:
    def create_coin(self, name):
        if CoinModel.get_or_none(CoinModel.name == name):
            return {
            "success": False,
            "data": None,
            "error": "Coin already exists"
        }
        
        coin = CoinModel.create(name=name)

        return {
            "success": True,
            "data": coin,
            "error": None
        }
  
    def get_all_coins(self):
        coins = list(CoinModel.select())

        return {
            "success": True,
            "data": coins,
            "error": None
        }

    def get_coin_by_name(self, name):
        coin = CoinModel.get_or_none(CoinModel.name == name)

        return {
            "success": True,
            "data": coin,
            "error": None
        }
    
    def get_coin_by_id(self, coin_id):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        return {
            "success": True,
            "data": coin,
            "error": None
        }
        
    
    def update_completion_status(self, coin_id):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin:
            return None

        coin.is_complete = True
        coin.save()

        return coin

    def assign_duty(self, coin_id, duty_number):
        coin = CoinModel.get_or_none(
            CoinModel.id == coin_id
        )

        duty = DutyModel.get_or_none(
            DutyModel.number == duty_number
        )

        if not coin or not duty:
            return None
        
        if duty in coin.duties:
            return None
        
        coin.duties.add(duty)

        return coin
