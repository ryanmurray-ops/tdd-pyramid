import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase



# Load environment variables from .env file
load_dotenv()

# Create database connection using environment variables
db = PostgresqlDatabase(
    os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=int(os.getenv("DATABASE_PORT"))
)

def init_db():
    from models.coin_model import CoinModel
    from models.duty_model import DutyModel
    
    db.connect(reuse_if_open=True)
    db.create_tables([CoinModel, DutyModel])