def test_create_coin_returns_coin():
    service = CoinService()
    coin = service.create_coin("Automate")
    assert coin.name == "Automate"