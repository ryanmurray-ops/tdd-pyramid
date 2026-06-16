import uuid
from peewee import CharField, TextField, UUIDField
from database.db import db

class DutyModel(db.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField()
    description = TextField()

    class Meta:
        database = db
        schema = "coins"