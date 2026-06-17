import pytest
from app import app
from database.db import db
from models.coin_model import CoinModel
from models.duty_model import DutyModel

@pytest.fixture(autouse=True)
def reset_duties():
    app.duty_service.duties.clear()   

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    db.connect(reuse_if_open=True)

    db.create_tables([CoinModel, DutyModel, CoinModel.duties.get_through_model()])

    yield

    db.drop_tables([CoinModel, DutyModel, CoinModel.duties.get_through_model()])

    db.close()

@pytest.fixture(autouse=True)
def clean_db():
    CoinModel.duties.get_through_model().delete().execute()
    CoinModel.delete().execute()
    DutyModel.delete().execute()