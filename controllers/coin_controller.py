from services.coin_service import CoinService

class CoinController:
    def __init__(self):
        self.service = CoinService()

    def create_coin(self, name, duties):
        return self.service.create_coin(name, duties)
    
    def get_all_coins(self):
        return self.service.get_all_coins()
    
    def get_coin_by_name(self, name):
        return self.service.get_coin_by_name(name)

    def get_coin_by_id(self, coin_id):
        return self.service.get_coin_by_id(coin_id)
    
    def update_completion_status(self, coin_id):
        return self.service.update_completion_status(coin_id)