from models.coin_model import CoinModel
from services.repositories.database_duty_repository import DatabaseDutyRepository


def test_database_duty_repository_can_be_created():
    repository = DatabaseDutyRepository()
    assert repository is not None

def test_database_duty_repository_can_be_created():
    repository = DatabaseDutyRepository()
    duties = repository.get_all_duties()
    assert duties == []

def test_database_duty_repository_can_create_duty():
    repository = DatabaseDutyRepository()

    coin = CoinModel.create(name="Automate")

    result = repository.create_duty(
        coin.id,
        "D1",
        "My First Duty"
    )

    assert result["number"] == "D1"
    assert result["description"] == "My First Duty"
    assert result["coin_id"] == coin.id

def test_database_duty_repository_can_get_all_duties():
    repository = DatabaseDutyRepository()

    coin = CoinModel.create(name="Automate")

    created_duty = repository.create_duty(
        coin.id,
        "D1",
        "My First Duty"
    )

    duties = repository.get_all_duties()

    assert len(duties) == 1
    assert duties[0]["number"] == "D1"
    assert duties[0]["description"] == "My First Duty"

def test_database_duty_repository_can_get_duty_by_id():
    repository = DatabaseDutyRepository()

    coin = CoinModel.create(name="Automate")

    created_duty = repository.create_duty(
        coin.id,
        "D1",
        "My First Duty"
    )

    retrieved_duty = repository.get_duty_by_id(created_duty["id"])

    assert retrieved_duty["id"] == created_duty["id"]
    assert retrieved_duty["number"] == "D1"
    assert retrieved_duty["description"] == "My First Duty"

def test_database_duty_repository_can_delete_duty():
    repository = DatabaseDutyRepository()

    coin = CoinModel.create(name="Automate")

    created_duty = repository.create_duty(
        coin.id,
        "D1",
        "My First Duty"
    )

    repository.delete_duty(created_duty["id"])

    duties = repository.get_all_duties()


    assert len(duties) == 0

