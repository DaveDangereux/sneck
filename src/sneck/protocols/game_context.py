from abc import abstractmethod
from typing import Protocol

from sneck.classes.board import Board
from sneck.classes.score_board_data import ScoreBoardData
from sneck.classes.screen import Screen
from sneck.protocols.game_state import GameState


class GameContext(Protocol):
    board: Board
    frame_duration: float
    score: int
    score_board_data: ScoreBoardData
    screen: Screen
    state: GameState

    @abstractmethod
    def transition_to_title_screen(self): ...

    @abstractmethod
    def transition_to_playing(self): ...

    @abstractmethod
    def transition_to_game_over(self): ...

    @abstractmethod
    def transition_to_score_board(self): ...
