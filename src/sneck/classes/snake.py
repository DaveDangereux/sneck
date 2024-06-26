from copy import copy

from sneck.classes.position import Position
from sneck.classes.text import Text
from sneck.enumerations import Direction, TextType


class Snake:
    _head_char = Text("█", TextType.SNAKE)

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
        self._direction = direction
        self._length = length if length > 0 else 1
        self.body_positions = [position]

    def get_head_position(self):
        return copy(self.body_positions[-1])

    def get_length(self) -> int:
        return self._length

    def set_direction(self, direction: Direction):
        if direction != self._OPPOSITE_DIRECTIONS[self._direction]:
            self._direction = direction

    def update_head_position(self):
        new_head_position = self._get_next_position()
        self.body_positions.append(new_head_position)

    def increase_length(self):
        self._length += 1

    def _get_next_position(self):
        next_position = copy(self.body_positions[-1])

        match self._direction:
            case Direction.UP:
                next_position.row -= 1
            case Direction.LEFT:
                next_position.col -= 1
            case Direction.RIGHT:
                next_position.col += 1
            case Direction.DOWN:
                next_position.row += 1

        return next_position
