import uuid

from models.duty_model import DutyModel

def test_can_create_duty():
    duty = DutyModel.create(
        number="D5",
        description="CI/CD Pipeline"
    )

    assert duty.number == "D5"
    assert duty.description == "CI/CD Pipeline"

def test_duty_has_uuid_id():
    duty = DutyModel.create(
        number="D5",
        description="CI/CD Pipeline"
    )

    assert duty.id is not None
    assert isinstance(duty.id, uuid.UUID)

