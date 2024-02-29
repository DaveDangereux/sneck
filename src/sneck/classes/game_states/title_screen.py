import time

from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext


class TitleScreenState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager
        self.game_context = state_manager.game

    def run(self):
        self.game_context.board.make_title_screen()

        while self.state_manager.state == self:
            self.game_context.renderer.erase()
            self.game_context.draw_board_to_screen()
            self.game_context.renderer.refresh()
            time.sleep(self.game_context.frame_duration)
            self._process_user_input()

    def _process_user_input(self):
        try:
            key = self.game_context.renderer.get_key()
        except Exception:
            key = ""

        if key != "":
            self.state_manager.transition_to_playing()
