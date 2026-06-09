class InMemoryCoinRepository:
    def __init__(self):
        self._coins = []
        self._duties = {}

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
    
    def create_duty(self, coin_id, duty_number, description):
        if coin_id not in self._duties:
            self._duties[coin_id] = []

            duty = {
                "coin_id": coin_id,
                "number": duty_number,
                "description": description
            }

            self._duties[coin_id].append(duty)

            return duty