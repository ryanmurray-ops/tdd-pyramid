class InMemoryCoinRepository:
    def __init__(self):
        self._coins = []

    def get_all_coins(self):
        return self._coins
    
    def create_coin(self, coin):
        self._coins.append(coin)