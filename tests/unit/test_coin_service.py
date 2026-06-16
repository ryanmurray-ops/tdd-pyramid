import uuid

from services.coin_service import CoinService
from services.duty_service import DutyService

def test_can_create_coin():
    service = CoinService()

    coin = service.create_coin("Automate")
    coins = service.get_all_coins()

    assert coin is not None
    assert coin.name == "Automate"
    assert len(coins) == 1
    
def test_can_get_all_coins():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coins = service.get_all_coins()

    coin_names = [coin.name for coin in coins]

    assert len(coins) == 2
    assert "Automate" in coin_names
    assert "Deploy" in coin_names

def test_can_get_coin_by_name():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coin = service.get_coin_by_name("Deploy")

    assert coin.name == "Deploy"

def test_cannot_create_duplicate_coin():
    service = CoinService()

    service.create_coin("Automate")
    result = service.create_coin("Automate")

    assert result is None
    assert len(service.get_all_coins()) == 1

def test_create_coin_returns_object():
    service = CoinService()

    coin = service.create_coin("Automate")

    assert coin.name == "Automate"

def test_can_get_coin_by_id():
    service = CoinService()

    coin = service.create_coin("Automate")

    coin_found = service.get_coin_by_id(coin.id)

    assert coin_found is not None
    assert coin_found.id == coin.id
    assert coin_found.name == "Automate"

def test_can_update_coin_completion_status_to_complete():
    service = CoinService()
    coin = service.create_coin("Automate")
    updated_coin = service.update_completion_status(coin.id)
    assert updated_coin.is_complete is True

def test_can_assign_duty_to_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    coin = coin_service.create_coin("Automate")
    duty = duty_service.create_duty("D5", "CI/CD Pipeline")

    updated_coin = coin_service.assign_duty(coin.id, duty.number)

    duties = list(updated_coin.duties)

    assert duty in duties 

def test_assign_duty_returns_none_when_coin_does_not_exist():
    coin_service = CoinService()
    duty_service = DutyService()

    duty = duty_service.create_duty("D5", "CI/CD Pipeline")

    result = coin_service.assign_duty(
        uuid.uuid4(),
        duty.number
    )

    assert result is None

def test_assign_duty_returns_none_when_duty_does_not_exist():
    coin_service = CoinService()

    coin = coin_service.create_coin("Automate")

    result = coin_service.assign_duty(
        coin.id,
        "D999"
    )

    assert result is None

def test_cannot_assign_same_duty_twice_to_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    coin = coin_service.create_coin("Automate")
    duty = duty_service.create_duty("D5", "CI/CD Pipeline")

    coin_service.assign_duty(coin.id, "D5")
    assign_duplicate_duty = coin_service.assign_duty(coin.id, "D5")

    assert assign_duplicate_duty is None
