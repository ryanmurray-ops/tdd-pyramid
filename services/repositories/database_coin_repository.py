from coin import Coin
from models.coin_model import CoinModel

class DatabaseCoinRepository:
    def get_all_coins(self):
        coin_models = CoinModel.select()
        return [
            Coin(
                id=coin.id,
                name=coin.name
            )
            for coin in coin_models
        ]

    def create_coin(self, coin):
        return CoinModel.create(
            id=coin.id,
            name=coin.name
        )
    
    def get_coin_by_id(self, coin_id):
        coin_model = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin_model:
            return None

        return Coin(
            name=coin_model.name,
            id=str(coin_model.id)
        )