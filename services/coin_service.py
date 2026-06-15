class CoinService:
    def __init__(self):
        self.coins =[]

    def create_coin(self, name):
        self.coins.append(name)
    
    def get_all_coins(self):
        return self.coins