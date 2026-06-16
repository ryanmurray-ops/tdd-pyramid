import uuid
from peewee import BooleanField, CharField, UUIDField, ManyToManyField
from database.db import db
from models.duty_model import DutyModel

class CoinModel(db.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(unique=True)
    is_complete = BooleanField(default=False)

    duties = ManyToManyField(DutyModel, backref='coins')

    class Meta:
        database = db
        schema = "coins"

