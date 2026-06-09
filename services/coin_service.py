from coin import Coin
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository

class CoinService:
    def __init__(self, repository):
        self.repository = repository
    
    def get_all_coins(self):
        return [
            {
                "id": coin.id,
                "name": coin.name
            }
            for coin in self.repository.get_all_coins()
        ]

    def create_coin(self, name):
        if self.repository.get_coin_by_name(name):
            return None
            
        coin = Coin(name)
        self.repository.create_coin(coin)
        return coin
    
    def get_coin_by_id(self, coin_id):
        return self.repository.get_coin_by_id(coin_id)
        
    def update_coin(self, coin_id, is_complete):
        coin = self.repository.update_coin(coin_id, is_complete)
        return coin
    
    def delete_coin(self, coin_id):
        return self.repository.delete_coin(coin_id)
    
    def add_duty_to_coin(self, coin_id, duty_number, description):
        return self.repository.create_duty(
            coin_id,
            duty_number,
            description
        )
        
        
    


    