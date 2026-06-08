from coin import Coin
from models.coin_model import CoinModel
from services.repositories.database_coin_repository import DatabaseCoinRepository

def test_database_repository_can_be_created():
    repository = DatabaseCoinRepository()
    assert repository is not None

def test_database_repository_can_store_a_coin():
    repository = DatabaseCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    stored_coin = CoinModel.get(CoinModel.name == "Automate")
    assert stored_coin.name == "Automate"

def test_database_repository_can_get_coin_by_id():
    repository = DatabaseCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    result = repository.get_coin_by_id(coin.id)
    assert result.name == "Automate"
    assert result.id == coin.id