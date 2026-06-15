from services.coin_service import CoinService

def test_can_create_coin():
    service = CoinService()

    service.create_coin("Automate")

    assert len(service.coins) == 1
    assert service.coins[0] == "Automate"