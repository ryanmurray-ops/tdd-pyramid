from models.coin_model import CoinModel
from models.duty_model import DutyModel

def test_duty_can_be_created_with_coin_relationship():
    coin = CoinModel.create(name="Automate")

    duty = DutyModel.create(
        number="1",
        description="My First Duty",
        coin=coin
    )

    assert duty.id is not None
    assert duty.coin.id == coin.id
    assert duty.number == "1"
