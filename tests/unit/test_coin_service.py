import uuid

from services.coin_service import CoinService
from services.duty_service import DutyService

def test_can_create_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    created_coin = coin_service.create_coin("Automate", ["D5"])
    coins = coin_service.get_all_coins()["data"]

    assert created_coin["success"] is True
    assert created_coin["data"].name == "Automate"
    assert len(coins) == 1

def test_create_coin_returns_error_when_coin_already_exists():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    coin_service.create_coin("Automate", ["D5"])

    duplicate_coin = coin_service.create_coin("Automate", ["D5"])

    assert duplicate_coin["success"] is False
    assert duplicate_coin["data"] is None
    assert duplicate_coin["error"] == "Coin already exists"
    
def test_can_get_all_coins():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    coin_service.create_coin("Automate", ["D5"])
    coin_service.create_coin("Deploy", ["D5"])

    coins = coin_service.get_all_coins()["data"]

    coin_names = [coin.name for coin in coins]

    assert len(coins) == 2
    assert "Automate" in coin_names
    assert "Deploy" in coin_names

def test_get_coin_by_name_returns_success_response():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    coin_service.create_coin("Automate", ["D5"])
    coin_service.create_coin("Deploy", ["D5"])

    found_coin = coin_service.get_coin_by_name("Deploy")

    assert found_coin["success"]
    assert found_coin["data"].name == "Deploy"
    assert found_coin["error"] is None

def test_get_coin_by_name_returns_error_when_coin_does_not_exist():
    service = CoinService()

    missing_coin = service.get_coin_by_name("DoesNotExist")

    assert missing_coin["success"] is False
    assert missing_coin["data"] is None
    assert missing_coin["error"] == "Coin not found"

def test_get_coin_by_id_returns_success_response():
    service = CoinService()
    
    created_coin = service.create_coin("Automate", ["D5"])

    found_coin = service.get_coin_by_id(created_coin["data"].id)

    assert found_coin["success"] == True
    assert found_coin["data"].id == created_coin["data"].id
    assert found_coin["data"].name == "Automate"
    assert found_coin["error"] is None

def test_get_coin_by_id_returns_error_when_coin_does_not_exist():
    service = CoinService()

    missing_coin = service.get_coin_by_id(uuid.uuid4())

    assert missing_coin["success"] is False
    assert missing_coin["data"] is None
    assert missing_coin["error"] == "Coin not found"

def test_update_completion_status_returns_success_response():
    service = CoinService()

    created_coin = service.create_coin("Automate", ["D5"])

    result = service.update_completion_status(created_coin["data"].id)

    assert result["success"] is True
    assert result["data"].is_complete is True
    assert result["error"] is None

def test_can_assign_duty_to_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")
    duty_service.create_duty("D6", "Monitoring")

    created_coin = coin_service.create_coin("Automate", ["D5"])
    
    coin_service.assign_duty(created_coin["data"].id, "D6")

    duty_numbers = [duty.number for duty in created_coin["data"].duties]

    assert "D5" in duty_numbers
    assert "D6" in duty_numbers

def test_assign_duty_returns_error_when_coin_does_not_exist():
    coin_service = CoinService()
    duty_service = DutyService()

    duty = duty_service.create_duty("D5", "CI/CD Pipeline")

    result = coin_service.assign_duty(
        uuid.uuid4(),
        duty["data"].number
    )

    assert result["success"] is False
    assert result["data"] is None
    assert result["error"] == "Coin not found"

def test_assign_duty_returns_error_when_duty_does_not_exist():
    coin_service = CoinService()

    created_coin = coin_service.create_coin("Automate", ["D5"])

    result = coin_service.assign_duty(
        created_coin["data"].id,
        "D999"
    )

    assert result["success"] is False
    assert result["data"] is None
    assert result["error"] == "Duty not found"

def test_cannot_assign_same_duty_twice_to_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    created_coin = coin_service.create_coin("Automate", ["D5"])

    assign_duplicate_duty = coin_service.assign_duty(created_coin["data"].id, "D5")

    assert assign_duplicate_duty["success"] is False
    assert assign_duplicate_duty["data"] is None
    assert assign_duplicate_duty["error"] == "Duty already assigned"

def test_can_delete_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    created_coin = coin_service.create_coin("Automate", ["D5"])
    coin_id = created_coin["data"].id

    result = coin_service.delete_coin(coin_id)

    assert result["success"] is True
    assert result["data"] == "Coin deleted"
    assert result["error"] is None

def test_delete_coin_returns_error_when_coin_not_found():
    service = CoinService()

    delete_request = service.delete_coin(uuid.uuid4())

    assert delete_request["success"] is False
    assert delete_request["data"] is None
    assert delete_request["error"] == "Coin not found"

def test_can_update_coin():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    created_coin = coin_service.create_coin("Automate", ["D5"])
    coin_id = created_coin["data"].id

    updated_coin = coin_service.update_coin(coin_id, "Deploy")

    assert updated_coin["success"] is True
    assert updated_coin["data"].name == "Deploy"
    assert updated_coin["error"] is None

def test_update_coin_returns_error_when_coin_not_found():
    service = CoinService()

    update_request = service.update_coin(uuid.uuid4(), "Deploy")

    assert update_request["success"] is False
    assert update_request["data"] is None
    assert update_request["error"] == "Coin not found"

def test_update_coin_returns_error_when_coin_already_exists():
    coin_service = CoinService()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    coin1 = coin_service.create_coin("Automate", ["D5"])
    coin2 = coin_service.create_coin("Deploy", ["D5"])

    update_request = coin_service.update_coin(coin2["data"].id, "Automate")

    assert update_request["success"] is False
    assert update_request["data"] is None
    assert update_request["error"] == "Coin already exists"
