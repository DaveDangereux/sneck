from typing import Protocol

from ..classes.board import Board
from ..classes.screen import Screen


class GameContext(Protocol):
    board: Board
    screen: Screen
    frame_duration: float
    game_counter: int
    score: int

    def enable_animation(self): ...
    def disable_animation(self): ...
    def draw_board_to_screen(self): ...
    def draw_score_to_screen(self): ...
