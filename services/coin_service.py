from models.coin_model import CoinModel

class CoinService:
    def create_coin(self, name):
        if CoinModel.get_or_none(CoinModel.name == name):
            return None
        
        return CoinModel.create(name=name)
  
    def get_all_coins(self):
        return list(CoinModel.select())

    def get_coin_by_name(self, name):
        return CoinModel.get_or_none(CoinModel.name == name)
    
    def get_coin_by_id(self, coin_id):
        return CoinModel.get_or_none(CoinModel.id == coin_id)
    
