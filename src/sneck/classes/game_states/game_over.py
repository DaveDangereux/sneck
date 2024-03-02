from ...protocols.game_state import GameState
from ...protocols.state_manager_context import StateManagerContext
from ..painter import Painter


class GameOverState(GameState):
    def __init__(self, state_manager: StateManagerContext):
        self.state_manager = state_manager
        self.game = state_manager.game

        self.game.disable_animation()

    def run(self):
        self.game.screen.erase()
        self.game.board.clear()
        Painter.paint_centre_text(
            self.game.board,
            [
                "G A M E  O V E R",
                "",
                f"Score: {self.game.score:03d}",
                "",
                "Press space",
                "to continue",
            ],
        )

        self.game.add_board_to_screen()
        self.game.screen.refresh()

        while self.state_manager.state == self:
            self._process_user_input()

    def _process_user_input(self) -> None:
        try:
            key = self.game.screen.get_key()
        except Exception:
            key = ""

        if key == " ":
            self.state_manager.transition_to_title_screen()
