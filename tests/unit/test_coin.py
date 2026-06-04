from coin import Coin

def test_coin_can_be_created():
    coin = Coin(name="Automate")

    assert coin.name == "Automate"

def test_coin_has_unique_id():
    first_coin = Coin(name="Automate")
    second_coin = Coin(name="Automate")

    assert first_coin.id is not None
    assert second_coin.id is not None
    assert first_coin.id != second_coin.id

def test_coin_starts_incomplete():
    coin = Coin(name="automate")
    assert coin.is_complete is False