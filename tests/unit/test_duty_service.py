from models.duty_model import DutyModel
from services.duty_service import DutyService

# ==================
# LEGACY TEST (Phase 1 only - will be removed after DB migration)
def test_duty_service_initially_has_empty_duties_list():
    service = DutyService()

    assert service.duties == []
# ==================

def test_service_can_create_duty_and_save_to_database():
    service = DutyService()

    duty = service.create_duty("D5", "CI/CD Pipeline")

    assert duty is not None
    assert DutyModel.get_or_none(DutyModel.number == "D5") is not None

def test_service_can_get_all_duties():
    service = DutyService()

    service.create_duty("D5", "CI/CD Pipeline")
    service.create_duty("D7", "Monitoring")

    duties = service.get_all_duties()

    duty_numbers = [duty.number for duty in duties]

    assert len(duties) == 2
    assert "D5" in duty_numbers
    assert "D7" in duty_numbers

def test_service_can_get_duty_by_number():
    service = DutyService()

    service.create_duty("D5", "CI/CD Pipeline")

    duty = service.get_duty_by_number("D5")

    assert duty is not None
    assert duty.number == "D5"
    assert duty.description == "CI/CD Pipeline"

def test_service_can_update_duty_description():
    service = DutyService()

    duty = service.create_duty("D5", "CI/CD Pipeline")

    updated_duty = service.update_duty_description("D5", "Updated Description")

    assert updated_duty.description == "Updated Description"

def test_service_returns_none_when_updating_non_existent_duty():
    service = DutyService()

    duty = service.update_duty_description("D5", "Does Not Exist")

    assert duty is None
