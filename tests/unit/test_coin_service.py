from services.coin_service import CoinService

def test_create_coin_returns_coin():
    service = CoinService()
    coin = service.create_coin("Automate")
    assert coin.name == "Automate"

def test_coin_service_rejects_duplicate_coin_names():
    service = CoinService()
    service.create_coin("Automate")
    result = service.create_coin("Automate")
    assert result is None

def test_get_coin_by_id_returns_coin_when_exists():
    service = CoinService()
    coin = service.create_coin("Automate")
    result = service.get_coin_by_id(coin.id)
    assert result == coin

