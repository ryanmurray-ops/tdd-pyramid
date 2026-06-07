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
    
    def get_coin_by_name(self, name):
        for coin in self._coins:
            if coin.name == name:
                return coin
            
        return None
    
    def update_coin(self, coin_id, is_complete):
        for coin in self._coins:
            if coin.id == coin_id:
                coin.is_complete = is_complete
                return coin
            
        return None
    
    def delete_coin(self, coin_id):
        for coin in self._coins:
            if coin.id == coin_id:
                self._coins.remove(coin)
                return True
        
        return False