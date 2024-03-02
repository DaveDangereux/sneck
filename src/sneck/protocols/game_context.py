from typing import Protocol

from ..classes.board import Board
from ..classes.screen import Screen


class GameContext(Protocol):
    board: Board
    screen: Screen
    frame_duration: float
    score: int
