from services.coin_service import CoinService

def test_can_create_coin():
    service = CoinService()

    coin = service.create_coin("Automate")
    coins = service.get_all_coins()

    assert coin is not None
    assert coin.name == "Automate"
    assert len(coins) == 1
    
def test_can_get_all_coins():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coins = service.get_all_coins()

    coin_names = [coin.name for coin in coins]

    assert len(coins) == 2
    assert "Automate" in coin_names
    assert "Deploy" in coin_names

def test_can_get_coin_by_name():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coin = service.get_coin_by_name("Deploy")

    assert coin.name == "Deploy"

def test_cannot_create_duplicate_coin():
    service = CoinService()

    service.create_coin("Automate")
    result = service.create_coin("Automate")

    assert result is None
    assert len(service.get_all_coins()) == 1

def test_create_coin_returns_object():
    service = CoinService()

    coin = service.create_coin("Automate")

    assert coin.name == "Automate"