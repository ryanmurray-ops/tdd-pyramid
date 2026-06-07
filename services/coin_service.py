from coin import Coin
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository

class CoinService:
    def __init__(self):
        self.coins = []
        self.repository = InMemoryCoinRepository()
    
    def get_all_coins(self):
        return [
            {
                "id": coin.id,
                "name": coin.name
            }
            for coin in self.repository.get_all_coins()
        ]

    def create_coin(self, name):
        for coin in self.coins:
            if coin.name == name:
                return None
            
        coin = Coin(name)
        self.coins.append(coin)
        self.repository.create_coin(coin)
        return coin
    
    def get_coin_by_id(self, coin_id):
        return self.repository.get_coin_by_id(coin_id)
        
    def update_coin(self, coin_id, is_complete):
        coin = self.get_coin_by_id(coin_id)
        if coin:
            coin.is_complete = is_complete
            return coin
        return None
    
    def delete_coin(self, coin_id):
        coin = self.repository.get_coin_by_id(coin_id)
        if not coin:
            return False
        
        self.repository.delete_coin(coin_id)

        if coin in self.coins:
            self.coins.remove(coin)

        return True
        
        
    


    