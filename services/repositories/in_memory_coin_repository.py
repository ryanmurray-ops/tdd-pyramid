class InMemoryCoinRepository:
    def __init__(self):
        self._coins = []

    def get_all_coins(self):
        return self._coins
    
    def create_coin(self, coin):
        self._coins.append(coin)
    
    def get_coin_by_id(self, coin_id):
        for coin in self._coins:
            if coin.id == coin_id:
                return coin
        
        return None