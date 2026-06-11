from services.repositories.in_memory_duty_repository import InMemoryDutyRepository

def test_repository_starts_empty():
    repository = InMemoryDutyRepository()
    assert repository.get_all_duties() == []