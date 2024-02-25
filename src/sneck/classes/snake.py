from copy import copy

from ..assets.ascii_chars import snake_chars
from .direction import Direction
from .position import Position


class Snake:
    head = snake_chars["head"]

    OPPOSITE_DIRECTIONS = {
        Direction.UP: Direction.DOWN,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT,
        Direction.DOWN: Direction.UP,
    }

    def __init__(
        self,
        initial_position: Position,
        length: int = 4,
        direction: Direction = Direction.UP,
    ):
        self._current_direction = direction
        self._body_positions = [initial_position]
        self._length = length if length > 0 else 1
        self._old_tail_position = initial_position

    def get_head_position(self):
        return copy(self._body_positions[-1])

    def get_old_tail_position(self) -> Position:
        return self._old_tail_position

    def get_length(self) -> int:
        return self._length

    def set_direction(self, direction: Direction):
        if direction != self.OPPOSITE_DIRECTIONS[self._current_direction]:
            self._current_direction = direction

    def move(self):
        current_position = self.get_head_position()

        match self._current_direction:
            case Direction.UP:
                current_position.row -= 1
            case Direction.LEFT:
                current_position.col -= 1
            case Direction.RIGHT:
                current_position.col += 1
            case Direction.DOWN:
                current_position.row += 1

        self._body_positions.append(current_position)
        if len(self._body_positions) > self._length:
            self._old_tail_position = self._body_positions.pop(0)
