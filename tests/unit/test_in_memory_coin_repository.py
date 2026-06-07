from coin import Coin
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository

def test_repository_starts_empty():
    repository = InMemoryCoinRepository()
    assert repository.get_all_coins() == []

def test_repositoy_can_store_a_coin():
    repository = InMemoryCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    assert len(repository.get_all_coins()) == 1

def test_repositoy_returns_stored_coin():
    repository = InMemoryCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    result = repository.get_all_coins()
    assert result[0] == coin