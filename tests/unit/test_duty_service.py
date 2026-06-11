
from services.duty_service import DutyService
from services.repositories.in_memory_duty_repository import InMemoryDutyRepository


def test_service_can_create_duty():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    duty_created = service.create_duty(
        number="D1",
        description="My First Duty"
    )
    

    assert duty_created["number"] == "D1"
    assert duty_created["description"] == "My First Duty"

def test_service_rejects_duplicate_duty_numbers():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    service.create_duty(
        number="D1",
        description="My First Duty"
    )

    created_duty = service.create_duty(
        number="D1",
        description="Duplicate Duty"
    )

    assert created_duty is None

def test_service_can_get_all_duties():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    duty_created = service.create_duty(
        number="D1",
        description="My First Duty"
    )

    duties = service.get_all_duties()

    assert len(duties) == 1
    assert duties[0]["number"] == "D1"
    assert duties[0]["description"] == "My First Duty"

def test_service_can_get_duty_by_id():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    duty_created = service.create_duty(
        number="D1",
        description="My First Duty"
    )

    result = service.get_duty_by_id(duty_created["id"])

    assert result["id"] == duty_created["id"]
    assert result["number"] == "D1"
    assert result["description"] == "My First Duty"

def test_service_can_delete_duty():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    duty_created = service.create_duty(
        number="D1",
        description="My First Duty"
    )

    service.delete_duty(duty_created["id"])

    duties = service.get_all_duties()

    assert len(duties) == 0

