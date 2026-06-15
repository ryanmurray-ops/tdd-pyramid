from models.coin_model import CoinModel

def test_can_create_coin():
    coin = CoinModel.create(name="Automate")
    assert coin.name == "Automate"