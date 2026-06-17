from controllers.coin_controller import CoinController

def test_controller_can_create_coin():
    controller = CoinController()

    created_coin = controller.create_coin("Automate")

    assert created_coin["success"] is True
    assert created_coin["data"].name == "Automate"
    assert created_coin["error"] is None