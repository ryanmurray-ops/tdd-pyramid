from peewee import Model, CharField
from database.db import db

class CoinModel(Model):
    name = CharField()

    class Meta:
        database = db
        schema = "coins"