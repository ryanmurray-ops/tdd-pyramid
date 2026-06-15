import pytest
from app import app
from database.db import db
from models.coin_model import CoinModel

@pytest.fixture(autouse=True)
def reset_duties():
    app.service.duties.clear()   

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    db.connect(reuse_if_open=True)
    db.drop_tables([CoinModel], safe=True)
    db.create_tables([CoinModel])
    yield
    db.close()

@pytest.fixture(autouse=True)
def clean_db():
    CoinModel.delete().execute()