from coin import Coin

def test_coin_can_be_created():
    coin = Coin(name="Automate")

    assert coin.name == "Automate"