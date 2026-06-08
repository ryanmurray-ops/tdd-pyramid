import uuid

class Coin:
    def __init__(self, name, id=None, is_complete=False):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.is_complete = is_complete
        self.duties = []