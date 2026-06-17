from services.coin_service import CoinService

class CoinController:
    def __init__(self):
        self.service = CoinService()

    def create_coin(self, name):
        return self.service.create_coin(name)
    
    def get_all_coins(self):
        return self.service.get_all_coins()