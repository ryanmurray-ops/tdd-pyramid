import uuid
from peewee import CharField, TextField, UUIDField
from database.db import db

class DutyModel(db.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    number = CharField(unique=True)
    description = TextField()

    class Meta:
        database = db
        schema = "coins"