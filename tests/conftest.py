import pytest
from app import app
from models.coin_model import CoinModel

@pytest.fixture(autouse=True)
def reset_duties():
    app.duty_service.duties.clear()   

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page

@pytest.fixture(autouse=True)
def reset_coins():
    app.coin_service.repository._coins.clear()

@pytest.fixture(autouse=True)
def reset_db():
    CoinModel.delete().execute()