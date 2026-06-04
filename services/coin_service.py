from coin import Coin

class CoinService:
    def __init__(self):
        self.coins = []

    def create_coin(self, name):
        coin = Coin(name)
        self.coins.append(coin)
        return coin