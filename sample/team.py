from api import API


class Team:
    def __init__(self, id: int):
        if not isinstance(id, int):
            raise TypeError
