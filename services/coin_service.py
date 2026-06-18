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

        return self._success(coins)

    def get_coin_by_name(self, name):
        coin = CoinModel.get_or_none(CoinModel.name == name)

        if not coin:
            return self._error("Coin not found")

        return self._success(coin)
    
    def get_coin_by_id(self, coin_id):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin:
            return self._error("Coin not found")

        return self._success(coin)
        
    
    def update_completion_status(self, coin_id):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin:
            return self._error("Coin not found")
        
        coin.is_complete = True
        coin.save()

        return self._success(coin)
    
    def delete_coin(self, coin_id):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin:
            return self._error("Coin not found")
        
        coin.delete_instance()

        return self._success("Coin deleted")

    def update_coin(self, coin_id, update_data):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin:
            return self._error("Coin not found")
        
        existing_coin = CoinModel.get_or_none(CoinModel.name == update_data)

        if existing_coin:
            return self._error("Coin already exists")
        
        coin.name = update_data
        coin.save()

        return self._success(coin)

    def assign_duty(self, coin_id, duty_number):
        coin = CoinModel.get_or_none(CoinModel.id == coin_id)

        duty = DutyModel.get_or_none(DutyModel.number == duty_number)

        if not coin:
            return self._error("Coin not found")
        
        if not duty:
            return self._error("Duty not found")
        
        if duty in coin.duties:
            return self._error("Duty already assigned")
         
        coin.duties.add(duty)

        return self._success(coin)
