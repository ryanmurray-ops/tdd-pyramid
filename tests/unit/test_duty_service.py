
from services.duty_service import DutyService
from services.repositories.in_memory_duty_repository import InMemoryDutyRepository


def test_service_can_create_duty():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    created_duty = service.create_duty(
        number="D1",
        description="My First Duty"
    )
    

    assert created_duty["number"] == "D1"
    assert created_duty["description"] == "My First Duty"

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

    created_duty = service.create_duty(
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

    created_duty = service.create_duty(
        number="D1",
        description="My First Duty"
    )

    result = service.get_duty_by_id(created_duty["id"])

    assert result["id"] == created_duty["id"]
    assert result["number"] == "D1"
    assert result["description"] == "My First Duty"

def test_service_can_delete_duty():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    created_duty = service.create_duty(
        number="D1",
        description="My First Duty"
    )

    service.delete_duty(created_duty["id"])

    duties = service.get_all_duties()

    assert len(duties) == 0

def test_service_updates_duty_description():
    repository = InMemoryDutyRepository()
    service = DutyService(repository)

    created_duty = service.create_duty(
        number="D1",
        description="My First Duty"
    )

    updated_duty = service.update_duty(
        created_duty["id"],
        {"description": "Updated"}
    )

    assert updated_duty["description"] == "Updated"