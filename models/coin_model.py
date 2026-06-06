from peewee import Model, UUIDField, CharField, BooleanField
import uuid
from database import db

class CoinModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField()
    is_complete = BooleanField(default=False)

    class Meta:
        database = db
        schema = "coins"