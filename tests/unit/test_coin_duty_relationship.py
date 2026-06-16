from models.coin_model import CoinModel
from models.duty_model import DutyModel


def test_coin_can_have_duties():
    coin = CoinModel.create(name="Automate")
    duty = DutyModel.create(number="D5", description="CI/CD")

    coin.duties.add(duty)

    assert duty in coin.duties

def test_coin_duty_relationship_stores_via_db():
    coin = CoinModel.create(name="Automate")
    duty = DutyModel.create(number="D5", description="CI/CD")

    coin.duties.add(duty)

    db_coin = CoinModel.get(CoinModel.id == coin.id)

    assert duty in db_coin.duties