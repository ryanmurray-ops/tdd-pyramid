from models.coin_model import CoinModel
from services.repositories.database_coin_repository import DatabaseCoinRepository

def test_database_repository_can_be_created():
    repository = DatabaseCoinRepository()
    assert repository is not None

def test_database_repository_can_store_a_coin():
    repository = DatabaseCoinRepository()
    repository.create_coin("Automate")
    stored_coin = CoinModel.get(
        CoinModel.name == "Automate"
    )
    assert stored_coin.name == "Automate"