from app import create_app
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository
from services.repositories.in_memory_duty_repository import InMemoryDutyRepository

def test_create_app_uses_provided_repository():
    coin_repository = InMemoryCoinRepository()
    duty_repository = InMemoryDutyRepository()

    app = create_app(coin_repository, duty_repository)
    assert app.coin_service.repository is coin_repository
    assert app.duty_service.repository is duty_repository