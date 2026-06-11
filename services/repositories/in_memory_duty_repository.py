class InMemoryDutyRepository:
    def __init__(self):
        self._duties = []

    def get_all_duties(self):
        return self._duties