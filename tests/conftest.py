import pytest
from app import create_app
from database import init_db
from models.coin_model import CoinModel
from models.duty_model import DutyModel
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page

@pytest.fixture(autouse=True)
def reset_db():
    DutyModel.delete().execute()
    CoinModel.delete().execute()

@pytest.fixture
def app():
    return create_app(InMemoryCoinRepository())

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def setup_db():
    init_db()
    