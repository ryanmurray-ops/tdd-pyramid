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

def test_coin_defaults_to_not_complete_status():
    coin = CoinModel.create(name="Automate")
    assert coin.is_complete is False

def test_can_retrieve_all_coins():
    CoinModel.create(name="Automate")
    CoinModel.create(name="Deploy")
    coins = CoinModel.select()
    coin_names = [coin.name for coin in coins]
    assert len(list(coins)) == 2
    assert "Automate" in coin_names
    assert "Deploy" in coin_names
    