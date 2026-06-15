import uuid
import pytest
from peewee import IntegrityError

from models.coin_model import CoinModel

def test_can_create_coin():
    coin = CoinModel.create(name="Automate")
    assert coin.name == "Automate"

def test_coin_has_uuid_coin_id():
    coin = CoinModel.create(name="Automate")
    assert coin.id is not None
    assert isinstance(coin.id, uuid.UUID)

def test_coin_names_must_be_unique():
    CoinModel.create(name="Automate")
    with pytest.raises(IntegrityError):
        CoinModel.create(name="Automate")

    