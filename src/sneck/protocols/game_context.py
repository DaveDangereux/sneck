from typing import Protocol

from sneck.classes.board import Board
from sneck.classes.score_board_data import ScoreBoardData
from sneck.classes.screen import Screen


class GameContext(Protocol):
    board: Board
    frame_duration: float
    score_board_data: ScoreBoardData
    screen: Screen
    score: int
