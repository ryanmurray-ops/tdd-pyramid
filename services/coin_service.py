class Coin:
    def __init__(self, name):
        self.name = name

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
    
    def get_all_coins(self):
        return self.coins

    def get_coin_by_name(self, name):
        for coin in self.coins:
            if coin.name == name:
                return coin
        return None