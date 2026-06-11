
from services.duty_service import DutyService
from services.repositories.in_memory_duty_repository import InMemoryDutyRepository


def test_service_can_create_duty():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    duty = service.create_duty(
        number="D1",
        description="My First Duty"
    )

    assert duty["number"] == "D1"
    assert duty["description"] == "My First Duty"