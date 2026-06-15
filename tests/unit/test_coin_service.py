from services.coin_service import CoinService

def test_can_create_coin():
    service = CoinService()

    service.create_coin("Automate")

    assert len(service.coins) == 1
    assert service.coins[0] == "Automate"

def test_can_get_all_coins():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coins = service.get_all_coins()

    assert len(coins) == 2
    assert coins[0] == "Automate"
    assert coins[1] == "Deploy"

def test_can_get_coin_by_name():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coin = service.get_coin_by_name("Deploy")

    assert coin == "Deploy"

def test_cannot_create_duplicate_coin():
    service = CoinService()

    service.create_coin("Automate")
    result = service.create_coin("Automate")

    assert result is None
    assert len(service.coins) == 1 