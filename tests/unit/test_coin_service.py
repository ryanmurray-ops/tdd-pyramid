from services.coin_service import CoinService

def test_create_coin_returns_coin():
    service = CoinService()
    coin = service.create_coin("Automate")
    assert coin.name == "Automate"

def test_coin_service_rejeects_duplicate_coin_names():
    service = CoinService()
    service.create_coin("Automate")
    result = service.create_coin("Automate")
    assert result is None

