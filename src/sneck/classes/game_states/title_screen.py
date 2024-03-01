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
            self.game.renderer.erase()
            self.game.draw_board_to_screen()
            self.game.renderer.refresh()
            time.sleep(self.game.frame_duration)
            self._process_user_input()

    def _process_user_input(self):
        try:
            key = self.game.renderer.get_key()
        except Exception:
            key = ""

        if key != "":
            self.state_manager.transition_to_playing()
