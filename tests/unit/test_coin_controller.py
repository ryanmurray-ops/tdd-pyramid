from controllers.coin_controller import CoinController
from services.duty_service import DutyService

def test_controller_can_create_coin():
    controller = CoinController()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    created_coin = controller.create_coin("Automate", ["D5"])

    assert created_coin["success"] is True
    assert created_coin["data"].name == "Automate"
    assert created_coin["error"] is None

def test_controller_can_get_all_coins():
    controller = CoinController()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    controller.create_coin("Automate", ["D5"])
    controller.create_coin("Deploy", ["D5"])

    found_coins = controller.get_all_coins()

    assert len(found_coins["data"]) == 2

def test_controller_can_get_coin_by_name():
    controller = CoinController()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    controller.create_coin("Automate", ["D5"])

    found_coin = controller.get_coin_by_name("Automate")

    assert found_coin["data"].name == "Automate"

def test_get_coin_by_id():
    controller = CoinController()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    created_coin = controller.create_coin("Automate", ["D5"])

    found_coin = controller.get_coin_by_id(created_coin["data"].id)

    assert found_coin["data"].id == created_coin["data"].id

def test_controller_can_update_completion_status():
    controller = CoinController()
    duty_service = DutyService()

    duty_service.create_duty("D5", "CI/CD Pipeline")

    created_coin = controller.create_coin("Automate", ["D5"])

    updated_coin = controller.update_completion_status(created_coin["data"].id)

    assert updated_coin["data"].is_complete is True