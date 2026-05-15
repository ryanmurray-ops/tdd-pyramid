from services.duty_service import DutyService

def test_duty_service_initially_has_empty_duties_list():
    service = DutyService()

    assert service.duties == []