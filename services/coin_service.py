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
        
    def update_coin(self, coin_id, is_complete):
        coin = self.get_coin_by_id(coin_id)
        if coin:
            coin.is_complete = is_complete
            return coin
        return None
    
    def delete_coin(self, coin_id):
        coin = self.get_coin_by_id(coin_id)
        if coin:
            self.coins.remove(coin)
            return True
        return None
        
    