import uuid

from models.coin_model import CoinModel

def test_can_create_coin():
    coin = CoinModel.create(name="Automate")
    assert coin.name == "Automate"

def test_coin_has_uuid_coin_id():
    coin = CoinModel.create(name="Automate")
    assert coin.id is not None
    assert isinstance(coin.id, uuid.UUID)
    