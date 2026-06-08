import uuid
from peewee import ForeignKeyField, Model, UUIDField, CharField
from models.coin_model import CoinModel
from database import db


class DutyModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    number = CharField()
    description = CharField()
    coin = ForeignKeyField(CoinModel, backref="duties")

    class Meta:
        database = db
        schema = "coins"