import uuid
from peewee import Model, CharField, UUIDField
from database.db import db

class CoinModel(db.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(unique=True)

    class Meta:
        database = db
        schema = "coins"