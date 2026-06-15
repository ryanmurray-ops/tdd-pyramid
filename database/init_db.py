from database.db import db
from models.coin_model import CoinModel

def init_db():
    db.connect(reuse_if_open=True)
    db.create_tables([CoinModel])
    print("Tables created")