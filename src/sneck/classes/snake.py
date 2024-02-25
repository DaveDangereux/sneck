from ..assets.ascii_chars import snake_chars
from .direction import Direction
from .position import Position


class Snake:
    head = snake_chars["head"]

    def __init__(self, position: Position, direction: Direction = Direction.UP):
        print(self.head)
        self._position = position
        self._direction = direction

    def get_position(self):
        return self._position

    def set_direction(self, direction: Direction):
        self._direction = direction

    def move(self):
        match self._direction:
            case Direction.UP:
                self._position.row -= 1
            case Direction.LEFT:
                self._position.col -= 1
            case Direction.RIGHT:
                self._position.col += 1
            case Direction.DOWN:
                self._position.row += 1
