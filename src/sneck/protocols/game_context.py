from typing import Protocol

from ..classes.board import Board
from ..classes.renderer import Renderer


class GameContext(Protocol):
    board: Board
    renderer: Renderer
    frame_duration: float
    game_counter: int
    score: int

    def enable_animation(self): ...
    def disable_animation(self): ...
    def draw_board_to_screen(self): ...
    def draw_score_to_screen(self): ...
