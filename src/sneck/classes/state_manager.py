from sneck.classes.game_states import (GameOverState, PlayingState,
                                       ScoreBoardState, TitleScreenState)
from sneck.protocols.game_context import GameContext
from sneck.protocols.game_state import GameState
from sneck.protocols.state_manager_context import StateManagerContext


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
