import pytest
from app import create_app
from models.coin_model import CoinModel
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page

@pytest.fixture(autouse=True)
def reset_db():
    CoinModel.delete().execute()

@pytest.fixture
def app():
    return create_app(InMemoryCoinRepository())

@pytest.fixture
def client(app):
    return app.test_client()
    