import uuid
import pytest
from peewee import IntegrityError

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

def test_duty_numbers_must_be_unique():
    DutyModel.create(
        number="D5",
        description="CI/CD Pipeline"
    )

    with pytest.raises(IntegrityError):
        DutyModel.create(
            number="D5",
            description="Another Description"
        )
