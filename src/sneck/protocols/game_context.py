from abc import abstractmethod
from typing import Protocol

from sneck.classes.display import Display
from sneck.classes.output import Output
from sneck.classes.score_board_data import ScoreBoardData
from sneck.protocols.game_state import GameState


class GameContext(Protocol):
    output: Output
    score: int
    state: GameState
    display: Display
    score_board_data: ScoreBoardData

    @abstractmethod
    def handle_input(self, key: str): ...

    @abstractmethod
    def run(self): ...

    @abstractmethod
    def get_output(self) -> Output: ...

    @abstractmethod
    def transition_to_title_screen(self): ...

    @abstractmethod
    def transition_to_playing(self): ...

    @abstractmethod
    def transition_to_game_over(self): ...

    @abstractmethod
    def transition_to_score_board(self): ...
