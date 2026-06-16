from database.db import db
from models.coin_model import CoinModel
from models.duty_model import DutyModel

def init_db():
    db.connect(reuse_if_open=True)
    db.create_tables([CoinModel, DutyModel])
    print("Tables created")