from ..protocols.game_context import GameContext
from ..protocols.game_state import GameState
from ..protocols.state_manager_context import StateManagerContext
from .game_states.game_over import GameOverState
from .game_states.playing import PlayingState
from .game_states.score_board import ScoreBoardState
from .game_states.title_screen import TitleScreenState


class StateManager(StateManagerContext):
    def __init__(self, game_context: GameContext):
        self.game = game_context
        self.state: GameState = TitleScreenState(self)

    def run(self):
        self.state.run()

    def transition_to_title_screen(self):
        self.state = TitleScreenState(self)

    def transition_to_playing(self):
        self.state = PlayingState(self)

    def transition_to_game_over(self):
        self.state = GameOverState(self)

    def transition_to_score_board(self):
        self.state = ScoreBoardState(self)
