from services.repositories.database_coin_repository import DatabaseCoinRepository

def test_database_repository_can_be_created():
    repository = DatabaseCoinRepository()
    assert repository is not None