from models.coin_model import CoinModel

def test_coin_model_can_be_created():
    coin = CoinModel.create(name="Automate")
    assert coin.id is not None
    assert coin.name == "Automate"
    assert coin.is_complete is False

