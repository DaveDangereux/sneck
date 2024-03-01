import time

from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext


class TitleScreenState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager
        self.game = state_manager.game

        self.game.disable_animation()

    def run(self):
        self.game.board.make_title_screen()

        while self.state_manager.state == self:
            self.game.add_board_to_screen()
            self.game.screen.refresh()
            time.sleep(self.game.frame_duration)
            self._process_user_input()

    def _process_user_input(self):
        key = self.game.screen.get_key()

        if key == " ":
            self.state_manager.transition_to_playing()
