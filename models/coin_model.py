import uuid
from peewee import BooleanField, Model, CharField, UUIDField
from database.db import db

class CoinModel(db.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(unique=True)
    is_complete = BooleanField(default=False)

    class Meta:
        database = db
        schema = "coins"