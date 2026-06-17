from controllers.coin_controller import CoinController

def test_controller_can_create_coin():
    controller = CoinController()

    created_coin = controller.create_coin("Automate")

    assert created_coin["success"] is True
    assert created_coin["data"].name == "Automate"
    assert created_coin["error"] is None

def test_controller_can_get_all_coins():
    controller = CoinController()

    controller.create_coin("Automate")
    controller.create_coin("Deploy")

    found_coins = controller.get_all_coins()

    assert len(found_coins["data"]) == 2