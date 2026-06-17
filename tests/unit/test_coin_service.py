import uuid

from services.coin_service import CoinService
from services.duty_service import DutyService

def test_can_create_coin():
    service = CoinService()

    created_coin = service.create_coin("Automate")
    coins = service.get_all_coins()["data"]

    assert created_coin["success"] is True
    assert created_coin["data"].name == "Automate"
    assert len(coins) == 1
    
def test_can_get_all_coins():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coins = service.get_all_coins()["data"]

    coin_names = [coin.name for coin in coins]

    assert len(coins) == 2
    assert "Automate" in coin_names
    assert "Deploy" in coin_names

def test_get_all_coins_returns_success_response():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    retrieved_coins = service.get_all_coins()

    assert retrieved_coins["success"] is True
    assert len(retrieved_coins["data"]) == 2
    assert retrieved_coins["error"] == None

def test_can_get_coin_by_name():
    service = CoinService()

    service.create_coin("Automate")
    service.create_coin("Deploy")

    coin = service.get_coin_by_name("Deploy")

    assert coin.name == "Deploy"

def test_create_coin_returns_success_response():
    service = CoinService()
    
    created_coin = service.create_coin("Automate")

    assert created_coin["success"] is True
    assert created_coin["data"].name == "Automate"
    assert created_coin["error"] is None

def test_create_coin_returns_error_when_coin_already_exists():
    service = CoinService()

    service.create_coin("Automate")

    duplicate_coin = service.create_coin("Automate")

    assert duplicate_coin["success"] is False
    assert duplicate_coin["data"] is None
    assert duplicate_coin["error"] == "Coin already exists"

def test_get_coin_by_id_returns_success_response():
    service = CoinService()
    
    created_coin = service.create_coin("Automate")

    found_coin = service.get_coin_by_id(created_coin["data"].id)

    assert found_coin["success"] == True
    assert found_coin["data"].id == created_coin["data"].id
    assert found_coin["data"].name == "Automate"
    assert found_coin["error"] is None

def test_can_update_coin_completion_status_to_complete():
    service = CoinService()
    created_coin = service.create_coin("Automate")
    updated_coin = service.update_completion_status(created_coin["data"].id)
    assert updated_coin.is_complete is True

def test_can_assign_duty_to_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    created_coin = coin_service.create_coin("Automate")
    duty = duty_service.create_duty("D5", "CI/CD Pipeline")

    updated_coin = coin_service.assign_duty(created_coin["data"].id, duty.number)

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

    created_coin = coin_service.create_coin("Automate")

    result = coin_service.assign_duty(
        created_coin["data"].id,
        "D999"
    )

    assert result is None

def test_cannot_assign_same_duty_twice_to_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    created_coin = coin_service.create_coin("Automate")
    created_duty = duty_service.create_duty("D5", "CI/CD Pipeline")

    coin_service.assign_duty(created_coin["data"].id, "D5")
    assign_duplicate_duty = coin_service.assign_duty(created_coin["data"].id, "D5")

    assert assign_duplicate_duty is None