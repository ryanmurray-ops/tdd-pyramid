from app import create_app
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository

def test_create_app_uses_provided_repository():
    repository = InMemoryCoinRepository()
    app = create_app(repository)
    assert app.coin_service.repository is repository