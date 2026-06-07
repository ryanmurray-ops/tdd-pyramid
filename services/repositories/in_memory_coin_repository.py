class InMemoryCoinRepository:
    def __init__(self):
        self._coins = []

    def get_all_coins(self):
        return self._coins