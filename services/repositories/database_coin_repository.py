from models.coin_model import CoinModel

class DatabaseCoinRepository:
    def create_coin(self, name):
        return CoinModel.create(name=name)