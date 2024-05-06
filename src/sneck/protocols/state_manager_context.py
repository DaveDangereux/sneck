from typing import Protocol

from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState


class StateManagerContext(Protocol):
    game: GameContext
    state: GameState

    def transition_to_title_screen(self): ...
    def transition_to_playing(self): ...
    def transition_to_game_over(self): ...
    def transition_to_score_board(self): ...
