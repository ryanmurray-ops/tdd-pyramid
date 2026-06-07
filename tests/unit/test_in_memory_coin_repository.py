from services.repository.in_memory_coin_repository import InMemoryCoinRepository

def test_repository_starts_empty():
    repository = InMemoryCoinRepository()
    assert repository.get_all_coins() == []