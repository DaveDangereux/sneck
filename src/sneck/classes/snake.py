from copy import copy

from ..assets.ascii_chars import snake_chars
from ..enumerations.direction import Direction
from .position import Position


class Snake:
    head_char = snake_chars["head"]

    _OPPOSITE_DIRECTIONS = {
        Direction.UP: Direction.DOWN,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT,
        Direction.DOWN: Direction.UP,
    }

    def __init__(
        self,
        position: Position,
        length: int = 4,
        direction: Direction = Direction.UP,
    ):
        self._initial_position = position
        self._initial_direction = direction
        self._initial_length = length

        self.reset_snake()

    def reset_snake(self) -> None:
        self._current_direction = self._initial_direction
        self._body_positions = [self._initial_position]
        self._length = self._initial_length if self._initial_length > 0 else 1
        self._old_tail_position = self._initial_position

    def get_head_position(self):
        return copy(self._body_positions[-1])

    def get_old_tail_position(self) -> Position:
        return self._old_tail_position

    def get_length(self) -> int:
        return self._length

    def set_direction(self, direction: Direction):
        if direction != self._OPPOSITE_DIRECTIONS[self._current_direction]:
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

    def increase_length(self):
        self._length += 1
