from coin import Coin
from models.coin_model import CoinModel

class DatabaseCoinRepository:
    def get_all_coins(self):
        coin_models = CoinModel.select()
        return [
            Coin(
                id=str(coin.id),
                name=coin.name,
                is_complete=coin.is_complete
            )
            for coin in coin_models
        ]

    def create_coin(self, coin):
        CoinModel.create(
            id=coin.id,
            name=coin.name,
            is_complete=coin.is_complete
        )

        return coin
    
    def get_coin_by_id(self, coin_id):
        coin_model = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin_model:
            return None

        return Coin(
            id=str(coin_model.id),
            name=coin_model.name,
            is_complete=coin_model.is_complete
        )

    def update_coin(self, coin_id, is_complete):
        coin_model = CoinModel.get_or_none(CoinModel.id == coin_id)

        if not coin_model:
            return None
        
        coin_model.is_complete = is_complete
        coin_model.save()

        return Coin(
            id=str(coin_model.id),
            name=coin_model.name,
            is_complete=coin_model.is_complete
        )