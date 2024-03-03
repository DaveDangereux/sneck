from typing import Protocol

from ..classes.board import Board
from ..classes.score_board_data import ScoreBoardData
from ..classes.screen import Screen


class GameContext(Protocol):
    board: Board
    frame_duration: float
    score_board_data: ScoreBoardData
    screen: Screen
    score: int
