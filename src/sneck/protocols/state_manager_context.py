from typing import Protocol

from .game_context import GameContext
from .game_state import GameState


class StateManagerContext(Protocol):
    game: GameContext
    state: GameState

    def transition_to_title_screen(self): ...
    def transition_to_playing(self): ...
    def transition_to_game_over(self): ...
