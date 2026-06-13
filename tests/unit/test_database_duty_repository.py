from services.repositories.database_duty_repository import DatabaseDutyRepository


def test_database_duty_repository_can_be_created():
    repository = DatabaseDutyRepository()
    assert repository is not None

def test_database_duty_repository_can_be_created():
    repository = DatabaseDutyRepository()
    duties = repository.get_all_duties()
    assert duties == []
