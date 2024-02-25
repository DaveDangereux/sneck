from ..assets.ascii_chars import snake_chars
from .position import Position


class Snake:
    head = snake_chars["head"]

    def __init__(self, position: Position):
        print(self.head)
        self.position = position
