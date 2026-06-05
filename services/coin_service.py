from coin import Coin

class CoinService:
    def __init__(self):
        self.coins = []

    def create_coin(self, name):
        for coin in self.coins:
            if coin.name == name:
                return None
            
        coin = Coin(name)
        self.coins.append(coin)
        return coin
    
    def get_coin_by_id(self, coin_id):
        for coin in self.coins:
            if coin.id == coin_id:
                return coin
            return None