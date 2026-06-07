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

def test_reposiroty_can_get_coin_by_id():
    repository = InMemoryCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    result = repository.get_coin_by_id(coin.id)
    assert result == coin

def test_reposirtory_can_update_coin_completion_status():
    repository = InMemoryCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    repository.update_coin(coin.id, True)
    updated_coin = repository.get_coin_by_id(coin.id)
    assert updated_coin.is_complete is True


def test_repository_can_delete_coin():
    repository = InMemoryCoinRepository()
    coin = Coin("Automate")
    repository.create_coin(coin)
    repository.delete_coin(coin.id)
    result = repository.get_coin_by_id(coin.id)
    assert result is None