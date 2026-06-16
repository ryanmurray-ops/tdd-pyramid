from models.coin_model import CoinModel
from models.duty_model import DutyModel


def test_coin_can_have_duties():
    coin = CoinModel.create(name="Automate")
    duty = DutyModel.create(number="D5", description="CI/CD")

    coin.duties.add(duty)

    assert duty in coin.duties