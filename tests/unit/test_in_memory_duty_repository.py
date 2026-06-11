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
