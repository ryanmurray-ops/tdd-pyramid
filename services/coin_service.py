from models.coin_model import CoinModel
from models.duty_model import DutyModel

class CoinService:
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
    
    def create_coin(self, name):
        if CoinModel.get_or_none(CoinModel.name == name):
            return self._error("Coin already exists")
        
        coin = CoinModel.create(name=name)

        return self._success(coin)
  
    def get_all_coins(self):
        coins = list(CoinModel.select())

        return {
            "success": True,
            "data": coins,
            "error": None
        }

    def get_coin_by_name(self, name):
        coin = CoinModel.get_or_none(CoinModel.name == name)

        if not coin:
            return {
            "success": False,
            "data": None,
            "error": "Coin not found"
        }

        return {
            "success": True,
            "data": coin,
            "error": None
        }
    
    def get_coin_by_id(self, coin_id):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin:
            return {
            "success": False,
            "data": None,
            "error": "Coin not found"
        }

        return {
            "success": True,
            "data": coin,
            "error": None
        }
        
    
    def update_completion_status(self, coin_id):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin:
            return {
                "success": False,
                "data": None,
                "error": "Coin not found"
            }
        
        coin.is_complete = True
        coin.save()

        return {
            "success": True,
            "data": coin,
            "error": None
        }

    def assign_duty(self, coin_id, duty_number):
        coin = CoinModel.get_or_none(
            CoinModel.id == coin_id
        )

        duty = DutyModel.get_or_none(
            DutyModel.number == duty_number
        )

        if not coin:
            return {
            "success": False,
            "data": None,
            "error": "Coin not found"
        }
        
        if not duty:
            return {
            "success": False,
            "data": None,
            "error": "Duty not found"
        }
        
        if duty in coin.duties:
            return {
            "success": False,
            "data": None,
            "error": "Duty already assigned"
        }
        
        coin.duties.add(duty)

        return {
            "success": True,
            "data": coin,
            "error": None
        }
