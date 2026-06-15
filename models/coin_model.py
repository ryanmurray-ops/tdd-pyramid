import uuid
from peewee import Model, CharField, UUIDField
from database.db import db

class CoinModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField()

    class Meta:
        database = db
        schema = "coins"