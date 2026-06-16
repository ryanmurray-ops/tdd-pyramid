
from models.duty_model import DutyModel

def test_can_create_duty():
    duty = DutyModel.create(
        name="D5",
        description="CI/CD Pipeline"
    )

    assert duty.name == "D5"
    assert duty.description == "CI/CD Pipeline"