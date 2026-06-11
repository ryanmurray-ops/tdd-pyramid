from coin import Coin
from services.repositories.in_memory_duty_repository import InMemoryDutyRepository

def test_repository_starts_empty():
    repository = InMemoryDutyRepository()
    assert repository.get_all_duties() == []

def test_repository_can_create_duty():
    repository = InMemoryDutyRepository()
    coin = Coin("Automate")
    
    repository.create_duty(
        number="D1",
        description="My First Duty"
    )

    duties = repository.get_all_duties()

    assert len(duties) == 1
    assert duties[0]["number"] == "D1"
    assert duties[0]["description"] == "My First Duty"

def test_repository_can_get_duty_by_id():
    repository = InMemoryDutyRepository()
    duty_created = repository.create_duty(
        number="D1",
        description="My First Duty"
    )
    
    result = repository.get_duty_by_id(duty_created["id"])

    assert result["id"] == duty_created["id"]
    assert result["number"] == "D1"
    assert result["description"] == "My First Duty"
