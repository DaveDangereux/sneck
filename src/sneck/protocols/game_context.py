from typing import Protocol

from ..classes.board import Board
from ..classes.screen import Screen


class GameContext(Protocol):
    board: Board
    screen: Screen
    frame_duration: float
    score: int

    def enable_animation(self): ...
    def disable_animation(self): ...
    def add_board_to_screen(self): ...
    def add_score_to_screen(self): ...
    def add_debug_info_to_screen(self, text: str): ...
