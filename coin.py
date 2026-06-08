import uuid

class Coin:
    def __init__(self, name, id=None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.is_complete = False
        self.duties = []