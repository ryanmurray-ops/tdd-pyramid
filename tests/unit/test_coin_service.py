from services.coin_service import CoinService
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository

def test_create_coin_returns_coin():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    coin = service.create_coin("Automate")
    assert coin.name == "Automate"

def test_coin_service_rejects_duplicate_coin_names():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    service.create_coin("Automate")
    result = service.create_coin("Automate")
    assert result is None

def test_get_coin_by_id_returns_coin_when_exists():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    coin = service.create_coin("Automate")
    result = service.get_coin_by_id(coin.id)
    assert result == coin

def test_update_coin_sets_is_complete_status():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    coin = service.create_coin("Automate")
    service.update_coin(coin.id, True)
    assert coin.is_complete is True

def test_update_coin_returns_none_when_coin_not_found():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    result = service.update_coin("fake-id", True)
    assert result is None

def test_delete_coin_renmoves_coin():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    coin = service.create_coin("Automate")
    service.delete_coin(coin.id)
    assert service.get_coin_by_id(coin.id) == None

def test_delete_coin_returns_false_when_coin_not_found():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    result = service.delete_coin("fake-id")
    assert result is False

def test_coin_service_uses_provided_repository():
    repository = InMemoryCoinRepository()
    service = CoinService(repository)
    assert service.repository is repository

