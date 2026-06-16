from models.duty_model import DutyModel
from services.duty_service import DutyService

# ==================
# LEGACY TEST (Phase 1 only - will be removed after DB migration)
def test_duty_service_initially_has_empty_duties_list():
    service = DutyService()

    assert service.duties == []
# ==================

def test_create_duty_saves_to_database():
    service = DutyService()

    duty = service.create_duty("D5", "CI/CD Pipeline")

    assert duty is not None
    assert DutyModel.get_or_none(DutyModel.number == "D5") is not None

