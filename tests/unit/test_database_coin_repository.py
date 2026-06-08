from coin import Coin
from models.coin_model import CoinModel
from models.duty_model import DutyModel
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

def test_database_repository_can_get_all_coins():
    repository = DatabaseCoinRepository()
    coin1 = Coin("Automate")
    coin2 = Coin("Assemble")
    repository.create_coin(coin1)
    repository.create_coin(coin2)
    result = repository.get_all_coins()
    
    assert len(result) == 2

    names = [coin.name for coin in result]
    assert "Automate" in names
    assert "Assemble" in names

def test_database_repository_can_update_an_existing_coin():
    repository = DatabaseCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    repository.update_coin(coin.id, True)
    updated_coin = repository.get_coin_by_id(coin.id)
    assert updated_coin.is_complete is True
    
def test_database_repository_can_delete_coin():
    repository = DatabaseCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    repository.delete_coin(coin.id)
    result = repository.get_coin_by_id(coin.id)
    assert result is None

def test_database_repository_can_get_coin_by_name():
    repository = DatabaseCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    result = repository.get_coin_by_name("Automate")
    assert result is not None
    assert result.name == "Automate"

def test_database_respository_can_get_all_duties_associated_with_a_coin():
    repository = DatabaseCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    DutyModel.create(
        number="1",
        description="My First Duty",
        coin=coin.id
    )
    duties = repository.get_duties_for_coin(coin.id)
    assert len(duties) == 1
    